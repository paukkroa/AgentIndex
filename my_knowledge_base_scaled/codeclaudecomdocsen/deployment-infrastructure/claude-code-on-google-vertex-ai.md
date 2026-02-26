---
id: 0.0.4.2
title: "Claude Code on Google Vertex AI"
nav_summary: "Deploy Claude Code on Vertex AI: Setup, models, regions, IAM."
ref: https://code.claude.com/docs/en/google-vertex-ai
ref_type: url
---

# Claude Code on Google Vertex AI

Claude Code on Google Vertex AI integrates Anthropic’s Claude models with Google Cloud’s Vertex AI platform, enabling advanced generative AI capabilities within the Vertex AI ecosystem. This guide outlines a **step-by-step setup process**, including enabling the Vertex AI API, requesting access to Claude models (e.g., Claude Sonnet 4.6), configuring GCP credentials, and configuring Claude Code via environment variables (`CLAUDE_CODE_USE_VERTEX`, `ANTHROPIC_VERTEX_PROJECT_ID`). Key considerations include **region-specific model support** (global vs. regional endpoints), **IAM permissions**, and **quota allocation** in GCP. The guide also covers **model version pinning** to avoid breaking changes, **1M-token context window support**, and troubleshooting common issues. Prerequisites include a GCP account with billing, Vertex AI API enabled, and Google Cloud SDK (`gcloud`) installed. Additional resources cover network configuration, LLM gateways, and development containers for seamless deployment.

---

[Link to original](https://code.claude.com/docs/en/google-vertex-ai)
