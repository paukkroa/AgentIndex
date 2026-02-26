---
id: 0.0.23.0.2
title: "xml.dom.pulldom— Support for building partial DOM trees¶"
nav_summary: "The `xml"
ref: https://docs.python.org/3/library/xml.dom.pulldom.html
ref_type: url
---

# xml.dom.pulldom— Support for building partial DOM trees¶

The `xml.dom.pulldom` module implements a **pull parser** for XML, enabling incremental processing of XML streams while selectively constructing **partial DOM (Document Object Model) fragments** on demand. Unlike SAX (which relies on event callbacks), `pulldom` requires explicit event retrieval via iteration, offering finer control over parsing. Key features include:
- **Event-driven processing** with constants like `START_ELEMENT`, `END_ELEMENT`, `COMMENT`, etc., paired with DOM-compatible nodes (`Document`, `Element`, or `Text`).
- **Lazy DOM construction**: Nodes are only expanded into full DOM trees when explicitly requested via `expandNode()`, optimizing memory usage for large documents.
- **Flexible input handling**: Supports file paths, file-like objects, or raw strings for parsing.
- **Security considerations**: Defaults to blocking external entity processing (since Python 3.7.1) for security; custom parsers can re-enable it if needed.
- **Two parser classes**:
  - `PullDOM`: A basic pull parser subclass of `ContentHandler`.
  - `SAX2DOM`: A SAX2-compatible pull parser subclass, also inheriting from `ContentHandler`.
- **

[Link to original](https://docs.python.org/3/library/xml.dom.pulldom.html)
