---
id: 0.0.1.0.4.1
title: "stringprep— Internet String Preparation¶"
nav_summary: "`stringprep` module: RFC 3454 Unicode string normalization functions."
ref: https://docs.python.org/3/library/stringprep.html
ref_type: url
---

# stringprep— Internet String Preparation¶

The `stringprep` module implements **RFC 3454**’s Internet String Preparation (stringprep) procedure, standardizing Unicode string normalization for internet protocols (e.g., domain names). It provides **character membership checks** (e.g., `in_table_a1` for unassigned Unicode code points) and **mapping functions** (e.g., `map_table_b2` for case-folding) via optimized lookups in the Unicode database, avoiding explicit table storage. Key tables include:
- **Table A.1/A.2**: Unassigned/private-use code points.
- **Table B.1/B.2/B.3**: Case-folding mappings (with/without NFKC normalization).
- **Table C.1.1/C.1.2**: ASCII/non-ASCII whitespace checks.
- **Table C.2.1/C.2.2**: ASCII/non-ASCII control character checks.
Profiles like `nameprep` (for IDNs) rely on these functions to enforce valid character sets and normalize strings before transmission.

---

[Link to original](https://docs.python.org/3/library/stringprep.html)
