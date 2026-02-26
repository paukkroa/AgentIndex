---
id: 0.0.9.4.1
title: "concurrent.interpreters— Multiple interpreters in the same process¶"
nav_summary: "`concurrent.interpreters`: Manage isolated Python subinterpreters in-process."
ref: https://docs.python.org/3/library/concurrent.interpreters.html
ref_type: url
---

# concurrent.interpreters— Multiple interpreters in the same process¶

The `concurrent.interpreters` module (introduced in Python 3.14) provides a high-level API for managing and utilizing **subinterpreters**—isolated execution contexts within the same process. Built atop the lower-level `_interpreters` module, it enables running code in separate interpreters, each maintaining its own runtime state (e.g., imports, builtins, and thread-specific state like exceptions). While isolation is the core feature, true concurrency requires pairing with threading (e.g., via `threading` or `InterpreterPoolExecutor`). Key limitations include incomplete isolation (due to shared process memory) and limited PyPI package compatibility. The module is unavailable on WASI/WebAssembly. PEP 554, 734, and 684 underpin its design.

---

[Link to original](https://docs.python.org/3/library/concurrent.interpreters.html)
