---
id: 0.0.15.3
title: "faulthandler— Dump the Python traceback¶"
nav_summary: "The `faulthandler` module (introduced in Python 3"
ref: https://docs.python.org/3/library/faulthandler.html
ref_type: url
---

# faulthandler— Dump the Python traceback¶

The `faulthandler` module (introduced in Python 3.3) provides functions to programmatically dump Python tracebacks during catastrophic failures (e.g., segmentation faults, floating-point errors, or illegal instructions) or via explicit calls. By enabling fault handlers via `faulthandler.enable()`, users can catch signals like `SIGSEGV`, `SIGFPE`, `SIGABRT`, `SIGBUS`, and `SIGILL` and log minimal yet critical traceback details (e.g., filenames, function names, and line numbers) to `sys.stderr` or a custom file. The module leverages a signal-safe alternative stack (via `sigaltstack`) to avoid stack overflows, ensuring tracebacks are captured even in deadlocks or crashes. Key limitations include ASCII-only output, truncated strings (≤500 chars), and limited depth (≤100 frames/threads). The module is C-implemented for reliability and integrates with system fault handlers (e.g., Apport, Windows). Python’s **Development Mode** automatically enables it. For manual traceback dumping, use `dump_traceback()` (supports file descriptors since Python 3.5) or `

[Link to original](https://docs.python.org/3/library/faulthandler.html)
