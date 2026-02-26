---
id: 0.0.8.0.0
title: "os— Miscellaneous operating system interfaces¶"
nav_summary: "The `os` module in Python provides a **portable interface** to operating system-dependent functionality, enabling cross-platform compatibility while e"
ref: https://docs.python.org/3/library/os.html
ref_type: url
---

# os— Miscellaneous operating system interfaces¶

The `os` module in Python provides a **portable interface** to operating system-dependent functionality, enabling cross-platform compatibility while exposing OS-specific features where necessary. It offers core operations like file/directory manipulation (e.g., `os.listdir()`, `os.rename()`), process management (e.g., `os.fork()`, `os.execve()`), and system information retrieval (e.g., `os.name`, `os.uname()`). Key features include:
- **Unified interfaces** for POSIX/Windows (e.g., `os.stat()` returns consistent stat data).
- **Path handling** (via `os.path`) and **file operations** (e.g., `os.open()`, `os.remove()`), supporting both string/bytes inputs/outputs.
- **Environment interaction** (e.g., `os.getenv()`, `os.environ`), command execution (`os.system()`, `os.popen()`), and process control (e.g., `os.wait()`, `os.kill()`).
- **Platform-specific caveats**: Limited support on WebAssembly/Android/iOS (e.g., no `fork()` or signals), with emulated stubs for basic functions like `getuid()`.
- **Error handling**: All functions raise

[Link to original](https://docs.python.org/3/library/os.html)
