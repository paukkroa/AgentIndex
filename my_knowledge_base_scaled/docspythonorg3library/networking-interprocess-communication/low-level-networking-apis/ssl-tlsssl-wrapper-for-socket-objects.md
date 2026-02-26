---
id: 0.0.10.0.1
title: "ssl— TLS/SSL wrapper for socket objects¶"
nav_summary: "The **`ssl` module** in Python provides a **TLS/SSL wrapper** for socket objects, enabling secure communication over network connections by encrypting"
ref: https://docs.python.org/3/library/ssl.html
ref_type: url
---

# ssl— TLS/SSL wrapper for socket objects¶

The **`ssl` module** in Python provides a **TLS/SSL wrapper** for socket objects, enabling secure communication over network connections by encrypting data and authenticating peers using the OpenSSL library. It is an **optional module**, requiring OpenSSL installation (version 1.1.1+ recommended) and may exhibit platform-dependent behavior due to OS and OpenSSL API variations. Key components include:
- **`SSLSocket`**: A subclass of `socket.socket` that encrypts/decrypts traffic and supports methods like `getpeercert()`, `cipher()`, and certificate chain retrieval (`get_verified_chain()`, `get_unverified_chain()`).
- **`SSLContext`**: Manages SSL/TLS configurations (e.g., certificates, protocols) and enables reusable settings for sockets via `wrap_socket()`.
- **Helper functions**: `create_default_context()` provides pre-configured secure defaults.
- **Security considerations**: Default settings may not suffice; review [Security considerations](#ssl-security) to avoid vulnerabilities.
- **Compatibility**: Not available on WASI/WebAssembly; deprecated OpenSSL versions (e.g., 0.9.8) are unsupported post-Python 3.6.

[Link to original](https://docs.python.org/3/library/ssl.html)
