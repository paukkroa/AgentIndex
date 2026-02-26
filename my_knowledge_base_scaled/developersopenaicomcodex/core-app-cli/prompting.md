---
id: 0.0.1.5
title: "Prompting"
nav_summary: "Guide Codex via prompts; manage threads (local/cloud) with context limits."
ref: https://developers.openai.com/codex/prompting.md
ref_type: url
---

# Prompting

The **Prompting** documentation explains how to interact with **Codex** by sending structured prompts to guide its actions, such as code generation, file edits, or debugging. Prompts trigger a loop where the model processes input, executes tasks (e.g., file operations or tool calls), and iterates until completion or cancellation. Effective prompting relies on clear instructions, verification steps (e.g., testing, linting), and breaking tasks into smaller, modular steps. **Threads** organize sessions, combining prompts and outputs, and can run locally (sandboxed for safety) or in the cloud (isolated environments for parallel work). Context—like file references or selected text—enhances accuracy, while the model’s **context window** limits input size, with automatic compaction for long tasks. Threads persist across sessions and support delegation from local/remote devices.

---

[Link to original](https://developers.openai.com/codex/prompting.md)
