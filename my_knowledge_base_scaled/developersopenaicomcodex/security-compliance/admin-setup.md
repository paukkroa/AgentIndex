---
id: 0.0.6.2
title: "Admin Setup"
nav_summary: "Admin Guide: Secure Codex setup (local/cloud, RBAC, GitHub Connector)"
ref: https://developers.openai.com/codex/enterprise/admin-setup.md
ref_type: url
---

# Admin Setup

This guide outlines **Admin Setup for Codex in ChatGPT Enterprise**, emphasizing **enterprise-grade security** (no data training, AES-256 encryption, zero retention, and granular RBAC). It details **dual deployment modes**: **local** (sandboxed CLI/IDE/app) and **cloud** (GitHub-hosted workflows via Slack/Code Review). Local setup requires enabling **"Allow members to use Codex Local"** in workspace settings, while cloud setup mandates **GitHub repository access** and activating the **GitHub Connector**. Admins can enforce **Team Config** via `config.toml` (defaults), `rules/` (command restrictions), and `skills/` (shared capabilities) to standardize workflows. Cloud access is managed via **RBAC**, with a **10-minute propagation delay** post-enablement.

---

[Link to original](https://developers.openai.com/codex/enterprise/admin-setup.md)
