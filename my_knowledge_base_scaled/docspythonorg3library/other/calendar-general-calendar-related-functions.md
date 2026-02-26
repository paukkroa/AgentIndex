---
id: 0.0.24.1
title: "calendar— General calendar-related functions¶"
nav_summary: "The **`calendar`** module in Python provides utilities for generating and manipulating calendars, mirroring functionality akin to the Unix `cal` comma"
ref: https://docs.python.org/3/library/calendar.html
ref_type: url
---

# calendar— General calendar-related functions¶

The **`calendar`** module in Python provides utilities for generating and manipulating calendars, mirroring functionality akin to the Unix `cal` command. It operates under the **proleptic Gregorian calendar**, extending indefinitely backward and forward, adhering to ISO 8601 conventions (e.g., year 0 = 1 BC, year -1 = 2 BC). By default, weeks start on **Monday (0)** and end on **Sunday (6)**, but this can be reconfigured using `setfirstweekday()` to align with other conventions (e.g., Sunday-first). Core features include:
- **`Calendar` class**: A base class for calendar operations, enabling customization of weekdays and iteration over dates (e.g., `iterweekdays()`, `itermonthdates()`).
- **Weekday constants**: `MONDAY` (0) and `SUNDAY` (6) define default weekday indices.
- **Date handling**: Functions like `itermonthdates()` yield iterable date objects for a given month/year, while `iterweekdays()` generates weekday sequences.
- **Integration**: Complements `datetime` and `time` modules for advanced time/date operations.

[Link to original](https://docs.python.org/3/library/calendar.html)
