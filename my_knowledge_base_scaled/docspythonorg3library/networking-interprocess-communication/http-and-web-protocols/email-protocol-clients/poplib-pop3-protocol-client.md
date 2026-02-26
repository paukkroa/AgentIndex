---
id: 0.0.10.3.2.1
title: "poplib— POP3 protocol client¶"
nav_summary: "The `poplib` module provides Python classes for interacting with **POP3 (Post Office Protocol version 3)** servers, adhering to **RFC 1939** (with opt"
ref: https://docs.python.org/3/library/poplib.html
ref_type: url
---

# poplib— POP3 protocol client¶

The `poplib` module provides Python classes for interacting with **POP3 (Post Office Protocol version 3)** servers, adhering to **RFC 1939** (with optional extensions from **RFC 2595** for encrypted communication via `STLS`). It includes two primary classes:
1. **`POP3`** – A basic POP3 client connecting to port **110** (or customizable port) with support for timeouts and auditing events (`poplib.connect`, `poplib.putline`). It implements both minimal and optional POP3 commands, including encrypted sessions via `STLS`.
2. **`POP3_SSL`** – A subclass of `POP3` for **SSL-encrypted connections** (default port **995**), allowing custom SSL contexts (`ssl.SSLContext`) for secure communication. Both classes raise auditing events for connection and command logging.

**Key Features:**
- **Protocol Compliance:** Supports POP3’s core and optional commands (e.g., `USER`, `PASS`, `STAT`, `RETR`, `DELE`, `QUIT`).
- **Security:** Encrypted sessions via `STLS

[Link to original](https://docs.python.org/3/library/poplib.html)
