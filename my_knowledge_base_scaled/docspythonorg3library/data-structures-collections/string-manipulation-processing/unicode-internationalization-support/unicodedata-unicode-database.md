---
id: 0.0.1.0.4.0
title: "unicodedata— Unicode Database¶"
nav_summary: "The **`unicodedata`** module provides Python developers with programmatic access to the **Unicode Character Database (UCD)**, a standardized repositor"
ref: https://docs.python.org/3/library/unicodedata.html
ref_type: url
---

# unicodedata— Unicode Database¶

The **`unicodedata`** module provides Python developers with programmatic access to the **Unicode Character Database (UCD)**, a standardized repository defining properties for all Unicode characters (based on **UCD 16.0.0**). It adheres to **Unicode Standard Annex #44**, offering functions to query character metadata such as names, numeric values, digit representations, and general categories. Key features include:
- **`lookup(name)`**: Retrieves a character by its Unicode name (e.g., `'LEFT CURLY BRACKET'` → `'{'`), mirroring `\N{NAME}` escape sequences.
- **`name(chr)`**: Returns a character’s official Unicode name (e.g., `'½'` → `'VULGAR FRACTION ONE HALF'`), with a fallback default value.
- **Numeric functions**: `decimal()`, `digit()`, and `numeric()` return decimal, digit, or floating-point numeric values (e.g., `'½'` → `0.5`), raising `ValueError` if undefined.
- **`category(chr)`**: Returns a 2-letter general category (e.g., `'Ll'` for lowercase letters), referencing the [Unicode TR44 General

[Link to original](https://docs.python.org/3/library/unicodedata.html)
