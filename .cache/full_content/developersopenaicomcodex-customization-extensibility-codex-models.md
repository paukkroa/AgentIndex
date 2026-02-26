# Codex Models
## Recommended modelsFor most coding tasks in Codex, start with gpt-5.3-codex. It is available for
ChatGPT-authenticated Codex sessions in the Codex app, CLI, IDE extension, and
Codex Cloud. API access for GPT-5.3-Codex will come soon. The
gpt-5.3-codex-spark model is available in research preview for ChatGPT Pro
subscribers.
## Alternative models

{" "}

## Other models
Codex works best with the models listed above.
You can also point Codex at any model and provider that supports either the [Chat Completions](https://platform.openai.com/docs/api-reference/chat) or [Responses APIs](https://platform.openai.com/docs/api-reference/responses) to fit your specific use case.
Support for the Chat Completions API is deprecated and will be removed in
future releases of Codex.
## Configuring models
### Configure your default local model
The Codex CLI and IDE extension use the same `config.toml` [configuration file](https://developers.openai.com/codex/config-basic). To specify a model, add a `model` entry to your configuration file. If you don't specify a model, the Codex app, CLI, or IDE Extension defaults to a recommended model.
```toml
model = "gpt-5.2"
```
### Choosing a different local model temporarily
In the Codex CLI, you can use the `/model` command during an active thread to change the model. In the IDE extension, you can use the model selector below the input box to choose your model.
To start a new Codex CLI thread with a specific model or to specify the model for `codex exec` you can use the `--model`/`-m` flag:
```bash
codex -m gpt-5.3-codex
```
### Choosing your model for cloud tasks
Currently, you can't change the default model for Codex cloud tasks.