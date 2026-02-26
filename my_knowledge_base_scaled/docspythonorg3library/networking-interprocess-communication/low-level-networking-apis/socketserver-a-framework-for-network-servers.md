---
id: 0.0.10.0.4
title: "socketserver— A framework for network servers¶"
nav_summary: "Python’s `socketserver` simplifies network server development with TCP/UDP/Unix socket support."
ref: https://docs.python.org/3/library/socketserver.html
ref_type: url
---

# socketserver— A framework for network servers¶

The `socketserver` module in Python provides a high-level framework for building network servers, abstracting low-level socket operations to simplify server development. It offers four primary server classes—`TCPServer`, `UDPServer`, `UnixStreamServer`, and `UnixDatagramServer`—supporting TCP, UDP, and Unix domain sockets (the latter two being Unix-specific). These classes handle synchronous request processing, blocking until each request completes. For performance-critical applications requiring concurrent handling of long-running or data-intensive requests, the module includes mix-in classes like `ForkingMixIn` (process-based) and `ThreadingMixIn` (thread-based) to enable asynchronous behavior. Server creation involves subclassing `BaseRequestHandler` to define request processing logic (via the `handle()` method) and instantiating a server class with the target address and handler. The module emphasizes resource safety, recommending use within a `with` statement for automatic cleanup.

---

[Link to original](https://docs.python.org/3/library/socketserver.html)
