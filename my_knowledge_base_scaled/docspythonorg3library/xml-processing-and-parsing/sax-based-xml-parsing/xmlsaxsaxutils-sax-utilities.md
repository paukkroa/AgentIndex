---
id: 0.0.23.1.2
title: "xml.sax.saxutils— SAX Utilities¶"
nav_summary: "The `xml"
ref: https://docs.python.org/3/library/xml.sax.utils.html
ref_type: url
---

# xml.sax.saxutils— SAX Utilities¶

The `xml.sax.saxutils` module provides essential utilities for SAX (Simple API for XML) applications, offering functions and a class to handle XML character escaping, attribute quoting, and XML document reconstruction. Key features include:
- **`escape()`**: Escapes XML-sensitive characters (`&`, `<`, `>`) in strings, with optional custom entity replacements via a dictionary. Ensures safe XML serialization.
- **`unescape()`**: Reverses escaping by converting XML entities (`&amp;`, `&lt;`, `&gt;`) back to their original characters, with support for custom entity mappings.
- **`quoteattr()`**: Prepares string data for XML/SGML attribute values by escaping quotes and selecting optimal quote characters (single/double) to avoid encoding conflicts.
- **`XMLGenerator`**: A `ContentHandler` implementation that reconstructs an XML document from SAX events, writing output to a file-like object (default: `sys.stdout`). Supports configurable encoding (`iso-8859-1` by default) and formatting of empty elements (short or full tags).

These utilities are critical for XML parsing, serialization, and attribute handling in SAX-based workflows, ensuring compliance

[Link to original](https://docs.python.org/3/library/xml.sax.utils.html)
