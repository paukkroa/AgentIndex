---
id: 0.0.10.5.5
title: "uuid— UUID objects according toRFC 9562¶"
nav_summary: "The `uuid` module in Python provides immutable **UUID (Universally Unique Identifier)** objects compliant with **RFC 9562** (replacing RFC 4122), enab"
ref: https://docs.python.org/3/library/uuid.html
ref_type: url
---

# uuid— UUID objects according toRFC 9562¶

The `uuid` module in Python provides immutable **UUID (Universally Unique Identifier)** objects compliant with **RFC 9562** (replacing RFC 4122), enabling generation and manipulation of UUIDs across **six versions** (excluding version 2). Core features include:
- **UUID class**: Constructs UUIDs from hex strings, byte arrays (big/little-endian), raw fields, or 128-bit integers, supporting flexible input formats (e.g., `UUID('12345678123456781234567812345678')` or `UUID(bytes=b'\x12\x34\x56\x78'*4)`).
- **Factory functions**: Generates UUIDs via `uuid1()` (time-based, privacy-sensitive), `uuid4()` (random), and others (`uuid3()`, `uuid5()`), with `is_safe` attribute indicating platform-safe multiprocessing generation (values: `SafeUUID.safe`, `SafeUUID.unsafe`, or `SafeUUID.unknown`).
- **Compatibility**: Supports legacy RFC 4122

[Link to original](https://docs.python.org/3/library/uuid.html)
