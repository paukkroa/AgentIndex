---
id: 0.0.1.3.3
title: "array— Efficient arrays of numeric values¶"
nav_summary: "`array` module: Compact numeric arrays with"
ref: https://docs.python.org/3/library/array.html
ref_type: url
---

# array— Efficient arrays of numeric values¶

The `array` module in Python provides a memory-efficient, mutable sequence type for storing homogeneous numeric values (integers, floats, or Unicode characters) using a compact binary layout. Arrays are similar to lists but enforce a fixed data type (specified via a single-character *type code*), enabling optimized memory usage and faster operations compared to generic lists. Supported type codes include signed/unsigned integers (`'b'`, `'B'`, `'h'`, `'H'`, `'i'`, `'I'`, `'l'`, `'L'`, `'q'`, `'Q'`), floating-point numbers (`'f'`, `'d'`), and Unicode characters (`'u'`, `'w'`). The actual memory footprint per element is platform-dependent but can be queried via `array.itemsize`. Arrays support standard sequence operations (indexing, slicing, concatenation) and buffer protocol compatibility, though slice assignments require matching type codes. Initialization can occur via `bytes`, `bytearray`, Unicode strings, or iterables of compatible types, with methods like `frombytes()`, `fromunicode()`, and `extend()` facilitating data population.

---

[Link to original](https://docs.python.org/3/library/array.html)
