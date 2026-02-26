---
id: 0.0.24.5
title: "plistlib— Generate and parse Apple.plistfiles¶"
nav_summary: "`plistlib: Parse/generate Apple ."
ref: https://docs.python.org/3/library/plistlib.html
ref_type: url
---

# plistlib— Generate and parse Apple.plistfiles¶

The `plistlib` module provides Python’s interface for generating and parsing Apple’s **`.plist` (property list)** files, supporting both **binary and XML formats**. These files store serialized data in a structured format, commonly used in macOS/iOS applications, and typically contain dictionaries, lists, strings, numbers, booleans, or specialized objects like `bytes`, `bytearray`, or `datetime` instances. Key functions include:
- **`load()`/`loads()`**: Parse `.plist` files from file objects or raw data (bytes/strings), with optional format detection (`FMT_XML`/`FMT_BINARY`) and custom dictionary types.
- **`dump()`/`dumps()`**: Serialize Python objects into `.plist` format for writing or in-memory use.
- **Version updates**: Added support for **UID tokens** (3.8), deprecated old APIs (3.9), and introduced `aware_datetime` for timezone-aware datetime objects (3.13). The module leverages **Expat XML parser** for XML validation and raises `InvalidFileException` on errors.

---

[Link to original](https://docs.python.org/3/library/plistlib.html)
