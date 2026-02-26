---
id: 0.0.2.0.1
title: "Extend Claude with skills"
nav_summary: "Customize Claude AI with skills via `SKILL.md` files"
ref: https://code.claude.com/docs/en/skills
ref_type: url
---

# Extend Claude with skills

Extend Claude with **customizable skills** by creating a `SKILL.md` file in `.claude/skills/` (or nested directories) to define AI-driven capabilities. Skills integrate with Claude’s toolkit, enabling automatic invocation for relevant queries or manual triggering via `/skill-name`. Key features include **frontmatter configuration** (e.g., `invocation: user` or `auto`), **supporting files** (e.g., code snippets, diagrams), **dynamic context injection**, and **subagent execution** for workflows. Skills adhere to the **Agent Skills open standard** but extend it with Claude-specific enhancements like **restricted access control** and **visual output generation**. Advanced patterns include argument passing, nested directory discovery, and integration with third-party tools. Skills replace legacy slash commands, offering richer functionality while maintaining backward compatibility.

---

[Link to original](https://code.claude.com/docs/en/skills)
