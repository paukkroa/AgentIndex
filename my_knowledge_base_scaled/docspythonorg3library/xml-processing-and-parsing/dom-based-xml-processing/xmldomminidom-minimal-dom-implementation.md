---
id: 0.0.23.0.1
title: "xml.dom.minidom— Minimal DOM implementation¶"
nav_summary: "`"
ref: https://docs.python.org/3/library/xml.dom.minidom.html
ref_type: url
---

# xml.dom.minidom— Minimal DOM implementation¶

The `xml.dom.minidom` module provides a **minimal, lightweight implementation of the Document Object Model (DOM) API** for parsing and manipulating XML data in Python. It offers a **simplified subset of the full DOM standard**, prioritizing ease of use over feature richness. Key features include:
- **DOM Parsing:** Parses XML files or strings into a structured `Document` object via `parse()` (for files) or `parseString()` (for strings).
- **SAX Integration:** Uses a SAX parser (e.g., `parser=None` parameter) to convert XML events into a DOM tree, enabling compatibility with existing SAX workflows.
- **DOM Construction:** Supports manual DOM creation via `getDOMImplementation()` to generate `Document` objects programmatically, allowing node manipulation (e.g., adding child elements).
- **Namespace Support:** Built-in namespace handling for XML documents.
- **Security Note:** Caution advised for untrusted data (see [XML security](xml.html#xml-security)).
Ideal for developers familiar with DOM but seeking a **smaller, simpler alternative** to `xml.etree.ElementTree` or full DOM implementations.

---

[Link to original](https://docs.python.org/3/library/xml.dom.minidom.html)
