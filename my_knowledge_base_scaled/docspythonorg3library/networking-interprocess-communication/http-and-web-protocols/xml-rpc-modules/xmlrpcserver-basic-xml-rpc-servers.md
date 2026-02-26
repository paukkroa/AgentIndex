---
id: 0.0.10.3.3.2
title: "xmlrpc.server— Basic XML-RPC servers¶"
nav_summary: "XML-RPC server classes: `SimpleXMLRPCServer`, `CGIXMLRPCRequestHandler`"
ref: https://docs.python.org/3/library/xmlrpc.server.html
ref_type: url
---

# xmlrpc.server— Basic XML-RPC servers¶

The `xmlrpc.server` module in Python provides foundational components for building XML-RPC servers, enabling remote procedure calls via XML-based communication. It offers two primary server implementations: **`SimpleXMLRPCServer`**, a standalone TCP-based server for direct use, and **`CGIXMLRPCRequestHandler`**, designed for integration within CGI environments. Key features include configurable request logging, customizable response handling (e.g., `allow_none`, `encoding`), and support for built-in type processing (e.g., dates, binary data) via the `use_builtin_types` flag. The module leverages `socketserver.TCPServer` for networking and integrates with `xmlrpc.client` for XML-RPC protocol compliance. Security warnings emphasize its unsuitability for untrusted/unauthenticated data, directing users to XML security best practices. Introduced in Python 3.3, `use_builtin_types` enhances type handling flexibility.

---

[Link to original](https://docs.python.org/3/library/xmlrpc.server.html)
