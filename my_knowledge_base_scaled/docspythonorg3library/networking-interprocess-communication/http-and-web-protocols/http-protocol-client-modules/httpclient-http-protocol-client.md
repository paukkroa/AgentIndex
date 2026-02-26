---
id: 0.0.10.3.0.0
title: "http.client— HTTP protocol client¶"
nav_summary: "The `http"
ref: https://docs.python.org/3/library/http.client.html
ref_type: url
---

# http.client— HTTP protocol client¶

The `http.client` module provides Python’s low-level implementation for HTTP/HTTPS client-side communication, enabling direct interaction with web servers via the `HTTPConnection` and `HTTPSConnection` classes. `HTTPConnection` manages plain HTTP connections (default port 80) with configurable timeouts, source addresses, and buffer sizes (default 8192 bytes), while `HTTPSConnection` extends it with SSL/TLS support (default port 443) via the `ssl` module. Key features include:
- **Connection Management**: Automatic port resolution (e.g., `host:port` or default 80/443) and timeout handling.
- **SSL/TLS Integration**: `HTTPSConnection` leverages `ssl.SSLContext` for secure connections, with support for SNI (Server Name Indication) and hostname verification.
- **Historical Notes**: Deprecated features (e.g., `strict` parameter in 3.4) and additions (e.g., `source_address` in 3.2, `blocksize` in 3.7) reflect evolving protocol standards.
- **Use Cases**: Primarily used internally by `urllib.request`; higher-level alternatives

[Link to original](https://docs.python.org/3/library/http.client.html)
