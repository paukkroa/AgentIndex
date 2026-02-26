# GEMINI.md: Project Context for Agentic Index

## Project Overview

This project, "Agentic Index," is a Python-based tool for creating a hierarchical, explorable index of documents from websites or local directories. Its core purpose is to structure content in a way that is easily navigable by an AI agent.

The key features are:

*   **Hierarchical Indexing:** It crawls a source (like a website or a folder) and arranges the content into a tree structure.
*   **AI-Powered Summarization:** It uses a Large Language Model (LLM), specifically supporting Google Gemini, to generate summaries for each node in the tree. This allows an agent to understand the content of a branch without reading the full documents.
*   **Multiple Interfaces:** The index can be interacted with in several ways:
    *   A **Command-Line Interface (CLI)** for building, searching, and exploring the index.
    *   A **Web UI** for visual browsing and management.
    *   An **MCP Server** which exposes the index's capabilities (search, explore, fetch content) as a set of tools for other AI agents to use.

The project is built with Python 3.11+ and utilizes libraries such as `google-genai`, `click`, `pydantic`, `fastapi`, and `httpx`.

## Key Architectural Components

*   **`src/agentic_index/models.py`**: Defines the core data structures, including `AgenticIndex` and `IndexNode`, which represent the index and its tree structure using `pydantic`.
*   **`src/agentic_index/builder.py`**: Orchestrates the entire indexing pipeline, which consists of four main stages:
    1.  **Crawl**: Fetches documents from the web or local filesystem (`crawlers/`).
    2.  **Structure**: Organizes the crawled pages into a hierarchy (`structurers/`).
    3.  **Summarize**: Uses an LLM to create summaries for nodes (`summarizer.py`).
    4.  **Assemble**: Combines everything into the final `AgenticIndex` object.
*   **`src/agentic_index/cli.py`**: Implements the command-line interface using `click`.
*   **`src/agentic_index/search.py`**: Provides keyword-based search functionality over the index with TF-IDF-like scoring.
*   **`src/agentic_index/server/mcp_server.py`**: Exposes agentic tools for interacting with the index over the MCP protocol.

## Building and Running

### 1. Installation

Set up the environment and install dependencies, including development and evaluation tools:

```bash
pip install -e ".[dev,eval]"
```

### 2. Building an Index

To create an index from a source, use the `build` command. The LLM provider (e.g., Gemini) will be used for summarization.

```bash
# Build an index from a website
agentic-index build https://code.claude.com/docs/en -o claude_docs_index.json --provider gemini

# Build an index from a local directory
agentic-index build ./src -o local_code_index.json --provider gemini
```

### 3. Running Tests

The project uses `pytest`. To run the test suite:

```bash
pytest
```

### 4. Code Style and Linting

The project uses `ruff` for linting and formatting. To check the code:

```bash
ruff check .
```

### 5. Using the Tool

Once an index is built, you can interact with it in several ways:

```bash
# Interactively explore the index tree from the command line
agentic-index explore claude_docs_index.json

# Search for a term
agentic-index search "authentication" claude_docs_index.json

# Start the web UI
agentic-index ui claude_docs_index.json

# Start the MCP server for agentic interaction
agentic-index serve claude_docs_index.json
```

## Development Conventions

*   **Asynchronous Operations**: The project makes extensive use of `asyncio` for I/O-bound tasks like crawling and calling LLM APIs.
*   **Data Modeling**: `pydantic` is used for all core data models, ensuring type safety and serialization.
*   **Dependency Management**: Dependencies are managed in `pyproject.toml`. There are separate optional dependencies for `dev` and `eval`.
*   **Testing**: Tests are located in the `tests/` directory and are written using `pytest`. Asynchronous code is tested using `pytest-asyncio`.
