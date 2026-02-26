---
id: 0.0.5.2.2
title: "Use Codex in Slack"
nav_summary: "Trigger coding tasks in Slack via `@Codex` with prompts."
ref: https://developers.openai.com/codex/integrations/slack.md
ref_type: url
---

# Use Codex in Slack

The **Codex Slack integration** enables developers to initiate cloud-based coding tasks directly from Slack channels or threads by mentioning `@Codex` with a prompt. Users must first set up Codex cloud tasks (requiring a paid OpenAI plan, GitHub connection, and an environment) and install the Slack app via Codex settings. Tasks reference thread context automatically, but users can specify environments/repositories (e.g., `@Codex fix the above in openai/codex`). Codex processes requests against the default branch of the first repository in the selected environment’s repo map. For Enterprise users, admins can disable answer-posting in thread replies for security. Data handling adheres to OpenAI’s privacy policies, though users should verify outputs due to model limitations. Troubleshooting includes reconnecting accounts, manually overriding environments, or summarizing thread context for clarity.

---

[Link to original](https://developers.openai.com/codex/integrations/slack.md)
