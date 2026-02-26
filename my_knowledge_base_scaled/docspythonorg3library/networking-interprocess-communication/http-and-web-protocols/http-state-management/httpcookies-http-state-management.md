---
id: 0.0.10.3.1.0
title: "http.cookies— HTTP state management¶"
nav_summary: "HTTP cookie parsing, state management, `BaseCookie`, `SimpleCookie` classes"
ref: https://docs.python.org/3/library/http.cookies.html
ref_type: url
---

# http.cookies— HTTP state management¶

The `http.cookies` module in Python’s standard library provides classes for managing HTTP cookies, enabling stateful interactions between clients and servers. It supports both simple string-based cookies and complex serializable data types as cookie values. The module adheres to relaxed parsing rules (compared to legacy RFC 2109/2068) to accommodate modern browser and server behavior, allowing characters like `:`, ASCII letters, digits, and specific symbols (`!#$%&'*+-.^_`|~`) in cookie names. Key components include:
- **`CookieError`**: Raised for malformed cookies violating RFC 2109 standards.
- **`BaseCookie`**: A dictionary-like object storing cookies as `Morsel` instances (key-value pairs with metadata like expiration, path, or domain).
- **`SimpleCookie`**: A subclass of `BaseCookie` optimized for string values, using Python’s `str()` for encoding/decoding.
The module is designed for server-side cookie handling, while `http.cookiejar` complements it for client-side automation.

---

[Link to original](https://docs.python.org/3/library/http.cookies.html)
