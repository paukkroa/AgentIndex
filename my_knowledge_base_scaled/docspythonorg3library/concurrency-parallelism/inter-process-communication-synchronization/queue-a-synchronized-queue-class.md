---
id: 0.0.9.3.1
title: "queue— A synchronized queue class¶"
nav_summary: "Thread-safe queues: FIFO, LIFO, priority, and simple unbounded."
ref: https://docs.python.org/3/library/queue.html
ref_type: url
---

# queue— A synchronized queue class¶

The `queue` module in Python’s standard library provides thread-safe, multi-producer/multi-consumer queue implementations for concurrent programming. It offers four queue types: **FIFO (`Queue`)**, **LIFO (`LifoQueue`)**, **priority (`PriorityQueue`)**, and **unbounded FIFO (`SimpleQueue`)**. All queues use internal locks to synchronize access, preventing race conditions in threaded environments. The `Queue` and `LifoQueue` support configurable bounded sizes (default: infinite), blocking insertion/consumption when full/empty. The `PriorityQueue` retrieves items based on priority (using `heapq` for ordering), requiring tuples or custom classes (e.g., `@dataclass(order=True)`) for prioritization. `SimpleQueue` is a lightweight, unbounded FIFO alternative with minimal overhead. Exceptions like `Empty` signal failed non-blocking operations.

---

[Link to original](https://docs.python.org/3/library/queue.html)
