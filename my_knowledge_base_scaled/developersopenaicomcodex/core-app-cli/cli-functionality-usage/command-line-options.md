---
id: 0.0.1.4.1
title: "Command line options"
nav_summary: "This page documents the **command-line options** for the Codex CLI, detailing **global flags** that customize behavior across commands, including sess"
ref: https://developers.openai.com/codex/cli/reference.md
ref_type: url
---

# Command line options

This page documents the **command-line options** for the Codex CLI, detailing **global flags** that customize behavior across commands, including session prompts (`PROMPT`), model selection (`--model`), sandboxing policies (`--sandbox`), and security controls (`--ask-for-approval`, `--yolo`). Key features include:
- **Image attachment** (`--image/-i`) for multi-file support via comma-separated paths.
- **Configuration overrides** (`--config/-c`) for runtime JSON or string-based settings.
- **Feature toggling** (`--enable`/`--disable`) for experimental capabilities.
- **Sandboxing modes** (`read-only`, `workspace-write`, `danger-full-access`) to restrict command execution.
- **Web search integration** (`--search`) for live vs. cached results.
- **Directory access control** (`--add-dir`) for workspace extensions.
- **TUI customization** (`--no-alt-screen`) and **auto-mode shortcuts** (`--full-auto`).
- **Profile-based config loading** (`--profile/-p`) from `~/.codex/config.toml`.
- **Experimental commands** like `codex app-server` and `codex debug app-server send-message-v

[Link to original](https://developers.openai.com/codex/cli/reference.md)
