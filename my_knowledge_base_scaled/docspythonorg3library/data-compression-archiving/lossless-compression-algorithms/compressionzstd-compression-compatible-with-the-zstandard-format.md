---
id: 0.0.5.0.0
title: "compression.zstd— Compression compatible with the Zstandard format¶"
nav_summary: "The `compression"
ref: https://docs.python.org/3/library/compression.zstd.html
ref_type: url
---

# compression.zstd— Compression compatible with the Zstandard format¶

The `compression.zstd` module (introduced in Python 3.14) provides Python bindings for the **Zstandard (zstd)** compression algorithm, a fast, lossless compression library optimized for real-time scenarios with zlib-level speed and superior compression ratios. It includes:
- **File handling** via `open()` and `ZstdFile` for reading/writing `.zst` files or raw streams.
- **Incremental compression/decompression** using `ZstdCompressor`/`ZstdDecompressor` for streaming data.
- **One-shot compression/decompression** via `compress()`/`decompress()` functions.
- **Dictionary-based compression** with `train_dict()`, `finalize_dict()`, and `ZstdDict` for improved compression ratios on repetitive data.
- **Parameter control** through `CompressionParameter`, `DecompressionParameter`, and `Strategy` classes for tuning speed/ratio trade-offs.
- **Error handling** via `ZstdError` exceptions for compression/decompression failures.
As an optional module, it requires external dependencies (e.g., `libzstd`) and may not be included by default in all Python distributions.

---
**NAVIG

[Link to original](https://docs.python.org/3/library/compression.zstd.html)
