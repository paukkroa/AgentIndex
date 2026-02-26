---
id: 0.0.10
title: "Workflows"
nav_summary: "Codex workflows: IDE/CLI examples for codebase docs"
ref: https://developers.openai.com/codex/workflows.md
ref_type: url
---

# Workflows

The **Workflows** page provides end-to-end examples for leveraging Codex (IDE extension, CLI, or cloud) to onboard, debug, and test code. It emphasizes structured workflows with **context-aware prompts**, **verification steps**, and **surface-specific optimizations** (e.g., IDE auto-context vs. CLI explicit file attachment). Key workflows include:
- **Codebase Explanation**: Use IDE for local exploration (select code + prompt) or CLI for transcript-driven analysis (attach files via `@`/`/mention`). Verification includes diagrams or checklists.
- **Bug Fixing**: CLI enables tight loops with reproduction steps + constraints; IDE focuses on targeted file selection. Verification involves re-running repros or test suites.
- **Test Writing**: IDE-based selection of function lines to generate targeted tests.
*Context notes* clarify what Codex auto-includes (e.g., open files in IDE) vs. what users must provide (e.g., file paths in CLI). Each workflow balances specificity (e.g., "backward compatibility rules") with actionable outputs (e.g., patch proposals).

---

[Link to original](https://developers.openai.com/codex/workflows.md)
