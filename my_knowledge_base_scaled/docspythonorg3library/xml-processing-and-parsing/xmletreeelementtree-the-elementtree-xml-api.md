---
id: 0.0.23.3
title: "xml.etree.ElementTree— The ElementTree XML API¶"
nav_summary: "Python’s fast XML parsing/manipulation module (`ElementTree`)."
ref: https://docs.python.org/3/library/xml.etree.elementtree.html
ref_type: url
---

# xml.etree.ElementTree— The ElementTree XML API¶

The `xml.etree.ElementTree` module provides a lightweight, efficient API for parsing, manipulating, and generating XML data in Python. It leverages a tree-based structure to represent XML hierarchically, with two core classes: **`ElementTree`** (for the entire document) and **`Element`** (for individual nodes). Key features include:
- **Parsing XML** from files (`ET.parse()`) or strings (`ET.fromstring()`), returning either an `ElementTree` or root `Element`.
- **Tree traversal** via methods like `getroot()`, iteration over child elements, and attribute access via `tag` and `attrib`.
- **Performance optimizations** (since Python 3.3) for faster processing.
- **Deprecation note**: `xml.etree.cElementTree` is deprecated in favor of this module.
- **Security considerations**: Untrusted data requires additional validation (see [XML security](xml.html#xml-security)).

---

[Link to original](https://docs.python.org/3/library/xml.etree.elementtree.html)
