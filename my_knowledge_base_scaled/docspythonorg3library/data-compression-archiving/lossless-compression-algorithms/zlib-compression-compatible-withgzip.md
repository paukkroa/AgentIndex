---
id: 0.0.5.0.1
title: "zlib— Compression compatible withgzip¶"
nav_summary: "The **`zlib`** module provides Python bindings to the **zlib library**, enabling efficient **lossless data compression** compatible with **gzip** form"
ref: https://docs.python.org/3/library/zlib.html
ref_type: url
---

# zlib— Compression compatible withgzip¶

The **`zlib`** module provides Python bindings to the **zlib library**, enabling efficient **lossless data compression** compatible with **gzip** formats. As an **optional module**, it must be explicitly installed via the Python distributor or system package manager. Key features include:
- **Compression/Decompression**: Functions like `compress()` and `decompress()` (via `zlib.decompress()`) handle data reduction with adjustable compression levels (`Z_BEST_SPEED` to `Z_BEST_COMPRESSION`).
- **Checksums**: `adler32()` computes a lightweight checksum (faster than CRC32) for data integrity verification, though not cryptographically secure.
- **Window Size Control**: The `wbits` parameter configures memory usage (e.g., `MAX_WBITS=15` for default 32KB window) and output format (header/trailer inclusion or raw streams).
- **Error Handling**: The `zlib.error` exception flags failures during compression/decompression.
- **Compatibility**: While `zlib` handles raw compression, the [`gzip`](gzip.html) module extends its functionality for `.gz` file operations

[Link to original](https://docs.python.org/3/library/zlib.html)
