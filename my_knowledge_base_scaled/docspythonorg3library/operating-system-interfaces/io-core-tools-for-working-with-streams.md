---
id: 0.0.8.1
title: "io— Core tools for working with streams¶"
nav_summary: "The `io` module in Python provides core tools for handling **text, binary, and raw I/O streams**, enabling flexible data processing across various bac"
ref: https://docs.python.org/3/library/io.html
ref_type: url
---

# io— Core tools for working with streams¶

The `io` module in Python provides core tools for handling **text, binary, and raw I/O streams**, enabling flexible data processing across various backing stores (e.g., files, sockets, or in-memory buffers). Key features include:
- **Stream Types**: Supports **text I/O** (handling `str` objects with automatic encoding/decoding and newline translation), **binary I/O** (working with `bytes`-like objects without encoding), and **raw I/O** (low-level byte manipulation).
- **Stream Capabilities**: Streams can be **read-only, write-only, or read-write**, with **random access** (via `seek()`) or **sequential access** (e.g., sockets/pipes). Type safety ensures `TypeError` is raised for mismatched data types (e.g., passing `str` to a binary stream).
- **Key Classes**:
  - **Text Streams**: `TextIOBase` (API reference), `StringIO` (in-memory text), and `open()` with `encoding` (e.g., `utf-8`).
  - **Binary Streams**: `BufferedIOBase` (API reference), `BytesIO` (in-memory binary),

[Link to original](https://docs.python.org/3/library/io.html)
