---
id: 0.0.10.3.3.0
title: "xmlrpc— XMLRPC server and client modules¶"
nav_summary: "`xmlrpc` module: XML-RPC server/client for HTTP/XML RPC."
ref: https://docs.python.org/3/library/xmlrpc.html
ref_type: url
---

# xmlrpc— XMLRPC server and client modules¶

The `xmlrpc` package in Python provides server and client modules for implementing **XML-RPC**, a lightweight remote procedure call (RPC) protocol that transmits data as **XML over HTTP**. It enables clients to invoke methods on remote servers via URIs, receiving structured responses. The package includes two core modules:
- **`xmlrpc.client`** for client-side communication, allowing calls to remote XML-RPC services with parameters and receiving XML-encoded results.
- **`xmlrpc.server`** for server-side implementation, offering basic server classes (e.g., `SimpleXMLRPCServer`) to expose methods as XML-RPC endpoints. Features include fault handling, request parsing, and response generation, with support for customizable request/response processing. XML-RPC is ideal for simple cross-language interoperability but lacks modern security features like HTTPS encryption by default.

---

[Link to original](https://docs.python.org/3/library/xmlrpc.html)
