---
id: 0.0.14.3
title: "Python Development Mode¶"
nav_summary: "The **Python Development Mode**, introduced in **Python 3"
ref: https://docs.python.org/3/library/devmode.html
ref_type: url
---

# Python Development Mode¶

The **Python Development Mode**, introduced in **Python 3.7**, activates runtime checks for performance-sensitive but critical issues, emitting warnings only when problems are detected. It can be enabled via the `-X dev` CLI flag or by setting `PYTHONDEVMODE=1`. This mode combines multiple debugging features, including:
1. **Warning Filtering**: Displays `DeprecationWarning`, `ImportWarning`, `PendingDeprecationWarning`, and `ResourceWarning` (equivalent to `-W default`).
2. **Memory Debugging**: Installs debug hooks on allocators to detect buffer underflows, overflows, API violations, and unsafe GIL usage (simulates `PYTHONMALLOC=debug`).
3. **Crash Handling**: Enables `faulthandler` to dump tracebacks on fatal signals (`SIGSEGV`, `SIGFPE`, etc.).
4. **AsyncIO Debugging**: Activates asyncio debug mode to log unawaited coroutines (equivalent to `PYTHONASYNCIODEBUG=1`).
To exclude memory checks, set `PYTHONMALLOC=default`. Warnings can be treated as errors via `-W error

[Link to original](https://docs.python.org/3/library/devmode.html)
