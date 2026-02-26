---
id: 0.0.10.0.2
title: "select— Waiting for I/O completion¶"
nav_summary: "`select` module: I/O multiplexing via `select()`, `poll()`, `epoll()`,"
ref: https://docs.python.org/3/library/select.html
ref_type: url
---

# select— Waiting for I/O completion¶

The `select` module in Python provides cross-platform access to low-level I/O multiplexing primitives, including `select()`, `poll()`, `devpoll()` (Solaris), `epoll()` (Linux 2.5+), and `kqueue()` (BSD). It enables efficient waiting for I/O readiness on sockets, pipes, and other file descriptors (but not regular files). For high-level abstractions, users are advised to use the [`selectors`](selectors.html) module instead. Key features include:
- **`select.error`**: Deprecated alias for `OSError` (replaced in Python 3.3+).
- **`devpoll()`**: Solaris-specific polling object with non-inheritable descriptors.
- **`epoll()`**: Linux edge/level-triggered I/O monitoring with optional size hints and context manager support.
- **Cross-platform limitations**: Windows restricts usage to sockets; WASI/WebAssembly unsupported.
- **Descriptor management**: New descriptors are non-inheritable, and `epoll` objects auto-close via `with` statements.

---

[Link to original](https://docs.python.org/3/library/select.html)
