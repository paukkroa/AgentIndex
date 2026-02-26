---
id: 0.0.3.6
title: "Agent Skills"
nav_summary: "Modular task workflows for Codex via reusable skills (CLI/"
ref: https://developers.openai.com/codex/skills.md
ref_type: url
---

# Agent Skills

Agent Skills in Codex extend its capabilities by encapsulating task-specific workflows into reusable, modular components. Each skill is a self-contained directory structure comprising a mandatory `SKILL.md` file (defining metadata like `name`, `description`, and instructions) and optional subdirectories (`scripts/`, `references/`, `assets/`) for executable logic, documentation, or resources. Skills adhere to the **open agent skills standard**, enabling cross-team collaboration and community sharing. Codex employs **progressive disclosure** to optimize performance: it loads only metadata initially, deferring full `SKILL.md` parsing until a skill is invoked. Skills can be triggered explicitly (via CLI/IDE commands like `/skills` or `$`) or implicitly (based on task context matching the skill’s `description`). The built-in `$skill-creator` simplifies creation, though manual setup requires a `SKILL.md` with clear scope definitions. Skills are scoped to repositories, user directories, or system locations, with priority given to the closest matching scope. Updates are auto-detected, though a Codex restart may be required for changes to reflect.

---

[Link to original](https://developers.openai.com/codex/skills.md)
