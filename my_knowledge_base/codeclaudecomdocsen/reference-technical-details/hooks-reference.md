---
id: 0.0.7.1
title: "Hooks reference"
nav_summary: "Customize system events via hooks, lifecycle, inputs/outputs, and event handlers."
ref: https://code.claude.com/docs/en/hooks
ref_type: url
---

# Hooks reference

The **Hooks reference** provides an in-depth guide to customizing and extending Claude Code’s functionality via hooks—a flexible mechanism for intercepting and modifying system events. It covers the **hook lifecycle** (trigger points like `SessionStart`, `PreToolUse`, or `TaskCompleted`), **resolution logic** (how hooks execute and interact with system inputs/outputs), and **configuration options** (matcher patterns, event-specific fields, and decision control). Key sections detail **hook locations** (skills, agents, or global), **input/output schemas** (JSON, exit codes, and dynamic fields), and **event-specific behaviors** (e.g., `PermissionRequest` or `PostToolUseFailure`). Advanced topics include **prompt/agent-based hooks**, **async execution**, and **background processing**, along with examples like multi-criteria stop conditions. The guide also explains **disabling/removing hooks**, **environment variable persistence**, and **menu navigation** (`/hooks`), empowering developers to build modular, event-driven workflows.

---

[Link to original](https://code.claude.com/docs/en/hooks)
