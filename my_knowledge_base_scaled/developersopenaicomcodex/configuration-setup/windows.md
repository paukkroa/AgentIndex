---
id: 0.0.2.5
title: "Windows"
nav_summary: "Windows: Native CLI/IDE or WSL2"
ref: https://developers.openai.com/codex/windows.md
ref_type: url
---

# Windows

The **Windows** documentation outlines two primary methods for running **Codex** on Windows: **native IDE/CLI setup** (with an experimental sandbox for restricted filesystem/network access) or **Windows Subsystem for Linux (WSL2)** for a Linux-like environment. The native approach uses an **AppContainer-based sandbox** to block unauthorized filesystem writes and network access outside the working directory, though it lacks full protection for world-writable folders (e.g., `C:\Users\Public`). For full compatibility, **WSL2** provides a Linux shell with Unix semantics, enabling seamless integration with VS Code via the **WSL extension**. Key steps include installing WSL (`wsl --install`), setting up Node.js (via `nvm`), and running Codex via `npm i -g @openai/codex`. Best practices recommend storing projects in the Linux home directory (`~/code/`) for performance, avoiding Windows-mounted paths (`/mnt/c/...`). The sandbox’s limitations (e.g., no write prevention in `Everyone`-accessible folders) can be mitigated by manually granting read access via `/sandbox-add-read-dir`.

---

[Link to original](https://developers.openai.com/codex/windows.md)
