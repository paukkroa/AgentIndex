---
id: 0.0.10.4.0
title: "urllib— URL handling modules¶"
nav_summary: "`urllib`: URL handling modules (request, parse, error, robots.txt)."
ref: https://docs.python.org/3/library/urllib.html
ref_type: url
---

# urllib— URL handling modules¶

The `urllib` package in Python’s standard library provides a modular framework for handling URLs, comprising four core submodules: **`urllib.request`** for fetching and reading URLs (including HTTP/HTTPS, FTP, and file URLs), **`urllib.error`** for defining exceptions (e.g., `URLError`, `HTTPError`) raised during operations; **`urllib.parse`** for parsing and reconstructing URLs into components (scheme, netloc, path, etc.) via functions like `urlparse()` and `urljoin()`; and **`urllib.robotparser`** for parsing `robots.txt` files to determine web crawl permissions. This package abstracts low-level networking complexities, offering a unified interface for URL manipulation, error handling, and protocol-agnostic operations while integrating seamlessly with Python’s broader internet support modules.

---

[Link to original](https://docs.python.org/3/library/urllib.html)
