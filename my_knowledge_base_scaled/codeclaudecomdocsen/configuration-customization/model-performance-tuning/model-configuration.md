---
id: 0.0.3.0.0
title: "Model configuration"
nav_summary: "Configure AI models via aliases, names, or settings for dynamic switching, restrictions, and performance tuning."
ref: https://code.claude.com/docs/en/model-config
ref_type: url
---

# Model configuration

The **Model Configuration** page in Claude Code Docs outlines how to manage and customize AI model selection, behavior, and performance within the application. Users can configure models via **aliases** (e.g., `default`, `sonnet`, `opus`, `haiku`) for convenience or specify exact model names (e.g., `claude-opus-4-6`) for precision. Key features include **dynamic switching** mid-session via `/model <alias|name>`, **startup/environment variable overrides**, and **persistent settings** in config files. Enterprise admins can enforce model restrictions via `availableModels` in settings. Advanced options include **context window adjustments** (e.g., `sonnet[1m]`), **special modes** like `opusplan`, and **effort-level tuning** for response speed/quality trade-offs. Environment variables (`ANTHROPIC_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`) further enable programmatic control. The page also covers **prompt caching**, **default model behavior**, and **third-party deployment pinning** for reproducibility.

---

[Link to original](https://code.claude.com/docs/en/model-config)
