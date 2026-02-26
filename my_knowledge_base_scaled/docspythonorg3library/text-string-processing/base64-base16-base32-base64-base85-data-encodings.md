---
id: 0.0.2.1
title: "base64— Base16, Base32, Base64, Base85 Data Encodings¶"
nav_summary: "`base64"
ref: https://docs.python.org/3/library/base64.html
ref_type: url
---

# base64— Base16, Base32, Base64, Base85 Data Encodings¶

The Python `base64` module provides robust functions for encoding binary data into printable ASCII characters and vice versa, adhering to **RFC 4648** standards (Base16, Base32, Base64) and non-standard **Base85**. It offers two interfaces: a **modern interface** (supports encoding/decoding bytes-like objects to/from ASCII `bytes`, including URL/filenames-safe variants) and a **legacy interface** (limited to Base64 with RFC 2045 line breaks, primarily for email handling). Key functions include `b64encode()` (encodes bytes to Base64) and `b64decode()` (decodes Base64 to bytes), with optional `altchars` for custom alphabets (e.g., URL-safe). The module also supports ASCII-only Unicode strings in decoding (since Python 3.3) and broader bytes-like object compatibility (since Python 3.4). Base85 encoding was added in Python 3.4. For RFC 2045 compliance (e.g., email), the `email` package is recommended.

---

[Link to original](https://docs.python.org/3/library/base64.html)
