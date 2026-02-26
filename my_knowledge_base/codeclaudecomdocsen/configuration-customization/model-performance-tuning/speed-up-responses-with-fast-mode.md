---
id: 0.0.3.0.1
title: "Speed up responses with fast mode"
nav_summary: "Enable Opus 4.6 speed boost via `/fast` ("
ref: https://code.claude.com/docs/en/fast-mode
ref_type: url
---

# Speed up responses with fast mode

Fast mode is a **research preview** feature for **Claude Opus 4.6** that prioritizes **response speed** (2.5x faster) over cost efficiency by adjusting API configurations while maintaining identical model quality. Toggle it via `/fast` in the **Claude Code CLI or VS Code extension**, or set `"fastMode": true` in user settings. Pricing starts at **$30/150 MTok** (input/output) for <200K tokens, with a **50% discount** until **Feb 16, 2025**. Available to **subscription users (Pro/Max/Team/Enterprise)** and **Claude Console** via extra usage. Key tradeoffs include **higher per-token costs** (up to **$60/225 MTok** for >200K tokens) and **persistent activation** across sessions. Fast mode **auto-switches to Opus 4.6** if not already selected and shows a **↯ icon** during active use. Rate limits apply separately from subscription tiers.

---

[Link to original](https://code.claude.com/docs/en/fast-mode)
