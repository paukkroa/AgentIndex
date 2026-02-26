[Skip to main content](#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘KAsk AI

Search...

Navigation

Configuration

Speed up responses with fast mode

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

* [Toggle fast mode](#toggle-fast-mode)
* [Understand the cost tradeoff](#understand-the-cost-tradeoff)
* [Decide when to use fast mode](#decide-when-to-use-fast-mode)
* [Fast mode vs effort level](#fast-mode-vs-effort-level)
* [Requirements](#requirements)
* [Enable fast mode for your organization](#enable-fast-mode-for-your-organization)
* [Handle rate limits](#handle-rate-limits)
* [Research preview](#research-preview)
* [See also](#see-also)

Fast mode is in [research preview](#research-preview). The feature, pricing, and availability may change based on feedback.

Fast mode is a high-speed configuration for Claude Opus 4.6, making the model 2.5x faster at a higher cost per token. Toggle it on with `/fast` when you need speed for interactive work like rapid iteration or live debugging, and toggle it off when cost matters more than latency.
Fast mode is not a different model. It uses the same Opus 4.6 with a different API configuration that prioritizes speed over cost efficiency. You get identical quality and capabilities, just faster responses.
What to know:

* Use `/fast` to toggle on fast mode in Claude Code CLI. Also available via `/fast` in Claude Code VS Code Extension.
* Fast mode for Opus 4.6 pricing starts at $30/150 MTok. Fast mode is available at a 50% discount for all plans until 11:59pm PT on February 16.
* Available to all Claude Code users on subscription plans (Pro/Max/Team/Enterprise) and Claude Console.
* For Claude Code users on subscription plans (Pro/Max/Team/Enterprise), fast mode is available via extra usage only and not included in the subscription rate limits.

This page covers how to [toggle fast mode](#toggle-fast-mode), its [cost tradeoff](#understand-the-cost-tradeoff), [when to use it](#decide-when-to-use-fast-mode), [requirements](#requirements), and [rate limit behavior](#handle-rate-limits).

## [​](#toggle-fast-mode) Toggle fast mode

Toggle fast mode in either of these ways:

* Type `/fast` and press Tab to toggle on or off
* Set `"fastMode": true` in your [user settings file](/docs/en/settings)

Fast mode persists across sessions. For the best cost efficiency, enable fast mode at the start of a session rather than switching mid-conversation. See [understand the cost tradeoff](#understand-the-cost-tradeoff) for details.
When you enable fast mode:

* If you’re on a different model, Claude Code automatically switches to Opus 4.6
* You’ll see a confirmation message: “Fast mode ON”
* A small `↯` icon appears next to the prompt while fast mode is active
* Run `/fast` again at any time to check whether fast mode is on or off

When you disable fast mode with `/fast` again, you remain on Opus 4.6. The model does not revert to your previous model. To switch to a different model, use `/model`.

## [​](#understand-the-cost-tradeoff) Understand the cost tradeoff

Fast mode has higher per-token pricing than standard Opus 4.6:

| Mode | Input (MTok) | Output (MTok) |
| --- | --- | --- |
| Fast mode on Opus 4.6 (<200K) | $30 | $150 |
| Fast mode on Opus 4.6 (>200K) | $60 | $225 |

Fast mode is compatible with the 1M token extended context window.
When you switch into fast mode mid-conversation, you pay the full fast mode uncached input token price for the entire conversation context. This costs more than if you had enabled fast mode from the start.

## [​](#decide-when-to-use-fast-mode) Decide when to use fast mode

Fast mode is best for interactive work where response latency matters more than cost:

* Rapid iteration on code changes
* Live debugging sessions
* Time-sensitive work with tight deadlines

Standard mode is better for:

* Long autonomous tasks where speed matters less
* Batch processing or CI/CD pipelines
* Cost-sensitive workloads

### [​](#fast-mode-vs-effort-level) Fast mode vs effort level

Fast mode and effort level both affect response speed, but differently:

| Setting | Effect |
| --- | --- |
| **Fast mode** | Same model quality, lower latency, higher cost |
| **Lower effort level** | Less thinking time, faster responses, potentially lower quality on complex tasks |

You can combine both: use fast mode with a lower [effort level](/docs/en/model-config#adjust-effort-level) for maximum speed on straightforward tasks.

## [​](#requirements) Requirements

Fast mode requires all of the following:

* **Not available on third-party cloud providers**: fast mode is not available on Amazon Bedrock, Google Vertex AI, or Microsoft Azure Foundry. Fast mode is available through the Anthropic Console API and for Claude subscription plans using extra usage.
* **Extra usage enabled**: your account must have extra usage enabled, which allows billing beyond your plan’s included usage. For individual accounts, enable this in your [Console billing settings](https://platform.claude.com/settings/organization/billing). For Teams and Enterprise, an admin must enable extra usage for the organization.

Fast mode usage is billed directly to extra usage, even if you have remaining usage on your plan. This means fast mode tokens do not count against your plan’s included usage and are charged at the fast mode rate from the first token.

* **Admin enablement for Teams and Enterprise**: fast mode is disabled by default for Teams and Enterprise organizations. An admin must explicitly [enable fast mode](#enable-fast-mode-for-your-organization) before users can access it.

If your admin has not enabled fast mode for your organization, the `/fast` command will show “Fast mode has been disabled by your organization.”

### [​](#enable-fast-mode-for-your-organization) Enable fast mode for your organization

Admins can enable fast mode in:

* **Console** (API customers): [Claude Code preferences](https://platform.claude.com/claude-code/preferences)
* **Claude AI** (Teams and Enterprise): [Admin Settings > Claude Code](https://claude.ai/admin-settings/claude-code)

## [​](#handle-rate-limits) Handle rate limits

Fast mode has separate rate limits from standard Opus 4.6. When you hit the fast mode rate limit or run out of extra usage credits:

1. Fast mode automatically falls back to standard Opus 4.6
2. The `↯` icon turns gray to indicate cooldown
3. You continue working at standard speed and pricing
4. When the cooldown expires, fast mode automatically re-enables

To disable fast mode manually instead of waiting for cooldown, run `/fast` again.

## [​](#research-preview) Research preview

Fast mode is a research preview feature. This means:

* The feature may change based on feedback
* Availability and pricing are subject to change
* The underlying API configuration may evolve

Report issues or feedback through your usual Anthropic support channels.

## [​](#see-also) See also

* [Model configuration](/docs/en/model-config): switch models and adjust effort levels
* [Manage costs effectively](/docs/en/costs): track token usage and reduce costs
* [Status line configuration](/docs/en/statusline): display model and context information

Was this page helpful?

YesNo

[Model configuration](/docs/en/model-config)[Memory management](/docs/en/memory)

Assistant

Responses are generated using AI and may contain mistakes.