---
id: 0.0.23.1.1
title: "xml.sax.handler— Base classes for SAX handlers¶"
nav_summary: "SAX handler base classes: `ContentHandler`, `DTDHandler`, `EntityResolver`, `ErrorHandler`, `LexicalHandler`."
ref: https://docs.python.org/3/library/xml.sax.handler.html
ref_type: url
---

# xml.sax.handler— Base classes for SAX handlers¶

The `xml.sax.handler` module provides foundational base classes for implementing **SAX (Simple API for XML) event handlers**, enabling structured XML parsing via callback interfaces. It defines five core handler types: **`ContentHandler`** (for document content events), **`DTDHandler`** (for DTD-related events), **`EntityResolver`** (for external entity resolution), **`ErrorHandler`** (for error/warning reporting), and **`LexicalHandler`** (for low-frequency lexical events). Applications subclass these classes to extend default behavior, ensuring consistent method signatures. The module also includes **feature flags** like `feature_namespaces` (enables XML namespace processing) and `feature_string_interning` (optimizes string storage via Python’s `intern()`), alongside `feature_namespace_prefixes` (controls namespace prefix reporting). These constants allow runtime configuration of parser behavior, balancing performance and correctness.

---

[Link to original](https://docs.python.org/3/library/xml.sax.handler.html)
