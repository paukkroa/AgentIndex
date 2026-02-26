---
id: 0.0.10.3.4
title: "http— HTTP modules¶"
nav_summary: "The `http` package in Python’s standard library provides a collection of modules for interacting with the **HyperText Transfer Protocol (HTTP)**, enab"
ref: https://docs.python.org/3/library/http.html
ref_type: url
---

# http— HTTP modules¶

The `http` package in Python’s standard library provides a collection of modules for interacting with the **HyperText Transfer Protocol (HTTP)**, enabling developers to handle HTTP clients, servers, cookies, and status codes. Key components include:
- **`http.client`**: A low-level HTTP/HTTPS client module for direct protocol interactions (requires sockets), ideal for custom HTTP requests beyond `urllib.request`.
- **`http.server`**: A framework for building HTTP servers using `socketserver`, offering basic server classes and request handlers.
- **`http.cookies`**: Utilities for managing HTTP state via cookies, including parsing, generating, and handling cookie headers.
- **`http.cookiejar`**: Persistent cookie storage with classes for automatic cookie management across sessions.
- **`HTTPStatus` (enum)**: A standardized enum defining **IANA-registered HTTP status codes** (e.g., `200 OK`, `404 NOT_FOUND`) with numeric values, reason phrases, and detailed descriptions, aligned with **RFC 9110** and other HTTP standards. Supports all standard codes (1xx–5xx) and includes extended codes like `103 EARLY_HINTS`.

The

[Link to original](https://docs.python.org/3/library/http.html)
