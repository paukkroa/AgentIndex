---
id: 0.0.2.2
title: "binascii— Convert between binary and ASCII¶"
nav_summary: "The `binascii` module provides **low-level, high-performance C-implemented functions** for converting between binary data and ASCII-encoded formats, p"
ref: https://docs.python.org/3/library/binascii.html
ref_type: url
---

# binascii— Convert between binary and ASCII¶

The `binascii` module provides **low-level, high-performance C-implemented functions** for converting between binary data and ASCII-encoded formats, primarily used internally by higher-level modules like `base64` and `quopri`. It supports **uuencode, Base64, and quoted-printable (QP) encoding/decoding**, with strict adherence to **RFC standards** (e.g., RFC 3548 for Base64). Key features include:
- **`a2b_*` functions** (e.g., `a2b_uu`, `a2b_base64`) decode ASCII strings (ASCII-only Unicode or bytes-like objects) into binary data.
- **`b2a_*` functions** (e.g., `b2a_uu`, `b2a_base64`) encode binary data into ASCII formats, with optional parameters like `strict_mode` (Base64) or `backtick` (uuencode).
- **Strict validation**: Newer versions (e.g., `strict_mode` in `a2b_base64`) enforce RFC compliance, raising `binascii.Error` for invalid input.
- **Performance**: Optimized for

[Link to original](https://docs.python.org/3/library/binascii.html)
