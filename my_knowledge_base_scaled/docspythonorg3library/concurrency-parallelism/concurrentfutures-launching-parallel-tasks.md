---
id: 0.0.9.2
title: "concurrent.futures— Launching parallel tasks¶"
nav_summary: "High-level parallel task execution with threads/process"
ref: https://docs.python.org/3/library/concurrent.futures.html
ref_type: url
---

# concurrent.futures— Launching parallel tasks¶

The `concurrent.futures` module (introduced in Python 3.2) offers a high-level abstraction for executing callables asynchronously using threads or processes, simplifying parallel task management. It provides three executor implementations—`ThreadPoolExecutor` (for thread-based concurrency), `ProcessPoolExecutor` (for process-based parallelism), and `InterpreterPoolExecutor` (for isolated Python interpreter execution)—all adhering to the same `Executor` interface. Core features include:
- **`submit()`**: Asynchronously schedules callables, returning a `Future` object representing the task’s execution state.
- **`map()`**: Parallelizes function application over iterables, with configurable buffering and concurrency control.
- **`Future` objects**: Track task status (pending/running/done) and retrieve results via `.result()` or handle exceptions via `.exception()`.
- **Thread safety**: Executors manage worker pools, limiting resource contention.
- **Non-WASI compatibility**: Not supported on WebAssembly platforms.

Key distinctions from `asyncio.Future` include lack of coroutine integration and reliance on blocking I/O for task coordination.

---

[Link to original](https://docs.python.org/3/library/concurrent.futures.html)
