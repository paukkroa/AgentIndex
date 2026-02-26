---
id: 0.0.5.0.2
title: "bz2— Support forbzip2compression¶"
nav_summary: "`bz2` module: bzip2 compression/decompression tools & file handling."
ref: https://docs.python.org/3/library/bz2.html
ref_type: url
---

# bz2— Support forbzip2compression¶

The `bz2` module in Python provides a robust interface for **bzip2 compression**, a high-quality lossless compression algorithm. It supports both **file-based compression/decompression** via the `open()` function and `BZ2File` class (for binary/text modes) and **stream-based compression/decompression** using `BZ2Compressor`/`BZ2Decompressor` classes or standalone `compress()`/`decompress()` functions. Key features include configurable compression levels (1–9), support for **path-like objects**, and **text mode wrappers** (via `io.TextIOWrapper`) for encoding/decoding. The module is **optional**—if missing, it requires external dependencies (e.g., `libbz2`). Introduced in Python 3.3, it later added exclusive file creation (`'x'` mode) and path-like object support in 3.6.

---

[Link to original](https://docs.python.org/3/library/bz2.html)
