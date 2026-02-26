---
id: 0.0.1.0
title: "Extend Claude Code"
nav_summary: "Claude Code’s **Extend** documentation outlines how to customize and enhance the core agentic system by integrating external tools, workflows, and aut"
ref: https://code.claude.com/docs/en/features-overview
ref_type: url
---

# Extend Claude Code

Claude Code’s **Extend** documentation outlines how to customize and enhance the core agentic system by integrating external tools, workflows, and automation. The platform supports **five primary extension types**:
1. **CLAUDE.md** – Persistent project context (e.g., conventions, rules) loaded across sessions.
2. **Skills** – Reusable markdown-based workflows or knowledge bases invoked via slash commands (e.g., `/deploy`) or auto-loaded contextually.
3. **MCP (Model Customization Protocol)** – Bridges Claude to external APIs/tools for real-time data access.
4. **Subagents** – Isolated agent loops (e.g., for parallel tasks) that return summaries to the main session.
5. **Agent Teams** – Coordinates multiple agents via shared tasks and peer messaging.
6. **Hooks** – Deterministic scripts executed outside the agent loop (e.g., pre/post-event triggers).
7. **Plugins/Marketplaces** – Pre-packaged extensions for distribution.

Key considerations include **context costs** (e.g., persistent vs. on-demand features), **feature layering** (e.g., combining skills with subagents), and **cost breakdowns** by feature type. The guide

[Link to original](https://code.claude.com/docs/en/features-overview)
