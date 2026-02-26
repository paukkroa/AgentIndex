# Agentic Index

A filesystem-based hierarchical documentation index designed for AI agents.

Agentic Index turns documentation websites or local folders into a structured, explorable file tree that agents can navigate using simple tools like `ls`, `read`, and `fetch`. This architecture is designed to be version-controlled, human-readable, and easily shared.

## Features

- **Filesystem-as-Database**: Indexes are standard directories with Markdown files, making them git-friendly and transparent.
- **Agentic Navigation**: Exposes an MCP (Model Context Protocol) server with `ls`, `read`, and `fetch` tools for intuitive agent exploration.
- **Multi-Source Support**: Combine multiple documentation sources (e.g., "Claude Docs" + "Python Docs") into a single knowledge base.
- **AI-Powered Summarization**: Automatically generates summaries for directory nodes to guide agents.

## Installation

```bash
# Using uv (recommended)
uv pip install -e ".[dev]"

# Or standard pip
pip install -e ".[dev]"
```

## Quick Start

### 1. Initialize a Knowledge Base
Create a root directory for your indexes.

```bash
agentic-index init my_docs
```

### 2. Add Documentation Sources
Crawl and index websites into your knowledge base.

```bash
# Add Claude documentation
agentic-index add https://code.claude.com/docs/en my_docs --provider gemini

# Add another source (e.g., Python tutorial)
agentic-index add https://docs.python.org/3/tutorial/ my_docs --provider gemini
```

This creates a structured file tree:
```text
my_docs/
├── _meta.json
├── _summary.md
├── claude-docs/
│   ├── getting-started/
│   └── ...
└── python-tutorial/
    └── ...
```

### 3. Serve to Agents
Start the MCP server to expose this index to Claude Desktop or other agents.

```bash
agentic-index serve my_docs
```

## MCP Tools

When served, the following tools are available to the agent:

- **`ls(path)`**: Lists the contents of a directory (categories and documents).
- **`read(path)`**: Reads the content of a document or the summary of a directory.
- **`fetch(path)`**: Fetches the live/latest content of a document from its original URL.

## Configuration

To use the MCP server with **Claude Desktop**, add this to your config:

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

## Development

Run tests:
```bash
pytest
```

Linting:
```bash
ruff check .
```
