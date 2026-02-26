---
id: 0.0.3.2.0
title: "Customize your status line"
nav_summary: "Customize real-time status bar with shell scripts"
ref: https://code.claude.com/docs/en/statusline
ref_type: url
---

# Customize your status line

The **Customize Your Status Line** feature in Claude Code allows users to create a fully programmable status bar at the bottom of the interface by executing custom shell scripts. The status line receives real-time JSON session data via stdin, enabling dynamic display of context usage, Git status, cost tracking, or any other metrics. Users can generate scripts automatically via the `/statusline` command (e.g., `/statusline show model name and context percentage with a progress bar`) or manually configure them in `~/.claude/settings.json` by specifying a shell command or script path. Key components include **data fields** (e.g., model name, context window usage, Git branch), **multi-line support**, **color-coded visuals**, and **clickable links**. Advanced features include caching expensive operations, session cost/duration tracking, and integration with Git status. The system processes JSON input, executes scripts, and renders output persistently, offering granular control over session visibility and workflow efficiency.

---

[Link to original](https://code.claude.com/docs/en/statusline)
