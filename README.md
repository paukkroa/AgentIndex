# AgentIndex

AgentIndex turns documentation websites and local folders into navigable semantic file trees that AI agents can explore with simple tools. Instead of retrieving chunks statistically, agents navigate a clean directory hierarchy to find exactly what they need — with precise control over how much context they consume at each step.

---

## Installation

```bash
# Using uv (recommended)
uv pip install -e .

# Or standard pip
pip install -e .
```

---

## LLM Provider Setup

AgentIndex uses an LLM to structure and summarise the index during the build phase. Two providers are supported:

### Ollama (local, no API key required)

Install [Ollama](https://ollama.com) and pull a model:

```bash
ollama pull llama3.2
```

AgentIndex auto-detects a running Ollama instance. No configuration needed.

### Gemini (cloud)

Set your API key:

```bash
export GEMINI_API_KEY=your_key_here
```

AgentIndex auto-detects the key and uses Gemini if Ollama is not running. You can also pass `--provider gemini` explicitly.

---

## Quick Start

### 1. Initialize a knowledge base

```bash
agentic-index init my_docs
```

### 2. Add a documentation source

```bash
# From a website
agentic-index add https://docs.example.com/guide my_docs

# From a local folder
agentic-index add ./path/to/local/docs my_docs
```

AgentIndex crawls the source (using `llms.txt` when available, BFS otherwise for web; recursive file walk for local paths), groups pages into semantic categories with an LLM, summarises each node bottom-up, and writes the result as a directory tree:

```
my_docs/
├── _meta.json
├── _summary.md
├── getting-started/
│   ├── _summary.md
│   ├── installation.md
│   └── quickstart.md
├── configuration/
│   ├── _summary.md
│   ├── environment-variables.md
│   └── provider-setup.md
└── api-reference/
    ├── _summary.md
    └── authentication.md
```

Each subsequent `add` appends a new source's subtree alongside existing ones and updates `_meta.json`.

### 3. Serve to agents

```bash
agentic-index serve my_docs
```

This starts an MCP server that exposes four tools to the agent (see [MCP Tools](#mcp-tools-explicit-toolset) below).

---

## Index Management

| Command | Description |
|---|---|
| `agentic-index init <path>` | Create a new empty index root directory |
| `agentic-index add <source> <root>` | Crawl a source and add it to an existing index root |
| `agentic-index build <source> [-o <path>]` | Build a standalone index from a single source |
| `agentic-index build-multi <s1> <s2> ... [-o <path>]` | Build an index from multiple sources (optionally with semantic grouping) |
| `agentic-index update <source-id> <index>` | Re-crawl and incrementally update a source |
| `agentic-index serve <index>` | Start the MCP server |

Sources can be a website URL (`https://...`) or a local directory path.

### Incremental updates

The `update` command only re-processes pages that actually changed since the last crawl:

```bash
agentic-index update my-source-id my_docs
```

Changed pages are detected by SHA-256 content hash. Only modified leaves and their ancestor branches are re-summarised. Pass `--restructure` to force a full rebuild instead:

```bash
agentic-index update my-source-id my_docs --restructure
```

### Semantic (cross-source) indexing

By default, each source gets its own subtree (`root → source → categories → leaves`). Use `build-multi --structure-mode semantic` to merge all sources into a single topic hierarchy regardless of source origin:

```bash
agentic-index build-multi ./docs/technical ./docs/hr ./docs/finance \
    --structure-mode semantic -o my_docs
```

In semantic mode, pages from different sources can share the same category (e.g. an "Authentication" folder may contain pages from three vendors). Each leaf retains a `source_id` field in its frontmatter so the origin is always traceable.

---

## MCP Tools (Explicit Toolset)

When served, four tools are available to the agent:

| Tool | Description | When to use |
|---|---|---|
| `ls(path, depth, include_summaries)` | List directory contents by name | First step when exploring; add `include_summaries=true` for quick orientation |
| `find(pattern)` | Search all node names/paths for a substring or glob | When you know a keyword and want to jump directly to it |
| `get_summary(path)` | Read YAML frontmatter + AI summary (local, no network) | Peek at a document before committing to a full fetch |
| `get_details(path)` | Fetch the full content — from the original URL or from disk for local sources | When you need exact technical details or code examples |

The key design: `ls` returns **names only** by default, `get_summary` is a cheap local read, and `get_details` is the only tool that may make a network request (skipped entirely for local file sources). Agents control context cost at every step.

For full usage patterns (top-down drill-down, find-then-drill, peek-before-fetch), see [docs/agent-interaction.md](docs/agent-interaction.md).

---

## Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "my-docs": {
      "command": "uv",
      "args": [
        "run",
        "agentic-index",
        "serve",
        "/absolute/path/to/my_docs"
      ]
    }
  }
}
```

---

## Tree Structure

Each index is a standard filesystem directory of Markdown files. Group nodes are directories with a `_summary.md`; leaf nodes are `.md` files with YAML frontmatter containing the `ref` (URL or file path), title, AI-generated summaries, source identifier, and content hash.

See [docs/tree-structure.md](docs/tree-structure.md) for the full node format and an explanation of LLM-structured, path-based, and semantic cross-source trees.

---

## Evaluation

AgentIndex was evaluated against a Hybrid RAG baseline (ChromaDB + BM25/RRF) on 40 human-judged questions across a 450-document noise-rich corpus (Claude Code docs + OpenAI Codex + Python stdlib + Purina dog breeds).

**Key results:**
- Up to **~18% improvement in precision and ~19% in recall** on procedural tasks vs Hybrid RAG
- **1.00 precision** on multi-hop tasks with the Explicit toolset
- Quality **stable across corpus sizes** — hierarchy shields the agent from haystack growth
- AgentIndex retrieved **1.17 sources per query** vs **3.9–4.2 for RAG** (mostly noise)

See [evaluation/README.md](evaluation/README.md) for methodology, dataset details, and how to reproduce the experiment.

---

## Development

Run tests:

```bash
uv run pytest
```

Linting:

```bash
ruff check .
```

Install dev and eval dependencies:

```bash
uv pip install -e ".[dev,eval]"
```
