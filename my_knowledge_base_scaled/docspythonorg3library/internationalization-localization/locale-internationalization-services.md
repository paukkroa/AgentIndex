---
id: 0.0.12.2
title: "locale— Internationalization services¶"
nav_summary: "`locale` module: POSIX locale services for cultural formatting & conventions."
ref: https://docs.python.org/3/library/locale.html
ref_type: url
---

# locale— Internationalization services¶

The `locale` module in Python provides access to POSIX locale services, enabling applications to handle cultural and regional formatting (e.g., dates, numbers, collation) without hardcoding platform-specific details. Built atop the `_locale` module (which leverages ANSI C’s locale implementation), it centralizes locale management via **`setlocale(category, locale)`**, allowing dynamic switching between locales (e.g., `'de_DE.UTF-8'` for German formatting) or retrieving the current settings. Supported categories include `LC_ALL`, `LC_COLLATE`, `LC_CTYPE`, etc. The module raises `locale.Error` for invalid locales. Additional functions like **`localeconv()`** return a dictionary of locale-specific conventions (e.g., decimal separators, thousand separators) for numeric formatting. Thread-safety is limited; applications should initialize locales early (e.g., `locale.setlocale(locale.LC_ALL, '')`) to avoid race conditions.

---

[Link to original](https://docs.python.org/3/library/locale.html)
