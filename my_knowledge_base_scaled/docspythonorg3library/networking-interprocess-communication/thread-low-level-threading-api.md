---
id: 0.0.10.2
title: "_thread— Low-level threading API¶"
nav_summary: "Low-level threading primitives: locks, threads, signals, and exits."
ref: https://docs.python.org/3/library/_thread.html
ref_type: url
---

# _thread— Low-level threading API¶

The `_thread` module provides a **low-level threading API** for managing lightweight processes (threads) in Python, enabling concurrent execution within a shared memory space. It offers primitive synchronization mechanisms, primarily **mutex locks (`LockType`)** for thread-safe operations. Key functions include:
- **`start_new_thread(function, args[, kwargs])`**: Launches a new thread executing the given function with provided arguments; exceptions are handled via `sys.unraisablehook()`.
- **`interrupt_main(signum=signal.SIGINT)`**: Simulates signal delivery (e.g., `SIGINT`) to the main thread, triggering its handler if configured.
- **`exit()`**: Terminates the current thread by raising `SystemExit`.
- **`allocate_lock()`**: Creates a lock object for thread synchronization (deprecated in favor of `threading.Lock` in higher-level APIs).

Since Python 3.7, this module is **always available** (previously optional). For higher-level abstractions, the [`threading`](threading.html) module is recommended.

---

[Link to original](https://docs.python.org/3/library/_thread.html)
