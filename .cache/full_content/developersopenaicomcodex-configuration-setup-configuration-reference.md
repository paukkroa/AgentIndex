# Configuration Reference
Use this page as a searchable reference for Codex configuration files. For conceptual guidance and examples, start with [Config basics](https://developers.openai.com/codex/config-basic) and [Advanced Config](https://developers.openai.com/codex/config-advanced).
## `config.toml`
User-level configuration lives in `~/.codex/config.toml`. You can also add project-scoped overrides in `.codex/config.toml` files. Codex loads project-scoped config files only when you trust the project.
For sandbox and approval keys (`approval\_policy`, `sandbox\_mode`, and `sandbox\_workspace\_write.\*`), pair this reference with [Sandbox and approvals](https://developers.openai.com/codex/security#sandbox-and-approvals), [Protected paths in writable roots](https://developers.openai.com/codex/security#protected-paths-in-writable-roots), and [Network access](https://developers.openai.com/codex/security#network-access).
",
description:
'Additional writable roots when `sandbox\_mode = "workspace-write"`.',
},
{
key: "sandbox\_workspace\_write.network\_access",
type: "boolean",
description:
"Allow outbound network access inside the workspace-write sandbox.",
},
{
key: "sandbox\_workspace\_write.exclude\_tmpdir\_env\_var",
type: "boolean",
description:
"Exclude `$TMPDIR` from writable roots in workspace-write mode.",
},
{
key: "sandbox\_workspace\_write.exclude\_slash\_tmp",
type: "boolean",
description:
"Exclude `/tmp` from writable roots in workspace-write mode.",
},
{
key: "notify",
type: "array",
description:
"Command invoked for notifications; receives a JSON payload from Codex.",
},
{
key: "check\_for\_update\_on\_startup",
type: "boolean",
description:
"Check for Codex updates on startup (set to false only when updates are centrally managed).",
},
{
key: "feedback.enabled",
type: "boolean",
description:
"Enable feedback submission via `/feedback` across Codex surfaces (default: true).",
},
{
key: "instructions",
type: "string",
description:
"Reserved for future use; prefer `model\_instructions\_file` or `AGENTS.md`.",
},
{
key: "developer\_instructions",
type: "string",
description:
"Additional developer instructions injected into the session (optional).",
},
{
key: "log\_dir",
type: "string (path)",
description:
"Directory where Codex writes log files (for example `codex-tui.log`); defaults to `$CODEX\_HOME/log`.",
},
{
key: "compact\_prompt",
type: "string",
description: "Inline override for the history compaction prompt.",
},
{
key: "model\_instructions\_file",
type: "string (path)",
description:
"Replacement for built-in instructions instead of `AGENTS.md`.",
},
{
key: "personality",
type: "none | friendly | pragmatic",
description:
"Default communication style for models that advertise `supportsPersonality`; can be overridden per thread/turn or via `/personality`.",
},
{
key: "experimental\_compact\_prompt\_file",
type: "string (path)",
description:
"Load the compaction prompt override from a file (experimental).",
},
{
key: "skills.config",
type: "array",
description: "Per-skill enablement overrides stored in config.toml.",
},
{
key: "skills.config..path",
type: "string (path)",
description: "Path to a skill folder containing `SKILL.md`.",
},
{
key: "skills.config..enabled",
type: "boolean",
description: "Enable or disable the referenced skill.",
},
{
key: "apps..enabled",
type: "boolean",
description:
"Enable or disable a specific app/connector by id (default: true).",
},
{
key: "apps..disabled\_reason",
type: "unknown | user",
description:
"Optional reason attached when an app/connector is disabled.",
},
{
key: "features.apps",
type: "boolean",
description: "Enable ChatGPT Apps/connectors support (experimental).",
},
{
key: "features.apps\_mcp\_gateway",
type: "boolean",
description:
"Route Apps MCP calls through the OpenAI connectors MCP gateway (`https://api.openai.com/v1/connectors/mcp/`) instead of legacy routing (experimental).",
},
{
key: "mcp\_servers..command",
type: "string",
description: "Launcher command for an MCP stdio server.",
},
{
key: "mcp\_servers..args",
type: "array",
description: "Arguments passed to the MCP stdio server command.",
},
{
key: "mcp\_servers..env",
type: "map",
description: "Environment variables forwarded to the MCP stdio server.",
},
{
key: "mcp\_servers..env\_vars",
type: "array",
description:
"Additional environment variables to whitelist for an MCP stdio server.",
},
{
key: "mcp\_servers..cwd",
type: "string",
description: "Working directory for the MCP stdio server process.",
},
{
key: "mcp\_servers..url",
type: "string",
description: "Endpoint for an MCP streamable HTTP server.",
},
{
key: "mcp\_servers..bearer\_token\_env\_var",
type: "string",
description:
"Environment variable sourcing the bearer token for an MCP HTTP server.",
},
{
key: "mcp\_servers..http\_headers",
type: "map",
description: "Static HTTP headers included with each MCP HTTP request.",
},
{
key: "mcp\_servers..env\_http\_headers",
type: "map",
description:
"HTTP headers populated from environment variables for an MCP HTTP server.",
},
{
key: "mcp\_servers..enabled",
type: "boolean",
description: "Disable an MCP server without removing its configuration.",
},
{
key: "mcp\_servers..required",
type: "boolean",
description:
"When true, fail startup/resume if this enabled MCP server cannot initialize.",
},
{
key: "mcp\_servers..startup\_timeout\_sec",
type: "number",
description:
"Override the default 10s startup timeout for an MCP server.",
},
{
key: "mcp\_servers..startup\_timeout\_ms",
type: "number",
description: "Alias for `startup\_timeout\_sec` in milliseconds.",
},
{
key: "mcp\_servers..tool\_timeout\_sec",
type: "number",
description:
"Override the default 60s per-tool timeout for an MCP server.",
},
{
key: "mcp\_servers..enabled\_tools",
type: "array",
description: "Allow list of tool names exposed by the MCP server.",
},
{
key: "mcp\_servers..disabled\_tools",
type: "array",
description:
"Deny list applied after `enabled\_tools` for the MCP server.",
},
{
key: "agents.max\_threads",
type: "number",
description:
"Maximum number of agent threads that can be open concurrently.",
},
{
key: "agents..description",
type: "string",
description:
"Role guidance shown to Codex when choosing and spawning that agent type.",
},
{
key: "agents..config\_file",
type: "string (path)",
description:
"Path to a TOML config layer for that role; relative paths resolve from the config file that declares the role.",
},
{
key: "features.unified\_exec",
type: "boolean",
description: "Use the unified PTY-backed exec tool (beta).",
},
{
key: "features.shell\_snapshot",
type: "boolean",
description:
"Snapshot shell environment to speed up repeated commands (beta).",
},
{
key: "features.apply\_patch\_freeform",
type: "boolean",
description: "Expose the freeform `apply\_patch` tool (experimental).",
},
{
key: "features.multi\_agent",
type: "boolean",
description:
"Enable multi-agent collaboration tools (`spawn\_agent`, `send\_input`, `resume\_agent`, `wait`, and `close\_agent`) (experimental; off by default).",
},
{
key: "features.personality",
type: "boolean",
description:
"Enable personality selection controls (stable; on by default).",
},
{
key: "features.web\_search",
type: "boolean",
description:
"Deprecated legacy toggle; prefer the top-level `web\_search` setting.",
},
{
key: "features.web\_search\_cached",
type: "boolean",
description:
'Deprecated legacy toggle. When `web\_search` is unset, true maps to `web\_search = "cached"`.',
},
{
key: "features.web\_search\_request",
type: "boolean",
description:
'Deprecated legacy toggle. When `web\_search` is unset, true maps to `web\_search = "live"`.',
},
{
key: "features.shell\_tool",
type: "boolean",
description:
"Enable the default `shell` tool for running commands (stable; on by default).",
},
{
key: "features.request\_rule",
type: "boolean",
description:
"Enable Smart approvals (`prefix\_rule` suggestions on escalation requests; stable; on by default).",
},
{
key: "features.search\_tool",
type: "boolean",
description:
"Enable `search\_tool\_bm25` for Apps tool discovery before invoking app MCP tools (experimental).",
},
{
key: "features.collaboration\_modes",
type: "boolean",
description:
"Enable collaboration modes such as plan mode (stable; on by default).",
},
{
key: "features.use\_linux\_sandbox\_bwrap",
type: "boolean",
description:
"Use the bubblewrap-based Linux sandbox pipeline (experimental; off by default).",
},
{
key: "features.experimental\_windows\_sandbox",
type: "boolean",
description: "Run the Windows restricted-token sandbox (experimental).",
},
{
key: "features.elevated\_windows\_sandbox",
type: "boolean",
description:
"Enable the elevated Windows sandbox pipeline (experimental).",
},
{
key: "features.remote\_models",
type: "boolean",
description:
"Refresh remote model list before showing readiness (experimental).",
},
{
key: "features.runtime\_metrics",
type: "boolean",
description:
"Show runtime metrics summary in TUI turn separators (experimental).",
},
{
key: "features.powershell\_utf8",
type: "boolean",
description: "Force PowerShell UTF-8 output (defaults to true).",
},
{
key: "features.child\_agents\_md",
type: "boolean",
description:
"Append AGENTS.md scope/precedence guidance even when no AGENTS.md is present (experimental).",
},
{
key: "suppress\_unstable\_features\_warning",
type: "boolean",
description:
"Suppress the warning that appears when under-development feature flags are enabled.",
},
{
key: "model\_providers..name",
type: "string",
description: "Display name for a custom model provider.",
},
{
key: "model\_providers..base\_url",
type: "string",
description: "API base URL for the model provider.",
},
{
key: "model\_providers..env\_key",
type: "string",
description: "Environment variable supplying the provider API key.",
},
{
key: "model\_providers..env\_key\_instructions",
type: "string",
description: "Optional setup guidance for the provider API key.",
},
{
key: "model\_providers..experimental\_bearer\_token",
type: "string",
description:
"Direct bearer token for the provider (discouraged; use `env\_key`).",
},
{
key: "model\_providers..requires\_openai\_auth",
type: "boolean",
description:
"The provider uses OpenAI authentication (defaults to false).",
},
{
key: "model\_providers..wire\_api",
type: "chat | responses",
description:
"Protocol used by the provider (defaults to `chat` if omitted).",
},
{
key: "model\_providers..query\_params",
type: "map",
description: "Extra query parameters appended to provider requests.",
},
{
key: "model\_providers..http\_headers",
type: "map",
description: "Static HTTP headers added to provider requests.",
},
{
key: "model\_providers..env\_http\_headers",
type: "map",
description:
"HTTP headers populated from environment variables when present.",
},
{
key: "model\_providers..request\_max\_retries",
type: "number",
description:
"Retry count for HTTP requests to the provider (default: 4).",
},
{
key: "model\_providers..stream\_max\_retries",
type: "number",
description: "Retry count for SSE streaming interruptions (default: 5).",
},
{
key: "model\_providers..stream\_idle\_timeout\_ms",
type: "number",
description:
"Idle timeout for SSE streams in milliseconds (default: 300000).",
},
{
key: "model\_reasoning\_effort",
type: "minimal | low | medium | high | xhigh",
description:
"Adjust reasoning effort for supported models (Responses API only; `xhigh` is model-dependent).",
},
{
key: "model\_reasoning\_summary",
type: "auto | concise | detailed | none",
description:
"Select reasoning summary detail or disable summaries entirely.",
},
{
key: "model\_verbosity",
type: "low | medium | high",
description:
"Control GPT-5 Responses API verbosity (defaults to `medium`).",
},
{
key: "model\_supports\_reasoning\_summaries",
type: "boolean",
description: "Force Codex to send or not send reasoning metadata.",
},
{
key: "shell\_environment\_policy.inherit",
type: "all | core | none",
description:
"Baseline environment inheritance when spawning subprocesses.",
},
{
key: "shell\_environment\_policy.ignore\_default\_excludes",
type: "boolean",
description:
"Keep variables containing KEY/SECRET/TOKEN before other filters run.",
},
{
key: "shell\_environment\_policy.exclude",
type: "array",
description:
"Glob patterns for removing environment variables after the defaults.",
},
{
key: "shell\_environment\_policy.include\_only",
type: "array",
description:
"Whitelist of patterns; when set only matching variables are kept.",
},
{
key: "shell\_environment\_policy.set",
type: "map",
description:
"Explicit environment overrides injected into every subprocess.",
},
{
key: "shell\_environment\_policy.experimental\_use\_profile",
type: "boolean",
description: "Use the user shell profile when spawning subprocesses.",
},
{
key: "project\_root\_markers",
type: "array",
description:
"List of project root marker filenames; used when searching parent directories for the project root.",
},
{
key: "project\_doc\_max\_bytes",
type: "number",
description:
"Maximum bytes read from `AGENTS.md` when building project instructions.",
},
{
key: "project\_doc\_fallback\_filenames",
type: "array",
description: "Additional filenames to try when `AGENTS.md` is missing.",
},
{
key: "profile",
type: "string",
description:
"Default profile applied at startup (equivalent to `--profile`).",
},
{
key: "profiles..\*",
type: "various",
description:
"Profile-scoped overrides for any of the supported configuration keys.",
},
{
key: "profiles..include\_apply\_patch\_tool",
type: "boolean",
description:
"Legacy name for enabling freeform apply\_patch; prefer `[features].apply\_patch\_freeform`.",
},
{
key: "profiles..web\_search",
type: "disabled | cached | live",
description:
'Profile-scoped web search mode override (default: `"cached"`).',
},
{
key: "profiles..personality",
type: "none | friendly | pragmatic",
description:
"Profile-scoped communication style override for supported models.",
},
{
key: "profiles..experimental\_use\_unified\_exec\_tool",
type: "boolean",
description:
"Legacy name for enabling unified exec; prefer `[features].unified\_exec`.",
},
{
key: "profiles..experimental\_use\_freeform\_apply\_patch",
type: "boolean",
description:
"Legacy name for enabling freeform apply\_patch; prefer `[features].apply\_patch\_freeform`.",
},
{
key: "profiles..oss\_provider",
type: "lmstudio | ollama",
description: "Profile-scoped OSS provider for `--oss` sessions.",
},
{
key: "history.persistence",
type: "save-all | none",
description:
"Control whether Codex saves session transcripts to history.jsonl.",
},
{
key: "tool\_output\_token\_limit",
type: "number",
description:
"Token budget for storing individual tool/function outputs in history.",
},
{
key: "history.max\_bytes",
type: "number",
description:
"If set, caps the history file size in bytes by dropping oldest entries.",
},
{
key: "file\_opener",
type: "vscode | vscode-insiders | windsurf | cursor | none",
description:
"URI scheme used to open citations from Codex output (default: `vscode`).",
},
{
key: "otel.environment",
type: "string",
description:
"Environment tag applied to emitted OpenTelemetry events (default: `dev`).",
},
{
key: "otel.exporter",
type: "none | otlp-http | otlp-grpc",
description:
"Select the OpenTelemetry exporter and provide any endpoint metadata.",
},
{
key: "otel.trace\_exporter",
type: "none | otlp-http | otlp-grpc",
description:
"Select the OpenTelemetry trace exporter and provide any endpoint metadata.",
},
{
key: "otel.log\_user\_prompt",
type: "boolean",
description:
"Opt in to exporting raw user prompts with OpenTelemetry logs.",
},
{
key: "otel.exporter..endpoint",
type: "string",
description: "Exporter endpoint for OTEL logs.",
},
{
key: "otel.exporter..protocol",
type: "binary | json",
description: "Protocol used by the OTLP/HTTP exporter.",
},
{
key: "otel.exporter..headers",
type: "map",
description: "Static headers included with OTEL exporter requests.",
},
{
key: "otel.trace\_exporter..endpoint",
type: "string",
description: "Trace exporter endpoint for OTEL logs.",
},
{
key: "otel.trace\_exporter..protocol",
type: "binary | json",
description: "Protocol used by the OTLP/HTTP trace exporter.",
},
{
key: "otel.trace\_exporter..headers",
type: "map",
description: "Static headers included with OTEL trace exporter requests.",
},
{
key: "otel.exporter..tls.ca-certificate",
type: "string",
description: "CA certificate path for OTEL exporter TLS.",
},
{
key: "otel.exporter..tls.client-certificate",
type: "string",
description: "Client certificate path for OTEL exporter TLS.",
},
{
key: "otel.exporter..tls.client-private-key",
type: "string",
description: "Client private key path for OTEL exporter TLS.",
},
{
key: "otel.trace\_exporter..tls.ca-certificate",
type: "string",
description: "CA certificate path for OTEL trace exporter TLS.",
},
{
key: "otel.trace\_exporter..tls.client-certificate",
type: "string",
description: "Client certificate path for OTEL trace exporter TLS.",
},
{
key: "otel.trace\_exporter..tls.client-private-key",
type: "string",
description: "Client private key path for OTEL trace exporter TLS.",
},
{
key: "tui",
type: "table",
description:
"TUI-specific options such as enabling inline desktop notifications.",
},
{
key: "tui.notifications",
type: "boolean | array",
description:
"Enable TUI notifications; optionally restrict to specific event types.",
},
{
key: "tui.notification\_method",
type: "auto | osc9 | bel",
description:
"Notification method for unfocused terminal notifications (default: auto).",
},
{
key: "tui.animations",
type: "boolean",
description:
"Enable terminal animations (welcome screen, shimmer, spinner) (default: true).",
},
{
key: "tui.alternate\_screen",
type: "auto | always | never",
description:
"Control alternate screen usage for the TUI (default: auto; auto skips it in Zellij to preserve scrollback).",
},
{
key: "tui.show\_tooltips",
type: "boolean",
description:
"Show onboarding tooltips in the TUI welcome screen (default: true).",
},
{
key: "tui.status\_line",
type: "array | null",
description:
"Ordered list of TUI footer status-line item identifiers. `null` disables the status line.",
},
{
key: "hide\_agent\_reasoning",
type: "boolean",
description:
"Suppress reasoning events in both the TUI and `codex exec` output.",
},
{
key: "show\_raw\_agent\_reasoning",
type: "boolean",
description:
"Surface raw reasoning content when the active model emits it.",
},
{
key: "disable\_paste\_burst",
type: "boolean",
description: "Disable burst-paste detection in the TUI.",
},
{
key: "windows\_wsl\_setup\_acknowledged",
type: "boolean",
description: "Track Windows onboarding acknowledgement (Windows only).",
},
{
key: "chatgpt\_base\_url",
type: "string",
description: "Override the base URL used during the ChatGPT login flow.",
},
{
key: "cli\_auth\_credentials\_store",
type: "file | keyring | auto",
description:
"Control where the CLI stores cached credentials (file-based auth.json vs OS keychain).",
},
{
key: "mcp\_oauth\_credentials\_store",
type: "auto | file | keyring",
description: "Preferred store for MCP OAuth credentials.",
},
{
key: "mcp\_oauth\_callback\_port",
type: "integer",
description:
"Optional fixed port for the local HTTP callback server used during MCP OAuth login. When unset, Codex binds to an ephemeral port chosen by the OS.",
},
{
key: "experimental\_use\_unified\_exec\_tool",
type: "boolean",
description:
"Legacy name for enabling unified exec; prefer `[features].unified\_exec` or `codex --enable unified\_exec`.",
},
{
key: "experimental\_use\_freeform\_apply\_patch",
type: "boolean",
description:
"Legacy name for enabling freeform apply\_patch; prefer `[features].apply\_patch\_freeform` or `codex --enable apply\_patch\_freeform`.",
},
{
key: "include\_apply\_patch\_tool",
type: "boolean",
description:
"Legacy name for enabling freeform apply\_patch; prefer `[features].apply\_patch\_freeform`.",
},
{
key: "tools.web\_search",
type: "boolean",
description:
"Deprecated legacy toggle for web search; prefer the top-level `web\_search` setting.",
},
{
key: "web\_search",
type: "disabled | cached | live",
description:
'Web search mode (default: `"cached"`; cached uses an OpenAI-maintained index and does not fetch live pages; if you use `--yolo` or another full access sandbox setting, it defaults to `"live"`). Use `"live"` to fetch the most recent data from the web, or `"disabled"` to remove the tool.',
},
{
key: "projects..trust\_level",
type: "string",
description:
'Mark a project or worktree as trusted or untrusted (`"trusted"` | `"untrusted"`). Untrusted projects skip project-scoped `.codex/` layers.',
},
{
key: "notice.hide\_full\_access\_warning",
type: "boolean",
description: "Track acknowledgement of the full access warning prompt.",
},
{
key: "notice.hide\_world\_writable\_warning",
type: "boolean",
description:
"Track acknowledgement of the Windows world-writable directories warning.",
},
{
key: "notice.hide\_rate\_limit\_model\_nudge",
type: "boolean",
description: "Track opt-out of the rate limit model switch reminder.",
},
{
key: "notice.hide\_gpt5\_1\_migration\_prompt",
type: "boolean",
description: "Track acknowledgement of the GPT-5.1 migration prompt.",
},
{
key: "notice.hide\_gpt-5.1-codex-max\_migration\_prompt",
type: "boolean",
description:
"Track acknowledgement of the gpt-5.1-codex-max migration prompt.",
},
{
key: "notice.model\_migrations",
type: "map",
description: "Track acknowledged model migrations as old->new mappings.",
},
{
key: "forced\_login\_method",
type: "chatgpt | api",
description: "Restrict Codex to a specific authentication method.",
},
{
key: "forced\_chatgpt\_workspace\_id",
type: "string (uuid)",
description: "Limit ChatGPT logins to a specific workspace identifier.",
},
]}
client:load
/>
You can find the latest JSON schema for `config.toml` [here](https://developers.openai.com/codex/config-schema.json).
To get autocompletion and diagnostics when editing `config.toml` in VS Code or Cursor, you can install the [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) extension and add this line to the top of your `config.toml`:
```toml
#:schema https://developers.openai.com/codex/config-schema.json
```
Note: Rename `experimental\_instructions\_file` to `model\_instructions\_file`. Codex deprecates the old key; update existing configs to the new name.
## `requirements.toml`
`requirements.toml` is an admin-enforced configuration file that constrains security-sensitive settings users can't override. For details, locations, and examples, see [Admin-enforced requirements](https://developers.openai.com/codex/security#admin-enforced-requirements-requirementstoml).
For ChatGPT Business and Enterprise users, Codex can also apply cloud-fetched
requirements. See the security page for precedence details.
",
description: "Allowed values for `approval\_policy`.",
},
{
key: "allowed\_sandbox\_modes",
type: "array",
description: "Allowed values for `sandbox\_mode`.",
},
{
key: "allowed\_web\_search\_modes",
type: "array",
description:
"Allowed values for `web\_search` (`disabled`, `cached`, `live`). `disabled` is always allowed; an empty list effectively allows only `disabled`.",
},
{
key: "mcp\_servers",
type: "table",
description:
"Allowlist of MCP servers that may be enabled. Both the server name (``) and its identity must match for the MCP server to be enabled. Any configured MCP server not in the allowlist (or with a mismatched identity) is disabled.",
},
{
key: "mcp\_servers..identity",
type: "table",
description:
"Identity rule for a single MCP server. Set either `command` (stdio) or `url` (streamable HTTP).",
},
{
key: "mcp\_servers..identity.command",
type: "string",
description:
"Allow an MCP stdio server when its `mcp\_servers..command` matches this command.",
},
{
key: "mcp\_servers..identity.url",
type: "string",
description:
"Allow an MCP streamable HTTP server when its `mcp\_servers..url` matches this URL.",
},
{
key: "rules",
type: "table",
description:
"Admin-enforced command rules merged with `.rules` files. Requirements rules must be restrictive.",
},
{
key: "rules.prefix\_rules",
type: "array

",
description:
"List of enforced prefix rules. Each rule must include `pattern` and `decision`.",
},
{
key: "rules.prefix\_rules[].pattern",
type: "array

",
description:
"Command prefix expressed as pattern tokens. Each token sets either `token` or `any\_of`.",
},
{
key: "rules.prefix\_rules[].pattern[].token",
type: "string",
description: "A single literal token at this position.",
},
{
key: "rules.prefix\_rules[].pattern[].any\_of",
type: "array",
description: "A list of allowed alternative tokens at this position.",
},
{
key: "rules.prefix\_rules[].decision",
type: "prompt | forbidden",
description:
"Required. Requirements rules can only prompt or forbid (not allow).",
},
{
key: "rules.prefix\_rules[].justification",
type: "string",
description:
"Optional non-empty rationale surfaced in approval prompts or rejection messages.",
},
]}
client:load
/>