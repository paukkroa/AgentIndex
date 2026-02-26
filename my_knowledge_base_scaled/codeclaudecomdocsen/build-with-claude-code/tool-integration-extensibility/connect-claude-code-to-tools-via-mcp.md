---
id: 0.0.2.1.0
title: "Connect Claude Code to tools via MCP"
nav_summary: "Connect Claude Code tools via MCP servers (HTTP/SSE/local/stdio)."
ref: https://code.claude.com/docs/en/mcp
ref_type: url
---

# Connect Claude Code to tools via MCP

The **Model Context Protocol (MCP)** enables **Claude Code** to integrate with external tools, APIs, and data sources via standardized HTTP/SSE or local stdio interfaces. This page outlines **three primary connection methods**:
1. **Remote HTTP/SSE servers** (for cloud-based tools like GitHub, Sentry, or PostgreSQL),
2. **Local stdio servers** (for CLI-based or self-hosted tools),
3. **Plugin-provided MCP servers** (for prebuilt or custom plugins).
Key features include **scope-based configuration** (local/project/user), **dynamic tool updates**, **authentication** (OAuth, JSON config, or Desktop import), and **restriction policies** (allowlists/denylists for security). Practical examples cover error monitoring, code reviews, and database queries. Advanced topics include **MCP prompt execution**, **tool search scaling**, and **server author guidelines**, with output limits and managed configurations for enterprise control.

---

[Link to original](https://code.claude.com/docs/en/mcp)
