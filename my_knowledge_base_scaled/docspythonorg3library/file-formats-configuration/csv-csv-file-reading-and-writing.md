---
id: 0.0.6.1
title: "csv— CSV File Reading and Writing¶"
nav_summary: "The **`csv` module** in Python provides robust tools for reading and writing **Comma-Separated Values (CSV)** files, a widely used format for tabular"
ref: https://docs.python.org/3/library/csv.html
ref_type: url
---

# csv— CSV File Reading and Writing¶

The **`csv` module** in Python provides robust tools for reading and writing **Comma-Separated Values (CSV)** files, a widely used format for tabular data exchange between spreadsheets, databases, and applications. While lacking a strict standard (e.g., **RFC 4180**), CSV files share enough consistency to allow unified processing via Python’s `csv` module. It abstracts platform-specific quirks (e.g., delimiters, quoting) by supporting customizable **dialects** (e.g., `excel`, `unix`) and formatting parameters (e.g., `delimiter`, `quotechar`). Core classes include:
- **`reader`/`writer`**: Process CSV data as sequences of strings (rows/columns).
- **`DictReader`/`DictWriter`**: Handle data as dictionaries (e.g., `{column_name: value}`), enabling column-based access.
Key features:
- **Dialects**: Predefined or user-defined formats (e.g., Excel’s `QUOTE_NONNUMERIC` converts unquoted numbers to floats).
- **Flexible Input**: Accepts file-like objects (opened with `newline=''`) or iter

[Link to original](https://docs.python.org/3/library/csv.html)
