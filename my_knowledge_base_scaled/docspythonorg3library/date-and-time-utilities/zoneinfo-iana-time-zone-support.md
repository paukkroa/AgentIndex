---
id: 0.0.17.2
title: "zoneinfo— IANA time zone support¶"
nav_summary: "`zoneinfo` module: IANA timezone support via `ZoneInfo` class."
ref: https://docs.python.org/3/library/zoneinfo.html
ref_type: url
---

# zoneinfo— IANA time zone support¶

The `zoneinfo` module (introduced in Python 3.9) provides a robust implementation of the IANA time zone database as outlined in **PEP 615**, offering accurate time zone support via the `ZoneInfo` class—a concrete subclass of `datetime.tzinfo`. It integrates seamlessly with Python’s `datetime` module, enabling timezone-aware datetime objects that automatically handle daylight saving transitions and ambiguous times (e.g., via the `fold` attribute from **PEP 495**). By default, it leverages system-provided timezone data or falls back to the first-party `tzdata` package. The module does not support WebAssembly (WASI). Key features include:
- **Timezone-aware datetime objects** with correct offset handling.
- **Ambiguity resolution** via `fold` (0 for pre-transition, 1 for post-transition).
- **Compatibility** with `datetime` arithmetic and timezone conversions.
- **Flexible data sources** (system or `tzdata` package).

---

[Link to original](https://docs.python.org/3/library/zoneinfo.html)
