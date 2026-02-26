---
id: 0.0.5.3
title: "Codex GitHub Action"
nav_summary: "Automate Codex in GitHub Actions for PR reviews, CI checks, or tasks."
ref: https://developers.openai.com/codex/github-action.md
ref_type: url
---

# Codex GitHub Action

The **Codex GitHub Action** (`openai/codex-action@v1`) automates OpenAI Codex integration in CI/CD pipelines by installing the Codex CLI, launching the Responses API proxy (via an API key), and executing `codex exec` with configurable permissions. Key features include **non-interactive pull request reviews**, **CI/CD gating via quality checks**, and **repeatable tasks** (e.g., code reviews, migrations) without manual CLI management. It supports **inline prompts** (`prompt`) or **external files** (`prompt-file`), custom CLI flags via `codex-args`, and sandboxed execution modes (`workspace-write`, `read-only`, etc.). Prerequisites include a GitHub-secretized OpenAI API key, Linux/macOS runners (or Windows with `safety-strategy: unsafe`), and checked-out repository access. The example workflow demonstrates automated PR feedback by fetching base/head refs, running Codex with a predefined prompt, and posting results as PR comments.

---

[Link to original](https://developers.openai.com/codex/github-action.md)
