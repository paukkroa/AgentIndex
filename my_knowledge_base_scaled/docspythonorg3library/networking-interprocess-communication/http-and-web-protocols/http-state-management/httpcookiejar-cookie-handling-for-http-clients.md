---
id: 0.0.10.3.1.1
title: "http.cookiejar— Cookie handling for HTTP clients¶"
nav_summary: "The `http"
ref: https://docs.python.org/3/library/http.cookiejar.html
ref_type: url
---

# http.cookiejar— Cookie handling for HTTP clients¶

The `http.cookiejar` module in Python’s standard library provides robust cookie handling for HTTP clients, supporting both **Netscape-style cookies** (de facto standard) and **RFC 2965 cookies** (disabled by default). It implements the **de-facto Netscape cookie protocol**, including advanced attributes like `max-age` and `port`, while parsing **RFC 2109 cookies** as Netscape-compatible. Key components include:

- **`LoadError`**: Exception raised when a `FileCookieJar` fails to load cookies from a file (subclass of `OSError`).
- **`CookieJar`**: Base class for storing/retrieving cookies, auto-expiring stale entries, and integrating with HTTP requests/responses.
- **`FileCookieJar`**: Subclass of `CookieJar` that persists cookies to/from disk via a specified filename. Supports delayed writes (`delayload`) for performance optimization.

The module enforces **cookie-attributes** (e.g., `domain`, `expires`) via a **`CookiePolicy`** interface, allowing customizable behavior. It is essential for managing session state in HTTP clients, particularly for websites relying on

[Link to original](https://docs.python.org/3/library/http.cookiejar.html)
