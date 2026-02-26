---
id: 0.0.9.0.0
title: "threading— Thread-based parallelism¶"
nav_summary: "The `threading` module in Python provides a high-level interface for creating and managing **thread-based parallelism**, enabling concurrent execution"
ref: https://docs.python.org/3/library/threading.html
ref_type: url
---

# threading— Thread-based parallelism¶

The `threading` module in Python provides a high-level interface for creating and managing **thread-based parallelism**, enabling concurrent execution of tasks within a single process by leveraging smaller execution units called threads. Built atop the low-level `_thread` module, it facilitates lightweight, shared-memory concurrency—ideal for I/O-bound operations (e.g., network requests or file operations) where threads spend time waiting for external resources. Key features include:
- **Thread creation** via `threading.Thread`, allowing customizable tasks via `target`, `args`, and `kwargs`.
- **Thread synchronization** through locks (`threading.Lock`), events (`threading.Event`), and condition variables (`threading.Condition`) to prevent race conditions.
- **Thread management** with methods like `start()`, `join()`, and `daemon` (for background threads).
- **Thread-safe data structures** (e.g., `queue.Queue`) for inter-thread communication.
- **Global Interpreter Lock (GIL) limitation**: CPython’s GIL restricts true parallelism for CPU-bound tasks, making `multiprocessing` preferable for CPU-heavy workloads.
- **Compatibility notes**: Python 3.7+ includes `thread

[Link to original](https://docs.python.org/3/library/threading.html)
