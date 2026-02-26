---
id: 0.0.7.4
title: "Checkpointing"
nav_summary: "Claude Code’s **checkpointing** feature provides automated, granular versioning of code edits during development sessions"
ref: https://code.claude.com/docs/en/checkpointing
ref_type: url
---

# Checkpointing

Claude Code’s **checkpointing** feature provides automated, granular versioning of code edits during development sessions. It captures file states before every edit, enabling seamless recovery via the `/rewind` command (triggered by `Esc` + `Esc`), which offers options to **restore code, conversation, or both** to prior checkpoints. Checkpoints persist across sessions (30-day retention by default) and are tied to user prompts, creating a safety net for iterative workflows. The **summarize** function condenses subsequent messages into a compact AI-generated summary while preserving earlier context, optimizing context window usage without altering disk files. Key distinctions include **restore** (reverting state) vs. **summarize** (compressing context), with the latter ideal for maintaining detailed early context while trimming later iterations. Use cases span **exploring alternatives**, **recovering from errors**, and **preserving experimental branches**—though it’s not a replacement for version control (e.g., Git). Limitations include untracked **Bash command changes** and **external file modifications**, emphasizing its role as a session-level safety mechanism rather than a full-fledged versioning system.

---
**NAVIGATIONAL

[Link to original](https://code.claude.com/docs/en/checkpointing)
