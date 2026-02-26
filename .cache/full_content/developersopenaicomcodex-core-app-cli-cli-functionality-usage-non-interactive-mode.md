# Non-interactive mode
Non-interactive mode lets you run Codex from scripts (for example, continuous integration (CI) jobs) without opening the interactive TUI.
You invoke it with `codex exec`.
For flag-level details, see [`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec).
## When to use `codex exec`
Use `codex exec` when you want Codex to:
- Run as part of a pipeline (CI, pre-merge checks, scheduled jobs).
- Produce output you can pipe into other tools (for example, to generate release notes or summaries).
- Run with explicit, pre-set sandbox and approval settings.
## Basic usage
Pass a task prompt as a single argument:
```bash
codex exec "summarize the repository structure and list the top 5 risky areas"
```
While `codex exec` runs, Codex streams progress to `stderr` and prints only the final agent message to `stdout`. This makes it straightforward to redirect or pipe the final result:
```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md
```
Use `--ephemeral` when you don't want to persist session rollout files to disk:
```bash
codex exec --ephemeral "triage this repository and suggest next steps"
```
## Permissions and safety
By default, `codex exec` runs in a read-only sandbox. In automation, set the least permissions needed for the workflow:
- Allow edits: `codex exec --full-auto ""`
- Allow broader access: `codex exec --sandbox danger-full-access ""`
Use `danger-full-access` only in a controlled environment (for example, an isolated CI runner or container).
If you configure an enabled MCP server with `required = true` and it fails to initialize, `codex exec` exits with an error instead of continuing without that server.
## Make output machine-readable
To consume Codex output in scripts, use JSON Lines output:
```bash
codex exec --json "summarize the repo structure" | jq
```
When you enable `--json`, `stdout` becomes a JSON Lines (JSONL) stream so you can capture every event Codex emits while it's running. Event types include `thread.started`, `turn.started`, `turn.completed`, `turn.failed`, `item.\*`, and `error`.
Item types include agent messages, reasoning, command executions, file changes, MCP tool calls, web searches, and plan updates.
Sample JSON stream (each line is a JSON object):
```jsonl
{"type":"thread.started","thread\_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item\_1","type":"command\_execution","command":"bash -lc ls","status":"in\_progress"}}
{"type":"item.completed","item":{"id":"item\_3","type":"agent\_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input\_tokens":24763,"cached\_input\_tokens":24448,"output\_tokens":122}}
```
If you only need the final message, write it to a file with `-o `/`--output-last-message `. This writes the final message to the file and still prints it to `stdout` (see [`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec) for details).
## Create structured outputs with a schema
If you need structured data for downstream steps, use `--output-schema` to request a final response that conforms to a JSON Schema.
This is useful for automated workflows that need stable fields (for example, job summaries, risk reports, or release metadata).
`schema.json`
```json
{
"type": "object",
"properties": {
"project\_name": { "type": "string" },
"programming\_languages": {
"type": "array",
"items": { "type": "string" }
}
},
"required": ["project\_name", "programming\_languages"],
"additionalProperties": false
}
```
Run Codex with the schema and write the final JSON response to disk:
```bash
codex exec "Extract project metadata" \
--output-schema ./schema.json \
-o ./project-metadata.json
```
Example final output (stdout):
```json
{
"project\_name": "Codex CLI",
"programming\_languages": ["Rust", "TypeScript", "Shell"]
}
```
## Authenticate in CI
`codex exec` reuses saved CLI authentication by default. In CI, it's common to provide credentials explicitly:
- Set `CODEX\_API\_KEY` as a secret environment variable for the job.
- Keep prompts and tool output in mind: they can include sensitive code or data.
To use a different API key for a single run, set `CODEX\_API\_KEY` inline:
```bash
CODEX\_API\_KEY= codex exec --json "triage open bug reports"
```
`CODEX\_API\_KEY` is only supported in `codex exec`.
## Resume a non-interactive session
If you need to continue a previous run (for example, a two-stage pipeline), use the `resume` subcommand:
```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"
```
You can also target a specific session ID with `codex exec resume `.
## Git repository required
Codex requires commands to run inside a Git repository to prevent destructive changes. Override this check with `codex exec --skip-git-repo-check` if you're sure the environment is safe.
## Common automation patterns
### Example: Autofix CI failures in GitHub Actions
You can use `codex exec` to automatically propose fixes when a CI workflow fails. The typical pattern is:
1. Trigger a follow-up workflow when your main CI workflow completes with an error.
2. Check out the failing commit SHA.
3. Install dependencies and run Codex with a narrow prompt and minimal permissions.
4. Re-run the test command.
5. Open a pull request with the resulting patch.
#### Minimal workflow using the Codex CLI
The example below shows the core steps. Adjust the install and test commands to match your stack.
```yaml
name: Codex auto-fix on CI failure
on:
workflow\_run:
workflows: ["CI"]
types: [completed]
permissions:
contents: write
pull-requests: write
jobs:
auto-fix:
if: ${{ github.event.workflow\_run.conclusion == 'failure' }}
runs-on: ubuntu-latest
env:
OPENAI\_API\_KEY: ${{ secrets.OPENAI\_API\_KEY }}
FAILED\_HEAD\_SHA: ${{ github.event.workflow\_run.head\_sha }}
FAILED\_HEAD\_BRANCH: ${{ github.event.workflow\_run.head\_branch }}
steps:
- uses: actions/checkout@v4
with:
ref: ${{ env.FAILED\_HEAD\_SHA }}
fetch-depth: 0
- uses: actions/setup-node@v4
with:
node-version: "20"
- name: Install dependencies
run: |
if [ -f package-lock.json ]; then npm ci; else npm i; fi
- name: Install Codex
run: npm i -g @openai/codex
- name: Authenticate Codex
run: codex login --api-key "$OPENAI\_API\_KEY"
- name: Run Codex
run: |
codex exec --full-auto --sandbox workspace-write \
"Read the repository, run the test suite, identify the minimal change needed to make all tests pass, implement only that change, and stop. Do not refactor unrelated files."
- name: Verify tests
run: npm test --silent
- name: Create pull request
if: success()
uses: peter-evans/create-pull-request@v6
with:
branch: codex/auto-fix-${{ github.event.workflow\_run.run\_id }}
base: ${{ env.FAILED\_HEAD\_BRANCH }}
title: "Auto-fix failing CI via Codex"
```
#### Alternative: Use the Codex GitHub Action
If you want to avoid installing the CLI yourself, you can run `codex exec` through the [Codex GitHub Action](https://developers.openai.com/codex/github-action) and pass the prompt as an input.