---
id: 0.0.5.2
title: "Security"
nav_summary: "Security: Permissions, Sandboxing, Privacy & Best Practices"
ref: https://code.claude.com/docs/en/security
ref_type: url
---

# Security

Claude Code’s **Security** documentation outlines a **multi-layered security framework** rooted in Anthropic’s rigorous security standards (SOC 2 Type 2, ISO 27001). Key features include a **permission-based architecture** enforcing strict read-only access by default, requiring explicit approval for actions like file edits or command execution (e.g., bash commands). Built-in protections include **sandboxed environments** for isolated filesystem/network operations, **write-access restrictions** (confined to the project directory), and **prompt fatigue mitigation** via allowlisting safe commands. Users retain full control over permissions, with safeguards against prompt injection, privacy risks, and unauthorized modifications. Additional protections cover **MCP (Model Configuration Protocol), IDE, and cloud execution security**, while best practices guide handling sensitive code and team collaboration. The documentation also emphasizes **user responsibility** in reviewing all proposed actions and provides channels for reporting security issues.

---

[Link to original](https://code.claude.com/docs/en/security)
