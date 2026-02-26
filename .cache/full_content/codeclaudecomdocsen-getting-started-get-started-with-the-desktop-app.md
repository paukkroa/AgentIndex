[Skip to main content](#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘KAsk AI

Search...

Navigation

Claude Code on desktop

Get started with the desktop app

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

  + [Get started](/docs/en/desktop-quickstart)
  + [Use Desktop](/docs/en/desktop)
* [Chrome extension (beta)](/docs/en/chrome)
* [Visual Studio Code](/docs/en/vs-code)
* [JetBrains IDEs](/docs/en/jetbrains)
* [GitHub Actions](/docs/en/github-actions)
* [GitLab CI/CD](/docs/en/gitlab-ci-cd)
* [Claude Code in Slack](/docs/en/slack)

On this page

* [Install](#install)
* [Start your first session](#start-your-first-session)
* [Now what?](#now-what)
* [Coming from the CLI?](#coming-from-the-cli)
* [What’s next](#what%E2%80%99s-next)

The desktop app gives you Claude Code with a graphical interface: visual diff review, live app preview, GitHub PR monitoring with auto-merge, parallel sessions with Git worktree isolation, and the ability to run tasks remotely. No terminal required.
This page walks through installing the app and starting your first session. If you’re already set up, see [Use Claude Code Desktop](/docs/en/desktop) for the full reference.

![The Claude Code Desktop interface showing the Code tab selected, with a prompt box, permission mode selector set to Ask permissions, model picker, folder selector, and Local environment option](https://mintcdn.com/claude-code/CNLUpFGiXoc9mhvD/images/desktop-code-tab-light.png?fit=max&auto=format&n=CNLUpFGiXoc9mhvD&q=85&s=9a36a7a27b9f4c6f2e1c83bdb34f69ce)![The Claude Code Desktop interface in dark mode showing the Code tab selected, with a prompt box, permission mode selector set to Ask permissions, model picker, folder selector, and Local environment option](https://mintcdn.com/claude-code/CNLUpFGiXoc9mhvD/images/desktop-code-tab-dark.png?fit=max&auto=format&n=CNLUpFGiXoc9mhvD&q=85&s=5463defe81c459fb9b1f91f6a958cfb8)

The desktop app has three tabs:

* **Chat**: General conversation with no file access, similar to claude.ai.
* **Cowork**: An autonomous background agent that works on tasks in a cloud VM with its own environment. It can run independently while you do other work.
* **Code**: An interactive coding assistant with direct access to your local files. You review and approve each change in real time.

Chat and Cowork are covered in the [Claude Desktop support articles](https://support.claude.com/en/collections/16163169-claude-desktop). This page focuses on the **Code** tab.

Claude Code requires a [Pro, Max, Teams, or Enterprise subscription](https://claude.com/pricing).

## [​](#install) Install

1

Download the app

Download Claude for your platform.

[## macOS

Universal build for Intel and Apple Silicon](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs)[## Windows

For x64 processors](https://claude.ai/api/desktop/win32/x64/exe/latest/redirect?utm_source=claude_code&utm_medium=docs)

For Windows ARM64, [download here](https://claude.ai/api/desktop/win32/arm64/exe/latest/redirect?utm_source=claude_code&utm_medium=docs).Linux is not currently supported.

2

Sign in

Launch Claude from your Applications folder (macOS) or Start menu (Windows). Sign in with your Anthropic account.

3

Open the Code tab

Click the **Code** tab at the top center. If clicking Code prompts you to upgrade, you need to [subscribe to a paid plan](https://claude.com/pricing) first. If it prompts you to sign in online, complete the sign-in and restart the app. If you see a 403 error, see [authentication troubleshooting](/docs/en/desktop#403-or-authentication-errors-in-the-code-tab).

The desktop app includes Claude Code. You don’t need to install Node.js or the CLI separately. To use `claude` from the terminal, install the CLI separately. See [Get started with the CLI](/docs/en/quickstart).

## [​](#start-your-first-session) Start your first session

With the Code tab open, choose a project and give Claude something to do.

1

Choose an environment and folder

Select **Local** to run Claude on your machine using your files directly. Click **Select folder** and choose your project directory.

Start with a small project you know well. It’s the fastest way to see what Claude Code can do. On Windows, [Git](https://git-scm.com/downloads/win) must be installed for local sessions to work. Most Macs include Git by default.

You can also select:

* **Remote**: Run sessions on Anthropic’s cloud infrastructure that continue even if you close the app. Remote sessions use the same infrastructure as [Claude Code on the web](/docs/en/claude-code-on-the-web).
* **SSH**: Connect to a remote machine over SSH (your own servers, cloud VMs, or dev containers). Claude Code must be installed on the remote machine.

2

Choose a model

Select a model from the dropdown next to the send button. See [models](/docs/en/model-config#available-models) for a comparison of Opus, Sonnet, and Haiku. You cannot change the model after the session starts.

3

Tell Claude what to do

Type what you want Claude to do:

* `Find a TODO comment and fix it`
* `Add tests for the main function`
* `Create a CLAUDE.md with instructions for this codebase`

A [session](/docs/en/desktop#work-in-parallel-with-sessions) is a conversation with Claude about your code. Each session tracks its own context and changes, so you can work on multiple tasks without them interfering with each other.

4

Review and accept changes

By default, the Code tab starts in [Ask permissions mode](/docs/en/desktop#choose-a-permission-mode), where Claude proposes changes and waits for your approval before applying them. You’ll see:

1. A [diff view](/docs/en/desktop#review-changes-with-diff-view) showing exactly what will change in each file
2. Accept/Reject buttons to approve or decline each change
3. Real-time updates as Claude works through your request

If you reject a change, Claude will ask how you’d like to proceed differently. Your files aren’t modified until you accept.

## [​](#now-what) Now what?

You’ve made your first edit. For the full reference on everything Desktop can do, see [Use Claude Code Desktop](/docs/en/desktop). Here are some things to try next.
**Interrupt and steer.** You can interrupt Claude at any point. If it’s going down the wrong path, click the stop button or type your correction and press **Enter**. Claude stops what it’s doing and adjusts based on your input. You don’t have to wait for it to finish or start over.
**Give Claude more context.** Type `@filename` in the prompt box to pull a specific file into the conversation, attach images and PDFs using the attachment button, or drag and drop files directly into the prompt. The more context Claude has, the better the results. See [Add files and context](/docs/en/desktop#add-files-and-context-to-prompts).
**Use skills for repeatable tasks.** Type `/` or click **+** → **Slash commands** to browse [built-in commands](/docs/en/interactive-mode#built-in-commands), [custom skills](/docs/en/skills), and plugin skills. Skills are reusable prompts you can invoke whenever you need them, like code review checklists or deployment steps.
**Review changes before committing.** After Claude edits files, a `+12 -1` indicator appears. Click it to open the [diff view](/docs/en/desktop#review-changes-with-diff-view), review modifications file by file, and comment on specific lines. Claude reads your comments and revises. Click **Review code** to have Claude evaluate the diffs itself and leave inline suggestions.
**Adjust how much control you have.** Your [permission mode](/docs/en/desktop#choose-a-permission-mode) controls the balance. Ask permissions (default) requires approval before every edit. Auto accept edits auto-accepts file edits for faster iteration. Plan mode lets Claude map out an approach without touching any files, which is useful before a large refactor.
**Add plugins for more capabilities.** Click the **+** button next to the prompt box and select **Plugins** to browse and install [plugins](/docs/en/desktop#install-plugins) that add skills, agents, MCP servers, and more.
**Preview your app.** Click the **Preview** dropdown to run your dev server directly in the desktop. Claude can view the running app, test endpoints, inspect logs, and iterate on what it sees. See [Preview your app](/docs/en/desktop#preview-your-app).
**Track your pull request.** After opening a PR, Claude Code monitors CI check results and can automatically fix failures or merge the PR once all checks pass. See [Monitor pull request status](/docs/en/desktop#monitor-pull-request-status).
**Scale up when you’re ready.** Open [parallel sessions](/docs/en/desktop#work-in-parallel-with-sessions) from the sidebar to work on multiple tasks at once, each in its own Git worktree. Send [long-running work to the cloud](/docs/en/desktop#run-long-running-tasks-remotely) so it continues even if you close the app, or [continue a session on the web or in your IDE](/docs/en/desktop#continue-in-another-surface) if a task takes longer than expected. [Connect external tools](/docs/en/desktop#extend-claude-code) like GitHub, Slack, and Linear to bring your workflow together.

## [​](#coming-from-the-cli) Coming from the CLI?

Desktop runs the same engine as the CLI with a graphical interface. You can run both simultaneously on the same project, and they share configuration (CLAUDE.md files, MCP servers, hooks, skills, and settings). For a full comparison of features, flag equivalents, and what’s not available in Desktop, see [CLI comparison](/docs/en/desktop#coming-from-the-cli).

## [​](#what’s-next) What’s next

* [Use Claude Code Desktop](/docs/en/desktop): permission modes, parallel sessions, diff view, connectors, and enterprise configuration
* [Troubleshooting](/docs/en/desktop#troubleshooting): solutions to common errors and setup issues
* [Best practices](/docs/en/best-practices): tips for writing effective prompts and getting the most out of Claude Code
* [Common workflows](/docs/en/common-workflows): tutorials for debugging, refactoring, testing, and more

Was this page helpful?

YesNo

[Claude Code on the web](/docs/en/claude-code-on-the-web)[Use Desktop](/docs/en/desktop)

Assistant

Responses are generated using AI and may contain mistakes.