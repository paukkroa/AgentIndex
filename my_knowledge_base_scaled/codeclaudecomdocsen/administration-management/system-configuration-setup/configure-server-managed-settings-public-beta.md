---
id: 0.0.5.0.1
title: "Configure server-managed settings (public beta)"
nav_summary: "Centralize Claude Code settings via web console (beta)"
ref: https://code.claude.com/docs/en/server-managed-settings
ref_type: url
---

# Configure server-managed settings (public beta)

Server-managed settings in Claude Code (public beta) enable administrators to centrally configure Claude Code via a web-based interface on **Claude.ai**, automatically pushing settings to authenticated users without requiring device management infrastructure (MDM). Ideal for organizations lacking MDM or managing unmanaged devices, this feature is available exclusively to **Claude for Teams/Enterprise** customers with compatible **Claude Code client versions** (2.1.38+ for Teams, 2.1.30+ for Enterprise). Settings are delivered via Anthropic’s servers during authentication, offering a simpler alternative to endpoint-managed configurations (which rely on MDM-deployed `managed-settings.json`). Key components include **access control**, **fetch/caching behavior**, **audit logging**, and **security considerations**, with precedence rules ensuring correct setting overrides. Limitations include platform availability constraints and evolving features before general availability.

---

[Link to original](https://code.claude.com/docs/en/server-managed-settings)
