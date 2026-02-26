---
id: 0.0.8.3.2
title: "logging.handlers— Logging handlers¶"
nav_summary: "The `logging"
ref: https://docs.python.org/3/library/logging.handlers.html
ref_type: url
---

# logging.handlers— Logging handlers¶

The `logging.handlers` module in Python’s standard library provides specialized logging handlers for advanced logging use cases, extending the core `logging` module’s functionality. It includes handlers like **`StreamHandler`** (defined in the core `logging` module but documented here), which directs log output to streams such as `sys.stdout`, `sys.stderr`, or custom file-like objects (requiring `write()` and `flush()` methods). Key features include:
- **Customizable output streams** via `setStream()` (added in Python 3.7), allowing dynamic redirection.
- **Configurable formatting** via a formatter, with optional exception traceback inclusion using `traceback.print_exception()`.
- **Terminator control** via the `terminator` attribute (defaults to `\n`), enabling custom line endings or suppression.
- **Manual flushing** via `flush()` to ensure output persistence, especially critical for buffered streams.
- **Inherited `close()`** from `Handler` (no direct output impact) and **stream flushing** before switching streams.

This module complements basic handlers like `FileHandler` and `NullHandler` (also documented here) by offering stream-based logging flexibility.

---
**NAV

[Link to original](https://docs.python.org/3/library/logging.handlers.html)
