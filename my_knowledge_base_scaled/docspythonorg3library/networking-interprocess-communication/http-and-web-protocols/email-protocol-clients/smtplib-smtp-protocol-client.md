---
id: 0.0.10.3.2.3
title: "smtplib— SMTP protocol client¶"
nav_summary: "The `smtplib` module provides a Python interface for interacting with **SMTP (Simple Mail Transfer Protocol)** and **ESMTP (Extended SMTP)** servers,"
ref: https://docs.python.org/3/library/smtplib.html
ref_type: url
---

# smtplib— SMTP protocol client¶

The `smtplib` module provides a Python interface for interacting with **SMTP (Simple Mail Transfer Protocol)** and **ESMTP (Extended SMTP)** servers, enabling email transmission via standard protocols defined in **RFC 821** and **RFC 1869**. It implements an `SMTP` class that encapsulates SMTP connections, supporting full protocol operations like authentication, message sending, and server commands. Key features include:
- **Connection Management**: Supports initialization with optional `host`, `port`, `local_hostname`, `timeout`, and `source_address` parameters for socket binding.
- **Core Methods**: Essential functions include `connect()`, `sendmail()`, and `quit()`, with support for context management via `with` statements (since Python 3.3) for automatic `QUIT` command execution.
- **Error Handling**: Raises `SMTPConnectError` on connection failures and `TimeoutError` if timeouts occur during blocking operations.
- **Protocol Extensions**: Supports SMTP extensions like **SMTPUTF8** (RFC 6531) for internationalized email addresses.
- **Compatibility**: Not available on **WASI/WebAssembly** platforms.

[Link to original](https://docs.python.org/3/library/smtplib.html)
