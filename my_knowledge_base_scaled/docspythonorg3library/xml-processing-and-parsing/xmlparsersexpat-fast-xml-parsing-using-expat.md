---
id: 0.0.23.2
title: "xml.parsers.expat— Fast XML parsing using Expat¶"
nav_summary: "The `xml"
ref: https://docs.python.org/3/library/pyexpat.html
ref_type: url
---

# xml.parsers.expat— Fast XML parsing using Expat¶

The `xml.parsers.expat` module provides a high-performance Python interface to the **Expat** XML parser, enabling fast, non-validating XML processing. It exposes a single core object, `xmlparser`, which acts as the parser state container, allowing assignment of handler functions (e.g., for start/end elements, character data, or errors) to process XML markup. The module leverages the deprecated `pyexpat` backend but remains a robust choice for parsing untrusted data (with security considerations noted). Key components include:
- **`ExpatError`/`error`**: Custom exceptions for parsing failures, with detailed error strings via `ErrorString(errno)`.
- **`XMLParserType`**: Return type for parser instances.
- **`ParserCreate()`**: Factory function to instantiate parsers with optional encoding (UTF-8/16, ISO-8859-1, ASCII) and namespace support (via a custom separator character). Root parsers lack parent contexts, while nested parsers (e.g., for external entities) are created via `ExternalEntityParserCreate`. Namespace-aware parsing expands element/attribute names with URI prefixes, configurable via the separator.

---
**NA

[Link to original](https://docs.python.org/3/library/pyexpat.html)
