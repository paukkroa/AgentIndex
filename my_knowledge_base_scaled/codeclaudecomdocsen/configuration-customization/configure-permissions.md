---
id: 0.0.3.1
title: "Configure permissions"
nav_summary: "Fine-grained tool permissions with modes, rules, and sandbox integration."
ref: https://code.claude.com/docs/en/permissions
ref_type: url
---

# Configure permissions

Claude Code’s **permission system** enforces granular control over agent capabilities via a tiered hierarchy (read-only, Bash, file edits) with explicit approval workflows. Rules—**deny**, **ask**, or **allow**—are evaluated sequentially, with deny rules taking precedence. Permission modes (`default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`) dictate approval behavior, from interactive prompts to full auto-approval or restrictions. Tools like Bash, WebFetch, or Task subagents support **fine-grained rules** (e.g., wildcards, specifiers) and hooks for custom logic. Permissions interact with sandboxing to isolate risks, while **managed settings** enforce organizational policies. Configurations are version-controlled and customizable per user or project, ensuring flexibility and security.

---

[Link to original](https://code.claude.com/docs/en/permissions)
