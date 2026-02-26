---
id: 0.0.1.2
title: "Automations"
nav_summary: "Automate tasks via prompts, skills, and scheduled runs in isolated worktrees."
ref: https://developers.openai.com/codex/app/automations.md
ref_type: url
---

# Automations

Codex Automations streamline repetitive tasks by executing them in the background, either within isolated **worktrees** (for Git repos) or directly in project directories (for non-versioned projects). Users can define prompts, integrate **skills** for complex workflows, and schedule runs via a dedicated automation pane in the Codex app. Automations inherit sandbox settings (read-only, workspace-write, or full access), with **rules** enabling granular control over tool permissions. Testing prompts manually in threads first ensures clarity and safety before scheduling. Worktree cleanup is recommended for Git projects to avoid clutter, while security warnings emphasize elevated risks in full-access mode. Admins in managed environments can enforce restrictions.

---

[Link to original](https://developers.openai.com/codex/app/automations.md)
