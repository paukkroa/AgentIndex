---
id: 0.0.6.0
title: "Authentication"
nav_summary: "Authentication: OpenAI login methods, MFA, caching, security, and admin controls."
ref: https://developers.openai.com/codex/auth.md
ref_type: url
---

# Authentication

Codex supports **two authentication methods** for OpenAI integration: **ChatGPT subscription login** (via browser-based OAuth) or **API key-based access** (usage-billed via OpenAI’s platform). The **Codex Cloud** enforces **stronger security** (e.g., **multi-factor authentication (MFA)**) due to direct codebase access, requiring MFA for email/password logins or SSO users. Login credentials are **cached locally** (in `~/.codex/auth.json` or OS credential stores) for convenience but must be secured (never shared). Admins can **restrict login methods** (ChatGPT/API key) or **workspaces** via config files, while **headless environments** may require alternative CLI authentication workflows. Credential storage can be managed via `cli_auth_credentials_store` (file, keyring, or auto), balancing security and usability.

---

[Link to original](https://developers.openai.com/codex/auth.md)
