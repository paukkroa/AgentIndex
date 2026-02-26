---
id: 0.0.4.3
title: "Claude Code on Microsoft Foundry"
nav_summary: "Deploy Claude Code in Azure Foundry via Azure CLI/RBAC."
ref: https://code.claude.com/docs/en/microsoft-foundry
ref_type: url
---

# Claude Code on Microsoft Foundry

Claude Code on Microsoft Foundry integrates Anthropic’s AI models into Azure’s **Microsoft Foundry**, enabling scalable, enterprise-grade deployment of Claude (Opus, Sonnet, Haiku) via Azure’s managed infrastructure. This guide outlines a **step-by-step setup**, including **prerequisites** (Azure subscription, RBAC permissions, Azure CLI), **resource provisioning** (creating Foundry deployments for each model), **authentication** (API key or Microsoft Entra ID via Azure SDK credential chain), and **configuration** (environment variables like `CLAUDE_CODE_USE_FOUNDRY` and `ANTHROPIC_FOUNDRY_RESOURCE`). Key considerations include **model version pinning** to avoid breaking changes from Anthropic updates and **RBAC configuration** for secure access. Troubleshooting and additional resources (e.g., network/configuration) are also provided for deployment challenges.

---

[Link to original](https://code.claude.com/docs/en/microsoft-foundry)
