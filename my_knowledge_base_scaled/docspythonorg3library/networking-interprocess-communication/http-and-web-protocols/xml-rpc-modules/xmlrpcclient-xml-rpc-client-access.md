---
id: 0.0.10.3.3.1
title: "xmlrpc.client— XML-RPC client access¶"
nav_summary: "The `xmlrpc"
ref: https://docs.python.org/3/library/xmlrpc.client.html
ref_type: url
---

# xmlrpc.client— XML-RPC client access¶

The `xmlrpc.client` module in Python provides a framework for creating **XML-RPC clients**, enabling remote procedure calls (RPCs) over HTTP(S) using XML as the data format. It abstracts the complexities of XML serialization/deserialization and HTTP communication, allowing developers to interact with remote XML-RPC servers seamlessly. The core class, **`ServerProxy`**, initializes with a URI (typically a server URL) and optional parameters like transport (defaulting to secure `SafeTransport` for HTTPS), encoding (UTF-8 by default), and debugging flags. Key features include:
- **Type Handling**: Supports Python-native types (e.g., `datetime`, `bytes`) via `use_builtin_types` or `use_datetime` (deprecated). `allow_none` enables sending `None` values (a non-standard extension).
- **Security**: Defaults to strict HTTPS certificate validation (since Python 3.5) and includes a `SafeTransport` for secure connections. Untrusted data requires manual validation.
- **Customization**: Allows HTTP headers via the `headers` parameter and SSL context configuration for HTTPS via `context`.
- **Compatibility**: Works with standard XML-RPC servers but

[Link to original](https://docs.python.org/3/library/xmlrpc.client.html)
