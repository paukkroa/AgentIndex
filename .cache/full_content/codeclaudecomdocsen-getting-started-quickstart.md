[Skip to main content](#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘KAsk AI

Search...

Navigation

Getting started

Quickstart

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

* [Before you begin](#before-you-begin)
* [Step 1: Install Claude Code](#step-1-install-claude-code)
* [Step 2: Log in to your account](#step-2-log-in-to-your-account)
* [Step 3: Start your first session](#step-3-start-your-first-session)
* [Step 4: Ask your first question](#step-4-ask-your-first-question)
* [Step 5: Make your first code change](#step-5-make-your-first-code-change)
* [Step 6: Use Git with Claude Code](#step-6-use-git-with-claude-code)
* [Step 7: Fix a bug or add a feature](#step-7-fix-a-bug-or-add-a-feature)
* [Step 8: Test out other common workflows](#step-8-test-out-other-common-workflows)
* [Essential commands](#essential-commands)
* [Pro tips for beginners](#pro-tips-for-beginners)
* [What’s next?](#what%E2%80%99s-next)
* [Getting help](#getting-help)

This quickstart guide will have you using AI-powered coding assistance in just a few minutes. By the end, you’ll understand how to use Claude Code for common development tasks.

## [​](#before-you-begin) Before you begin

Make sure you have:

* A terminal or command prompt open
* A code project to work with
* A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise), [Claude Console](https://console.anthropic.com/) account, or access through a [supported cloud provider](/docs/en/third-party-integrations)

This guide covers the terminal CLI. Claude Code is also available on the [web](https://claude.ai/code), as a [desktop app](/docs/en/desktop), in [VS Code](/docs/en/vs-code) and [JetBrains IDEs](/docs/en/jetbrains), in [Slack](/docs/en/slack), and in CI/CD with [GitHub Actions](/docs/en/github-actions) and [GitLab](/docs/en/gitlab-ci-cd). See [all interfaces](/docs/en/overview#use-claude-code-everywhere).

## [​](#step-1-install-claude-code) Step 1: Install Claude Code

To install Claude Code, use one of the following methods:

* Native Install (Recommended)
* Homebrew
* WinGet

**macOS, Linux, WSL:**

Report incorrect code

Copy

Ask AI

```
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

Report incorrect code

Copy

Ask AI

```
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

Report incorrect code

Copy

Ask AI

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Native installations automatically update in the background to keep you on the latest version.

Report incorrect code

Copy

Ask AI

```
brew install --cask claude-code
```

Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically to get the latest features and security fixes.

Report incorrect code

Copy

Ask AI

```
winget install Anthropic.ClaudeCode
```

WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.

## [​](#step-2-log-in-to-your-account) Step 2: Log in to your account

Claude Code requires an account to use. When you start an interactive session with the `claude` command, you’ll need to log in:

Report incorrect code

Copy

Ask AI

```
claude
# You'll be prompted to log in on first use
```

Report incorrect code

Copy

Ask AI

```
/login
# Follow the prompts to log in with your account
```

You can log in using any of these account types:

* [Claude Pro, Max, Teams, or Enterprise](https://claude.com/pricing) (recommended)
* [Claude Console](https://console.anthropic.com/) (API access with pre-paid credits). On first login, a “Claude Code” workspace is automatically created in the Console for centralized cost tracking.
* [Amazon Bedrock, Google Vertex AI, or Microsoft Foundry](/docs/en/third-party-integrations) (enterprise cloud providers)

Once logged in, your credentials are stored and you won’t need to log in again. To switch accounts later, use the `/login` command.

## [​](#step-3-start-your-first-session) Step 3: Start your first session

Open your terminal in any project directory and start Claude Code:

Report incorrect code

Copy

Ask AI

```
cd /path/to/your/project
claude
```

You’ll see the Claude Code welcome screen with your session information, recent conversations, and latest updates. Type `/help` for available commands or `/resume` to continue a previous conversation.

After logging in (Step 2), your credentials are stored on your system. Learn more in [Credential Management](/docs/en/authentication#credential-management).

## [​](#step-4-ask-your-first-question) Step 4: Ask your first question

Let’s start with understanding your codebase. Try one of these commands:

Report incorrect code

Copy

Ask AI

```
what does this project do?
```

Claude will analyze your files and provide a summary. You can also ask more specific questions:

Report incorrect code

Copy

Ask AI

```
what technologies does this project use?
```

Report incorrect code

Copy

Ask AI

```
where is the main entry point?
```

Report incorrect code

Copy

Ask AI

```
explain the folder structure
```

You can also ask Claude about its own capabilities:

Report incorrect code

Copy

Ask AI

```
what can Claude Code do?
```

Report incorrect code

Copy

Ask AI

```
how do I create custom skills in Claude Code?
```

Report incorrect code

Copy

Ask AI

```
can Claude Code work with Docker?
```

Claude Code reads your files as needed - you don’t have to manually add context. Claude also has access to its own documentation and can answer questions about its features and capabilities.

## [​](#step-5-make-your-first-code-change) Step 5: Make your first code change

Now let’s make Claude Code do some actual coding. Try a simple task:

Report incorrect code

Copy

Ask AI

```
add a hello world function to the main file
```

Claude Code will:

1. Find the appropriate file
2. Show you the proposed changes
3. Ask for your approval
4. Make the edit

Claude Code always asks for permission before modifying files. You can approve individual changes or enable “Accept all” mode for a session.

## [​](#step-6-use-git-with-claude-code) Step 6: Use Git with Claude Code

Claude Code makes Git operations conversational:

Report incorrect code

Copy

Ask AI

```
what files have I changed?
```

Report incorrect code

Copy

Ask AI

```
commit my changes with a descriptive message
```

You can also prompt for more complex Git operations:

Report incorrect code

Copy

Ask AI

```
create a new branch called feature/quickstart
```

Report incorrect code

Copy

Ask AI

```
show me the last 5 commits
```

Report incorrect code

Copy

Ask AI

```
help me resolve merge conflicts
```

## [​](#step-7-fix-a-bug-or-add-a-feature) Step 7: Fix a bug or add a feature

Claude is proficient at debugging and feature implementation.
Describe what you want in natural language:

Report incorrect code

Copy

Ask AI

```
add input validation to the user registration form
```

Or fix existing issues:

Report incorrect code

Copy

Ask AI

```
there's a bug where users can submit empty forms - fix it
```

Claude Code will:

* Locate the relevant code
* Understand the context
* Implement a solution
* Run tests if available

## [​](#step-8-test-out-other-common-workflows) Step 8: Test out other common workflows

There are a number of ways to work with Claude:
**Refactor code**

Report incorrect code

Copy

Ask AI

```
refactor the authentication module to use async/await instead of callbacks
```

**Write tests**

Report incorrect code

Copy

Ask AI

```
write unit tests for the calculator functions
```

**Update documentation**

Report incorrect code

Copy

Ask AI

```
update the README with installation instructions
```

**Code review**

Report incorrect code

Copy

Ask AI

```
review my changes and suggest improvements
```

**Remember**: Claude Code is your AI pair programmer. Talk to it like you would a helpful colleague - describe what you want to achieve, and it will help you get there.

## [​](#essential-commands) Essential commands

Here are the most important commands for daily use:

| Command | What it does | Example |
| --- | --- | --- |
| `claude` | Start interactive mode | `claude` |
| `claude "task"` | Run a one-time task | `claude "fix the build error"` |
| `claude -p "query"` | Run one-off query, then exit | `claude -p "explain this function"` |
| `claude -c` | Continue most recent conversation in current directory | `claude -c` |
| `claude -r` | Resume a previous conversation | `claude -r` |
| `claude commit` | Create a Git commit | `claude commit` |
| `/clear` | Clear conversation history | `/clear` |
| `/help` | Show available commands | `/help` |
| `exit` or Ctrl+C | Exit Claude Code | `exit` |

See the [CLI reference](/docs/en/cli-reference) for a complete list of commands.

## [​](#pro-tips-for-beginners) Pro tips for beginners

For more, see [best practices](/docs/en/best-practices) and [common workflows](/docs/en/common-workflows).

Be specific with your requests

Instead of: “fix the bug”Try: “fix the login bug where users see a blank screen after entering wrong credentials”

Use step-by-step instructions

Break complex tasks into steps:

Report incorrect code

Copy

Ask AI

```
1. create a new database table for user profiles
2. create an API endpoint to get and update user profiles
3. build a webpage that allows users to see and edit their information
```

Let Claude explore first

Before making changes, let Claude understand your code:

Report incorrect code

Copy

Ask AI

```
analyze the database schema
```

Report incorrect code

Copy

Ask AI

```
build a dashboard showing products that are most frequently returned by our UK customers
```

Save time with shortcuts

* Press `?` to see all available keyboard shortcuts
* Use Tab for command completion
* Press ↑ for command history
* Type `/` to see all commands and skills

## [​](#what’s-next) What’s next?

Now that you’ve learned the basics, explore more advanced features:

[## How Claude Code works

Understand the agentic loop, built-in tools, and how Claude Code interacts with your project](/docs/en/how-claude-code-works)[## Best practices

Get better results with effective prompting and project setup](/docs/en/best-practices)[## Common workflows

Step-by-step guides for common tasks](/docs/en/common-workflows)[## Extend Claude Code

Customize with CLAUDE.md, skills, hooks, MCP, and more](/docs/en/features-overview)

## [​](#getting-help) Getting help

* **In Claude Code**: Type `/help` or ask “how do I…”
* **Documentation**: You’re here! Browse other guides
* **Community**: Join our [Discord](https://www.anthropic.com/discord) for tips and support

Was this page helpful?

YesNo

[Overview](/docs/en/overview)[Changelog](/docs/en/changelog)

Assistant

Responses are generated using AI and may contain mistakes.