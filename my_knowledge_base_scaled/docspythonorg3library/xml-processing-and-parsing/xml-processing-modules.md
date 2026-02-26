---
id: 0.0.23.4
title: "XML Processing Modules¶"
nav_summary: "Python’s XML processing modules: DOM, SAX, ElementTree,"
ref: https://docs.python.org/3/library/xml.html
ref_type: url
---

# XML Processing Modules¶

Python’s `xml` package provides standardized interfaces for XML processing, including **DOM (Document Object Model)** and **SAX (Simple API for XML)** APIs, along with lightweight alternatives like **ElementTree**. The package relies on the **Expat parser** (bundled by default) for XML parsing, ensuring compatibility with SAX-compliant parsers. Key submodules include:
- **`xml.etree.ElementTree`**: A fast, memory-efficient API for parsing and manipulating XML.
- **`xml.dom`/`xml.dom.minidom`**: DOM implementations for hierarchical XML document traversal and modification.
- **`xml.sax`**: Base classes for SAX event-driven parsing.
- **`xml.parsers.expat`**: Direct binding to Expat’s non-validating parser.

Security considerations are critical: Expat (pre-2.7.2) and `xmlrpc` are vulnerable to **DoS attacks** (e.g., "billion laughs" entity expansion or decompression bombs). Always validate untrusted XML data to mitigate risks like file access or network exploits.

---

[Link to original](https://docs.python.org/3/library/xml.html)
