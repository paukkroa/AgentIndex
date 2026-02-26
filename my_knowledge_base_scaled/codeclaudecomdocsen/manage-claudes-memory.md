---
id: 0.0.10
title: "Manage Claude's memory"
nav_summary: "Claude Code’s **memory management system** integrates **auto memory** (session-persistent context like commands, preferences, and project patterns) an"
ref: https://code.claude.com/docs/en/memory
ref_type: url
---

# Manage Claude's memory

Claude Code’s **memory management system** integrates **auto memory** (session-persistent context like commands, preferences, and project patterns) and **CLAUDE.md files** (customizable Markdown-based instructions/rules) into a hierarchical, multi-level architecture. Memory types include **organization-wide policies** (managed via system paths like `/Library/Application Support/ClaudeCode/CLAUDE.md`), **project-level rules** (modular `.claude/rules/*.md` files for topic-specific guidelines), **team-shared project instructions** (`.claude/CLAUDE.md` or `./CLAUDE.md`), **user-specific preferences** (global `~/.claude/CLAUDE.md` or project-local `./CLAUDE.local.md`), and **auto-generated notes** (stored in `~/.claude/projects/<project>/memory/` with a 200-line limit per session). Rules support **glob patterns**, **path-specific overrides**, and **symlinks** for granular control. Memory lookup prioritizes proximity (child directories override parent files), and **organization-level management** enables centralized compliance enforcement. Best practices emphasize modularity, version control, and selective sharing to optimize performance and collaboration.

---
**NAV

[Link to original](https://code.claude.com/docs/en/memory)
