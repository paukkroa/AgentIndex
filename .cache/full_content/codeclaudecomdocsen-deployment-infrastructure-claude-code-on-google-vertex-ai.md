[Skip to main content](#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘KAsk AI

Search...

Navigation

Deployment

Claude Code on Google Vertex AI

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

* [Prerequisites](#prerequisites)
* [Region Configuration](#region-configuration)
* [Setup](#setup)
* [1. Enable Vertex AI API](#1-enable-vertex-ai-api)
* [2. Request model access](#2-request-model-access)
* [3. Configure GCP credentials](#3-configure-gcp-credentials)
* [4. Configure Claude Code](#4-configure-claude-code)
* [5. Pin model versions](#5-pin-model-versions)
* [IAM configuration](#iam-configuration)
* [1M token context window](#1m-token-context-window)
* [Troubleshooting](#troubleshooting)
* [Additional resources](#additional-resources)

## [​](#prerequisites) Prerequisites

Before configuring Claude Code with Vertex AI, ensure you have:

* A Google Cloud Platform (GCP) account with billing enabled
* A GCP project with Vertex AI API enabled
* Access to desired Claude models (for example, Claude Sonnet 4.6)
* Google Cloud SDK (`gcloud`) installed and configured
* Quota allocated in desired GCP region

If you are deploying Claude Code to multiple users, [pin your model versions](#5-pin-model-versions) to prevent breakage when Anthropic releases new models.

## [​](#region-configuration) Region Configuration

Claude Code can be used with both Vertex AI [global](https://cloud.google.com/blog/products/ai-machine-learning/global-endpoint-for-claude-models-generally-available-on-vertex-ai) and regional endpoints.

Vertex AI may not support the Claude Code default models in all [regions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#genai-partner-models) or on [global endpoints](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models#supported_models). You may need to switch to a supported region, use a regional endpoint, or specify a supported model.

## [​](#setup) Setup

### [​](#1-enable-vertex-ai-api) 1. Enable Vertex AI API

Enable the Vertex AI API in your GCP project:

Report incorrect code

Copy

Ask AI

```
# Set your project ID
gcloud config set project YOUR-PROJECT-ID

# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com
```

### [​](#2-request-model-access) 2. Request model access

Request access to Claude models in Vertex AI:

1. Navigate to the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)
2. Search for “Claude” models
3. Request access to desired Claude models (for example, Claude Sonnet 4.6)
4. Wait for approval (may take 24-48 hours)

### [​](#3-configure-gcp-credentials) 3. Configure GCP credentials

Claude Code uses standard Google Cloud authentication.
For more information, see [Google Cloud authentication documentation](https://cloud.google.com/docs/authentication).

When authenticating, Claude Code will automatically use the project ID from the `ANTHROPIC_VERTEX_PROJECT_ID` environment variable. To override this, set one of these environment variables: `GCLOUD_PROJECT`, `GOOGLE_CLOUD_PROJECT`, or `GOOGLE_APPLICATION_CREDENTIALS`.

### [​](#4-configure-claude-code) 4. Configure Claude Code

Set the following environment variables:

Report incorrect code

Copy

Ask AI

```
# Enable Vertex AI integration
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=global
export ANTHROPIC_VERTEX_PROJECT_ID=YOUR-PROJECT-ID

# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1

# When CLOUD_ML_REGION=global, override region for unsupported models
export VERTEX_REGION_CLAUDE_3_5_HAIKU=us-east5

# Optional: Override regions for other specific models
export VERTEX_REGION_CLAUDE_3_5_SONNET=us-east5
export VERTEX_REGION_CLAUDE_3_7_SONNET=us-east5
export VERTEX_REGION_CLAUDE_4_0_OPUS=europe-west1
export VERTEX_REGION_CLAUDE_4_0_SONNET=us-east5
export VERTEX_REGION_CLAUDE_4_1_OPUS=europe-west1
```

[Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) is automatically supported when you specify the `cache_control` ephemeral flag. To disable it, set `DISABLE_PROMPT_CACHING=1`. For heightened rate limits, contact Google Cloud support. When using Vertex AI, the `/login` and `/logout` commands are disabled since authentication is handled through Google Cloud credentials.

### [​](#5-pin-model-versions) 5. Pin model versions

Pin specific model versions for every deployment. If you use model aliases (`sonnet`, `opus`, `haiku`) without pinning, Claude Code may attempt to use a newer model version that isn’t enabled in your Vertex AI project, breaking existing users when Anthropic releases updates.

Set these environment variables to specific Vertex AI model IDs:

Report incorrect code

Copy

Ask AI

```
export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-6'
export ANTHROPIC_DEFAULT_SONNET_MODEL='claude-sonnet-4-6'
export ANTHROPIC_DEFAULT_HAIKU_MODEL='claude-haiku-4-5@20251001'
```

For current and legacy model IDs, see [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview). See [Model configuration](/docs/en/model-config#pin-models-for-third-party-deployments) for the full list of environment variables.
Claude Code uses these default models when no pinning variables are set:

| Model type | Default value |
| --- | --- |
| Primary model | `claude-sonnet-4-6` |
| Small/fast model | `claude-haiku-4-5@20251001` |

To customize models further:

Report incorrect code

Copy

Ask AI

```
export ANTHROPIC_MODEL='claude-opus-4-6'
export ANTHROPIC_SMALL_FAST_MODEL='claude-haiku-4-5@20251001'
```

## [​](#iam-configuration) IAM configuration

Assign the required IAM permissions:
The `roles/aiplatform.user` role includes the required permissions:

* `aiplatform.endpoints.predict` - Required for model invocation and token counting

For more restrictive permissions, create a custom role with only the permissions above.
For details, see [Vertex IAM documentation](https://cloud.google.com/vertex-ai/docs/general/access-control).

Create a dedicated GCP project for Claude Code to simplify cost tracking and access control.

## [​](#1m-token-context-window) 1M token context window

Claude Sonnet 4 and Sonnet 4.6 support the [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows#1m-token-context-window) on Vertex AI.

The 1M token context window is currently in beta. To use the extended context window, include the `context-1m-2025-08-07` beta header in your Vertex AI requests.

## [​](#troubleshooting) Troubleshooting

If you encounter quota issues:

* Check current quotas or request quota increase through [Cloud Console](https://cloud.google.com/docs/quotas/view-manage)

If you encounter “model not found” 404 errors:

* Confirm model is Enabled in [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)
* Verify you have access to the specified region
* If using `CLOUD_ML_REGION=global`, check that your models support global endpoints in [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden) under “Supported features”. For models that don’t support global endpoints, either:
  + Specify a supported model via `ANTHROPIC_MODEL` or `ANTHROPIC_SMALL_FAST_MODEL`, or
  + Set a regional endpoint using `VERTEX_REGION_<MODEL_NAME>` environment variables

If you encounter 429 errors:

* For regional endpoints, ensure the primary model and small/fast model are supported in your selected region
* Consider switching to `CLOUD_ML_REGION=global` for better availability

## [​](#additional-resources) Additional resources

* [Vertex AI documentation](https://cloud.google.com/vertex-ai/docs)
* [Vertex AI pricing](https://cloud.google.com/vertex-ai/pricing)
* [Vertex AI quotas and limits](https://cloud.google.com/vertex-ai/docs/quotas)

Was this page helpful?

YesNo

[Amazon Bedrock](/docs/en/amazon-bedrock)[Microsoft Foundry](/docs/en/microsoft-foundry)

Assistant

Responses are generated using AI and may contain mistakes.