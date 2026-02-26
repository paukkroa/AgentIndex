---
id: 0.0.22.3
title: "html.entities— Definitions of HTML general entities¶"
nav_summary: "HTML entity mappings for HTML5/XHTML parsing."
ref: https://docs.python.org/3/library/html.entities.html
ref_type: url
---

# html.entities— Definitions of HTML general entities¶

The `html.entities` module in Python’s standard library provides predefined dictionaries for mapping HTML general entities to their Unicode equivalents, enabling character escaping and decoding in web applications. It includes four key dictionaries: `html5` (maps HTML5 named character references like `&gt;` to Unicode characters, e.g., `>`), `entitydefs` (XHTML 1.0 entity definitions in ISO Latin-1), `name2codepoint` (HTML4 entity names to Unicode code points), and `codepoint2name` (Unicode code points back to HTML4 entity names). Introduced in Python 3.3, this module supports HTML/XML parsing by facilitating conversions between named entities and their Unicode representations, complementing functions like `html.unescape()`.

[Link to original](https://docs.python.org/3/library/html.entities.html)
