---
id: 0.0.3.1
title: "Custom Prompts"
nav_summary: "Deprecated: Local Markdown prompts via `/prompts:name` (CLI/IDE)."
ref: https://developers.openai.com/codex/custom-prompts.md
ref_type: url
---

# Custom Prompts

Custom prompts in Codex (now deprecated) allow users to create reusable Markdown-based instructions stored locally in `~/.codex/prompts/` for invocation via slash commands (`/prompts:name`) in the CLI or IDE. Key features include **YAML front matter** for metadata (e.g., `description`, `argument-hint`), **placeholder expansion** (positional `$1–$9`, named `$KEY=value`, or literal `$$`), and **argument handling** (e.g., `FILES="path1 path2" PR_TITLE="..."`). Prompts require explicit invocation and are not shared across repositories; for shared/reusable workflows, **skills** are the recommended replacement. Updates require a Codex restart or session reload. Only Markdown files in the top-level `prompts/` directory are recognized.

---

[Link to original](https://developers.openai.com/codex/custom-prompts.md)
