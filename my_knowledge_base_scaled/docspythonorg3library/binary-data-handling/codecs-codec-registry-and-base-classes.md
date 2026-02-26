---
id: 0.0.16.2
title: "codecs— Codec registry and base classes¶"
nav_summary: "The `codecs` module in Python provides foundational infrastructure for handling text encoding/decoding via a centralized **codec registry** and base c"
ref: https://docs.python.org/3/library/codecs.html
ref_type: url
---

# codecs— Codec registry and base classes¶

The `codecs` module in Python provides foundational infrastructure for handling text encoding/decoding via a centralized **codec registry** and base classes. It supports standard **text encodings** (e.g., UTF-8, ASCII) as well as custom codecs for arbitrary type conversions (e.g., text-to-text or bytes-to-bytes). Core functions include:
- **`encode()`** and **`decode()`**: Convert between text and bytes using a specified encoding (default: UTF-8) and error handling (e.g., `'strict'`, `'ignore'`).
- **`charmap_build()`**: Constructs a custom single-byte encoding mapping from a string of 256 characters.
- **`lookup()`**: Retrieves a `CodecInfo` object from the registry, caching results for efficiency. If unavailable, raises `LookupError`.

The module defines **base classes** (`CodecInfo`, `Codec`, `StreamReader`, etc.) to standardize codec behavior, including error handling (e.g., `UnicodeEncodeError`, `UnicodeDecodeError`). Encodings are prioritized from the registry cache, then searched via registered functions. This modular design enables extensibility for custom encoders/dec

[Link to original](https://docs.python.org/3/library/codecs.html)
