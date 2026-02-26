---
id: 0.0.6.6
title: "Security"
nav_summary: "Codex implements a multi-layered security architecture combining **sandboxing** and **approval policies** to protect code and data"
ref: https://developers.openai.com/codex/security.md
ref_type: url
---

# Security

Codex implements a multi-layered security architecture combining **sandboxing** and **approval policies** to protect code and data. The **sandbox mode** restricts technical capabilities (e.g., file access, network reach) via OS-level isolation (cloud containers or local OS mechanisms) or configurable TOML settings (e.g., `workspace_write` or `network_access`). The **approval policy** enforces user consent for elevated actions like network access, file edits outside the workspace, or tool calls with side effects. Defaults prioritize safety: **cloud mode** runs in OpenAI-managed containers with restricted access, while **CLI/IDE** defaults to no network access and workspace-limited writes. Users can adjust risk tolerance via presets like `Auto` (automated workspace edits) or `read-only` (no changes). Network access is disabled by default but can be selectively enabled (e.g., for domain allowlists or web search). Web search defaults to cached results to mitigate prompt injection risks, though live browsing requires explicit configuration. Codex dynamically adapts permissions based on folder version control (e.g., `Auto` for Git repos) and provides commands like `/permissions` or `/status` for manual oversight.

---
**

[Link to original](https://developers.openai.com/codex/security.md)
