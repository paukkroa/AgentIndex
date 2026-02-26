---
id: 0.0.2.2.0
title: "Orchestrate teams of Claude Code sessions"
nav_summary: "Coordinate parallel Claude Code sessions via team leads & teammates"
ref: https://code.claude.com/docs/en/agent-teams
ref_type: url
---

# Orchestrate teams of Claude Code sessions

Orchestrate teams of Claude Code sessions enables the coordination of multiple **parallel Claude Code instances** as a collaborative team, where one session acts as the **team lead** to delegate tasks, monitor progress, and synthesize results. Unlike **subagents** (which operate within a single session), agent teams allow **direct interaction with individual teammates** via their own context windows, enabling asynchronous, distributed workflows. Key features include **task assignment, permission-based approvals, real-time communication, and customizable shutdown/cleanup workflows**. The system leverages **environment variables** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`) to enable experimental mode, though limitations exist in session resumption and task coordination. Use cases span **parallel code reviews, hypothesis-driven investigations, and multi-step problem-solving**, with best practices emphasizing **context sharing, task granularity, and proactive monitoring**. Architecture details cover **permissions, token usage, and inter-agent communication protocols**, while troubleshooting guides address common issues like permission prompts or orphaned sessions.

---

[Link to original](https://code.claude.com/docs/en/agent-teams)
