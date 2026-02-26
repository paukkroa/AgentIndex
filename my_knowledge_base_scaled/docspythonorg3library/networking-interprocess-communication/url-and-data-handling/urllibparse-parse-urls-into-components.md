---
id: 0.0.10.4.2
title: "urllib.parse— Parse URLs into components¶"
nav_summary: "Parse URLs into components: schemes, paths, queries, fragments."
ref: https://docs.python.org/3/library/urllib.parse.html
ref_type: url
---

# urllib.parse— Parse URLs into components¶

The `urllib.parse` module provides a standardized interface for decomposing, reconstructing, and resolving URLs into their fundamental components (e.g., scheme, network location, path, query, and fragment). It adheres to **RFC 3986** standards for URL parsing while maintaining backward compatibility with legacy terms like `netloc` (deprecated in favor of `authority`). The module supports **19 URL schemes**, including `http`, `https`, `ftp`, and `file`, though Apple’s `itms-services` scheme may be excluded for App Store compliance. Core functions like `urlsplit()` break URLs into a structured `SplitResult` named tuple (e.g., `scheme`, `netloc`, `path`, `query`, `fragment`), preserving delimiters like `#` and `?` but leaving percent-encoded characters unexpanded. This module also enables relative-to-absolute URL resolution and URL component reassembly, facilitating robust web and network protocol interactions.

---

[Link to original](https://docs.python.org/3/library/urllib.parse.html)
