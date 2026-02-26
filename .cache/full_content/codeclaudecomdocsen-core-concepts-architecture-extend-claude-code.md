[Skip to main content](#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘KAsk AI

Search...

Navigation

Core concepts

Extend Claude Code

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

* [Overview](#overview)
* [Match features to your goal](#match-features-to-your-goal)
* [Compare similar features](#compare-similar-features)
* [Understand how features layer](#understand-how-features-layer)
* [Combine features](#combine-features)
* [Understand context costs](#understand-context-costs)
* [Context cost by feature](#context-cost-by-feature)
* [Understand how features load](#understand-how-features-load)
* [Learn more](#learn-more)

Claude Code combines a model that reasons about your code with [built-in tools](/docs/en/how-claude-code-works#tools) for file operations, search, execution, and web access. The built-in tools cover most coding tasks. This guide covers the extension layer: features you add to customize what Claude knows, connect it to external services, and automate workflows.

For how the core agentic loop works, see [How Claude Code works](/docs/en/how-claude-code-works).

**New to Claude Code?** Start with [CLAUDE.md](/docs/en/memory) for project conventions. Add other extensions as you need them.

## [​](#overview) Overview

Extensions plug into different parts of the agentic loop:

* **[CLAUDE.md](/docs/en/memory)** adds persistent context Claude sees every session
* **[Skills](/docs/en/skills)** add reusable knowledge and invocable workflows
* **[MCP](/docs/en/mcp)** connects Claude to external services and tools
* **[Subagents](/docs/en/sub-agents)** run their own loops in isolated context, returning summaries
* **[Agent teams](/docs/en/agent-teams)** coordinate multiple independent sessions with shared tasks and peer-to-peer messaging
* **[Hooks](/docs/en/hooks)** run outside the loop entirely as deterministic scripts
* **[Plugins](/docs/en/plugins)** and **[marketplaces](/docs/en/plugin-marketplaces)** package and distribute these features

[Skills](/docs/en/skills) are the most flexible extension. A skill is a markdown file containing knowledge, workflows, or instructions. You can invoke skills with a slash command like `/deploy`, or Claude can load them automatically when relevant. Skills can run in your current conversation or in an isolated context via subagents.

## [​](#match-features-to-your-goal) Match features to your goal

Features range from always-on context that Claude sees every session, to on-demand capabilities you or Claude can invoke, to background automation that runs on specific events. The table below shows what’s available and when each one makes sense.

| Feature | What it does | When to use it | Example |
| --- | --- | --- | --- |
| **CLAUDE.md** | Persistent context loaded every conversation | Project conventions, “always do X” rules | ”Use pnpm, not npm. Run tests before committing.” |
| **Skill** | Instructions, knowledge, and workflows Claude can use | Reusable content, reference docs, repeatable tasks | `/review` runs your code review checklist; API docs skill with endpoint patterns |
| **Subagent** | Isolated execution context that returns summarized results | Context isolation, parallel tasks, specialized workers | Research task that reads many files but returns only key findings |
| **[Agent teams](/docs/en/agent-teams)** | Coordinate multiple independent Claude Code sessions | Parallel research, new feature development, debugging with competing hypotheses | Spawn reviewers to check security, performance, and tests simultaneously |
| **MCP** | Connect to external services | External data or actions | Query your database, post to Slack, control a browser |
| **Hook** | Deterministic script that runs on events | Predictable automation, no LLM involved | Run ESLint after every file edit |

**[Plugins](/docs/en/plugins)** are the packaging layer. A plugin bundles skills, hooks, subagents, and MCP servers into a single installable unit. Plugin skills are namespaced (like `/my-plugin:review`) so multiple plugins can coexist. Use plugins when you want to reuse the same setup across multiple repositories or distribute to others via a **[marketplace](/docs/en/plugin-marketplaces)**.

### [​](#compare-similar-features) Compare similar features

Some features can seem similar. Here’s how to tell them apart.

* Skill vs Subagent
* CLAUDE.md vs Skill
* Subagent vs Agent team
* MCP vs Skill

Skills and subagents solve different problems:

* **Skills** are reusable content you can load into any context
* **Subagents** are isolated workers that run separately from your main conversation

| Aspect | Skill | Subagent |
| --- | --- | --- |
| **What it is** | Reusable instructions, knowledge, or workflows | Isolated worker with its own context |
| **Key benefit** | Share content across contexts | Context isolation. Work happens separately, only summary returns |
| **Best for** | Reference material, invocable workflows | Tasks that read many files, parallel work, specialized workers |

**Skills can be reference or action.** Reference skills provide knowledge Claude uses throughout your session (like your API style guide). Action skills tell Claude to do something specific (like `/deploy` that runs your deployment workflow).**Use a subagent** when you need context isolation or when your context window is getting full. The subagent might read dozens of files or run extensive searches, but your main conversation only receives a summary. Since subagent work doesn’t consume your main context, this is also useful when you don’t need the intermediate work to remain visible. Custom subagents can have their own instructions and can preload skills.**They can combine.** A subagent can preload specific skills (`skills:` field). A skill can run in isolated context using `context: fork`. See [Skills](/docs/en/skills) for details.

Both store instructions, but they load differently and serve different purposes.

| Aspect | CLAUDE.md | Skill |
| --- | --- | --- |
| **Loads** | Every session, automatically | On demand |
| **Can include files** | Yes, with `@path` imports | Yes, with `@path` imports |
| **Can trigger workflows** | No | Yes, with `/<name>` |
| **Best for** | ”Always do X” rules | Reference material, invocable workflows |

**Put it in CLAUDE.md** if Claude should always know it: coding conventions, build commands, project structure, “never do X” rules.**Put it in a skill** if it’s reference material Claude needs sometimes (API docs, style guides) or a workflow you trigger with `/<name>` (deploy, review, release).**Rule of thumb:** Keep CLAUDE.md under ~500 lines. If it’s growing, move reference content to skills.

Both parallelize work, but they’re architecturally different:

* **Subagents** run inside your session and report results back to your main context
* **Agent teams** are independent Claude Code sessions that communicate with each other

| Aspect | Subagent | Agent team |
| --- | --- | --- |
| **Context** | Own context window; results return to the caller | Own context window; fully independent |
| **Communication** | Reports results back to the main agent only | Teammates message each other directly |
| **Coordination** | Main agent manages all work | Shared task list with self-coordination |
| **Best for** | Focused tasks where only the result matters | Complex work requiring discussion and collaboration |
| **Token cost** | Lower: results summarized back to main context | Higher: each teammate is a separate Claude instance |

**Use a subagent** when you need a quick, focused worker: research a question, verify a claim, review a file. The subagent does the work and returns a summary. Your main conversation stays clean.**Use an agent team** when teammates need to share findings, challenge each other, and coordinate independently. Agent teams are best for research with competing hypotheses, parallel code review, and new feature development where each teammate owns a separate piece.**Transition point:** If you’re running parallel subagents but hitting context limits, or if your subagents need to communicate with each other, agent teams are the natural next step.

Agent teams are experimental and disabled by default. See [agent teams](/docs/en/agent-teams) for setup and current limitations.

MCP connects Claude to external services. Skills extend what Claude knows, including how to use those services effectively.

| Aspect | MCP | Skill |
| --- | --- | --- |
| **What it is** | Protocol for connecting to external services | Knowledge, workflows, and reference material |
| **Provides** | Tools and data access | Knowledge, workflows, reference material |
| **Examples** | Slack integration, database queries, browser control | Code review checklist, deploy workflow, API style guide |

These solve different problems and work well together:**MCP** gives Claude the ability to interact with external systems. Without MCP, Claude can’t query your database or post to Slack.**Skills** give Claude knowledge about how to use those tools effectively, plus workflows you can trigger with `/<name>`. A skill might include your team’s database schema and query patterns, or a `/post-to-slack` workflow with your team’s message formatting rules.Example: An MCP server connects Claude to your database. A skill teaches Claude your data model, common query patterns, and which tables to use for different tasks.

### [​](#understand-how-features-layer) Understand how features layer

Features can be defined at multiple levels: user-wide, per-project, via plugins, or through managed policies. You can also nest CLAUDE.md files in subdirectories or place skills in specific packages of a monorepo. When the same feature exists at multiple levels, here’s how they layer:

* **CLAUDE.md files** are additive: all levels contribute content to Claude’s context simultaneously. Files from your working directory and above load at launch; subdirectories load as you work in them. When instructions conflict, Claude uses judgment to reconcile them, with more specific instructions typically taking precedence. See [how Claude looks up memories](/docs/en/memory#how-claude-looks-up-memories).
* **Skills and subagents** override by name: when the same name exists at multiple levels, one definition wins based on priority (managed > user > project for skills; managed > CLI flag > project > user > plugin for subagents). Plugin skills are [namespaced](/docs/en/plugins#add-skills-to-your-plugin) to avoid conflicts. See [skill discovery](/docs/en/skills#where-skills-live) and [subagent scope](/docs/en/sub-agents#choose-the-subagent-scope).
* **MCP servers** override by name: local > project > user. See [MCP scope](/docs/en/mcp#scope-hierarchy-and-precedence).
* **Hooks** merge: all registered hooks fire for their matching events regardless of source. See [hooks](/docs/en/hooks).

### [​](#combine-features) Combine features

Each extension solves a different problem: CLAUDE.md handles always-on context, skills handle on-demand knowledge and workflows, MCP handles external connections, subagents handle isolation, and hooks handle automation. Real setups combine them based on your workflow.
For example, you might use CLAUDE.md for project conventions, a skill for your deployment workflow, MCP to connect to your database, and a hook to run linting after every edit. Each feature handles what it’s best at.

| Pattern | How it works | Example |
| --- | --- | --- |
| **Skill + MCP** | MCP provides the connection; a skill teaches Claude how to use it well | MCP connects to your database, a skill documents your schema and query patterns |
| **Skill + Subagent** | A skill spawns subagents for parallel work | `/review` skill kicks off security, performance, and style subagents that work in isolated context |
| **CLAUDE.md + Skills** | CLAUDE.md holds always-on rules; skills hold reference material loaded on demand | CLAUDE.md says “follow our API conventions,” a skill contains the full API style guide |
| **Hook + MCP** | A hook triggers external actions through MCP | Post-edit hook sends a Slack notification when Claude modifies critical files |

## [​](#understand-context-costs) Understand context costs

Every feature you add consumes some of Claude’s context. Too much can fill up your context window, but it can also add noise that makes Claude less effective; skills may not trigger correctly, or Claude may lose track of your conventions. Understanding these trade-offs helps you build an effective setup.

### [​](#context-cost-by-feature) Context cost by feature

Each feature has a different loading strategy and context cost:

| Feature | When it loads | What loads | Context cost |
| --- | --- | --- | --- |
| **CLAUDE.md** | Session start | Full content | Every request |
| **Skills** | Session start + when used | Descriptions at start, full content when used | Low (descriptions every request)\* |
| **MCP servers** | Session start | All tool definitions and schemas | Every request |
| **Subagents** | When spawned | Fresh context with specified skills | Isolated from main session |
| **Hooks** | On trigger | Nothing (runs externally) | Zero, unless hook returns additional context |

\*By default, skill descriptions load at session start so Claude can decide when to use them. Set `disable-model-invocation: true` in a skill’s frontmatter to hide it from Claude entirely until you invoke it manually. This reduces context cost to zero for skills you only trigger yourself.

### [​](#understand-how-features-load) Understand how features load

Each feature loads at different points in your session. The tabs below explain when each one loads and what goes into context.
![Context loading: CLAUDE.md and MCP load at session start and stay in every request. Skills load descriptions at start, full content on invocation. Subagents get isolated context. Hooks run externally.](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/images/context-loading.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=43114d93ae62bdc1ab6aa64660e2ba3b)

* CLAUDE.md
* Skills
* MCP servers
* Subagents
* Hooks

**When:** Session start**What loads:** Full content of all CLAUDE.md files (managed, user, and project levels).**Inheritance:** Claude reads CLAUDE.md files from your working directory up to the root, and discovers nested ones in subdirectories as it accesses those files. See [How Claude looks up memories](/docs/en/memory#how-claude-looks-up-memories) for details.

Keep CLAUDE.md under ~500 lines. Move reference material to skills, which load on-demand.

Skills are extra capabilities in Claude’s toolkit. They can be reference material (like an API style guide) or invocable workflows you trigger with `/<name>` (like `/deploy`). Some are built-in; you can also create your own. Claude uses skills when appropriate, or you can invoke one directly.**When:** Depends on the skill’s configuration. By default, descriptions load at session start and full content loads when used. For user-only skills (`disable-model-invocation: true`), nothing loads until you invoke them.**What loads:** For model-invocable skills, Claude sees names and descriptions in every request. When you invoke a skill with `/<name>` or Claude loads it automatically, the full content loads into your conversation.**How Claude chooses skills:** Claude matches your task against skill descriptions to decide which are relevant. If descriptions are vague or overlap, Claude may load the wrong skill or miss one that would help. To tell Claude to use a specific skill, invoke it with `/<name>`. Skills with `disable-model-invocation: true` are invisible to Claude until you invoke them.**Context cost:** Low until used. User-only skills have zero cost until invoked.**In subagents:** Skills work differently in subagents. Instead of on-demand loading, skills passed to a subagent are fully preloaded into its context at launch. Subagents don’t inherit skills from the main session; you must specify them explicitly.

Use `disable-model-invocation: true` for skills with side effects. This saves context and ensures only you trigger them.

**When:** Session start.**What loads:** All tool definitions and JSON schemas from connected servers.**Context cost:** [Tool search](/docs/en/mcp#scale-with-mcp-tool-search) (enabled by default) loads MCP tools up to 10% of context and defers the rest until needed.**Reliability note:** MCP connections can fail silently mid-session. If a server disconnects, its tools disappear without warning. Claude may try to use a tool that no longer exists. If you notice Claude failing to use an MCP tool it previously could access, check the connection with `/mcp`.

Run `/mcp` to see token costs per server. Disconnect servers you’re not actively using.

**When:** On demand, when you or Claude spawns one for a task.**What loads:** Fresh, isolated context containing:

* The system prompt (shared with parent for cache efficiency)
* Full content of skills listed in the agent’s `skills:` field
* CLAUDE.md and git status (inherited from parent)
* Whatever context the lead agent passes in the prompt

**Context cost:** Isolated from main session. Subagents don’t inherit your conversation history or invoked skills.

Use subagents for work that doesn’t need your full conversation context. Their isolation prevents bloating your main session.

**When:** On trigger. Hooks fire at specific lifecycle events like tool execution, session boundaries, prompt submission, permission requests, and compaction. See [Hooks](/docs/en/hooks) for the full list.**What loads:** Nothing by default. Hooks run as external scripts.**Context cost:** Zero, unless the hook returns output that gets added as messages to your conversation.

Hooks are ideal for side effects (linting, logging) that don’t need to affect Claude’s context.

## [​](#learn-more) Learn more

Each feature has its own guide with setup instructions, examples, and configuration options.

[## CLAUDE.md

Store project context, conventions, and instructions](/docs/en/memory)[## Skills

Give Claude domain expertise and reusable workflows](/docs/en/skills)[## Subagents

Offload work to isolated context](/docs/en/sub-agents)[## Agent teams

Coordinate multiple sessions working in parallel](/docs/en/agent-teams)[## MCP

Connect Claude to external services](/docs/en/mcp)[## Hooks

Automate workflows with hooks](/docs/en/hooks-guide)[## Plugins

Bundle and share feature sets](/docs/en/plugins)[## Marketplaces

Host and distribute plugin collections](/docs/en/plugin-marketplaces)

Was this page helpful?

YesNo

[How Claude Code works](/docs/en/how-claude-code-works)[Common workflows](/docs/en/common-workflows)

Assistant

Responses are generated using AI and may contain mistakes.