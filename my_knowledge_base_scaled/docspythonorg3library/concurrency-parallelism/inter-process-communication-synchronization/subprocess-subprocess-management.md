---
id: 0.0.9.3.0
title: "subprocess— Subprocess management¶"
nav_summary: "The `subprocess` module in Python enables robust management of external processes by providing tools to spawn new processes, interact with their input"
ref: https://docs.python.org/3/library/subprocess.html
ref_type: url
---

# subprocess— Subprocess management¶

The `subprocess` module in Python enables robust management of external processes by providing tools to spawn new processes, interact with their input/output/error streams, and retrieve return codes. It replaces legacy functions like `os.system` and `os.spawn*`, offering a more flexible and secure interface. The module’s core functionality revolves around two primary components: the high-level `subprocess.run()` function and the low-level `subprocess.Popen` class. `subprocess.run()` simplifies process execution by handling creation, execution, and cleanup in a single call, returning a `CompletedProcess` object with results. Key features include:
- **Stream Handling**: Control over `stdin`, `stdout`, and `stderr` via `PIPE`, `STDOUT`, or file objects.
- **Output Capture**: The `capture_output=True` parameter automatically pipes stdout/stderr to a `CompletedProcess` object.
- **Timeouts**: Enforce execution limits via `timeout`, raising `TimeoutExpired` if exceeded.
- **Error Handling**: The `check=True` flag raises `CalledProcessError` on non-zero exit codes.
- **Advanced Control**: For granular management, `Popen` offers methods like `communicate

[Link to original](https://docs.python.org/3/library/subprocess.html)
