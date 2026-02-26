---
id: 0.0.10.4.3
title: "urllib.error— Exception classes raised by urllib.request¶"
nav_summary: "`urllib.error: HTTP/URL exceptions (URLError, HTTPError, ContentTooShortError)`"
ref: https://docs.python.org/3/library/urllib.error.html
ref_type: url
---

# urllib.error— Exception classes raised by urllib.request¶

The `urllib.error` module defines core exception classes for handling errors in `urllib.request`, with `URLError` as the base class (subclass of `OSError`). Key exceptions include:
- **`URLError`**: Base exception for network-related issues, with a `reason` attribute (string or nested exception).
- **`HTTPError`**: Subclass of `URLError` for HTTP-specific errors (e.g., 404, 500), providing HTTP status `code`, `reason`, headers (`headers`), and a file-like `fp` for error body access. It also doubles as a file-like object for non-exceptional HTTP responses.
- **`ContentTooShortError`**: Triggered by `urlretrieve()` when downloaded content length (via `Content-Length` header) is shorter than expected, with `content` and `msg` attributes.

[Link to original](https://docs.python.org/3/library/urllib.error.html)
