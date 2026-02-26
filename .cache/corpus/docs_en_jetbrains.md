[Skip to main content](#content-area)

[Claude Code Docs home page](/docs)

English

Search...

⌘KAsk AI

Search...

Navigation

Platforms and integrations

JetBrains IDEs

[Getting started](/docs/en/overview)[Build with Claude Code](/docs/en/sub-agents)[Deployment](/docs/en/third-party-integrations)[Administration](/docs/en/setup)[Configuration](/docs/en/settings)[Reference](/docs/en/cli-reference)[Resources](/docs/en/legal-and-compliance)

##### Getting started

* [Overview](/docs/en/overview)
* [Quickstart](/docs/en/quickstart)
* [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

##### Core concepts

* [How Claude Code works](/docs/en/how-claude-code-works)
* [Extend Claude Code](/docs/en/features-overview)
* [Common workflows](/docs/en/common-workflows)
* [Best practices](/docs/en/best-practices)

##### Platforms and integrations

* [Claude Code on the web](/docs/en/claude-code-on-the-web)
* Claude Code on desktop
* [Chrome extension (beta)](/docs/en/chrome)
* [Visual Studio Code](/docs/en/vs-code)
* [JetBrains IDEs](/docs/en/jetbrains)
* [GitHub Actions](/docs/en/github-actions)
* [GitLab CI/CD](/docs/en/gitlab-ci-cd)
* [Claude Code in Slack](/docs/en/slack)

On this page

* [Supported IDEs](#supported-ides)
* [Features](#features)
* [Installation](#installation)
* [Marketplace Installation](#marketplace-installation)
* [Usage](#usage)
* [From Your IDE](#from-your-ide)
* [From External Terminals](#from-external-terminals)
* [Configuration](#configuration)
* [Claude Code Settings](#claude-code-settings)
* [Plugin Settings](#plugin-settings)
* [General Settings](#general-settings)
* [ESC Key Configuration](#esc-key-configuration)
* [Special Configurations](#special-configurations)
* [Remote Development](#remote-development)
* [WSL Configuration](#wsl-configuration)
* [Troubleshooting](#troubleshooting)
* [Plugin Not Working](#plugin-not-working)
* [IDE Not Detected](#ide-not-detected)
* [Command Not Found](#command-not-found)
* [Security Considerations](#security-considerations)

Claude Code integrates with JetBrains IDEs through a dedicated plugin, providing features like interactive diff viewing, selection context sharing, and more.

## [​](#supported-ides) Supported IDEs

The Claude Code plugin works with most JetBrains IDEs, including:

* IntelliJ IDEA
* PyCharm
* Android Studio
* WebStorm
* PhpStorm
* GoLand

## [​](#features) Features

* **Quick launch**: Use `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux) to open Claude Code directly from your editor, or click the Claude Code button in the UI
* **Diff viewing**: Code changes can be displayed directly in the IDE diff viewer instead of the terminal
* **Selection context**: The current selection/tab in the IDE is automatically shared with Claude Code
* **File reference shortcuts**: Use `Cmd+Option+K` (Mac) or `Alt+Ctrl+K` (Linux/Windows) to insert file references (for example, @File#L1-99)
* **Diagnostic sharing**: Diagnostic errors (lint, syntax, etc.) from the IDE are automatically shared with Claude as you work

## [​](#installation) Installation

### [​](#marketplace-installation) Marketplace Installation

Find and install the [Claude Code plugin](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-) from the JetBrains marketplace and restart your IDE.
If you haven’t installed Claude Code yet, see [our quickstart guide](/docs/en/quickstart) for installation instructions.

After installing the plugin, you may need to restart your IDE completely for it to take effect.

## [​](#usage) Usage

### [​](#from-your-ide) From Your IDE

Run `claude` from your IDE’s integrated terminal, and all integration features will be active.

### [​](#from-external-terminals) From External Terminals

Use the `/ide` command in any external terminal to connect Claude Code to your JetBrains IDE and activate all features:

Report incorrect code

Copy

Ask AI

```
claude
> /ide
```

If you want Claude to have access to the same files as your IDE, start Claude Code from the same directory as your IDE project root.

## [​](#configuration) Configuration

### [​](#claude-code-settings) Claude Code Settings

Configure IDE integration through Claude Code’s settings:

1. Run `claude`
2. Enter the `/config` command
3. Set the diff tool to `auto` for automatic IDE detection

### [​](#plugin-settings) Plugin Settings

Configure the Claude Code plugin by going to **Settings → Tools → Claude Code [Beta]**:

#### [​](#general-settings) General Settings

* **Claude command**: Specify a custom command to run Claude (for example, `claude`, `/usr/local/bin/claude`, or `npx @anthropic/claude`)
* **Suppress notification for Claude command not found**: Skip notifications about not finding the Claude command
* **Enable using Option+Enter for multi-line prompts** (macOS only): When enabled, Option+Enter inserts new lines in Claude Code prompts. Disable if experiencing issues with the Option key being captured unexpectedly (requires terminal restart)
* **Enable automatic updates**: Automatically check for and install plugin updates (applied on restart)

For WSL users: Set `wsl -d Ubuntu -- bash -lic "claude"` as your Claude command (replace `Ubuntu` with your WSL distribution name)

#### [​](#esc-key-configuration) ESC Key Configuration

If the ESC key doesn’t interrupt Claude Code operations in JetBrains terminals:

1. Go to **Settings → Tools → Terminal**
2. Either:
   * Uncheck “Move focus to the editor with Escape”, or
   * Click “Configure terminal keybindings” and delete the “Switch focus to Editor” shortcut
3. Apply the changes

This allows the ESC key to properly interrupt Claude Code operations.

## [​](#special-configurations) Special Configurations

### [​](#remote-development) Remote Development

When using JetBrains Remote Development, you must install the plugin in the remote host via **Settings → Plugin (Host)**.

The plugin must be installed on the remote host, not on your local client machine.

### [​](#wsl-configuration) WSL Configuration

WSL users may need additional configuration for IDE detection to work properly. See our [WSL troubleshooting guide](/docs/en/troubleshooting#jetbrains-ide-not-detected-on-wsl2) for detailed setup instructions.

WSL configuration may require:

* Proper terminal configuration
* Networking mode adjustments
* Firewall settings updates

## [​](#troubleshooting) Troubleshooting

### [​](#plugin-not-working) Plugin Not Working

* Ensure you’re running Claude Code from the project root directory
* Check that the JetBrains plugin is enabled in the IDE settings
* Completely restart the IDE (you may need to do this multiple times)
* For Remote Development, ensure the plugin is installed in the remote host

### [​](#ide-not-detected) IDE Not Detected

* Verify the plugin is installed and enabled
* Restart the IDE completely
* Check that you’re running Claude Code from the integrated terminal
* For WSL users, see the [WSL troubleshooting guide](/docs/en/troubleshooting#jetbrains-ide-not-detected-on-wsl2)

### [​](#command-not-found) Command Not Found

If clicking the Claude icon shows “command not found”:

1. Verify Claude Code is installed: `npm list -g @anthropic-ai/claude-code`
2. Configure the Claude command path in plugin settings
3. For WSL users, use the WSL command format mentioned in the configuration section

## [​](#security-considerations) Security Considerations

When Claude Code runs in a JetBrains IDE with auto-edit permissions enabled, it may be able to modify IDE configuration files that can be automatically executed by your IDE. This may increase the risk of running Claude Code in auto-edit mode and allow bypassing Claude Code’s permission prompts for bash execution.
When running in JetBrains IDEs, consider:

* Using manual approval mode for edits
* Taking extra care to ensure Claude is only used with trusted prompts
* Being aware of which files Claude Code has access to modify

For additional help, see our [troubleshooting guide](/docs/en/troubleshooting).

Was this page helpful?

YesNo

[Visual Studio Code](/docs/en/vs-code)[GitHub Actions](/docs/en/github-actions)

Assistant

Responses are generated using AI and may contain mistakes.