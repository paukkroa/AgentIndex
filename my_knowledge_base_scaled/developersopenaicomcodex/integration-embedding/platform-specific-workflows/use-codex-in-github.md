---
id: 0.0.5.2.0
title: "Use Codex in GitHub"
nav_summary: "Automate PR reviews with Codex AI in GitHub"
ref: https://developers.openai.com/codex/integrations/github.md
ref_type: url
---

# Use Codex in GitHub

Use **Codex in GitHub** to automate code reviews directly within pull requests via AI-powered feedback. After enabling **Codex cloud** and activating **Code review** settings in your repository, trigger a review by commenting `@codex review` in a PR. Codex generates standardized, human-like feedback, including suggestions, warnings, and actionable insights. For automation, enable **Automatic reviews** to apply to all PRs. Customize review behavior via **`AGENTS.md`** files, where you define **review guidelines** (e.g., security checks, PII handling) or task-specific instructions (e.g., `@codex fix CI failures`). Codex adheres to the closest `AGENTS.md` file for each modified file, allowing granular control. Supports prioritized issues (P0/P1) and extendable tasks like documentation fixes or security audits.

---

[Link to original](https://developers.openai.com/codex/integrations/github.md)
