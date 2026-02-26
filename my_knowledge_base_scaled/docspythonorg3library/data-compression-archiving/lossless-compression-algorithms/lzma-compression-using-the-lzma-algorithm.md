---
id: 0.0.5.0.3
title: "lzma— Compression using the LZMA algorithm¶"
nav_summary: "Python’s LZMA compression module for `.x"
ref: https://docs.python.org/3/library/lzma.html
ref_type: url
---

# lzma— Compression using the LZMA algorithm¶

The `lzma` module in Python provides high-efficiency compression and decompression using the **LZMA algorithm**, a lossless data compression method known for its strong compression ratios. It supports `.xz` and legacy `.lzma` file formats, offering both file-based and stream-based operations via classes like `LZMAFile`, `LZMACompressor`, and `LZMADecompressor`. The interface mirrors the `bz2` module but lacks thread-safety for `LZMAFile` objects, requiring explicit locking for multi-threaded access. Key features include configurable compression levels (*preset*), checksum verification (*check*), and customizable filters (*filters*). The `lzma.open()` function acts as a versatile entry point for both binary and text-mode file operations, supporting modes like read (`"r"`, `"rb"`), write (`"w"`, `"wb"`), and exclusive creation (`"x"`, `"xb"`). Errors are handled via the `LZMAError` exception. Optional dependencies must be installed separately, as this module is not included by default in CPython.

---

[Link to original](https://docs.python.org/3/library/lzma.html)
