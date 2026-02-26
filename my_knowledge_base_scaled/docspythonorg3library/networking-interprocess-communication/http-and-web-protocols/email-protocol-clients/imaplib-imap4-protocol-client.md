---
id: 0.0.10.3.2.2
title: "imaplib— IMAP4 protocol client¶"
nav_summary: "Python IMAP4 client library for email servers (RFC 2060/1730)."
ref: https://docs.python.org/3/library/imaplib.html
ref_type: url
---

# imaplib— IMAP4 protocol client¶

The `imaplib` module provides Python classes (`IMAP4`, `IMAP4_SSL`, and `IMAP4_stream`) for interacting with **IMAP4/IMAP4rev1** email servers, adhering to **RFC 2060** (and backward-compatible with **RFC 1730**). The core `IMAP4` class establishes connections to servers (default port **143**), supports **context managers** (via `with` statement) for automatic logout, and includes **timeout** configuration (since Python 3.9). It raises custom exceptions (`IMAP4.error`, `IMAP4.abort`, `IMAP4.readonly`) for server errors, disconnections, or permission changes. For secure connections, `IMAP4_SSL` (default port **993**) leverages SSL/TLS via an optional `ssl_context` parameter. The module excludes **WASI/WebAssembly** support and lacks `STATUS` command support (IMAP4-only limitation).

---

[Link to original](https://docs.python.org/3/library/imaplib.html)
