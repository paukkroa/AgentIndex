---
id: 0.0.7.1
title: "Agent internet access"
nav_summary: "Secure agent internet access: risks, allowlists, and HTTP method restrictions"
ref: https://developers.openai.com/codex/cloud/internet-access.md
ref_type: url
---

# Agent internet access

Agent internet access in Codex is disabled by default during the agent phase to enhance security, allowing only setup scripts to access the internet for dependency installation. Enabling internet access introduces risks such as **prompt injection** (e.g., malicious instructions in untrusted web content or READMEs), **data exfiltration** (e.g., leaking secrets via `POST` requests), **malware downloads**, or **license violations**. To mitigate these risks, restrict access to **specific domains** (via allowlists like *Common dependencies* or *None*) and **HTTP methods** (default to `GET`, `HEAD`, `OPTIONS`). The system supports per-environment configuration, with options like *Off* (block all access) or *On* (with granular restrictions). Preset domain lists (e.g., for GitHub, npm, Docker) streamline setup, but users must manually refine allowlists as needed. Critical safeguards include avoiding `POST`/`PUT` methods and validating agent output/logs for anomalies.

---

[Link to original](https://developers.openai.com/codex/cloud/internet-access.md)
