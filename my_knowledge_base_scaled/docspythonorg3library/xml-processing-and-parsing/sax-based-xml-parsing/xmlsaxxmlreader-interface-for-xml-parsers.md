---
id: 0.0.23.1.3
title: "xml.sax.xmlreader— Interface for XML parsers¶"
nav_summary: "The `xml"
ref: https://docs.python.org/3/library/xml.sax.reader.html
ref_type: url
---

# xml.sax.xmlreader— Interface for XML parsers¶

The `xml.sax.xmlreader` module defines the core **SAX (Simple API for XML) parser interface** in Python, enabling XML parsing via event-driven processing. It introduces the abstract `XMLReader` class as the foundational interface for SAX parsers, requiring implementations to provide a `create_parser()` function for instantiation via `xml.sax.make_parser()`. Key components include:
- **IncrementalParser**: Supports chunked parsing via `feed()`, `close()`, and `reset()` methods, ideal for streaming or non-blocking scenarios (though `parse()` remains blocking by default).
- **Locator**: Tracks document position (line/column) during SAX event handling (e.g., `startElement`, `endElement`).
- **InputSource**: Encapsulates entity metadata (URI, streams, encodings) for parsing or entity resolution.
- **AttributesImpl**: Provides a mutable container for XML attribute data during event processing.

The module emphasizes **extensibility** (via inheritance) and **flexibility** (e.g., incremental parsing), while adhering to SAX 2.0 standards. Applications interact with parsers by passing `InputSource` objects and handling events via registered handlers (e

[Link to original](https://docs.python.org/3/library/xml.sax.reader.html)
