---
id: 0.0.2.3
title: "quopri— Encode and decode MIME quoted-printable data¶"
nav_summary: "Qu"
ref: https://docs.python.org/3/library/quopri.html
ref_type: url
---

# quopri— Encode and decode MIME quoted-printable data¶

The `quopri` module in Python implements **MIME Quoted-Printable (QP) encoding/decoding** as defined in **RFC 1521**, a method optimized for text data containing **few nonprintable characters** (unlike base64, which is better for binary data). It provides functions to encode/decode **binary file streams** or **bytes objects**, with support for **header-specific formatting** (e.g., underscores as spaces in headers per **RFC 1522**). Key functions include:
- **`decode(input, output, header=False)`** and **`decodestring(s, header=False)`**: Reverse QP encoding, handling embedded whitespace (e.g., tabs as spaces in headers).
- **`encode(input, output, quotetabs, header=False)`** and **`encodestring(s, quotetabs=False, header=False)`**: Convert binary data to QP format, optionally encoding spaces/tabs (controlled by `quotetabs`) and using underscores for header spaces.
- **Edge cases**: Trailing spaces/tabs are always encoded, while leading whitespace is preserved.

[Link to original](https://docs.python.org/3/library/quopri.html)
