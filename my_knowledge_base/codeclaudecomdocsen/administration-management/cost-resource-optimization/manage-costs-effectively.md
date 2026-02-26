---
id: 0.0.5.3.1
title: "Manage costs effectively"
nav_summary: "This page provides a comprehensive guide to **cost management in Claude Code**, focusing on token-based billing, usage tracking, and optimization stra"
ref: https://code.claude.com/docs/en/costs
ref_type: url
---

# Manage costs effectively

This page provides a comprehensive guide to **cost management in Claude Code**, focusing on token-based billing, usage tracking, and optimization strategies. It explains that costs depend on factors like codebase size, query complexity, and conversation length, with average daily costs of **$6–$12 per developer** and **$100–$200/month per developer** for API-heavy usage (e.g., Sonnet 4.6). Key sections cover:
- **Tracking costs** via the `/cost` command (API users) or `/stats` (subscribers), displaying token consumption, session duration, and code changes.
- **Team management** through workspace spend limits and centralized cost reporting in the **Claude Console**, including usage analytics and API token-based billing.
- **Cost reduction techniques**, including:
  - **Token optimization**: Using subagents, skills, and hooks to offload processing, reducing overhead.
  - **Model selection**: Choosing efficient models (e.g., Sonnet 4.6) and adjusting extended thinking.
  - **Prompt refinement**: Writing specific prompts and delegating verbose tasks to subagents.
  - **Context management**: Proactively limiting context size and leveraging plugins

[Link to original](https://code.claude.com/docs/en/costs)
