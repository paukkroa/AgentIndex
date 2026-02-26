---
id: 0.0.20.0
title: "ctypes— A foreign function library for Python¶"
nav_summary: "The `ctypes` module is a **foreign function interface (FFI)** library in Python that enables seamless interaction with **C-compatible data types** and"
ref: https://docs.python.org/3/library/ctypes.html
ref_type: url
---

# ctypes— A foreign function library for Python¶

The `ctypes` module is a **foreign function interface (FFI)** library in Python that enables seamless interaction with **C-compatible data types** and **dynamic link libraries (DLLs/shared libraries)**. It allows Python to call functions from external libraries (e.g., `.dll` on Windows or `.so` on Unix) as if they were native Python functions. Key features include:
- **C-compatible types** (`c_int`, `c_char`, `c_float`, etc.) for type-safe interoperability.
- **Library loading** via `cdll` (C calling convention), `windll` (Windows `stdcall`), and `oledll` (Windows COM/OLE with `HRESULT` error handling).
- **Cross-platform support** (Windows, Linux, macOS) with platform-specific conventions.
- **Optional module** (may require installation; check your Python distribution).
- **Error handling** (e.g., `OSError` for failed function calls).
- **Tutorial-driven examples** using `doctest` for interactive verification.
- **Low-level control** over memory management and data structures (e.g., `c_void_p`, `c_buffer`).

Use cases include interf

[Link to original](https://docs.python.org/3/library/ctypes.html)
