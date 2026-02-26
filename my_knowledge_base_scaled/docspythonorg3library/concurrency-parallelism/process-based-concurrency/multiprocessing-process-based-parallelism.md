---
id: 0.0.9.1.0
title: "multiprocessing— Process-based parallelism¶"
nav_summary: "`multiprocessing: Process-based parallelism, bypasses GIL, Pool, Process lifecycle`"
ref: https://docs.python.org/3/library/multiprocessing.html
ref_type: url
---

# multiprocessing— Process-based parallelism¶

The `multiprocessing` module enables **process-based parallelism** in Python by bypassing the **Global Interpreter Lock (GIL)** via subprocesses, allowing full utilization of multi-core systems. It provides APIs for **local and remote concurrency**, including the **`Pool`** class for **data parallelism** (distributing tasks across processes) and **`Process`** objects for explicit process management. Key features include **process lifecycle control** (start, terminate, kill, interrupt), **shared memory** (via `multiprocessing.shared_memory`), and **cross-platform support** (POSIX/Windows). Unlike `threading`, it offers **forceful process termination** and integrates with higher-level abstractions like `concurrent.futures.ProcessPoolExecutor` for asynchronous task execution. Example: A `Pool` with 5 workers computes `[x²]` for inputs `[1, 2, 3]` efficiently.

---

[Link to original](https://docs.python.org/3/library/multiprocessing.html)
