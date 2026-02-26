---
id: 0.0.9.4.2
title: "sched— Event scheduler¶"
nav_summary: "`Python event scheduler with priority-based absolute/relative timing`"
ref: https://docs.python.org/3/library/sched.html
ref_type: url
---

# sched— Event scheduler¶

The `sched` module in Python provides a **`scheduler` class** for managing event-driven tasks with configurable timing and priority. The scheduler requires two functions: a **`timefunc`** (default: `time.monotonic`) to measure elapsed time and a **`delayfunc`** (default: `time.sleep`) to pause execution. Events can be scheduled either **absolutely** (`enterabs`) via a fixed timestamp or **relatively** (`enter`) after a specified delay. Each event is executed with a given **priority** (lower = higher priority) and can include **positional arguments** (`argument`) or **keyword arguments** (`kwargs`). Events are run sequentially, with cancellations supported via the `cancel()` method. Introduced in Python 3.3, the scheduler is **thread-safe** and allows optional `timefunc`/`delayfunc` parameters.

---

[Link to original](https://docs.python.org/3/library/sched.html)
