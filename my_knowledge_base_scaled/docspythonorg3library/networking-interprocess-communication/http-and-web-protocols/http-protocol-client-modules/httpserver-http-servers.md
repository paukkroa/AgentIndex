---
id: 0.0.10.3.0.1
title: "http.server— HTTP servers¶"
nav_summary: "The `http"
ref: https://docs.python.org/3/library/http.server.html
ref_type: url
---

# http.server— HTTP servers¶

The `http.server` module provides foundational classes for creating **basic HTTP servers** in Python, leveraging `socketserver` for low-level socket handling. It includes three primary server classes:
1. **`HTTPServer`** – A subclass of `socketserver.TCPServer` that listens on a specified address (`server_name`, `server_port`) and dispatches requests to a `RequestHandlerClass` (e.g., `BaseHTTPRequestHandler`). Suitable for simple, single-threaded use but **blocking** under concurrent connections (e.g., browser pre-connections).
2. **`ThreadingHTTPServer`** – Extends `HTTPServer` with threading support (via `socketserver.ThreadingMixIn`) to handle concurrent requests efficiently, avoiding indefinite blocking. Introduced in **Python 3.7**.
3. **`HTTPSServer`** – A secure HTTPS wrapper using the `ssl` module, requiring certificate (`certfile`) and key (`keyfile`) files. Supports ALPN protocol negotiation and password-protected PKCS#8 keys, though **not recommended for production** due to limited security features (e.g., no TLS 1.3, weak defaults).

**Key Features:**
-

[Link to original](https://docs.python.org/3/library/http.server.html)
