---
id: 0.0.1.0.3.0
title: "difflib— Helpers for computing deltas¶"
nav_summary: "The `difflib` module in Python provides robust tools for comparing sequences (e"
ref: https://docs.python.org/3/library/difflib.html
ref_type: url
---

# difflib— Helpers for computing deltas¶

The `difflib` module in Python provides robust tools for comparing sequences (e.g., text, files, or directories) and generating human-readable diffs. Its core class, **`SequenceMatcher`**, implements a quadratic-time algorithm (inspired by Ratcliff-Obershelp’s gestalt pattern matching) to identify the longest contiguous matching subsequences while handling "junk" elements (e.g., whitespace or duplicates) via an optional **autojunk heuristic** (enabled by default for sequences ≥200 items). This heuristic automatically flags popular items (appearing >1% of the time) as junk, improving performance and relevance.

For text-based comparisons, **`Differ`** extends `SequenceMatcher` to produce **contextual or unified diffs** (e.g., Git-style patches) with clear markers:
- `'- '`: Lines unique to sequence 1.
- `'+ '`: Lines unique to sequence 2.
- `'  '`: Common lines.
- `'? '`: Intraline differences (not present in either input).

Outputs can be formatted as plain text, HTML, or other formats. While `difflib` excels at sequence comparison, for directory/file operations, pair it

[Link to original](https://docs.python.org/3/library/difflib.html)
