---
id: 0.0.3.4
title: "Sandboxing"
nav_summary: "Sandboxing: OS-level isolation for secure agent execution"
ref: https://code.claude.com/docs/en/sandboxing
ref_type: url
---

# Sandboxing

Claude Code’s **sandboxing** implements OS-level security to isolate agent execution, eliminating repetitive permission prompts while maintaining strict access controls. It enforces **filesystem isolation** (default read/write to working directories) and **network isolation** (blocking unauthorized outbound connections) via OS primitives, reducing attack surfaces and enabling autonomous workflows. Key features include **boundary definition** (explicitly configured directories/hosts), **real-time notifications** for boundary violations, and **transparent operation** without sacrificing security. Advanced configurations allow custom proxy setups, integration with existing security tools, and granular permissions. While mitigating risks like prompt injection and unauthorized data exfiltration, limitations (e.g., OS-specific enforcement) and best practices (e.g., avoiding bypasses) must be considered for robust deployment.

---

[Link to original](https://code.claude.com/docs/en/sandboxing)
