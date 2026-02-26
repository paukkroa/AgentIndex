---
id: 0.0.3.0.1
title: "pathlib— Object-oriented filesystem paths¶"
nav_summary: "Object-oriented filesystem paths (Python 3.4+)."
ref: https://docs.python.org/3/library/pathlib.html
ref_type: url
---

# pathlib— Object-oriented filesystem paths¶

The `pathlib` module (introduced in Python 3.4) provides an **object-oriented interface** for filesystem path manipulation, abstracting platform-specific complexities (e.g., Unix vs. Windows paths). It distinguishes between **pure paths** (computational-only, no filesystem I/O) and **concrete paths** (inherit pure paths + I/O operations). The primary class, `Path`, dynamically instantiates the appropriate concrete path type (`PosixPath` or `WindowsPath`) for the host OS. Pure paths (`PurePosixPath`, `PureWindowsPath`) enable cross-platform path operations without filesystem access, useful for testing or emulation. Key features include intuitive path navigation (e.g., `p / 'subdir'`), recursive directory traversal (`glob()`), and filesystem queries (`exists()`, `is_dir()`). Exceptions like `UnsupportedOperation` flag unsupported operations. Backward compatibility with `os.path` is maintained for low-level string-based path handling.

---

[Link to original](https://docs.python.org/3/library/pathlib.html)
