---
id: 0.0.10.1.1
title: "signal— Set handlers for asynchronous events¶"
nav_summary: "The `signal` module in Python enables the registration of custom handlers for asynchronous system signals (e"
ref: https://docs.python.org/3/library/signal.html
ref_type: url
---

# signal— Set handlers for asynchronous events¶

The `signal` module in Python enables the registration of custom handlers for asynchronous system signals (e.g., `SIGINT`, `SIGPIPE`), allowing programs to respond to low-level events like process termination requests or broken pipes. Key features include:
- **Signal Registration**: Use `signal.signal()` to assign handlers (e.g., ignore `SIGPIPE` or convert `SIGINT` to `KeyboardInterrupt`).
- **Execution Model**: Handlers run asynchronously via a flag set by the C-level signal handler, deferred to the Python VM (e.g., at the next bytecode instruction), which may delay execution during long C operations (e.g., regex matching).
- **Threading Constraints**: Handlers execute *only* in the main thread, preventing cross-thread communication; use `threading` primitives instead.
- **Platform Limitations**: WebAssembly lacks native signal support, and synchronous errors (e.g., `SIGSEGV`) may cause hangs due to C-level re-raising. The `faulthandler` module aids debugging such cases.
- **Default Behavior**: `SIGCHLD` follows the OS implementation; other signals persist until explicitly reset.

---

**NAVIGATION

[Link to original](https://docs.python.org/3/library/signal.html)
