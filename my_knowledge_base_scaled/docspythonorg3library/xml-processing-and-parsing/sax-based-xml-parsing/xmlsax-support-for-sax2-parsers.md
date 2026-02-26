---
id: 0.0.23.1.0
title: "xml.sax— Support for SAX2 parsers¶"
nav_summary: "The `xml"
ref: https://docs.python.org/3/library/xml.sax.html
ref_type: url
---

# xml.sax— Support for SAX2 parsers¶

The `xml.sax` module in Python’s standard library implements the **SAX2 (Simple API for XML)** interface, enabling lightweight XML parsing via event-driven handlers. It provides core SAX exceptions (e.g., `SAXParseException`) and utility functions like `make_parser()` to instantiate parsers from a priority list of modules (e.g., `xml.sax.xmlreader.XMLReader`). The `parse()` and `parseString()` functions streamline parsing from files, file objects, or in-memory strings, delegating event handling to `ContentHandler` instances (e.g., for start/end tags) and optional `ErrorHandler` instances for validation errors. Security updates in Python 3.7+ disable external entity processing by default to mitigate risks like XXE attacks, though it can be re-enabled via `setFeature(feature_external_ges)`. SAX operates asynchronously, emitting events (e.g., `startElement`, `endElement`) to handlers rather than constructing a DOM tree, making it memory-efficient for large documents. Key components include:
- **Readers/parsers** (e.g., `XMLReader`) for input processing.
- **Handlers** (`ContentHandler`, `ErrorHandler`)

[Link to original](https://docs.python.org/3/library/xml.sax.html)
