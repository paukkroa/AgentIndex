---
id: 0.0.5.2.1
title: "Use Codex in Linear"
nav_summary: "Integrate Codex AI for automated issue delegation in Linear."
ref: https://developers.openai.com/codex/integrations/linear.md
ref_type: url
---

# Use Codex in Linear

Codex integration in Linear enables automated task delegation by assigning issues to Codex or mentioning `@Codex` in comments, triggering cloud-based AI-driven execution. Available on paid plans (including Enterprise, requiring admin setup in ChatGPT workspace settings), this feature creates cloud tasks linked to GitHub repositories via Codex environments. Users can delegate work by assigning issues to Codex (like assigning to teammates) or tagging `@Codex` in comments, with progress tracked via **Activity** or direct task links. Codex dynamically selects repositories based on issue context or recent usage, defaulting to the primary repo in the environment’s repo map. Ambiguous requests prompt users to specify repositories (e.g., `@Codex fix this in openai/codex`). For Enterprise users, automated delegation via **Triage rules** streamlines workflows by auto-assigning issues to Codex based on predefined criteria. Task completion results in a summary and PR-ready link, with detailed progress visible in the task interface.

---

[Link to original](https://developers.openai.com/codex/integrations/linear.md)
