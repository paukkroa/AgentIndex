---
id: 0.0.23.0.0
title: "xml.dom— The Document Object Model API¶"
nav_summary: "The `xml"
ref: https://docs.python.org/3/library/xml.dom.html
ref_type: url
---

# xml.dom— The Document Object Model API¶

The `xml.dom` module in Python implements the **W3C Document Object Model (DOM) API**, enabling structured access and manipulation of XML documents as a hierarchical tree. Unlike event-driven parsers like SAX, DOM provides **random-access traversal** of XML nodes (elements, attributes, text), allowing direct navigation, modification, and querying of document content. Based on **DOM Level 2** (with partial Level 3 support), it abstracts XML into objects with standardized interfaces (e.g., `Document`, `Element`, `Node`). Key features include:
- **Tree-based representation**: XML parsed into a DOM tree for efficient traversal.
- **Standardized methods/properties**: Aligns with W3C’s IDL/Java mappings (though Python-specific deviations exist).
- **Implementation flexibility**: Uses `getDOMImplementation()` to create documents or access parsers (e.g., `xml.dom.minidom`).
- **Limited parsing integration**: No built-in parser; relies on external modules (e.g., `xml.etree.ElementTree`) for XML loading.
- **Conformance notes**: Python’s mapping prioritizes usability over strict IDL compliance.

Ideal for applications requiring **in-memory XML manipulation**

[Link to original](https://docs.python.org/3/library/xml.dom.html)
