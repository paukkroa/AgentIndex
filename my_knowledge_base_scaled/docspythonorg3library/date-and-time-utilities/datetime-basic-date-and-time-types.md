---
id: 0.0.17.1
title: "datetime— Basic date and time types¶"
nav_summary: "`datetime` module: Date/time classes, aware/naive objects, timezone support."
ref: https://docs.python.org/3/library/datetime.html
ref_type: url
---

# datetime— Basic date and time types¶

The `datetime` module in Python provides core classes for handling dates, times, and time zones, emphasizing efficient attribute extraction for formatting and manipulation. It distinguishes between **aware** (timezone-annotated) and **naive** (timezone-agnostic) objects, where aware objects resolve ambiguity by including UTC offsets, daylight saving adjustments, and timezone names via the `tzinfo` attribute (e.g., `datetime.timezone`). The module includes built-in constants like `MINYEAR` (for minimum valid year values) and supports basic arithmetic operations. While it offers a fixed-offset `timezone` class for simple timezones (e.g., UTC, EST), deeper timezone logic (e.g., DST rules) requires third-party libraries like `zoneinfo` or `dateutil`. Key classes include `datetime`, `time`, and `date`, with `tzinfo` serving as an abstract base for timezone implementations.

---

[Link to original](https://docs.python.org/3/library/datetime.html)
