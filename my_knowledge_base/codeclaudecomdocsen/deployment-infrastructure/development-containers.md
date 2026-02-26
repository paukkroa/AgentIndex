---
id: 0.0.4.6
title: "Development containers"
nav_summary: "Preconfigured Node.js dev containers with Docker, VS Code, and security controls."
ref: https://code.claude.com/docs/en/devcontainer
ref_type: url
---

# Development containers

The **Development Containers** feature in Claude Code provides a preconfigured, production-ready Node.js environment (Node.js 20) with enhanced security, developer tools, and seamless VS Code integration. Built using Docker and the **VS Code Dev Containers extension**, it offers isolation via a custom firewall, restricting network access to essential services only. Key components include:
- **`devcontainer.json`**: Configures container settings, extensions, and volume mounts.
- **`Dockerfile`**: Defines the base image and installed tools (e.g., Git, ZSH, `fzf`).
- **`init-firewall.sh`**: Enforces network security rules for restricted access.

Security measures include isolation and firewall protections, though **`--dangerously-skip-permissions`** bypasses safeguards for unattended operations (use only with trusted repositories). Features like session persistence, cross-platform compatibility (macOS/Windows/Linux), and pre-configured VS Code extensions streamline development. Follow security best practices and monitor activity to mitigate risks.

---

[Link to original](https://code.claude.com/docs/en/devcontainer)
