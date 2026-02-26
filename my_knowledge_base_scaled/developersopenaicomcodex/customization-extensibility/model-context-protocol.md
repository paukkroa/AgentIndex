---
id: 0.0.3.4
title: "Model Context Protocol"
nav_summary: "Connect Codex to tools via MCP servers (STDIO/HTTP) using"
ref: https://developers.openai.com/codex/mcp.md
ref_type: url
---

# Model Context Protocol

The **Model Context Protocol (MCP)** enables seamless integration between Codex (or similar AI models) and external tools or documentation via standardized servers. MCP supports two server types: **STDIO servers** (local processes with environment variables) and **streamable HTTP servers** (remote endpoints with OAuth/Bearer token authentication). Configuration is centralized in `config.toml` (default: `~/.codex/config.toml`), shared across CLI and IDE extensions, allowing project-scoped or global setup. Key features include:
- **STDIO servers**: Local processes launched via CLI commands with customizable environment variables, args, and working directories.
- **HTTP servers**: Remote endpoints with configurable authentication (OAuth/Bearer tokens), headers, and tool restrictions (allow/deny lists).
- **Advanced options**: Timeout controls, startup validation, and OAuth callback port customization.
- **Management**: CLI commands (`codex mcp add`, `codex mcp --help`) or manual `config.toml` editing for granular control. OAuth flows are streamlined via `codex mcp login <server-name>`.

---

[Link to original](https://developers.openai.com/codex/mcp.md)
