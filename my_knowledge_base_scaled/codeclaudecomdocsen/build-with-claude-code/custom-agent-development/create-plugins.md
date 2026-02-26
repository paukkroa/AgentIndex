---
id: 0.0.2.0.2
title: "Create plugins"
nav_summary: "Create reusable custom skills/agents via plugins (skills, hooks,"
ref: https://code.claude.com/docs/en/plugins
ref_type: url
---

# Create plugins

Claude Code plugins enable developers to extend the platform’s core functionality by encapsulating custom skills, agents, hooks, and Model Context Protocol (MCP) servers into reusable, versioned packages. This guide outlines the distinction between **standalone configurations** (ideal for project-specific, non-shared tweaks) and **plugins** (designed for team collaboration, version control, and marketplace distribution). Key components include a structured `plugin.json` manifest defining metadata, skills (e.g., `/plugin-name:hello`), LSP servers for IDE integration, and hooks for automation. The workflow begins with a **quickstart** (local testing via `--plugin-dir`), progresses through modular plugin architecture (e.g., organizing complex plugins with subdirectories), and covers advanced features like default settings, local testing, debugging, and migration from standalone configs. Plugins support **namespacing** (e.g., `/my-plugin:skill`) to avoid conflicts and integrate seamlessly with existing Claude Code workflows. Target audiences include both **plugin users** (who install/share plugins) and **developers** (who build, test, and publish them).

---

[Link to original](https://code.claude.com/docs/en/plugins)
