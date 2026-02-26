---
id: 0.0.10.0.3
title: "selectors— High-level I/O multiplexing¶"
nav_summary: "High-level"
ref: https://docs.python.org/3/library/selectors.html
ref_type: url
---

# selectors— High-level I/O multiplexing¶

The `selectors` module provides a high-level, efficient abstraction for **I/O multiplexing** in Python, built atop the lower-level `select` module. It simplifies handling multiple file descriptors (sockets, pipes, etc.) by offering an **abstract base class (`BaseSelector`)** and platform-specific implementations (`EpollSelector`, `KqueueSelector`, `PollSelector`, etc.). The **`DefaultSelector`** automatically selects the most efficient backend for the current OS (e.g., `Epoll` on Linux, `Kqueue` on BSD/macOS). Key features include:
- **Event-driven I/O monitoring** via bitmask flags (`EVENT_READ`, `EVENT_WRITE`) to track readiness for read/write operations.
- **`SelectorKey` objects** (immutable `namedtuple`s) that associate file objects with their descriptors, events, and optional metadata.
- **Cross-platform support** (Windows: sockets only; Unix: pipes, FIFOs, etc.), though **not available on WASI/WebAssembly**.
- **Thread-safe** and optimized for scalability, ideal for async networking (e.g., HTTP servers, WebSockets).

---

[Link to original](https://docs.python.org/3/library/selectors.html)
