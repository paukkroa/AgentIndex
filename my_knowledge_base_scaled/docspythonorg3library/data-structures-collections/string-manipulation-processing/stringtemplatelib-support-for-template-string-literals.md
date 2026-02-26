---
id: 0.0.1.0.1
title: "string.templatelib— Support for template string literals¶"
nav_summary: "Template string literals (`t-strings`) for structured string processing."
ref: https://docs.python.org/3/library/string.templatelib.html
ref_type: url
---

# string.templatelib— Support for template string literals¶

The `string.templatelib` module, introduced in **Python 3.14**, provides support for **template string literals (t-strings)**, an extension of f-strings that return a `Template` object instead of directly evaluating interpolated expressions. Unlike f-strings, which immediately render dynamic content, t-strings preserve the structure of the template—separating static strings and interpolations—into an immutable `Template` instance. This allows programmatic access to the raw components (e.g., `strings`, `interpolations`, and `values`) before final evaluation. The syntax mirrors f-strings but uses a `t` prefix (e.g., `t"Hello {name}!"`). The `Template` class stores static segments as a tuple (`strings`) and dynamic expressions as `Interpolation` objects, enabling custom processing (e.g., validation, formatting) before rendering. Key attributes include `strings` (static parts), `interpolations` (dynamic expressions), and `values` (resolved values). This design facilitates advanced use cases like template validation or conditional rendering.

---

[Link to original](https://docs.python.org/3/library/string.templatelib.html)
