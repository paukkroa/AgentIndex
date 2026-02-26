---
id: 0.0.16.1
title: "struct— Interpret bytes as packed binary data¶"
nav_summary: "The `struct` module in Python enables conversion between Python values and C-style binary data represented as `bytes` objects, facilitating low-level"
ref: https://docs.python.org/3/library/struct.html
ref_type: url
---

# struct— Interpret bytes as packed binary data¶

The `struct` module in Python enables conversion between Python values and C-style binary data represented as `bytes` objects, facilitating low-level data exchange with external systems (e.g., files, network protocols) or communication between Python and C extensions. It uses **format strings** to define compact layouts for packing/unpacking data, where each character specifies a C data type (e.g., `'h'` for short integer, `'d'` for double). Key functions include:
- **`pack()`**: Serializes Python values into a `bytes` object based on a format string.
- **`pack_into()`**: Writes packed data directly into a writable buffer (e.g., `bytearray`) at a specified offset, avoiding intermediate copies.
- **`unpack()`**: Deserializes binary data into Python values, returning a tuple (even for single items).
- **`unpack_from()`**: Extracts data from a buffer starting at a given offset, useful for partial or fragmented binary data.
- **`calcsize()`**: Computes the byte size required for a given format string, ensuring buffer alignment and padding.

The module supports **native byte order** (platform-dependent) and **explicit byte ordering** (e

[Link to original](https://docs.python.org/3/library/struct.html)
