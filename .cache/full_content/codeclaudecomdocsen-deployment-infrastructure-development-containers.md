[Skip to main content](#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘KAsk AI

Search...

Navigation

Deployment

Development containers

[Getting started](/docs/en/overview)[Build with Claude Code](/docs/en/sub-agents)[Deployment](/docs/en/third-party-integrations)[Administration](/docs/en/setup)[Configuration](/docs/en/settings)[Reference](/docs/en/cli-reference)[Resources](/docs/en/legal-and-compliance)

##### Deployment

* [Overview](/docs/en/third-party-integrations)
* [Amazon Bedrock](/docs/en/amazon-bedrock)
* [Google Vertex AI](/docs/en/google-vertex-ai)
* [Microsoft Foundry](/docs/en/microsoft-foundry)
* [Network configuration](/docs/en/network-config)
* [LLM gateway](/docs/en/llm-gateway)
* [Development containers](/docs/en/devcontainer)

On this page

* [Key features](#key-features)
* [Getting started in 4 steps](#getting-started-in-4-steps)
* [Configuration breakdown](#configuration-breakdown)
* [Security features](#security-features)
* [Customization options](#customization-options)
* [Example use cases](#example-use-cases)
* [Secure client work](#secure-client-work)
* [Team onboarding](#team-onboarding)
* [Consistent CI/CD environments](#consistent-ci%2Fcd-environments)
* [Related resources](#related-resources)

The reference [devcontainer setup](https://github.com/anthropics/claude-code/tree/main/.devcontainer) and associated [Dockerfile](https://github.com/anthropics/claude-code/blob/main/.devcontainer/Dockerfile) offer a preconfigured development container that you can use as is, or customize for your needs. This devcontainer works with the Visual Studio Code [Dev Containers extension](https://code.visualstudio.com/docs/devcontainers/containers) and similar tools.
The container’s enhanced security measures (isolation and firewall rules) allow you to run `claude --dangerously-skip-permissions` to bypass permission prompts for unattended operation.

While the devcontainer provides substantial protections, no system is completely immune to all attacks.
When executed with `--dangerously-skip-permissions`, devcontainers don’t prevent a malicious project from exfiltrating anything accessible in the devcontainer including Claude Code credentials.
We recommend only using devcontainers when developing with trusted repositories.
Always maintain good security practices and monitor Claude’s activities.

## [​](#key-features) Key features

* **Production-ready Node.js**: Built on Node.js 20 with essential development dependencies
* **Security by design**: Custom firewall restricting network access to only necessary services
* **Developer-friendly tools**: Includes git, ZSH with productivity enhancements, fzf, and more
* **Seamless VS Code integration**: Pre-configured extensions and optimized settings
* **Session persistence**: Preserves command history and configurations between container restarts
* **Works everywhere**: Compatible with macOS, Windows, and Linux development environments

## [​](#getting-started-in-4-steps) Getting started in 4 steps

1. Install VS Code and the Remote - Containers extension
2. Clone the [Claude Code reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer) repository
3. Open the repository in VS Code
4. When prompted, click “Reopen in Container” (or use Command Palette: Cmd+Shift+P → “Remote-Containers: Reopen in Container”)

## [​](#configuration-breakdown) Configuration breakdown

The devcontainer setup consists of three primary components:

* [**devcontainer.json**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/devcontainer.json): Controls container settings, extensions, and volume mounts
* [**Dockerfile**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/Dockerfile): Defines the container image and installed tools
* [**init-firewall.sh**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/init-firewall.sh): Establishes network security rules

## [​](#security-features) Security features

The container implements a multi-layered security approach with its firewall configuration:

* **Precise access control**: Restricts outbound connections to whitelisted domains only (npm registry, GitHub, Claude API, etc.)
* **Allowed outbound connections**: The firewall permits outbound DNS and SSH connections
* **Default-deny policy**: Blocks all other external network access
* **Startup verification**: Validates firewall rules when the container initializes
* **Isolation**: Creates a secure development environment separated from your main system

## [​](#customization-options) Customization options

The devcontainer configuration is designed to be adaptable to your needs:

* Add or remove VS Code extensions based on your workflow
* Modify resource allocations for different hardware environments
* Adjust network access permissions
* Customize shell configurations and developer tooling

## [​](#example-use-cases) Example use cases

### [​](#secure-client-work) Secure client work

Use devcontainers to isolate different client projects, ensuring code and credentials never mix between environments.

### [​](#team-onboarding) Team onboarding

New team members can get a fully configured development environment in minutes, with all necessary tools and settings pre-installed.

### [​](#consistent-ci/cd-environments) Consistent CI/CD environments

Mirror your devcontainer configuration in CI/CD pipelines to ensure development and production environments match.

## [​](#related-resources) Related resources

* [VS Code devcontainers documentation](https://code.visualstudio.com/docs/devcontainers/containers)
* [Claude Code security best practices](/docs/en/security)
* [Enterprise network configuration](/docs/en/network-config)

Was this page helpful?

YesNo

[LLM gateway](/docs/en/llm-gateway)

Assistant

Responses are generated using AI and may contain mistakes.