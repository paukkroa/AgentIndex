---
id: 0.0.16.0
title: "Binary Data Services¶"
nav_summary: "Binary data parsing/packing tools: `struct`, `codecs"
ref: https://docs.python.org/3/library/binary.html
ref_type: url
---

# Binary Data Services¶

The **Binary Data Services** chapter in the Python Standard Library provides essential tools for handling binary data manipulation, focusing on low-level operations distinct from file formats or network protocols. Key modules include:
- **`struct`**: Parses and packs binary data using format strings, supporting byte order, size, and alignment for native and standard formats (e.g., C structs, network byte order). Includes functions, exceptions, and practical examples.
- **`codecs`**: Manages encoding/decoding pipelines via base classes (e.g., `IncrementalEncoder`, `StreamReader`), error handlers, and Unicode support. Features standard encodings (UTF-8, ASCII) and Python-specific transforms (e.g., `encodings.idna` for IDNA). Submodules like `encodings.mbcs` handle platform-specific codepages.

Additionally, built-in binary types (`bytes`, `bytearray`, `memoryview`) are documented in *Binary Sequence Types*. Overlaps with text processing modules (e.g., `re`, `difflib`) are noted for ASCII-compatible or general binary operations.

---

[Link to original](https://docs.python.org/3/library/binary.html)
