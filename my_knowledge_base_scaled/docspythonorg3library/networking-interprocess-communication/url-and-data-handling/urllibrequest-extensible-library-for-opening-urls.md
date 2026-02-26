---
id: 0.0.10.4.1
title: "urllib.request— Extensible library for opening URLs¶"
nav_summary: "`urllib.request` – Fetch URLs with HTTP/HTTPS/FTP support."
ref: https://docs.python.org/3/library/urllib.request.html
ref_type: url
---

# urllib.request— Extensible library for opening URLs¶

The `urllib.request` module is a core Python library for opening and interacting with URLs, supporting HTTP/HTTPS, FTP, and other protocols while handling complexities like authentication (basic/digest), redirects, cookies, and proxies. It provides the `urlopen()` function to fetch URLs (strings or `Request` objects) with optional data payloads, timeouts, and SSL contexts. The returned objects (e.g., `HTTPResponse` or `addinfourl`) include metadata like headers, status codes, and URLs, and act as context managers. Key features include HTTP/1.1 compliance, proxy support, and integration with `ssl.SSLContext` for secure connections. Note macOS-specific caveats with `os.fork()` and WASI/WebAssembly incompatibility.

---

[Link to original](https://docs.python.org/3/library/urllib.request.html)
