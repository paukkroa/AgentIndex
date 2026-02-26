---
id: 0.0.9.1.1
title: "multiprocessing.shared_memory— Shared memory for direct access across processes¶"
nav_summary: "The `multiprocessing"
ref: https://docs.python.org/3/library/multiprocessing.shared_memory.html
ref_type: url
---

# multiprocessing.shared_memory— Shared memory for direct access across processes¶

The `multiprocessing.shared_memory` module (introduced in Python 3.8) enables efficient inter-process communication via **POSIX-style shared memory blocks**, allowing multiple processes to directly read/write volatile memory regions without serialization overhead. The core class, [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory), facilitates allocation (`create=True`) or attachment (`create=False`) of shared memory blocks with a unique `name` (auto-generated if omitted). Key methods include:
- **`close()`**: Detaches the current process from the shared block (but retains the block for other processes).
- **`unlink()`**: Deletes the shared block entirely when no processes require it, ensuring resource cleanup.

For lifecycle management across processes, the [`SharedMemoryManager`](https://docs.python.org/3/library/multiprocessing.managers.html#multiprocessing.managers.SharedMemoryManager) (from `multiprocessing.managers`) provides centralized control. This mechanism avoids IPC bottlenecks (e.g., sockets, pipes) by bypassing serialization, delivering near-native performance for high-throughput parallel tasks on SMP/multicore

[Link to original](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
