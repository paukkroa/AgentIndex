---
id: 0.0.22.1
title: "html— HyperText Markup Language support¶"
nav_summary: "`html` module: Escape/unescape HTML chars, parser & entities."
ref: https://docs.python.org/3/library/html.html
ref_type: url
---

# html— HyperText Markup Language support¶

The `html` module in Python provides essential utilities for manipulating HTML content, including **`html.escape()`**, which converts special characters (`&`, `<`, `>`, `"`, `'`) into their HTML-safe equivalents (e.g., `&amp;`, `&lt;`, `&gt;`, `&quot;`, `&#39;`), ensuring safe rendering in web contexts. The optional `quote` parameter controls whether quotes are escaped. Introduced in **Python 3.2**, this function is critical for preventing **XSS (Cross-Site Scripting)** attacks by sanitizing user input. Additionally, **`html.unescape()`** (since **Python 3.4**) reverses the process, converting HTML entities (e.g., `&gt;`, `&#62;`) back to Unicode characters, adhering to **HTML5 standards**. The module also includes submodules like **`html.parser`** (for parsing HTML/XHTML) and **`html.entities`** (for predefined HTML entity definitions), offering a robust foundation for structured markup processing.

---

[Link to original](https://docs.python.org/3/library/html.html)
