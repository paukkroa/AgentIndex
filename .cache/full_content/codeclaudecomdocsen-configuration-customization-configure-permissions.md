[Skip to main content](#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘KAsk AI

Search...

Navigation

Configuration

Configure permissions

[Getting started](/docs/en/overview)[Build with Claude Code](/docs/en/sub-agents)[Deployment](/docs/en/third-party-integrations)[Administration](/docs/en/setup)[Configuration](/docs/en/settings)[Reference](/docs/en/cli-reference)[Resources](/docs/en/legal-and-compliance)

##### Configuration

* [Settings](/docs/en/settings)
* [Permissions](/docs/en/permissions)
* [Sandboxing](/docs/en/sandboxing)
* [Terminal configuration](/docs/en/terminal-config)
* [Model configuration](/docs/en/model-config)
* [Speed up responses with fast mode](/docs/en/fast-mode)
* [Memory management](/docs/en/memory)
* [Customize status line](/docs/en/statusline)
* [Customize keyboard shortcuts](/docs/en/keybindings)

On this page

* [Permission system](#permission-system)
* [Manage permissions](#manage-permissions)
* [Permission modes](#permission-modes)
* [Permission rule syntax](#permission-rule-syntax)
* [Match all uses of a tool](#match-all-uses-of-a-tool)
* [Use specifiers for fine-grained control](#use-specifiers-for-fine-grained-control)
* [Wildcard patterns](#wildcard-patterns)
* [Tool-specific permission rules](#tool-specific-permission-rules)
* [Bash](#bash)
* [Read and Edit](#read-and-edit)
* [WebFetch](#webfetch)
* [MCP](#mcp)
* [Task (subagents)](#task-subagents)
* [Extend permissions with hooks](#extend-permissions-with-hooks)
* [Working directories](#working-directories)
* [How permissions interact with sandboxing](#how-permissions-interact-with-sandboxing)
* [Managed settings](#managed-settings)
* [Managed-only settings](#managed-only-settings)
* [Settings precedence](#settings-precedence)
* [Example configurations](#example-configurations)
* [See also](#see-also)

Claude Code supports fine-grained permissions so that you can specify exactly what the agent is allowed to do and what it cannot. Permission settings can be checked into version control and distributed to all developers in your organization, as well as customized by individual developers.

## [​](#permission-system) Permission system

Claude Code uses a tiered permission system to balance power and safety:

| Tool type | Example | Approval required | ”Yes, don’t ask again” behavior |
| --- | --- | --- | --- |
| Read-only | File reads, Grep | No | N/A |
| Bash commands | Shell execution | Yes | Permanently per project directory and command |
| File modification | Edit/write files | Yes | Until session end |

## [​](#manage-permissions) Manage permissions

You can view and manage Claude Code’s tool permissions with `/permissions`. This UI lists all permission rules and the settings.json file they are sourced from.

* **Allow** rules let Claude Code use the specified tool without manual approval.
* **Ask** rules prompt for confirmation whenever Claude Code tries to use the specified tool.
* **Deny** rules prevent Claude Code from using the specified tool.

Rules are evaluated in order: **deny -> ask -> allow**. The first matching rule wins, so deny rules always take precedence.

## [​](#permission-modes) Permission modes

Claude Code supports several permission modes that control how tools are approved. Set the `defaultMode` in your [settings files](/docs/en/settings#settings-files):

| Mode | Description |
| --- | --- |
| `default` | Standard behavior: prompts for permission on first use of each tool |
| `acceptEdits` | Automatically accepts file edit permissions for the session |
| `plan` | Plan Mode: Claude can analyze but not modify files or execute commands |
| `dontAsk` | Auto-denies tools unless pre-approved via `/permissions` or `permissions.allow` rules |
| `bypassPermissions` | Skips all permission prompts (requires safe environment, see warning below) |

`bypassPermissions` mode disables all permission checks. Only use this in isolated environments like containers or VMs where Claude Code cannot cause damage. Administrators can prevent this mode by setting `disableBypassPermissionsMode` to `"disable"` in [managed settings](#managed-settings).

## [​](#permission-rule-syntax) Permission rule syntax

Permission rules follow the format `Tool` or `Tool(specifier)`.

### [​](#match-all-uses-of-a-tool) Match all uses of a tool

To match all uses of a tool, use just the tool name without parentheses:

| Rule | Effect |
| --- | --- |
| `Bash` | Matches all Bash commands |
| `WebFetch` | Matches all web fetch requests |
| `Read` | Matches all file reads |

`Bash(*)` is equivalent to `Bash` and matches all Bash commands.

### [​](#use-specifiers-for-fine-grained-control) Use specifiers for fine-grained control

Add a specifier in parentheses to match specific tool uses:

| Rule | Effect |
| --- | --- |
| `Bash(npm run build)` | Matches the exact command `npm run build` |
| `Read(./.env)` | Matches reading the `.env` file in the current directory |
| `WebFetch(domain:example.com)` | Matches fetch requests to example.com |

### [​](#wildcard-patterns) Wildcard patterns

Bash rules support glob patterns with `*`. Wildcards can appear at any position in the command. This configuration allows npm and git commit commands while blocking git push:

Report incorrect code

Copy

Ask AI

```
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(git commit *)",
      "Bash(git * main)",
      "Bash(* --version)",
      "Bash(* --help *)"
    ],
    "deny": [
      "Bash(git push *)"
    ]
  }
}
```

The space before `*` matters: `Bash(ls *)` matches `ls -la` but not `lsof`, while `Bash(ls*)` matches both. The legacy `:*` suffix syntax is equivalent to  `*` but is deprecated.

## [​](#tool-specific-permission-rules) Tool-specific permission rules

### [​](#bash) Bash

Bash permission rules support wildcard matching with `*`. Wildcards can appear at any position in the command, including at the beginning, middle, or end:

* `Bash(npm run build)` matches the exact Bash command `npm run build`
* `Bash(npm run test *)` matches Bash commands starting with `npm run test`
* `Bash(npm *)` matches any command starting with `npm`
* `Bash(* install)` matches any command ending with  `install`
* `Bash(git * main)` matches commands like `git checkout main`, `git merge main`

When `*` appears at the end with a space before it (like `Bash(ls *)`), it enforces a word boundary, requiring the prefix to be followed by a space or end-of-string. For example, `Bash(ls *)` matches `ls -la` but not `lsof`. In contrast, `Bash(ls*)` without a space matches both `ls -la` and `lsof` because there’s no word boundary constraint.

Claude Code is aware of shell operators (like `&&`) so a prefix match rule like `Bash(safe-cmd *)` won’t give it permission to run the command `safe-cmd && other-cmd`.

Bash permission patterns that try to constrain command arguments are fragile. For example, `Bash(curl http://github.com/ *)` intends to restrict curl to GitHub URLs, but won’t match variations like:

* Options before URL: `curl -X GET http://github.com/...`
* Different protocol: `curl https://github.com/...`
* Redirects: `curl -L http://bit.ly/xyz` (redirects to github)
* Variables: `URL=http://github.com && curl $URL`
* Extra spaces: `curl http://github.com`

For more reliable URL filtering, consider:

* **Restrict Bash network tools**: use deny rules to block `curl`, `wget`, and similar commands, then use the WebFetch tool with `WebFetch(domain:github.com)` permission for allowed domains
* **Use PreToolUse hooks**: implement a hook that validates URLs in Bash commands and blocks disallowed domains
* Instructing Claude Code about your allowed curl patterns via CLAUDE.md

Note that using WebFetch alone does not prevent network access. If Bash is allowed, Claude can still use `curl`, `wget`, or other tools to reach any URL.

### [​](#read-and-edit) Read and Edit

`Edit` rules apply to all built-in tools that edit files. Claude makes a best-effort attempt to apply `Read` rules to all built-in tools that read files like Grep and Glob.
Read and Edit rules both follow the [gitignore](https://git-scm.com/docs/gitignore) specification with four distinct pattern types:

| Pattern | Meaning | Example | Matches |
| --- | --- | --- | --- |
| `//path` | **Absolute** path from filesystem root | `Read(//Users/alice/secrets/**)` | `/Users/alice/secrets/**` |
| `~/path` | Path from **home** directory | `Read(~/Documents/*.pdf)` | `/Users/alice/Documents/*.pdf` |
| `/path` | Path **relative to settings file** | `Edit(/src/**/*.ts)` | `<settings file path>/src/**/*.ts` |
| `path` or `./path` | Path **relative to current directory** | `Read(*.env)` | `<cwd>/*.env` |

A pattern like `/Users/alice/file` is NOT an absolute path. It’s relative to your settings file. Use `//Users/alice/file` for absolute paths.

Examples:

* `Edit(/docs/**)`: edits in `<project>/docs/` (NOT `/docs/`)
* `Read(~/.zshrc)`: reads your home directory’s `.zshrc`
* `Edit(//tmp/scratch.txt)`: edits the absolute path `/tmp/scratch.txt`
* `Read(src/**)`: reads from `<current-directory>/src/`

In gitignore patterns, `*` matches files in a single directory while `**` matches recursively across directories. To allow all file access, use just the tool name without parentheses: `Read`, `Edit`, or `Write`.

### [​](#webfetch) WebFetch

* `WebFetch(domain:example.com)` matches fetch requests to example.com

### [​](#mcp) MCP

* `mcp__puppeteer` matches any tool provided by the `puppeteer` server (name configured in Claude Code)
* `mcp__puppeteer__*` wildcard syntax that also matches all tools from the `puppeteer` server
* `mcp__puppeteer__puppeteer_navigate` matches the `puppeteer_navigate` tool provided by the `puppeteer` server

### [​](#task-subagents) Task (subagents)

Use `Task(AgentName)` rules to control which [subagents](/docs/en/sub-agents) Claude can use:

* `Task(Explore)` matches the Explore subagent
* `Task(Plan)` matches the Plan subagent
* `Task(my-custom-agent)` matches a custom subagent named `my-custom-agent`

Add these rules to the `deny` array in your settings or use the `--disallowedTools` CLI flag to disable specific agents. To disable the Explore agent:

Report incorrect code

Copy

Ask AI

```
{
  "permissions": {
    "deny": ["Task(Explore)"]
  }
}
```

## [​](#extend-permissions-with-hooks) Extend permissions with hooks

[Claude Code hooks](/docs/en/hooks-guide) provide a way to register custom shell commands to perform permission evaluation at runtime. When Claude Code makes a tool call, PreToolUse hooks run before the permission system, and the hook output can determine whether to approve or deny the tool call in place of the permission system.

## [​](#working-directories) Working directories

By default, Claude has access to files in the directory where it was launched. You can extend this access:

* **During startup**: use `--add-dir <path>` CLI argument
* **During session**: use `/add-dir` command
* **Persistent configuration**: add to `additionalDirectories` in [settings files](/docs/en/settings#settings-files)

Files in additional directories follow the same permission rules as the original working directory: they become readable without prompts, and file editing permissions follow the current permission mode.

## [​](#how-permissions-interact-with-sandboxing) How permissions interact with sandboxing

Permissions and [sandboxing](/docs/en/sandboxing) are complementary security layers:

* **Permissions** control which tools Claude Code can use and which files or domains it can access. They apply to all tools (Bash, Read, Edit, WebFetch, MCP, and others).
* **Sandboxing** provides OS-level enforcement that restricts the Bash tool’s filesystem and network access. It applies only to Bash commands and their child processes.

Use both for defense-in-depth:

* Permission deny rules block Claude from even attempting to access restricted resources
* Sandbox restrictions prevent Bash commands from reaching resources outside defined boundaries, even if a prompt injection bypasses Claude’s decision-making
* Filesystem restrictions in the sandbox use Read and Edit deny rules, not separate sandbox configuration
* Network restrictions combine WebFetch permission rules with the sandbox’s `allowedDomains` list

## [​](#managed-settings) Managed settings

For organizations that need centralized control over Claude Code configuration, administrators can deploy `managed-settings.json` files to system directories. These policy files follow the same format as regular settings files and cannot be overridden by user or project settings. For organizations without device management infrastructure, [server-managed settings](/docs/en/server-managed-settings) provide an alternative that delivers configurations from Anthropic’s servers.
**Managed settings file locations**:

* **macOS**: `/Library/Application Support/ClaudeCode/managed-settings.json`
* **Linux and WSL**: `/etc/claude-code/managed-settings.json`
* **Windows**: `C:\Program Files\ClaudeCode\managed-settings.json`

These are system-wide paths (not user home directories like `~/Library/...`) that require administrator privileges. They are designed to be deployed by IT administrators.

### [​](#managed-only-settings) Managed-only settings

Some settings are only effective in managed settings:

| Setting | Description |
| --- | --- |
| `disableBypassPermissionsMode` | Set to `"disable"` to prevent `bypassPermissions` mode and the `--dangerously-skip-permissions` flag |
| `allowManagedPermissionRulesOnly` | When `true`, prevents user and project settings from defining `allow`, `ask`, or `deny` permission rules. Only rules in managed settings apply |
| `allowManagedHooksOnly` | When `true`, prevents loading of user, project, and plugin hooks. Only managed hooks and SDK hooks are allowed |
| `strictKnownMarketplaces` | Controls which plugin marketplaces users can add. See [managed marketplace restrictions](/docs/en/plugin-marketplaces#managed-marketplace-restrictions) |

## [​](#settings-precedence) Settings precedence

Permission rules follow the same [settings precedence](/docs/en/settings#settings-precedence) as all other Claude Code settings: managed settings have the highest precedence, followed by command line arguments, local project, shared project, and user settings.
If a permission is allowed in user settings but denied in project settings, the project setting takes precedence and the permission is blocked.

## [​](#example-configurations) Example configurations

This [repository](https://github.com/anthropics/claude-code/tree/main/examples/settings) includes starter settings configurations for common deployment scenarios. Use these as starting points and adjust them to fit your needs.

## [​](#see-also) See also

* [Settings](/docs/en/settings): complete configuration reference including the permission settings table
* [Sandboxing](/docs/en/sandboxing): OS-level filesystem and network isolation for Bash commands
* [Authentication](/docs/en/authentication): set up user access to Claude Code
* [Security](/docs/en/security): security safeguards and best practices
* [Hooks](/docs/en/hooks-guide): automate workflows and extend permission evaluation

Was this page helpful?

YesNo

[Settings](/docs/en/settings)[Sandboxing](/docs/en/sandboxing)

Assistant

Responses are generated using AI and may contain mistakes.