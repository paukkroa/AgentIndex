---
id: 0.0.1.4.3
title: "Non-interactive mode"
nav_summary: "`Run Codex CLI scripts in non-interactive mode for CI/CD, JSON output, or structured data.`"
ref: https://developers.openai.com/codex/noninteractive.md
ref_type: url
---

# Non-interactive mode

Non-interactive mode enables automated execution of **Codex** via CLI (`codex exec`) for scripts, CI/CD pipelines, or serverless workflows, bypassing the interactive TUI. Key features include **streamed progress** (via `stderr`) and **final output** (via `stdout`), enabling redirection or piping (e.g., `tee`, `jq`). Critical controls include **sandbox permissions** (`--full-auto` for edits, `--sandbox danger-full-access` for broad access) and **ephemeral execution** (`--ephemeral` to avoid disk persistence). For machine-readable output, **JSON Lines (JSONL)** streams capture real-time events (e.g., `turn.completed`, `agent_message`), while `--output-schema` enforces structured JSON responses for downstream processing. Safety defaults restrict permissions, and MCP server validation ensures compliance. Use cases range from **release notes generation** to **risk assessments**, with outputs optionally saved to files (`-o`) or schemas.

---

[Link to original](https://developers.openai.com/codex/noninteractive.md)
