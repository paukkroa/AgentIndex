---
id: 0.0.4.5
title: "LLM gateway configuration"
nav_summary: "Configure LLM proxy for API routing, auth, and cost control."
ref: https://code.claude.com/docs/en/llm-gateway
ref_type: url
---

# LLM gateway configuration

The **LLM Gateway Configuration** page outlines the technical setup for deploying a centralized proxy layer (LLM gateway) between Claude Code and large language model (LLM) providers. Key features include **centralized authentication** (unified API key management), **usage tracking** (cross-team monitoring), **cost controls** (budgets/rate limits), **audit logging** (compliance tracking), and **model routing** (seamless provider switching). The gateway must support specific API formats—**Anthropic Messages**, **Bedrock InvokeModel**, or **Vertex rawPredict**—with strict header/body field requirements to ensure compatibility. Configuration involves selecting models (default or custom-named), configuring LiteLLM (a third-party proxy) with prerequisites like updated Claude Code and LiteLLM server access, and setting authentication via static API keys or unified endpoints. Provider-specific pass-through endpoints are also supported as an alternative. Environment variables (e.g., `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`) may be required for feature parity.

---

[Link to original](https://code.claude.com/docs/en/llm-gateway)
