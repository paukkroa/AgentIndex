[Skip to main content](#content-area)

[Claude Code Docs home page](/docs)

English

Search...

⌘KAsk AI

Search...

Navigation

Deployment

Enterprise network configuration

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

* [Proxy configuration](#proxy-configuration)
* [Environment variables](#environment-variables)
* [Basic authentication](#basic-authentication)
* [Custom CA certificates](#custom-ca-certificates)
* [mTLS authentication](#mtls-authentication)
* [Network access requirements](#network-access-requirements)
* [Additional resources](#additional-resources)

Claude Code supports various enterprise network and security configurations through environment variables. This includes routing traffic through corporate proxy servers, trusting custom Certificate Authorities (CA), and authenticating with mutual Transport Layer Security (mTLS) certificates for enhanced security.

All environment variables shown on this page can also be configured in [`settings.json`](/docs/en/settings).

## [​](#proxy-configuration) Proxy configuration

### [​](#environment-variables) Environment variables

Claude Code respects standard proxy environment variables:

Report incorrect code

Copy

Ask AI

```
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

# Bypass proxy for specific requests - space-separated format
export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
# Bypass proxy for specific requests - comma-separated format
export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
# Bypass proxy for all requests
export NO_PROXY="*"
```

Claude Code does not support SOCKS proxies.

### [​](#basic-authentication) Basic authentication

If your proxy requires basic authentication, include credentials in the proxy URL:

Report incorrect code

Copy

Ask AI

```
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.

For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider using an LLM Gateway service that supports your authentication method.

## [​](#custom-ca-certificates) Custom CA certificates

If your enterprise environment uses custom CAs for HTTPS connections (whether through a proxy or direct API access), configure Claude Code to trust them:

Report incorrect code

Copy

Ask AI

```
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

## [​](#mtls-authentication) mTLS authentication

For enterprise environments requiring client certificate authentication:

Report incorrect code

Copy

Ask AI

```
# Client certificate for authentication
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem

# Client private key
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem

# Optional: Passphrase for encrypted private key
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE="your-passphrase"
```

## [​](#network-access-requirements) Network access requirements

Claude Code requires access to the following URLs:

* `api.anthropic.com`: Claude API endpoints
* `claude.ai`: authentication for claude.ai accounts
* `platform.claude.com`: authentication for Anthropic Console accounts

Ensure these URLs are allowlisted in your proxy configuration and firewall rules. This is especially important when using Claude Code in containerized or restricted network environments.

## [​](#additional-resources) Additional resources

* [Claude Code settings](/docs/en/settings)
* [Environment variables reference](/docs/en/settings#environment-variables)
* [Troubleshooting guide](/docs/en/troubleshooting)

Was this page helpful?

YesNo

[Microsoft Foundry](/docs/en/microsoft-foundry)[LLM gateway](/docs/en/llm-gateway)

Assistant

Responses are generated using AI and may contain mistakes.