---
id: 0.0.7.2
title: "Cloud environments"
nav_summary: "Manage task environments, dependencies, and caching in isolated Docker containers."
ref: https://developers.openai.com/codex/cloud/environments.md
ref_type: url
---

# Cloud environments

Codex **cloud environments** enable precise control over task execution by defining dependencies, tools (e.g., linters/formatters), and environment variables. Tasks run in isolated Docker containers, where Codex checks out the specified repo branch/commit, executes setup scripts (and optional maintenance scripts for cached containers), and enforces internet access policies (default: restricted for agents). The **default `universal` image** pre-installs common languages/packages, but custom packages can be added via setup scripts. **Environment variables** persist throughout tasks, while **secrets** (encrypted) are only available during setup. Automatic dependency management supports `npm`, `yarn`, `pip`, etc., but complex setups require custom Bash scripts. **Container caching** (12-hour default) accelerates repeat tasks by reusing setup states, invalidating only on script/environment changes. Business/Enterprise users share caches across teams. Internet access is configurable per phase (setup vs. agent).

---

[Link to original](https://developers.openai.com/codex/cloud/environments.md)
