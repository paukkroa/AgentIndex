---
id: 0.0.10.0.0
title: "socket— Low-level networking interface¶"
nav_summary: "The `socket` module in Python provides a low-level interface to the BSD socket API, enabling cross-platform networking across Unix, Windows, macOS, an"
ref: https://docs.python.org/3/library/socket.html
ref_type: url
---

# socket— Low-level networking interface¶

The `socket` module in Python provides a low-level interface to the BSD socket API, enabling cross-platform networking across Unix, Windows, macOS, and other modern systems. It abstracts OS-specific socket calls into Python’s object-oriented model, where the `socket()` function creates a socket object with methods mirroring system-level operations like `bind()`, `connect()`, `send()`, and `recv()`. Buffer handling is automated (e.g., implicit lengths for sends/receives), aligning with Python’s file I/O conventions. Socket families (e.g., `AF_UNIX`, `AF_INET`, `AF_INET6`) dictate address formats: `AF_UNIX` uses filesystem paths (UTF-8 or bytes), `AF_INET` pairs `(host, port)` (IPv4/IPv6), and `AF_INET6` supports IPv6-specific features like scope IDs. Addresses like `''` (bind to all interfaces) or `'<broadcast>'` (IPv4-only) are platform-dependent. The module integrates with higher-level constructs like `socketserver` for servers and `ssl` for encrypted connections, though it lacks support on WebAssembly (WASI). Platform-specific behaviors may vary due to underlying

[Link to original](https://docs.python.org/3/library/socket.html)
