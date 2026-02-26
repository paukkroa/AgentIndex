---
id: 0.0.2.3
title: "Output styles"
nav_summary: "Customize agent behavior via prompt-based output styles."
ref: https://code.claude.com/docs/en/output-styles
ref_type: url
---

# Output styles

Claude Code’s **Output Styles** enable flexible agent behavior while preserving core capabilities like local scripting, file operations, and TODO tracking. The system integrates three built-in styles—**Default** (optimized for engineering tasks), **Explanatory** (educational insights), and **Learning** (interactive, collaborative coding with `TODO(human)` prompts)—by modifying the system prompt to exclude generic instructions (e.g., conciseness) and append custom directives. Users can switch styles via `/output-style` commands or edit `.claude/settings.local.json`. Custom styles require Markdown files with frontmatter (e.g., `name`, `description`) and tailored instructions, allowing granular control over agent behavior (e.g., retaining coding instructions via `keep-coding-instructions: true`). Output styles differ from CLAUDE.md (static prompts), agents (multi-tasking), and skills (modular functions) by focusing on prompt-driven behavioral adjustments.

---

[Link to original](https://code.claude.com/docs/en/output-styles)
