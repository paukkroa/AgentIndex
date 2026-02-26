---
id: 0.0.10.3.2.0
title: "ftplib— FTP protocol client¶"
nav_summary: "The `ftplib` module provides Python’s implementation of the **FTP (File Transfer Protocol)** client, enabling automated file transfers via the **RFC 9"
ref: https://docs.python.org/3/library/ftplib.html
ref_type: url
---

# ftplib— FTP protocol client¶

The `ftplib` module provides Python’s implementation of the **FTP (File Transfer Protocol)** client, enabling automated file transfers via the **RFC 959** standard. It implements the `FTP` class, which handles connections, authentication (defaulting to anonymous login), directory navigation (`cwd`, `mkdir`, `rmdir`), file operations (`retrbinary`, `storbinary`, `retrlines`), and passive/active mode transfers. Key features include:
- **UTF-8 encoding** (per **RFC 2640**) for international filenames.
- **Timeout control** for blocking operations (e.g., `connect`, `retrbinary`).
- **Session management** with methods like `login`, `quit`, and `close`.
- **Passive mode support** for firewalled environments via `set_pasv`.
- **Error handling** via exceptions like `FTPPermitError`, `FTPTimeoutError`, and `FTPError`.
- **Integration** with `urllib.request` for FTP URL handling.
- **Non-WASI compatibility**: Unavailable on WebAssembly platforms.
Example workflows include directory listing (`LIST`), file downloads (`

[Link to original](https://docs.python.org/3/library/ftplib.html)
