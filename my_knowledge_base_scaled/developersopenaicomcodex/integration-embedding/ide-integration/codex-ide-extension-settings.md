---
id: 0.0.5.0.3
title: "Codex IDE extension settings"
nav_summary: "Customize Codex IDE extension via editor settings or CLI config."
ref: https://developers.openai.com/codex/ide/settings.md
ref_type: url
---

# Codex IDE extension settings

The **Codex IDE extension settings** allow users to customize the behavior of the Codex IDE extension within their editor (e.g., VS Code). Key settings include enabling **CodeLens for to-do comments** to auto-complete tasks via Codex, overriding the **UI language** (or auto-detecting), and controlling startup behavior (e.g., auto-opening the Codex sidebar). For advanced configurations like **default models, approvals, or sandbox settings**, users must edit the shared `~/.codex/config.toml` file instead of editor settings. The extension relies on the **Codex CLI**, with a dedicated setting (`chatgpt.cliExecutable`) for developers only. On **Windows**, users can configure Codex to run in **WSL (Windows Subsystem for Linux)** for enhanced security and performance, though this requires a VS Code reload. Settings are accessed via editor preferences, where users search for "Codex" or the specific setting name to modify values.

---

[Link to original](https://developers.openai.com/codex/ide/settings.md)
