# Sample Configuration
Use this example configuration as a starting point. It includes most keys Codex reads from `config.toml`, along with defaults and short notes.
For explanations and guidance, see:
- [Config basics](https://developers.openai.com/codex/config-basic)
- [Advanced Config](https://developers.openai.com/codex/config-advanced)
- [Config Reference](https://developers.openai.com/codex/config-reference)
- [Sandbox and approvals](https://developers.openai.com/codex/security#sandbox-and-approvals)
- [Managed configuration](https://developers.openai.com/codex/security#managed-configuration)
Use the snippet below as a reference. Copy only the keys and sections you need into `~/.codex/config.toml` (or into a project-scoped `.codex/config.toml`), then adjust values for your setup.
```toml
# Codex example configuration (config.toml)
#
# This file lists all keys Codex reads from config.toml, their default values,
# and concise explanations. Values here mirror the effective defaults compiled
# into the CLI. Adjust as needed.
#
# Notes
# - Root keys must appear before tables in TOML.
# - Optional keys that default to "unset" are shown commented out with notes.
# - MCP servers, profiles, and model providers are examples; remove or edit.
################################################################################
# Core Model Selection
################################################################################
# Primary model used by Codex. Default: "gpt-5.2-codex" on all platforms.
model = "gpt-5.2-codex"
# Default communication style for supported models. Default: "friendly".
# Allowed values: none | friendly | pragmatic
# personality = "friendly"
# Optional model override for /review. Default: unset (uses current session model).
# review\_model = "gpt-5.2-codex"
# Provider id selected from [model\_providers]. Default: "openai".
model\_provider = "openai"
# Default OSS provider for --oss sessions. When unset, Codex prompts. Default: unset.
# oss\_provider = "ollama"
# Optional manual model metadata. When unset, Codex auto-detects from model.
# Uncomment to force values.
# model\_context\_window = 128000 # tokens; default: auto for model
# model\_auto\_compact\_token\_limit = 0 # tokens; unset uses model defaults
# tool\_output\_token\_limit = 10000 # tokens stored per tool output; default: 10000 for gpt-5.2-codex
# log\_dir = "/absolute/path/to/codex-logs" # directory for Codex logs; default: "$CODEX\_HOME/log"
################################################################################
# Reasoning & Verbosity (Responses API capable models)
################################################################################
# Reasoning effort: minimal | low | medium | high | xhigh (default: medium; xhigh on gpt-5.2-codex and gpt-5.2)
model\_reasoning\_effort = "medium"
# Reasoning summary: auto | concise | detailed | none (default: auto)
# model\_reasoning\_summary = "auto"
# Text verbosity for GPT-5 family (Responses API): low | medium | high (default: medium)
# model\_verbosity = "medium"
# Force enable or disable reasoning summaries for current model
# model\_supports\_reasoning\_summaries = true
################################################################################
# Instruction Overrides
################################################################################
# Additional user instructions are injected before AGENTS.md. Default: unset.
# developer\_instructions = ""
# (Ignored) Optional legacy base instructions override (prefer AGENTS.md). Default: unset.
# instructions = ""
# Inline override for the history compaction prompt. Default: unset.
# compact\_prompt = ""
# Override built-in base instructions with a file path. Default: unset.
# model\_instructions\_file = "/absolute/or/relative/path/to/instructions.txt"
# Migration note: experimental\_instructions\_file was renamed to model\_instructions\_file (deprecated).
# Load the compact prompt override from a file. Default: unset.
# experimental\_compact\_prompt\_file = "/absolute/or/relative/path/to/compact\_prompt.txt"
# Legacy name for apply\_patch\_freeform. Default: false
include\_apply\_patch\_tool = false
################################################################################
# Notifications
################################################################################
# External notifier program (argv array). When unset: disabled.
# Example: notify = ["notify-send", "Codex"]
notify = [ ]
################################################################################
# Approval & Sandbox
################################################################################
# When to ask for command approval:
# - untrusted: only known-safe read-only commands auto-run; others prompt
# - on-request: model decides when to ask (default)
# - never: never prompt (risky)
approval\_policy = "on-request"
# Filesystem/network sandbox policy for tool calls:
# - read-only (default)
# - workspace-write
# - danger-full-access (no sandbox; extremely risky)
sandbox\_mode = "read-only"
################################################################################
# Authentication & Login
################################################################################
# Where to persist CLI login credentials: file (default) | keyring | auto
cli\_auth\_credentials\_store = "file"
# Base URL for ChatGPT auth flow (not OpenAI API). Default:
chatgpt\_base\_url = "https://chatgpt.com/backend-api/"
# Restrict ChatGPT login to a specific workspace id. Default: unset.
# forced\_chatgpt\_workspace\_id = ""
# Force login mechanism when Codex would normally auto-select. Default: unset.
# Allowed values: chatgpt | api
# forced\_login\_method = "chatgpt"
# Preferred store for MCP OAuth credentials: auto (default) | file | keyring
mcp\_oauth\_credentials\_store = "auto"
# Optional fixed port for MCP OAuth callback: 1-65535. Default: unset.
# mcp\_oauth\_callback\_port = 4321
################################################################################
# Project Documentation Controls
################################################################################
# Max bytes from AGENTS.md to embed into first-turn instructions. Default: 32768
project\_doc\_max\_bytes = 32768
# Ordered fallbacks when AGENTS.md is missing at a directory level. Default: []
project\_doc\_fallback\_filenames = []
# Project root marker filenames used when searching parent directories. Default: [".git"]
# project\_root\_markers = [".git"]
################################################################################
# History & File Opener
################################################################################
# URI scheme for clickable citations: vscode (default) | vscode-insiders | windsurf | cursor | none
file\_opener = "vscode"
################################################################################
# UI, Notifications, and Misc
################################################################################
# Suppress internal reasoning events from output. Default: false
hide\_agent\_reasoning = false
# Show raw reasoning content when available. Default: false
show\_raw\_agent\_reasoning = false
# Disable burst-paste detection in the TUI. Default: false
disable\_paste\_burst = false
# Track Windows onboarding acknowledgement (Windows only). Default: false
windows\_wsl\_setup\_acknowledged = false
# Check for updates on startup. Default: true
check\_for\_update\_on\_startup = true
################################################################################
# Web Search
################################################################################
# Web search mode: disabled | cached | live. Default: "cached"
# cached serves results from a web search cache (an OpenAI-maintained index).
# cached returns pre-indexed results; live fetches the most recent data.
# If you use --yolo or another full access sandbox setting, web search defaults to live.
web\_search = "cached"
################################################################################
# Profiles (named presets)
################################################################################
# Active profile name. When unset, no profile is applied.
# profile = "default"
################################################################################
# Skills (per-skill overrides)
################################################################################
# Disable or re-enable a specific skill without deleting it.
[[skills.config]]
# path = "/path/to/skill"
# enabled = false
################################################################################
# Experimental toggles (legacy; prefer [features])
################################################################################
experimental\_use\_unified\_exec\_tool = false
# Include apply\_patch via freeform editing path (affects default tool set). Default: false
experimental\_use\_freeform\_apply\_patch = false
################################################################################
# Sandbox settings (tables)
################################################################################
# Extra settings used only when sandbox\_mode = "workspace-write".
[sandbox\_workspace\_write]
# Additional writable roots beyond the workspace (cwd). Default: []
writable\_roots = []
# Allow outbound network access inside the sandbox. Default: false
network\_access = false
# Exclude $TMPDIR from writable roots. Default: false
exclude\_tmpdir\_env\_var = false
# Exclude /tmp from writable roots. Default: false
exclude\_slash\_tmp = false
################################################################################
# Shell Environment Policy for spawned processes (table)
################################################################################
[shell\_environment\_policy]
# inherit: all (default) | core | none
inherit = "all"
# Skip default excludes for names containing KEY/SECRET/TOKEN (case-insensitive). Default: true
ignore\_default\_excludes = true
# Case-insensitive glob patterns to remove (e.g., "AWS\_\*", "AZURE\_\*"). Default: []
exclude = []
# Explicit key/value overrides (always win). Default: {}
set = {}
# Whitelist; if non-empty, keep only matching vars. Default: []
include\_only = []
# Experimental: run via user shell profile. Default: false
experimental\_use\_profile = false
################################################################################
# History (table)
################################################################################
[history]
# save-all (default) | none
persistence = "save-all"
# Maximum bytes for history file; oldest entries are trimmed when exceeded. Example: 5242880
# max\_bytes = 0
################################################################################
# UI, Notifications, and Misc (tables)
################################################################################
[tui]
# Desktop notifications from the TUI: boolean or filtered list. Default: true
# Examples: false | ["agent-turn-complete", "approval-requested"]
notifications = false
# Notification mechanism for terminal alerts: auto | osc9 | bel. Default: "auto"
# notification\_method = "auto"
# Enables welcome/status/spinner animations. Default: true
animations = true
# Show onboarding tooltips in the welcome screen. Default: true
show\_tooltips = true
# Control alternate screen usage (auto skips it in Zellij to preserve scrollback).
# alternate\_screen = "auto"
# Ordered list of footer status-line item IDs. Default: null (disabled).
# status\_line = ["model", "context-remaining", "git-branch"]
# Control whether users can submit feedback from `/feedback`. Default: true
[feedback]
enabled = true
# In-product notices (mostly set automatically by Codex).
[notice]
# hide\_full\_access\_warning = true
# hide\_world\_writable\_warning = true
# hide\_rate\_limit\_model\_nudge = true
# hide\_gpt5\_1\_migration\_prompt = true
# "hide\_gpt-5.1-codex-max\_migration\_prompt" = true
# model\_migrations = { "gpt-4.1" = "gpt-5.1" }
# Suppress the warning shown when under-development feature flags are enabled.
# suppress\_unstable\_features\_warning = true
################################################################################
# Centralized Feature Flags (preferred)
################################################################################
[features]
# Leave this table empty to accept defaults. Set explicit booleans to opt in/out.
shell\_tool = true
# apps = false
# apps\_mcp\_gateway = false
# Deprecated legacy toggles; prefer the top-level `web\_search` setting.
# web\_search = false
# web\_search\_cached = false
# web\_search\_request = false
unified\_exec = false
shell\_snapshot = false
apply\_patch\_freeform = false
# search\_tool = false
# personality = true
request\_rule = true
collaboration\_modes = true
use\_linux\_sandbox\_bwrap = false
experimental\_windows\_sandbox = false
elevated\_windows\_sandbox = false
remote\_models = false
runtime\_metrics = false
powershell\_utf8 = true
child\_agents\_md = false
################################################################################
# Define MCP servers under this table. Leave empty to disable.
################################################################################
[mcp\_servers]
# --- Example: STDIO transport ---
# [mcp\_servers.docs]
# enabled = true # optional; default true
# required = true # optional; fail startup/resume if this server cannot initialize
# command = "docs-server" # required
# args = ["--port", "4000"] # optional
# env = { "API\_KEY" = "value" } # optional key/value pairs copied as-is
# env\_vars = ["ANOTHER\_SECRET"] # optional: forward these from the parent env
# cwd = "/path/to/server" # optional working directory override
# startup\_timeout\_sec = 10.0 # optional; default 10.0 seconds
# # startup\_timeout\_ms = 10000 # optional alias for startup timeout (milliseconds)
# tool\_timeout\_sec = 60.0 # optional; default 60.0 seconds
# enabled\_tools = ["search", "summarize"] # optional allow-list
# disabled\_tools = ["slow-tool"] # optional deny-list (applied after allow-list)
# --- Example: Streamable HTTP transport ---
# [mcp\_servers.github]
# enabled = true # optional; default true
# required = true # optional; fail startup/resume if this server cannot initialize
# url = "https://github-mcp.example.com/mcp" # required
# bearer\_token\_env\_var = "GITHUB\_TOKEN" # optional; Authorization: Bearer 
# http\_headers = { "X-Example" = "value" } # optional static headers
# env\_http\_headers = { "X-Auth" = "AUTH\_ENV" } # optional headers populated from env vars
# startup\_timeout\_sec = 10.0 # optional
# tool\_timeout\_sec = 60.0 # optional
# enabled\_tools = ["list\_issues"] # optional allow-list
################################################################################
# Model Providers
################################################################################
# Built-ins include:
# - openai (Responses API; requires login or OPENAI\_API\_KEY via auth flow)
# - oss (Chat Completions API; defaults to http://localhost:11434/v1)
[model\_providers]
# --- Example: OpenAI data residency with explicit base URL or headers ---
# [model\_providers.openaidr]
# name = "OpenAI Data Residency"
# base\_url = "https://us.api.openai.com/v1" # example with 'us' domain prefix
# wire\_api = "responses" # "responses" | "chat" (default varies)
# # requires\_openai\_auth = true # built-in OpenAI defaults to true
# # request\_max\_retries = 4 # default 4; max 100
# # stream\_max\_retries = 5 # default 5; max 100
# # stream\_idle\_timeout\_ms = 300000 # default 300\_000 (5m)
# # experimental\_bearer\_token = "sk-example" # optional dev-only direct bearer token
# # http\_headers = { "X-Example" = "value" }
# # env\_http\_headers = { "OpenAI-Organization" = "OPENAI\_ORGANIZATION", "OpenAI-Project" = "OPENAI\_PROJECT" }
# --- Example: Azure (Chat/Responses depending on endpoint) ---
# [model\_providers.azure]
# name = "Azure"
# base\_url = "https://YOUR\_PROJECT\_NAME.openai.azure.com/openai"
# wire\_api = "responses" # or "chat" per endpoint
# query\_params = { api-version = "2025-04-01-preview" }
# env\_key = "AZURE\_OPENAI\_API\_KEY"
# # env\_key\_instructions = "Set AZURE\_OPENAI\_API\_KEY in your environment"
# --- Example: Local OSS (e.g., Ollama-compatible) ---
# [model\_providers.ollama]
# name = "Ollama"
# base\_url = "http://localhost:11434/v1"
# wire\_api = "chat"
################################################################################
# Profiles (named presets)
################################################################################
[profiles]
# [profiles.default]
# model = "gpt-5.2-codex"
# model\_provider = "openai"
# approval\_policy = "on-request"
# sandbox\_mode = "read-only"
# oss\_provider = "ollama"
# model\_reasoning\_effort = "medium"
# model\_reasoning\_summary = "auto"
# model\_verbosity = "medium"
# personality = "friendly" # or "pragmatic" or "none"
# chatgpt\_base\_url = "https://chatgpt.com/backend-api/"
# experimental\_compact\_prompt\_file = "./compact\_prompt.txt"
# include\_apply\_patch\_tool = false
# experimental\_use\_unified\_exec\_tool = false
# experimental\_use\_freeform\_apply\_patch = false
# tools.web\_search = false # deprecated legacy alias; prefer top-level `web\_search`
# features = { unified\_exec = false }
################################################################################
# Apps / Connectors
################################################################################
# Optional per-app controls.
[apps]
# [apps.google\_drive]
# enabled = false
# disabled\_reason = "user" # or "unknown"
################################################################################
# Projects (trust levels)
################################################################################
# Mark specific worktrees as trusted or untrusted.
[projects]
# [projects."/absolute/path/to/project"]
# trust\_level = "trusted" # or "untrusted"
################################################################################
# OpenTelemetry (OTEL) - disabled by default
################################################################################
[otel]
# Include user prompt text in logs. Default: false
log\_user\_prompt = false
# Environment label applied to telemetry. Default: "dev"
environment = "dev"
# Exporter: none (default) | otlp-http | otlp-grpc
exporter = "none"
# Trace exporter: none (default) | otlp-http | otlp-grpc
trace\_exporter = "none"
# Example OTLP/HTTP exporter configuration
# [otel.exporter."otlp-http"]
# endpoint = "https://otel.example.com/v1/logs"
# protocol = "binary" # "binary" | "json"
# [otel.exporter."otlp-http".headers]
# "x-otlp-api-key" = "${OTLP\_TOKEN}"
# Example OTLP/gRPC exporter configuration
# [otel.exporter."otlp-grpc"]
# endpoint = "https://otel.example.com:4317",
# headers = { "x-otlp-meta" = "abc123" }
# Example OTLP exporter with mutual TLS
# [otel.exporter."otlp-http"]
# endpoint = "https://otel.example.com/v1/logs"
# protocol = "binary"
# [otel.exporter."otlp-http".headers]
# "x-otlp-api-key" = "${OTLP\_TOKEN}"
# [otel.exporter."otlp-http".tls]
# ca-certificate = "certs/otel-ca.pem"
# client-certificate = "/etc/codex/certs/client.pem"
# client-private-key = "/etc/codex/certs/client-key.pem"
```