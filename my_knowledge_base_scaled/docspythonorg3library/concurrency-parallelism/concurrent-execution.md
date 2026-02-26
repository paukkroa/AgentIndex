---
id: 0.0.9.5
title: "Concurrent Execution¶"
nav_summary: "The **Concurrent Execution** chapter in the Python Standard Library outlines modules for enabling concurrent task execution, tailored to task type (CP"
ref: https://docs.python.org/3/library/concurrency.html
ref_type: url
---

# Concurrent Execution¶

The **Concurrent Execution** chapter in the Python Standard Library outlines modules for enabling concurrent task execution, tailored to task type (CPU-bound vs. I/O-bound) and development preferences (cooperative vs. preemptive multitasking). It covers two primary paradigms: **thread-based parallelism** via the [`threading`](threading.html) module, which leverages lightweight threads under Python’s **Global Interpreter Lock (GIL)** for shared-memory concurrency, and **process-based parallelism** via [`multiprocessing`](multiprocessing.html), which bypasses the GIL by spawning separate memory spaces. Key features include:
- **Threading**: Thread objects, locks (`Lock`, `RLock`), condition variables, semaphores, events, timers, and barriers for synchronization, with support for context managers (`with` statements) for resource management.
- **Multiprocessing**: Process isolation via `Process` class, inter-process communication (IPC) through pipes, queues, and shared memory (`sharedctypes`), synchronization primitives (e.g., `Event`, `Condition`), and distributed task pools (`Pool`). Advanced topics include managers for shared state, authentication keys, and logging.
- **Trade

[Link to original](https://docs.python.org/3/library/concurrency.html)
