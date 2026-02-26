---
id: 0.0.4.4
title: "Enterprise network configuration"
nav_summary: "Enterprise proxy, CA certs, mTLS, network access rules"
ref: https://code.claude.com/docs/en/network-config
ref_type: url
---

# Enterprise network configuration

This page outlines **enterprise-grade network and security configurations** for Claude Code, enabling secure integration with corporate infrastructure. Key features include **proxy support** (HTTPS/HTTP with basic auth, excluding SOCKS), **custom CA certificate trust** via `NODE_EXTRA_CA_CERTS`, **mTLS authentication** (client cert/key/passphrase), and **network access controls** for Anthropic endpoints (`api.anthropic.com`, `claude.ai`, `platform.claude.com`). Environment variables (e.g., `HTTPS_PROXY`, `NO_PROXY`) and `settings.json` configurations centralize settings. Advanced auth (NTLM/Kerberos) requires an LLM Gateway. All configurations prioritize security and compliance for restricted environments.

---

[Link to original](https://code.claude.com/docs/en/network-config)
