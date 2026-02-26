---
id: 0.0.22.2
title: "html.parser— Simple HTML and XHTML parser¶"
nav_summary: "Lightweight HTML/XHTML parser with customizable tag handlers."
ref: https://docs.python.org/3/library/html.parser.html
ref_type: url
---

# html.parser— Simple HTML and XHTML parser¶

The `html.parser` module in Python provides a lightweight, non-validating **`HTMLParser`** class for parsing HTML and XHTML documents. It enables custom parsing behavior by subclassing `HTMLParser` and overriding handler methods like `handle_starttag()`, `handle_endtag()`, and `handle_data()` to process start tags, end tags, and text content, respectively. Key features include automatic conversion of character references (e.g., `&amp;` → `&`) via the `convert_charrefs` parameter (default: `True`), and control over script/noscript handling via the `scripting` parameter (default: `False`). The parser processes data incrementally via `feed()` and buffers incomplete markup until closure. It does **not** enforce tag nesting rules or validate markup, making it suitable for simple parsing tasks. Introduced in Python 3.4, it supports incremental parsing and is ideal for applications requiring basic HTML parsing without full validation.

---

[Link to original](https://docs.python.org/3/library/html.parser.html)
