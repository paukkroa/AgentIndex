---
id: 0.0.1.0.2
title: "re— Regular expression operations¶"
nav_summary: "The `re` module in Python provides robust regular expression (regex) operations, enabling pattern matching, searching, and text manipulation akin to P"
ref: https://docs.python.org/3/library/re.html
ref_type: url
---

# re— Regular expression operations¶

The `re` module in Python provides robust regular expression (regex) operations, enabling pattern matching, searching, and text manipulation akin to Perl. It supports both **Unicode strings (`str`)** and **8-bit strings (`bytes`)** but enforces type consistency—patterns and strings must match in type (e.g., cannot mix `str` with `bytes`). Key features include:
- **Escaping conflicts**: Backslashes (`\`) in regex patterns conflict with Python’s string literals, requiring **raw strings (`r"..."`)** to avoid double-escaping (e.g., `r"\n"` instead of `"\\n"`). Invalid escape sequences now trigger `SyntaxWarning` (future `SyntaxError`).
- **Core functions**: Module-level functions like `re.search()`, `re.match()`, and `re.findall()` provide shortcuts, while **compiled regex objects** (e.g., `re.compile()`) offer fine-grained control over flags (e.g., `re.IGNORECASE`) and performance.
- **Syntax flexibility**: Regexes combine primitives (characters, groups, quantifiers) via concatenation, alternation (`|`), grouping (`()`), and repetition (`*`, `+`,

[Link to original](https://docs.python.org/3/library/re.html)
