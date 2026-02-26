---
id: 0.0.22.0
title: "Structured Markup Processing Tools¶"
nav_summary: "The **Structured Markup Processing Tools** in Python provide robust support for parsing, manipulating, and generating **SGML, HTML, and XML** data"
ref: https://docs.python.org/3/library/markup.html
ref_type: url
---

# Structured Markup Processing Tools¶

The **Structured Markup Processing Tools** in Python provide robust support for parsing, manipulating, and generating **SGML, HTML, and XML** data. Key modules include:
- **HTML Processing**: The [`html`](html.html) module offers low-level HTML support, while [`html.parser`](html.parser.html) provides a simple parser for HTML/XHTML with customizable `HTMLParser` classes, including methods for handling tags, data, and errors. [`html.entities`](html.entities.html) defines standard HTML character entities.
- **XML Processing**: Python’s XML toolkit includes:
  - **ElementTree (`xml.etree.ElementTree`)** – A lightweight API for parsing, querying (via XPath), and modifying XML documents, supporting pull parsing for non-blocking operations, namespaces, and XInclude. Features include tree traversal, element manipulation, and custom exceptions.
  - **DOM (`xml.dom`)** – Implements the **W3C Document Object Model (DOM)**, offering a hierarchical object model for XML/HTML documents with objects like `Document`, `Element`, `Node`, and `NodeList`, enabling programmatic DOM manipulation and validation.
- **Security Considerations**: XML modules address vulnerabilities (e.g., XX

[Link to original](https://docs.python.org/3/library/markup.html)
