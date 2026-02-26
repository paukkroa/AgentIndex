---
id: 0.0.7.2
title: "hmac— Keyed-Hashing for Message Authentication¶"
nav_summary: "The `hmac` module in Python implements the **HMAC (Keyed-Hashing for Message Authentication)** algorithm as defined in **RFC 2104**, providing cryptog"
ref: https://docs.python.org/3/library/hmac.html
ref_type: url
---

# hmac— Keyed-Hashing for Message Authentication¶

The `hmac` module in Python implements the **HMAC (Keyed-Hashing for Message Authentication)** algorithm as defined in **RFC 2104**, providing cryptographic message integrity verification using a secret key. It supports any fixed-size hash function (e.g., SHA-256, MD5) via `hashlib` but excludes extendable output functions like SHAKE-128/256. Core functions include:
- **`hmac.new(key, msg=None, digestmod)`**: Creates an HMAC object with optional pre-update message; `digestmod` (e.g., `"sha256"`) is now **required** (since Python 3.8). The `key` can be bytes/bytearray, and `msg` supports any `hashlib`-compatible type.
- **`hmac.digest(key, msg, digest)`** (Python 3.7+): Optimized C-based digest computation for in-memory messages, using OpenSSL for supported algorithms.
- **`HMAC` class**: Manages HMAC operations with methods:
  - **`update(msg)`**: Appends data (supports any `hashlib`-compatible type

[Link to original](https://docs.python.org/3/library/hmac.html)
