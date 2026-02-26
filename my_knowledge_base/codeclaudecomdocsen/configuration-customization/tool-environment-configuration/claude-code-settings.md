---
id: 0.0.3.3.0
title: "Claude Code settings"
nav_summary: "Claude Code’s **settings system** enables granular configuration via a **scope-based hierarchy** (Managed, User, Project, Local) to control behavior a"
ref: https://code.claude.com/docs/en/settings
ref_type: url
---

# Claude Code settings

Claude Code’s **settings system** enables granular configuration via a **scope-based hierarchy** (Managed, User, Project, Local) to control behavior across environments. Managed settings enforce enterprise-wide policies (e.g., security, compliance) via `managed-settings.json`, while **User-level** settings (stored in `~/.claude/`) apply globally across projects for personal preferences like plugins, API keys, or editor themes. **Project-level** configurations (in `.claude/` directories) standardize team tools (e.g., permissions, hooks) and are version-controlled via Git, whereas **Local** settings (`.claude/*.local.*`) allow per-repo overrides (e.g., experimental features). Key features include **permission rules** (syntax: `allow/deny <resource> <action>`), **sandboxing** (isolating tools like Bash), **fast mode** (optimizing response speed), and **hooks** (extending tool behavior). Settings precedence follows a **cascading model** (Managed > Project > User > Local), with **environment variables** and **plugins** (managed via `enabledPlugins`, `extraKnownMarketplaces`) further customizing functionality. Tools like **system prompts

[Link to original](https://code.claude.com/docs/en/settings)
