---
id: 0.0.7.1
title: "hashlib— Secure hashes and message digests¶"
nav_summary: "The `hashlib` module in Python provides a standardized interface for computing secure cryptographic hash functions and message digests, supporting wid"
ref: https://docs.python.org/3/library/hashlib.html
ref_type: url
---

# hashlib— Secure hashes and message digests¶

The `hashlib` module in Python provides a standardized interface for computing secure cryptographic hash functions and message digests, supporting widely adopted algorithms like **SHA-2 (SHA224, SHA256, SHA384, SHA512)**, **SHA-3 (SHA3-224/256/384/512)**, **SHAKE (SHAKE-128/256)**, **BLAKE2 (BLAKE2b/BLAKE2s)**, and legacy algorithms such as **SHA-1** and **MD5** (though MD5 may be disabled in FIPS-compliant builds). Each algorithm is accessed via a dedicated constructor (e.g., `sha256()`, `blake2b()`) that returns a hash object with methods like `update()` for incremental data processing and `digest()`/`hexdigest()` to retrieve the hash output in binary or hexadecimal format. The module ensures thread safety by releasing the Python Global Interpreter Lock (GIL) during large updates (>2047 bytes). Additional algorithms (e.g., from OpenSSL) may be available via `hashlib.new()` but are

[Link to original](https://docs.python.org/3/library/hashlib.html)
