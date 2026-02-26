"""Abstract base class for retrieval systems under evaluation."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class RetrievalResult:
    """Output from a single retrieval + generation pass."""

    retrieved_sources: list[str] = field(default_factory=list)
    retrieved_content: str = ""
    answer: str = ""
    tokens_used: int = 0
    latency_ms: float = 0.0
    api_calls: int = 0

    # Detailed token breakdown for cost tracking
    input_tokens: int = 0
    output_tokens: int = 0
    embedding_tokens: int = 0
    model: str = ""
    tool_counts: dict[str, int] = field(default_factory=dict)


class RetrievalSystem(ABC):
    """Abstract base for all retrieval systems."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable system name."""
        ...

    @abstractmethod
    async def setup(self) -> None:
        """One-time setup (build index, load embeddings, etc.)."""
        ...

    @abstractmethod
    async def retrieve(self, question: str) -> RetrievalResult:
        """Run retrieval and generation for a single question."""
        ...

    async def teardown(self) -> None:
        """Optional cleanup."""
