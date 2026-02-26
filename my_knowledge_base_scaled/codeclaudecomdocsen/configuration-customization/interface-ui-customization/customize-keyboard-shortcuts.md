---
id: 0.0.3.2.1
title: "Customize keyboard shortcuts"
nav_summary: "Claude Code’s **keyboard shortcut customization** allows users to modify or extend default keybindings via a structured JSON configuration file (`~/"
ref: https://code.claude.com/docs/en/keybindings
ref_type: url
---

# Customize keyboard shortcuts

Claude Code’s **keyboard shortcut customization** allows users to modify or extend default keybindings via a structured JSON configuration file (`~/.claude/keybindings.json`), accessed via the `/keybindings` command. The configuration follows a schema-driven approach, where each **binding block** defines **context-specific** shortcuts (e.g., `Chat`, `Autocomplete`, `Settings`) mapped to predefined **actions** (e.g., `chat:externalEditor`, `history:rewind`). Key features include:
- **Dynamic application**: Changes take effect instantly without app restarts.
- **Modifiers & syntax**: Supports **chords** (e.g., `Ctrl+Shift+E`), **special keys** (e.g., `F1`), and **uppercase letters** for clarity.
- **Context granularity**: Bindings apply to **12+ contexts**, from global navigation to transcript/attachment management.
- **Conflict resolution**: Reserved shortcuts (e.g., `Ctrl+Q` for quit) and terminal conflicts are documented to avoid clashes.
- **Validation**: JSON Schema ensures syntax correctness, with optional `$schema` and `$docs` metadata for IDE support.
Example: Unbinding

[Link to original](https://code.claude.com/docs/en/keybindings)
