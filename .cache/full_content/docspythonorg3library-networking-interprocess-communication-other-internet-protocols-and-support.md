### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](webbrowser.html "webbrowser — Convenient web-browser controller") |
* [previous](pyexpat.html "xml.parsers.expat — Fast XML parsing using Expat") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Internet Protocols and Support
* |
* Theme
  Auto
  Light
  Dark
   |

# Internet Protocols and Support[¶](#internet-protocols-and-support "Link to this heading")

The modules described in this chapter implement internet protocols and support
for related technology. They are all implemented in Python. Most of these
modules require the presence of the system-dependent module [`socket`](socket.html#module-socket "socket: Low-level networking interface."), which
is currently supported on most popular platforms. Here is an overview:

* [`webbrowser` — Convenient web-browser controller](webbrowser.html)
  + [Command-line interface](webbrowser.html#command-line-interface)
  + [Browser controller objects](webbrowser.html#browser-controller-objects)
* [`wsgiref` — WSGI Utilities and Reference Implementation](wsgiref.html)
  + [`wsgiref.util` – WSGI environment utilities](wsgiref.html#module-wsgiref.util)
  + [`wsgiref.headers` – WSGI response header tools](wsgiref.html#module-wsgiref.headers)
  + [`wsgiref.simple_server` – a simple WSGI HTTP server](wsgiref.html#module-wsgiref.simple_server)
  + [`wsgiref.validate` — WSGI conformance checker](wsgiref.html#module-wsgiref.validate)
  + [`wsgiref.handlers` – server/gateway base classes](wsgiref.html#module-wsgiref.handlers)
  + [`wsgiref.types` – WSGI types for static type checking](wsgiref.html#module-wsgiref.types)
  + [Examples](wsgiref.html#examples)
* [`urllib` — URL handling modules](urllib.html)
* [`urllib.request` — Extensible library for opening URLs](urllib.request.html)
  + [Request Objects](urllib.request.html#request-objects)
  + [OpenerDirector Objects](urllib.request.html#openerdirector-objects)
  + [BaseHandler Objects](urllib.request.html#basehandler-objects)
  + [HTTPRedirectHandler Objects](urllib.request.html#httpredirecthandler-objects)
  + [HTTPCookieProcessor Objects](urllib.request.html#httpcookieprocessor-objects)
  + [ProxyHandler Objects](urllib.request.html#proxyhandler-objects)
  + [HTTPPasswordMgr Objects](urllib.request.html#httppasswordmgr-objects)
  + [HTTPPasswordMgrWithPriorAuth Objects](urllib.request.html#httppasswordmgrwithpriorauth-objects)
  + [AbstractBasicAuthHandler Objects](urllib.request.html#abstractbasicauthhandler-objects)
  + [HTTPBasicAuthHandler Objects](urllib.request.html#httpbasicauthhandler-objects)
  + [ProxyBasicAuthHandler Objects](urllib.request.html#proxybasicauthhandler-objects)
  + [AbstractDigestAuthHandler Objects](urllib.request.html#abstractdigestauthhandler-objects)
  + [HTTPDigestAuthHandler Objects](urllib.request.html#httpdigestauthhandler-objects)
  + [ProxyDigestAuthHandler Objects](urllib.request.html#proxydigestauthhandler-objects)
  + [HTTPHandler Objects](urllib.request.html#httphandler-objects)
  + [HTTPSHandler Objects](urllib.request.html#httpshandler-objects)
  + [FileHandler Objects](urllib.request.html#filehandler-objects)
  + [DataHandler Objects](urllib.request.html#datahandler-objects)
  + [FTPHandler Objects](urllib.request.html#ftphandler-objects)
  + [CacheFTPHandler Objects](urllib.request.html#cacheftphandler-objects)
  + [UnknownHandler Objects](urllib.request.html#unknownhandler-objects)
  + [HTTPErrorProcessor Objects](urllib.request.html#httperrorprocessor-objects)
  + [Examples](urllib.request.html#examples)
  + [Legacy interface](urllib.request.html#legacy-interface)
  + [`urllib.request` Restrictions](urllib.request.html#urllib-request-restrictions)
* [`urllib.response` — Response classes used by urllib](urllib.request.html#module-urllib.response)
* [`urllib.parse` — Parse URLs into components](urllib.parse.html)
  + [URL Parsing](urllib.parse.html#url-parsing)
  + [URL parsing security](urllib.parse.html#url-parsing-security)
  + [Parsing ASCII Encoded Bytes](urllib.parse.html#parsing-ascii-encoded-bytes)
  + [Structured Parse Results](urllib.parse.html#structured-parse-results)
  + [URL Quoting](urllib.parse.html#url-quoting)
* [`urllib.error` — Exception classes raised by urllib.request](urllib.error.html)
* [`urllib.robotparser` — Parser for robots.txt](urllib.robotparser.html)
* [`http` — HTTP modules](http.html)
  + [HTTP status codes](http.html#http-status-codes)
  + [HTTP status category](http.html#http-status-category)
  + [HTTP methods](http.html#http-methods)
* [`http.client` — HTTP protocol client](http.client.html)
  + [HTTPConnection Objects](http.client.html#httpconnection-objects)
  + [HTTPResponse Objects](http.client.html#httpresponse-objects)
  + [Examples](http.client.html#examples)
  + [HTTPMessage Objects](http.client.html#httpmessage-objects)
* [`ftplib` — FTP protocol client](ftplib.html)
  + [Reference](ftplib.html#reference)
    - [FTP objects](ftplib.html#ftp-objects)
    - [FTP\_TLS objects](ftplib.html#ftp-tls-objects)
    - [Module variables](ftplib.html#module-variables)
* [`poplib` — POP3 protocol client](poplib.html)
  + [POP3 Objects](poplib.html#pop3-objects)
  + [POP3 Example](poplib.html#pop3-example)
* [`imaplib` — IMAP4 protocol client](imaplib.html)
  + [IMAP4 Objects](imaplib.html#imap4-objects)
  + [IMAP4 Example](imaplib.html#imap4-example)
* [`smtplib` — SMTP protocol client](smtplib.html)
  + [SMTP Objects](smtplib.html#smtp-objects)
  + [SMTP Example](smtplib.html#smtp-example)
* [`uuid` — UUID objects according to **RFC 9562**](uuid.html)
  + [Command-Line Usage](uuid.html#command-line-usage)
  + [Example](uuid.html#example)
  + [Command-Line Example](uuid.html#command-line-example)
* [`socketserver` — A framework for network servers](socketserver.html)
  + [Server Creation Notes](socketserver.html#server-creation-notes)
  + [Server Objects](socketserver.html#server-objects)
  + [Request Handler Objects](socketserver.html#request-handler-objects)
  + [Examples](socketserver.html#examples)
    - [`socketserver.TCPServer` Example](socketserver.html#socketserver-tcpserver-example)
    - [`socketserver.UDPServer` Example](socketserver.html#socketserver-udpserver-example)
    - [Asynchronous Mixins](socketserver.html#asynchronous-mixins)
* [`http.server` — HTTP servers](http.server.html)
  + [Command-line interface](http.server.html#command-line-interface)
  + [Security considerations](http.server.html#security-considerations)
* [`http.cookies` — HTTP state management](http.cookies.html)
  + [Cookie Objects](http.cookies.html#cookie-objects)
  + [Morsel Objects](http.cookies.html#morsel-objects)
  + [Example](http.cookies.html#example)
* [`http.cookiejar` — Cookie handling for HTTP clients](http.cookiejar.html)
  + [CookieJar and FileCookieJar Objects](http.cookiejar.html#cookiejar-and-filecookiejar-objects)
  + [FileCookieJar subclasses and co-operation with web browsers](http.cookiejar.html#filecookiejar-subclasses-and-co-operation-with-web-browsers)
  + [CookiePolicy Objects](http.cookiejar.html#cookiepolicy-objects)
  + [DefaultCookiePolicy Objects](http.cookiejar.html#defaultcookiepolicy-objects)
  + [Cookie Objects](http.cookiejar.html#cookie-objects)
  + [Examples](http.cookiejar.html#examples)
* [`xmlrpc` — XMLRPC server and client modules](xmlrpc.html)
* [`xmlrpc.client` — XML-RPC client access](xmlrpc.client.html)
  + [ServerProxy Objects](xmlrpc.client.html#serverproxy-objects)
  + [DateTime Objects](xmlrpc.client.html#datetime-objects)
  + [Binary Objects](xmlrpc.client.html#binary-objects)
  + [Fault Objects](xmlrpc.client.html#fault-objects)
  + [ProtocolError Objects](xmlrpc.client.html#protocolerror-objects)
  + [MultiCall Objects](xmlrpc.client.html#multicall-objects)
  + [Convenience Functions](xmlrpc.client.html#convenience-functions)
  + [Example of Client Usage](xmlrpc.client.html#example-of-client-usage)
  + [Example of Client and Server Usage](xmlrpc.client.html#example-of-client-and-server-usage)
* [`xmlrpc.server` — Basic XML-RPC servers](xmlrpc.server.html)
  + [SimpleXMLRPCServer Objects](xmlrpc.server.html#simplexmlrpcserver-objects)
    - [SimpleXMLRPCServer Example](xmlrpc.server.html#simplexmlrpcserver-example)
  + [CGIXMLRPCRequestHandler](xmlrpc.server.html#cgixmlrpcrequesthandler)
  + [Documenting XMLRPC server](xmlrpc.server.html#documenting-xmlrpc-server)
  + [DocXMLRPCServer Objects](xmlrpc.server.html#docxmlrpcserver-objects)
  + [DocCGIXMLRPCRequestHandler](xmlrpc.server.html#doccgixmlrpcrequesthandler)
* [`ipaddress` — IPv4/IPv6 manipulation library](ipaddress.html)
  + [Convenience factory functions](ipaddress.html#convenience-factory-functions)
  + [IP Addresses](ipaddress.html#ip-addresses)
    - [Address objects](ipaddress.html#address-objects)
    - [Conversion to Strings and Integers](ipaddress.html#conversion-to-strings-and-integers)
    - [Operators](ipaddress.html#operators)
      * [Comparison operators](ipaddress.html#comparison-operators)
      * [Arithmetic operators](ipaddress.html#arithmetic-operators)
  + [IP Network definitions](ipaddress.html#ip-network-definitions)
    - [Prefix, net mask and host mask](ipaddress.html#prefix-net-mask-and-host-mask)
    - [Network objects](ipaddress.html#network-objects)
    - [Operators](ipaddress.html#id1)
      * [Logical operators](ipaddress.html#logical-operators)
      * [Iteration](ipaddress.html#iteration)
      * [Networks as containers of addresses](ipaddress.html#networks-as-containers-of-addresses)
  + [Interface objects](ipaddress.html#interface-objects)
    - [Operators](ipaddress.html#id2)
      * [Logical operators](ipaddress.html#id3)
  + [Other Module Level Functions](ipaddress.html#other-module-level-functions)
  + [Custom Exceptions](ipaddress.html#custom-exceptions)

#### Previous topic

[`xml.parsers.expat` — Fast XML parsing using Expat](pyexpat.html "previous chapter")

#### Next topic

[`webbrowser` — Convenient web-browser controller](webbrowser.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/internet.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](webbrowser.html "webbrowser — Convenient web-browser controller") |
* [previous](pyexpat.html "xml.parsers.expat — Fast XML parsing using Expat") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Internet Protocols and Support
* |
* Theme
  Auto
  Light
  Dark
   |

© [Copyright](../copyright.html) 2001 Python Software Foundation.
  
This page is licensed under the Python Software Foundation License Version 2.
  
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
  
See [History and License](/license.html) for more information.  
  
The Python Software Foundation is a non-profit corporation.
[Please donate.](https://www.python.org/psf/donations/)
  
  
Last updated on Feb 22, 2026 (06:32 UTC).
[Found a bug](/bugs.html)?
  
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.