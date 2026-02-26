"""LLM provider abstraction supporting Gemini and Ollama."""

from __future__ import annotations

import asyncio
import json
import logging
import os
from dataclasses import dataclass

import httpx

logger = logging.getLogger(__name__)

# Default models per provider
OLLAMA_DEFAULT_MODEL = "llama3.2"
GEMINI_DEFAULT_MODEL = "gemini-3-flash-preview"


@dataclass
class LLMResponse:
    text: str
    thought: str | None = None
    input_tokens: int = 0
    output_tokens: int = 0


class LLMProvider:
    """Base interface for LLM providers."""

    async def generate(
        self,
        user_message: str,
        system: str = "",
        max_tokens: int = 256,
        temperature: float = 0.0,
    ) -> LLMResponse:
        raise NotImplementedError


class OllamaProvider(LLMProvider):
    """LLM provider using a local Ollama instance."""

    def __init__(
        self,
        model: str = OLLAMA_DEFAULT_MODEL,
        base_url: str = "http://localhost:11434",
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")

    async def generate(
        self,
        user_message: str,
        system: str = "",
        max_tokens: int = 256,
        temperature: float = 0.0,
    ) -> LLMResponse:
        # Some models like ministral-3 seem to fail with the 'think' parameter in Ollama
        use_think = "ministral" not in self.model.lower()
        
        payload: dict = {
            "model": self.model,
            "messages": [],
            "stream": False,
            "options": {
                "num_predict": max_tokens,
                "temperature": temperature,
            },
        }
        if use_think:
            payload["think"] = True
            
        if system:
            payload["messages"].append({"role": "system", "content": system})
        payload["messages"].append({"role": "user", "content": user_message})

        async with httpx.AsyncClient(timeout=300.0) as client:
            try:
                resp = await client.post(
                    f"{self.base_url}/api/chat",
                    json=payload,
                )
                resp.raise_for_status()
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 400:
                    error_detail = e.response.text
                    if "think" in payload:
                        # Fallback: retry without thinking parameter
                        logger.warning("Ollama 400 error, retrying without 'think' parameter. Detail: %s", error_detail)
                        payload.pop("think")
                        resp = await client.post(
                            f"{self.base_url}/api/chat",
                            json=payload,
                        )
                        resp.raise_for_status()
                    else:
                        logger.error("Ollama 400 error (no think parameter used). Detail: %s", error_detail)
                        raise e
                else:
                    raise e

            data = resp.json()

        message = data.get("message", {})
        text = message.get("content", "")
        thought = message.get("thinking", None)
        
        # Ollama returns token counts in eval_count / prompt_eval_count
        return LLMResponse(
            text=text.strip(),
            thought=thought.strip() if thought else None,
            input_tokens=data.get("prompt_eval_count", 0),
            output_tokens=data.get("eval_count", 0),
        )

    def __repr__(self) -> str:
        return f"OllamaProvider(model={self.model!r})"


class GeminiProvider(LLMProvider):
    """LLM provider using Google Gemini API."""

    def __init__(
        self,
        model: str = GEMINI_DEFAULT_MODEL,
        api_key: str | None = None,
    ):
        self.model = model
        self._api_key = api_key or os.environ.get("GEMINI_API_KEY", "")
        if not self._api_key:
            raise ValueError(
                "Gemini API key required. Set GEMINI_API_KEY env var or pass api_key."
            )

    async def generate(
        self,
        user_message: str,
        system: str = "",
        max_tokens: int = 256,
        temperature: float = 0.0,
    ) -> LLMResponse:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=self._api_key)

        config = types.GenerateContentConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
            thinking_config=types.ThinkingConfig(include_thoughts=True)
        )
        if system:
            config.system_instruction = system

        try:
            response = await client.aio.models.generate_content(
                model=self.model,
                contents=user_message,
                config=config,
            )
        except Exception as e:
            # Fallback for models not supporting thinking
            if "thinking_config" in str(e) or "400" in str(e):
                logger.warning("Gemini error with thinking_config, retrying with standard config")
                config.thinking_config = None
                response = await client.aio.models.generate_content(
                    model=self.model,
                    contents=user_message,
                    config=config,
                )
            else:
                raise e

        text = ""
        thought = ""
        
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if part.thought:
                    thought += part.text or ""
                else:
                    text += part.text or ""

        # Extract token counts from usage metadata
        input_tokens = 0
        output_tokens = 0
        if response.usage_metadata:
            input_tokens = response.usage_metadata.prompt_token_count or 0
            output_tokens = response.usage_metadata.candidates_token_count or 0

        return LLMResponse(
            text=text.strip(),
            thought=thought.strip() if thought else None,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )

    def __repr__(self) -> str:
        return f"GeminiProvider(model={self.model!r})"


async def _check_ollama(base_url: str = "http://localhost:11434") -> bool:
    """Check if Ollama is running locally."""
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            resp = await client.get(f"{base_url}/api/tags")
            return resp.status_code == 200
    except Exception:
        return False


def get_provider(
    provider: str = "auto",
    model: str | None = None,
    api_key: str | None = None,
) -> LLMProvider:
    """Get an LLM provider instance.

    Args:
        provider: "ollama", "gemini", or "auto" (tries Ollama first, then Gemini).
        model: Model name override.
        api_key: API key for Gemini.
    """
    if provider == "ollama":
        return OllamaProvider(model=model or OLLAMA_DEFAULT_MODEL)

    if provider == "gemini":
        return GeminiProvider(model=model or GEMINI_DEFAULT_MODEL, api_key=api_key)

    # Auto: prefer Ollama if available, else Gemini
    if provider == "auto":
        # Synchronous check for Ollama
        import asyncio

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            # We're in an async context — can't do sync check, try Gemini first
            gemini_key = api_key or os.environ.get("GEMINI_API_KEY", "")
            if gemini_key:
                return GeminiProvider(model=model or GEMINI_DEFAULT_MODEL, api_key=gemini_key)
            return OllamaProvider(model=model or OLLAMA_DEFAULT_MODEL)
        else:
            # Sync context — we can check Ollama
            if asyncio.run(_check_ollama()):
                logger.info("Auto-detected Ollama, using local models")
                return OllamaProvider(model=model or OLLAMA_DEFAULT_MODEL)
            gemini_key = api_key or os.environ.get("GEMINI_API_KEY", "")
            if gemini_key:
                logger.info("Using Gemini API")
                return GeminiProvider(model=model or GEMINI_DEFAULT_MODEL, api_key=gemini_key)
            raise ValueError(
                "No LLM provider available. Either run Ollama locally or set GEMINI_API_KEY."
            )

    raise ValueError(f"Unknown provider: {provider}")
