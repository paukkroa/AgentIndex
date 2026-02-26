# Advanced Configuration
Use these options when you need more control over providers, policies, and integrations. For a quick start, see [Config basics](https://developers.openai.com/codex/config-basic).
For background on project guidance, reusable capabilities, custom slash commands, multi-agent workflows, and integrations, see [Customization](https://developers.openai.com/codex/concepts/customization). For configuration keys, see [Configuration Reference](https://developers.openai.com/codex/config-reference).
## Profiles
Profiles let you save named sets of configuration values and switch between them from the CLI.
Profiles are experimental and may change or be removed in future releases.
Profiles are not currently supported in the Codex IDE extension.
Define profiles under `[profiles.]` in `config.toml`, then run `codex --profile `:
```toml
model = "gpt-5-codex"
approval\_policy = "on-request"
[profiles.deep-review]
model = "gpt-5-pro"
model\_reasoning\_effort = "high"
approval\_policy = "never"
[profiles.lightweight]
model = "gpt-4.1"
approval\_policy = "untrusted"
```
To make a profile the default, add `profile = "deep-review"` at the top level of `config.toml`. Codex loads that profile unless you override it on the command line.
## One-off overrides from the CLI
In addition to editing `~/.codex/config.toml`, you can override configuration for a single run from the CLI:
- Prefer dedicated flags when they exist (for example, `--model`).
- Use `-c` / `--config` when you need to override an arbitrary key.
Examples:
```shell
# Dedicated flag
codex --model gpt-5.2
# Generic key/value override (value is TOML, not JSON)
codex --config model='"gpt-5.2"'
codex --config sandbox\_workspace\_write.network\_access=true
codex --config 'shell\_environment\_policy.include\_only=["PATH","HOME"]'
```
Notes:
- Keys can use dot notation to set nested values (for example, `mcp\_servers.context7.enabled=false`).
- `--config` values are parsed as TOML. When in doubt, quote the value so your shell doesn't split it on spaces.
- If the value can't be parsed as TOML, Codex treats it as a string.
## Config and state locations
Codex stores its local state under `CODEX\_HOME` (defaults to `~/.codex`).
Common files you may see there:
- `config.toml` (your local configuration)
- `auth.json` (if you use file-based credential storage) or your OS keychain/keyring
- `history.jsonl` (if history persistence is enabled)
- Other per-user state such as logs and caches
For authentication details (including credential storage modes), see [Authentication](https://developers.openai.com/codex/auth). For the full list of configuration keys, see [Configuration Reference](https://developers.openai.com/codex/config-reference).
For shared defaults, rules, and skills checked into repos or system paths, see [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config).
If you just need to point the built-in OpenAI provider at an LLM proxy, router, or data-residency enabled project, set environment variable `OPENAI\_BASE\_URL` instead of defining a new provider. This overrides the default OpenAI endpoint without a `config.toml` change.
```shell
export OPENAI\_BASE\_URL="https://api.openai.com/v1"
codex
```
## Project config files (`.codex/config.toml`)
In addition to your user config, Codex reads project-scoped overrides from `.codex/config.toml` files inside your repo. Codex walks from the project root to your current working directory and loads every `.codex/config.toml` it finds. If multiple files define the same key, the closest file to your working directory wins.
For security, Codex loads project-scoped config files only when the project is trusted. If the project is untrusted, Codex ignores `.codex/config.toml` files in the project.
Relative paths inside a project config (for example, `experimental\_instructions\_file`) are resolved relative to the `.codex/` folder that contains the `config.toml`.
## Agent roles (`[agents]` in `config.toml`)
For multi-agent role configuration (`[agents]` in `config.toml`), see [Multi-agents](https://developers.openai.com/codex/multi-agent).
## Project root detection
Codex discovers project configuration (for example, `.codex/` layers and `AGENTS.md`) by walking up from the working directory until it reaches a project root.
By default, Codex treats a directory containing `.git` as the project root. To customize this behavior, set `project\_root\_markers` in `config.toml`:
```toml
# Treat a directory as the project root when it contains any of these markers.
project\_root\_markers = [".git", ".hg", ".sl"]
```
Set `project\_root\_markers = []` to skip searching parent directories and treat the current working directory as the project root.
## Custom model providers
A model provider defines how Codex connects to a model (base URL, wire API, and optional HTTP headers).
Define additional providers and point `model\_provider` at them:
```toml
model = "gpt-5.1"
model\_provider = "proxy"
[model\_providers.proxy]
name = "OpenAI using LLM proxy"
base\_url = "http://proxy.example.com"
env\_key = "OPENAI\_API\_KEY"
[model\_providers.ollama]
name = "Ollama"
base\_url = "http://localhost:11434/v1"
[model\_providers.mistral]
name = "Mistral"
base\_url = "https://api.mistral.ai/v1"
env\_key = "MISTRAL\_API\_KEY"
```
Add request headers when needed:
```toml
[model\_providers.example]
http\_headers = { "X-Example-Header" = "example-value" }
env\_http\_headers = { "X-Example-Features" = "EXAMPLE\_FEATURES" }
```
## OSS mode (local providers)
Codex can run against a local "open source" provider (for example, Ollama or LM Studio) when you pass `--oss`. If you pass `--oss` without specifying a provider, Codex uses `oss\_provider` as the default.
```toml
# Default local provider used with `--oss`
oss\_provider = "ollama" # or "lmstudio"
```
## Azure provider and per-provider tuning
```toml
[model\_providers.azure]
name = "Azure"
base\_url = "https://YOUR\_PROJECT\_NAME.openai.azure.com/openai"
env\_key = "AZURE\_OPENAI\_API\_KEY"
query\_params = { api-version = "2025-04-01-preview" }
wire\_api = "responses"
[model\_providers.openai]
request\_max\_retries = 4
stream\_max\_retries = 10
stream\_idle\_timeout\_ms = 300000
```
## ChatGPT customers using data residency
Projects created with [data residency](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt) enabled can create a model provider to update the base\_url with the [correct prefix](https://platform.openai.com/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency).
```toml
model\_provider = "openaidr"
[model\_providers.openaidr]
name = "OpenAI Data Residency"
base\_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix
```
## Model reasoning, verbosity, and limits
```toml
model\_reasoning\_summary = "none" # Disable summaries
model\_verbosity = "low" # Shorten responses
model\_supports\_reasoning\_summaries = true # Force reasoning
model\_context\_window = 128000 # Context window size
```
`model\_verbosity` applies only to providers using the Responses API. Chat Completions providers will ignore the setting.
## Approval policies and sandbox modes
Pick approval strictness (affects when Codex pauses) and sandbox level (affects file/network access).
For operational details that are easy to miss while editing `config.toml`, see [Common sandbox and approval combinations](https://developers.openai.com/codex/security#common-sandbox-and-approval-combinations), [Protected paths in writable roots](https://developers.openai.com/codex/security#protected-paths-in-writable-roots), and [Network access](https://developers.openai.com/codex/security#network-access).
```toml
approval\_policy = "untrusted" # Other options: on-request, never
sandbox\_mode = "workspace-write"
[sandbox\_workspace\_write]
exclude\_tmpdir\_env\_var = false # Allow $TMPDIR
exclude\_slash\_tmp = false # Allow /tmp
writable\_roots = ["/Users/YOU/.pyenv/shims"]
network\_access = false # Opt in to outbound network
```
Need the complete key list (including profile-scoped overrides and requirements constraints)? See [Configuration Reference](https://developers.openai.com/codex/config-reference) and [Managed configuration](https://developers.openai.com/codex/security#managed-configuration).
In workspace-write mode, some environments keep `.git/` and `.codex/`
read-only even when the rest of the workspace is writable. This is why
commands like `git commit` may still require approval to run outside the
sandbox. If you want Codex to skip specific commands (for example, block `git
commit` outside the sandbox), use
[rules](/codex/rules).
Disable sandboxing entirely (use only if your environment already isolates processes):
```toml
sandbox\_mode = "danger-full-access"
```
## Shell environment policy
`shell\_environment\_policy` controls which environment variables Codex passes to any subprocess it launches (for example, when running a tool-command the model proposes). Start from a clean start (`inherit = "none"`) or a trimmed set (`inherit = "core"`), then layer on excludes, includes, and overrides to avoid leaking secrets while still providing the paths, keys, or flags your tasks need.
```toml
[shell\_environment\_policy]
inherit = "none"
set = { PATH = "/usr/bin", MY\_FLAG = "1" }
ignore\_default\_excludes = false
exclude = ["AWS\_\*", "AZURE\_\*"]
include\_only = ["PATH", "HOME"]
```
Patterns are case-insensitive globs (`\*`, `?`, `[A-Z]`); `ignore\_default\_excludes = false` keeps the automatic KEY/SECRET/TOKEN filter before your includes/excludes run.
## MCP servers
See the dedicated [MCP documentation](https://developers.openai.com/codex/mcp) for configuration details.
## Observability and telemetry
Enable OpenTelemetry (OTel) log export to track Codex runs (API requests, SSE/events, prompts, tool approvals/results). Disabled by default; opt in via `[otel]`:
```toml
[otel]
environment = "staging" # defaults to "dev"
exporter = "none" # set to otlp-http or otlp-grpc to send events
log\_user\_prompt = false # redact user prompts unless explicitly enabled
```
Choose an exporter:
```toml
[otel]
exporter = { otlp-http = {
endpoint = "https://otel.example.com/v1/logs",
protocol = "binary",
headers = { "x-otlp-api-key" = "${OTLP\_TOKEN}" }
}}
```
```toml
[otel]
exporter = { otlp-grpc = {
endpoint = "https://otel.example.com:4317",
headers = { "x-otlp-meta" = "abc123" }
}}
```
If `exporter = "none"` Codex records events but sends nothing. Exporters batch asynchronously and flush on shutdown. Event metadata includes service name, CLI version, env tag, conversation id, model, sandbox/approval settings, and per-event fields (see [Config Reference](https://developers.openai.com/codex/config-reference)).
### What gets emitted
Codex emits structured log events for runs and tool usage. Representative event types include:
- `codex.conversation\_starts` (model, reasoning settings, sandbox/approval policy)
- `codex.api\_request` (attempt, status/success, duration, and error details)
- `codex.sse\_event` (stream event kind, success/failure, duration, plus token counts on `response.completed`)
- `codex.websocket\_request` and `codex.websocket\_event` (request duration plus per-message kind/success/error)
- `codex.user\_prompt` (length; content redacted unless explicitly enabled)
- `codex.tool\_decision` (approved/denied and whether the decision came from config vs user)
- `codex.tool\_result` (duration, success, output snippet)
### OTel metrics emitted
When the OTel metrics pipeline is enabled, Codex emits counters and duration histograms for API, stream, and tool activity.
Each metric below also includes default metadata tags: `auth\_mode`, `originator`, `session\_source`, `model`, and `app.version`.
| Metric | Type | Fields | Description |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api\_request` | counter | `status`, `success` | API request count by HTTP status and success/failure. |
| `codex.api\_request.duration\_ms` | histogram | `status`, `success` | API request duration in milliseconds. |
| `codex.sse\_event` | counter | `kind`, `success` | SSE event count by event kind and success/failure. |
| `codex.sse\_event.duration\_ms` | histogram | `kind`, `success` | SSE event processing duration in milliseconds. |
| `codex.websocket.request` | counter | `success` | WebSocket request count by success/failure. |
| `codex.websocket.request.duration\_ms` | histogram | `success` | WebSocket request duration in milliseconds. |
| `codex.websocket.event` | counter | `kind`, `success` | WebSocket message/event count by type and success/failure. |
| `codex.websocket.event.duration\_ms` | histogram | `kind`, `success` | WebSocket message/event processing duration in milliseconds. |
| `codex.tool.call` | counter | `tool`, `success` | Tool invocation count by tool name and success/failure. |
| `codex.tool.call.duration\_ms` | histogram | `tool`, `success` | Tool execution duration in milliseconds by tool name and outcome. |
For more security and privacy guidance around telemetry, see [Security](https://developers.openai.com/codex/security#monitoring-and-telemetry).
### Metrics
By default, Codex periodically sends a small amount of anonymous usage and health data back to OpenAI. This helps detect when Codex isn't working correctly and shows what features and configuration options are being used, so the Codex team can focus on what matters most. These metrics don't contain any personally identifiable information (PII). Metrics collection is independent of OTel log/trace export.
If you want to disable metrics collection entirely across Codex surfaces on a machine, set the analytics flag in your config:
```toml
[analytics]
enabled = false
```
Each metric includes its own fields plus the default context fields below.
#### Default context fields (applies to every event/metric)
- `auth\_mode`: `swic` | `api` | `unknown`.
- `model`: name of the model used.
- `app.version`: Codex version.
#### Metrics catalog
Each metric includes the required fields plus the default context fields above. Every metric is prefixed by `codex.`.
If a metric includes the `tool` field, it reflects the internal tool used (for example, `apply\_patch` or `shell`) and doesn't contain the actual shell command or patch `codex` is trying to apply.
| Metric | Type | Fields | Description |
| ---------------------------------------- | --------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `feature.state` | counter | `feature`, `value` | Feature values that differ from defaults (emit one row per non-default). |
| `thread.started` | counter | `is\_git` | New thread created. |
| `thread.fork` | counter | | New thread created by forking an existing thread. |
| `thread.rename` | counter | | Thread renamed. |
| `task.compact` | counter | `type` | Number of compactions per type (`remote` or `local`), including manual and auto. |
| `task.user\_shell` | counter | | Number of user shell actions (`!` in the TUI for example). |
| `task.review` | counter | | Number of reviews triggered. |
| `task.undo` | counter | | Number of undo actions triggered. |
| `approval.requested` | counter | `tool`, `approved` | Tool approval request result (`approved`, `approved\_with\_amendment`, `approved\_for\_session`, `denied`, `abort`). |
| `conversation.turn.count` | counter | | User/assistant turns per thread, recorded at the end of the thread. |
| `turn.e2e\_duration\_ms` | histogram | | End-to-end time for a full turn. |
| `mcp.call` | counter | `status` | MCP tool invocation result (`ok` or error string). |
| `model\_warning` | counter | | Warning sent to the model. |
| `tool.call` | counter | `tool`, `success` | Tool invocation result (`success`: `true` or `false`). |
| `tool.call.duration\_ms` | histogram | `tool`, `success` | Tool execution time. |
| `remote\_models.fetch\_update.duration\_ms` | histogram | | Time to fetch remote model definitions. |
| `remote\_models.load\_cache.duration\_ms` | histogram | | Time to load the remote model cache. |
| `shell\_snapshot` | counter | `success` | Whether taking a shell snapshot succeeded. |
| `shell\_snapshot.duration\_ms` | histogram | `success` | Time to take a shell snapshot. |
| `db.init` | counter | `status` | State DB initialization outcomes (`opened`, `created`, `open\_error`, `init\_error`). |
| `db.backfill` | counter | `status` | Initial state DB backfill results (`upserted`, `failed`). |
| `db.backfill.duration\_ms` | histogram | `status` | Duration of the initial state DB backfill, tagged with `success`, `failed`, or `partial\_failure`. |
| `db.error` | counter | `stage` | Errors during state DB operations (for example, `extract\_metadata\_from\_rollout`, `backfill\_sessions`, `apply\_rollout\_items`). |
| `db.compare\_error` | counter | `stage`, `reason` | State DB discrepancies detected during reconciliation. |
### Feedback controls
By default, Codex lets users send feedback from `/feedback`. To disable feedback collection across Codex surfaces on a machine, update your config:
```toml
[feedback]
enabled = false
```
When disabled, `/feedback` shows a disabled message and Codex rejects feedback submissions.
### Hide or surface reasoning events
If you want to reduce noisy "reasoning" output (for example in CI logs), you can suppress it:
```toml
hide\_agent\_reasoning = true
```
If you want to surface raw reasoning content when a model emits it:
```toml
show\_raw\_agent\_reasoning = true
```
Enable raw reasoning only if it's acceptable for your workflow. Some models/providers (like `gpt-oss`) don't emit raw reasoning; in that case, this setting has no visible effect.
## Notifications
Use `notify` to trigger an external program whenever Codex emits supported events (currently only `agent-turn-complete`). This is handy for desktop toasts, chat webhooks, CI updates, or any side-channel alerting that the built-in TUI notifications don't cover.
```toml
notify = ["python3", "/path/to/notify.py"]
```
Example `notify.py` (truncated) that reacts to `agent-turn-complete`:
```python
#!/usr/bin/env python3
import json, subprocess, sys
def main() -> int:
notification = json.loads(sys.argv[1])
if notification.get("type") != "agent-turn-complete":
return 0
title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
message = " ".join(notification.get("input-messages", []))
subprocess.check\_output([
"terminal-notifier",
"-title", title,
"-message", message,
"-group", "codex-" + notification.get("thread-id", ""),
"-activate", "com.googlecode.iterm2",
])
return 0
if \_\_name\_\_ == "\_\_main\_\_":
sys.exit(main())
```
The script receives a single JSON argument. Common fields include:
- `type` (currently `agent-turn-complete`)
- `thread-id` (session identifier)
- `turn-id` (turn identifier)
- `cwd` (working directory)
- `input-messages` (user messages that led to the turn)
- `last-assistant-message` (last assistant message text)
Place the script somewhere on disk and point `notify` to it.
#### `notify` vs `tui.notifications`
- `notify` runs an external program (good for webhooks, desktop notifiers, CI hooks).
- `tui.notifications` is built in to the TUI and can optionally filter by event type (for example, `agent-turn-complete` and `approval-requested`).
- `tui.notification\_method` controls how the TUI emits terminal notifications (`auto`, `osc9`, or `bel`).
In `auto` mode, Codex prefers OSC 9 notifications (a terminal escape sequence some terminals interpret as a desktop notification) and falls back to BEL (`\x07`) otherwise.
See [Configuration Reference](https://developers.openai.com/codex/config-reference) for the exact keys.
## History persistence
By default, Codex saves local session transcripts under `CODEX\_HOME` (for example, `~/.codex/history.jsonl`). To disable local history persistence:
```toml
[history]
persistence = "none"
```
To cap the history file size, set `history.max\_bytes`. When the file exceeds the cap, Codex drops the oldest entries and compacts the file while keeping the newest records.
```toml
[history]
max\_bytes = 104857600 # 100 MiB
```
## Clickable citations
If you use a terminal/editor integration that supports it, Codex can render file citations as clickable links. Configure `file\_opener` to pick the URI scheme Codex uses:
```toml
file\_opener = "vscode" # or cursor, windsurf, vscode-insiders, none
```
Example: a citation like `/home/user/project/main.py:42` can be rewritten into a clickable `vscode://file/...:42` link.
## Project instructions discovery
Codex reads `AGENTS.md` (and related files) and includes a limited amount of project guidance in the first turn of a session. Two knobs control how this works:
- `project\_doc\_max\_bytes`: how much to read from each `AGENTS.md` file
- `project\_doc\_fallback\_filenames`: additional filenames to try when `AGENTS.md` is missing at a directory level
For a detailed walkthrough, see [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md).
## TUI options
Running `codex` with no subcommand launches the interactive terminal UI (TUI). Codex exposes some TUI-specific configuration under `[tui]`, including:
- `tui.notifications`: enable/disable notifications (or restrict to specific types)
- `tui.notification\_method`: choose `auto`, `osc9`, or `bel` for terminal notifications
- `tui.animations`: enable/disable ASCII animations and shimmer effects
- `tui.alternate\_screen`: control alternate screen usage (set to `never` to keep terminal scrollback)
- `tui.show\_tooltips`: show or hide onboarding tooltips on the welcome screen
`tui.notification\_method` defaults to `auto`. In `auto` mode, Codex prefers OSC 9 notifications (a terminal escape sequence some terminals interpret as a desktop notification) when the terminal appears to support them, and falls back to BEL (`\x07`) otherwise.
See [Configuration Reference](https://developers.openai.com/codex/config-reference) for the full key list.