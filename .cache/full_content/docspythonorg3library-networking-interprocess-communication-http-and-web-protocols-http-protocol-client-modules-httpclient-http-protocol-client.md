### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](ftplib.html "ftplib — FTP protocol client") |
* [previous](http.html "http — HTTP modules") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `http.client` — HTTP protocol client
* |
* Theme
  Auto
  Light
  Dark
   |

# `http.client` — HTTP protocol client[¶](#module-http.client "Link to this heading")

**Source code:** [Lib/http/client.py](https://github.com/python/cpython/tree/3.14/Lib/http/client.py)

---

This module defines classes that implement the client side of the HTTP and
HTTPS protocols. It is normally not used directly — the module
[`urllib.request`](urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.") uses it to handle URLs that use HTTP and HTTPS.

See also

The [Requests package](https://requests.readthedocs.io/en/latest/)
is recommended for a higher-level HTTP client interface.

Note

HTTPS support is only available if Python was compiled with SSL support
(through the [`ssl`](ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects") module).

[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

The module provides the following classes:

*class* http.client.HTTPConnection(*host*, *port=None*, [*timeout*, ]*source\_address=None*, *blocksize=8192*)[¶](#http.client.HTTPConnection "Link to this definition")
:   An [`HTTPConnection`](#http.client.HTTPConnection "http.client.HTTPConnection") instance represents one transaction with an HTTP
    server. It should be instantiated by passing it a host and optional port
    number. If no port number is passed, the port is extracted from the host
    string if it has the form `host:port`, else the default HTTP port (80) is
    used. If the optional *timeout* parameter is given, blocking
    operations (like connection attempts) will timeout after that many seconds
    (if it is not given, the global default timeout setting is used).
    The optional *source\_address* parameter may be a tuple of a (host, port)
    to use as the source address the HTTP connection is made from.
    The optional *blocksize* parameter sets the buffer size in bytes for
    sending a file-like message body.

    For example, the following calls all create instances that connect to the server
    at the same host and port:

    ```
    >>> h1 = http.client.HTTPConnection('www.python.org')
    >>> h2 = http.client.HTTPConnection('www.python.org:80')
    >>> h3 = http.client.HTTPConnection('www.python.org', 80)
    >>> h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)
    ```

    Changed in version 3.2: *source\_address* was added.

    Changed in version 3.4: The *strict* parameter was removed. HTTP 0.9-style “Simple Responses” are
    no longer supported.

    Changed in version 3.7: *blocksize* parameter was added.

*class* http.client.HTTPSConnection(*host*, *port=None*, *\**, [*timeout*, ]*source\_address=None*, *context=None*, *blocksize=8192*)[¶](#http.client.HTTPSConnection "Link to this definition")
:   A subclass of [`HTTPConnection`](#http.client.HTTPConnection "http.client.HTTPConnection") that uses SSL for communication with
    secure servers. Default port is `443`. If *context* is specified, it
    must be a [`ssl.SSLContext`](ssl.html#ssl.SSLContext "ssl.SSLContext") instance describing the various SSL
    options.

    Please read [Security considerations](ssl.html#ssl-security) for more information on best practices.

    Changed in version 3.2: *source\_address*, *context* and *check\_hostname* were added.

    Changed in version 3.2: This class now supports HTTPS virtual hosts if possible (that is,
    if [`ssl.HAS_SNI`](ssl.html#ssl.HAS_SNI "ssl.HAS_SNI") is true).

    Changed in version 3.4: The *strict* parameter was removed. HTTP 0.9-style “Simple Responses” are
    no longer supported.

    Changed in version 3.4.3: This class now performs all the necessary certificate and hostname checks
    by default. To revert to the previous, unverified, behavior
    `ssl._create_unverified_context()` can be passed to the *context*
    parameter.

    Changed in version 3.8: This class now enables TLS 1.3
    [`ssl.SSLContext.post_handshake_auth`](ssl.html#ssl.SSLContext.post_handshake_auth "ssl.SSLContext.post_handshake_auth") for the default *context* or
    when *cert\_file* is passed with a custom *context*.

    Changed in version 3.10: This class now sends an ALPN extension with protocol indicator
    `http/1.1` when no *context* is given. Custom *context* should set
    ALPN protocols with [`set_alpn_protocols()`](ssl.html#ssl.SSLContext.set_alpn_protocols "ssl.SSLContext.set_alpn_protocols").

    Changed in version 3.12: The deprecated *key\_file*, *cert\_file* and *check\_hostname* parameters
    have been removed.

*class* http.client.HTTPResponse(*sock*, *debuglevel=0*, *method=None*, *url=None*)[¶](#http.client.HTTPResponse "Link to this definition")
:   Class whose instances are returned upon successful connection. Not
    instantiated directly by user.

    Changed in version 3.4: The *strict* parameter was removed. HTTP 0.9 style “Simple Responses” are
    no longer supported.

This module provides the following function:

http.client.parse\_headers(*fp*)[¶](#http.client.parse_headers "Link to this definition")
:   Parse the headers from a file pointer *fp* representing a HTTP
    request/response. The file has to be a [`BufferedIOBase`](io.html#io.BufferedIOBase "io.BufferedIOBase") reader
    (i.e. not text) and must provide a valid [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) style header.

    This function returns an instance of [`http.client.HTTPMessage`](#http.client.HTTPMessage "http.client.HTTPMessage")
    that holds the header fields, but no payload
    (the same as [`HTTPResponse.msg`](#http.client.HTTPResponse.msg "http.client.HTTPResponse.msg")
    and [`http.server.BaseHTTPRequestHandler.headers`](http.server.html#http.server.BaseHTTPRequestHandler.headers "http.server.BaseHTTPRequestHandler.headers")).
    After returning, the file pointer *fp* is ready to read the HTTP body.

    Note

    [`parse_headers()`](#http.client.parse_headers "http.client.parse_headers") does not parse the start-line of a HTTP message;
    it only parses the `Name: value` lines. The file has to be ready to
    read these field lines, so the first line should already be consumed
    before calling the function.

The following exceptions are raised as appropriate:

*exception* http.client.HTTPException[¶](#http.client.HTTPException "Link to this definition")
:   The base class of the other exceptions in this module. It is a subclass of
    [`Exception`](exceptions.html#Exception "Exception").

*exception* http.client.NotConnected[¶](#http.client.NotConnected "Link to this definition")
:   A subclass of [`HTTPException`](#http.client.HTTPException "http.client.HTTPException").

*exception* http.client.InvalidURL[¶](#http.client.InvalidURL "Link to this definition")
:   A subclass of [`HTTPException`](#http.client.HTTPException "http.client.HTTPException"), raised if a port is given and is either
    non-numeric or empty.

*exception* http.client.UnknownProtocol[¶](#http.client.UnknownProtocol "Link to this definition")
:   A subclass of [`HTTPException`](#http.client.HTTPException "http.client.HTTPException").

*exception* http.client.UnknownTransferEncoding[¶](#http.client.UnknownTransferEncoding "Link to this definition")
:   A subclass of [`HTTPException`](#http.client.HTTPException "http.client.HTTPException").

*exception* http.client.UnimplementedFileMode[¶](#http.client.UnimplementedFileMode "Link to this definition")
:   A subclass of [`HTTPException`](#http.client.HTTPException "http.client.HTTPException").

*exception* http.client.IncompleteRead[¶](#http.client.IncompleteRead "Link to this definition")
:   A subclass of [`HTTPException`](#http.client.HTTPException "http.client.HTTPException").

*exception* http.client.ImproperConnectionState[¶](#http.client.ImproperConnectionState "Link to this definition")
:   A subclass of [`HTTPException`](#http.client.HTTPException "http.client.HTTPException").

*exception* http.client.CannotSendRequest[¶](#http.client.CannotSendRequest "Link to this definition")
:   A subclass of [`ImproperConnectionState`](#http.client.ImproperConnectionState "http.client.ImproperConnectionState").

*exception* http.client.CannotSendHeader[¶](#http.client.CannotSendHeader "Link to this definition")
:   A subclass of [`ImproperConnectionState`](#http.client.ImproperConnectionState "http.client.ImproperConnectionState").

*exception* http.client.ResponseNotReady[¶](#http.client.ResponseNotReady "Link to this definition")
:   A subclass of [`ImproperConnectionState`](#http.client.ImproperConnectionState "http.client.ImproperConnectionState").

*exception* http.client.BadStatusLine[¶](#http.client.BadStatusLine "Link to this definition")
:   A subclass of [`HTTPException`](#http.client.HTTPException "http.client.HTTPException"). Raised if a server responds with a HTTP
    status code that we don’t understand.

*exception* http.client.LineTooLong[¶](#http.client.LineTooLong "Link to this definition")
:   A subclass of [`HTTPException`](#http.client.HTTPException "http.client.HTTPException"). Raised if an excessively long line
    is received in the HTTP protocol from the server.

*exception* http.client.RemoteDisconnected[¶](#http.client.RemoteDisconnected "Link to this definition")
:   A subclass of [`ConnectionResetError`](exceptions.html#ConnectionResetError "ConnectionResetError") and [`BadStatusLine`](#http.client.BadStatusLine "http.client.BadStatusLine"). Raised
    by [`HTTPConnection.getresponse()`](#http.client.HTTPConnection.getresponse "http.client.HTTPConnection.getresponse") when the attempt to read the response
    results in no data read from the connection, indicating that the remote end
    has closed the connection.

    Added in version 3.5: Previously, [`BadStatusLine`](#http.client.BadStatusLine "http.client.BadStatusLine")`('')` was raised.

The constants defined in this module are:

http.client.HTTP\_PORT[¶](#http.client.HTTP_PORT "Link to this definition")
:   The default port for the HTTP protocol (always `80`).

http.client.HTTPS\_PORT[¶](#http.client.HTTPS_PORT "Link to this definition")
:   The default port for the HTTPS protocol (always `443`).

http.client.responses[¶](#http.client.responses "Link to this definition")
:   This dictionary maps the HTTP 1.1 status codes to the W3C names.

    Example: `http.client.responses[http.client.NOT_FOUND]` is `'Not Found'`.

See [HTTP status codes](http.html#http-status-codes) for a list of HTTP status codes that are
available in this module as constants.

## HTTPConnection Objects[¶](#httpconnection-objects "Link to this heading")

[`HTTPConnection`](#http.client.HTTPConnection "http.client.HTTPConnection") instances have the following methods:

HTTPConnection.request(*method*, *url*, *body=None*, *headers={}*, *\**, *encode\_chunked=False*)[¶](#http.client.HTTPConnection.request "Link to this definition")
:   This will send a request to the server using the HTTP request
    method *method* and the request URI *url*. The provided *url* must be
    an absolute path to conform with [**RFC 2616 §5.1.2**](https://datatracker.ietf.org/doc/html/rfc2616.html#section-5.1.2)
    (unless connecting to an HTTP proxy server or using the `OPTIONS` or
    `CONNECT` methods).

    If *body* is specified, the specified data is sent after the headers are
    finished. It may be a [`str`](stdtypes.html#str "str"), a [bytes-like object](../glossary.html#term-bytes-like-object), an
    open [file object](../glossary.html#term-file-object), or an iterable of [`bytes`](stdtypes.html#bytes "bytes"). If *body*
    is a string, it is encoded as ISO-8859-1, the default for HTTP. If it
    is a bytes-like object, the bytes are sent as is. If it is a [file
    object](../glossary.html#term-file-object), the contents of the file is sent; this file object should
    support at least the `read()` method. If the file object is an
    instance of [`io.TextIOBase`](io.html#io.TextIOBase "io.TextIOBase"), the data returned by the `read()`
    method will be encoded as ISO-8859-1, otherwise the data returned by
    `read()` is sent as is. If *body* is an iterable, the elements of the
    iterable are sent as is until the iterable is exhausted.

    The *headers* argument should be a mapping of extra HTTP headers to send
    with the request. A [**Host header**](https://datatracker.ietf.org/doc/html/rfc2616.html#section-14.23)
    must be provided to conform with [**RFC 2616 §5.1.2**](https://datatracker.ietf.org/doc/html/rfc2616.html#section-5.1.2)
    (unless connecting to an HTTP proxy server or using the `OPTIONS` or
    `CONNECT` methods).

    If *headers* contains neither Content-Length nor Transfer-Encoding,
    but there is a request body, one of those
    header fields will be added automatically. If
    *body* is `None`, the Content-Length header is set to `0` for
    methods that expect a body (`PUT`, `POST`, and `PATCH`). If
    *body* is a string or a bytes-like object that is not also a
    [file](../glossary.html#term-file-object), the Content-Length header is
    set to its length. Any other type of *body* (files
    and iterables in general) will be chunk-encoded, and the
    Transfer-Encoding header will automatically be set instead of
    Content-Length.

    The *encode\_chunked* argument is only relevant if Transfer-Encoding is
    specified in *headers*. If *encode\_chunked* is `False`, the
    HTTPConnection object assumes that all encoding is handled by the
    calling code. If it is `True`, the body will be chunk-encoded.

    For example, to perform a `GET` request to `https://docs.python.org/3/`:

    ```
    >>> import http.client
    >>> host = "docs.python.org"
    >>> conn = http.client.HTTPSConnection(host)
    >>> conn.request("GET", "/3/", headers={"Host": host})
    >>> response = conn.getresponse()
    >>> print(response.status, response.reason)
    200 OK
    ```

    Note

    Chunked transfer encoding has been added to the HTTP protocol
    version 1.1. Unless the HTTP server is known to handle HTTP 1.1,
    the caller must either specify the Content-Length, or must pass a
    [`str`](stdtypes.html#str "str") or bytes-like object that is not also a file as the
    body representation.

    Note

    Note that you must have read the whole response or call [`close()`](#http.client.HTTPConnection.close "http.client.HTTPConnection.close")
    if [`getresponse()`](#http.client.HTTPConnection.getresponse "http.client.HTTPConnection.getresponse") raised an non-[`ConnectionError`](exceptions.html#ConnectionError "ConnectionError") exception
    before you can send a new request to the server.

    Changed in version 3.2: *body* can now be an iterable.

    Changed in version 3.6: If neither Content-Length nor Transfer-Encoding are set in
    *headers*, file and iterable *body* objects are now chunk-encoded.
    The *encode\_chunked* argument was added.
    No attempt is made to determine the Content-Length for file
    objects.

HTTPConnection.getresponse()[¶](#http.client.HTTPConnection.getresponse "Link to this definition")
:   Should be called after a request is sent to get the response from the server.
    Returns an [`HTTPResponse`](#http.client.HTTPResponse "http.client.HTTPResponse") instance.

    Changed in version 3.5: If a [`ConnectionError`](exceptions.html#ConnectionError "ConnectionError") or subclass is raised, the
    [`HTTPConnection`](#http.client.HTTPConnection "http.client.HTTPConnection") object will be ready to reconnect when
    a new request is sent.

    Note that this does not apply to [`OSError`](exceptions.html#OSError "OSError")s raised by the underlying
    socket. Instead the caller is responsible to call [`close()`](#http.client.HTTPConnection.close "http.client.HTTPConnection.close") on the
    existing connection.

HTTPConnection.set\_debuglevel(*level*)[¶](#http.client.HTTPConnection.set_debuglevel "Link to this definition")
:   Set the debugging level. The default debug level is `0`, meaning no
    debugging output is printed. Any value greater than `0` will cause all
    currently defined debug output to be printed to stdout. The `debuglevel`
    is passed to any new [`HTTPResponse`](#http.client.HTTPResponse "http.client.HTTPResponse") objects that are created.

    Added in version 3.1.

HTTPConnection.set\_tunnel(*host*, *port=None*, *headers=None*)[¶](#http.client.HTTPConnection.set_tunnel "Link to this definition")
:   Set the host and the port for HTTP Connect Tunnelling. This allows running
    the connection through a proxy server.

    The *host* and *port* arguments specify the endpoint of the tunneled connection
    (i.e. the address included in the CONNECT request, *not* the address of the
    proxy server).

    The *headers* argument should be a mapping of extra HTTP headers to send with
    the CONNECT request.

    As HTTP/1.1 is used for HTTP CONNECT tunnelling request, [as per the RFC](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3.6), a HTTP `Host:`
    header must be provided, matching the authority-form of the request target
    provided as the destination for the CONNECT request. If a HTTP `Host:`
    header is not provided via the headers argument, one is generated and
    transmitted automatically.

    For example, to tunnel through a HTTPS proxy server running locally on port
    8080, we would pass the address of the proxy to the [`HTTPSConnection`](#http.client.HTTPSConnection "http.client.HTTPSConnection")
    constructor, and the address of the host that we eventually want to reach to
    the [`set_tunnel()`](#http.client.HTTPConnection.set_tunnel "http.client.HTTPConnection.set_tunnel") method:

    ```
    >>> import http.client
    >>> conn = http.client.HTTPSConnection("localhost", 8080)
    >>> conn.set_tunnel("www.python.org")
    >>> conn.request("HEAD","/index.html")
    ```

    Added in version 3.2.

    Changed in version 3.12: HTTP CONNECT tunnelling requests use protocol HTTP/1.1, upgraded from
    protocol HTTP/1.0. `Host:` HTTP headers are mandatory for HTTP/1.1, so
    one will be automatically generated and transmitted if not provided in
    the headers argument.

HTTPConnection.get\_proxy\_response\_headers()[¶](#http.client.HTTPConnection.get_proxy_response_headers "Link to this definition")
:   Returns a dictionary with the headers of the response received from
    the proxy server to the CONNECT request.

    If the CONNECT request was not sent, the method returns `None`.

    Added in version 3.12.

HTTPConnection.connect()[¶](#http.client.HTTPConnection.connect "Link to this definition")
:   Connect to the server specified when the object was created. By default,
    this is called automatically when making a request if the client does not
    already have a connection.

    Raises an [auditing event](sys.html#auditing) `http.client.connect` with arguments `self`, `host`, `port`.

HTTPConnection.close()[¶](#http.client.HTTPConnection.close "Link to this definition")
:   Close the connection to the server.

HTTPConnection.blocksize[¶](#http.client.HTTPConnection.blocksize "Link to this definition")
:   Buffer size in bytes for sending a file-like message body.

    Added in version 3.7.

As an alternative to using the [`request()`](#http.client.HTTPConnection.request "http.client.HTTPConnection.request") method described above, you can
also send your request step by step, by using the four functions below.

HTTPConnection.putrequest(*method*, *url*, *skip\_host=False*, *skip\_accept\_encoding=False*)[¶](#http.client.HTTPConnection.putrequest "Link to this definition")
:   This should be the first call after the connection to the server has been
    made. It sends a line to the server consisting of the *method* string,
    the *url* string, and the HTTP version (`HTTP/1.1`). To disable automatic
    sending of `Host:` or `Accept-Encoding:` headers (for example to accept
    additional content encodings), specify *skip\_host* or *skip\_accept\_encoding*
    with non-False values.

HTTPConnection.putheader(*header*, *argument*[, *...*])[¶](#http.client.HTTPConnection.putheader "Link to this definition")
:   Send an [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html)-style header to the server. It sends a line to the server
    consisting of the header, a colon and a space, and the first argument. If more
    arguments are given, continuation lines are sent, each consisting of a tab and
    an argument.

HTTPConnection.endheaders(*message\_body=None*, *\**, *encode\_chunked=False*)[¶](#http.client.HTTPConnection.endheaders "Link to this definition")
:   Send a blank line to the server, signalling the end of the headers. The
    optional *message\_body* argument can be used to pass a message body
    associated with the request.

    If *encode\_chunked* is `True`, the result of each iteration of
    *message\_body* will be chunk-encoded as specified in [**RFC 7230**](https://datatracker.ietf.org/doc/html/rfc7230.html),
    Section 3.3.1. How the data is encoded is dependent on the type of
    *message\_body*. If *message\_body* implements the [buffer interface](../c-api/buffer.html#bufferobjects) the encoding will result in a single chunk.
    If *message\_body* is a [`collections.abc.Iterable`](collections.abc.html#collections.abc.Iterable "collections.abc.Iterable"), each iteration
    of *message\_body* will result in a chunk. If *message\_body* is a
    [file object](../glossary.html#term-file-object), each call to `.read()` will result in a chunk.
    The method automatically signals the end of the chunk-encoded data
    immediately after *message\_body*.

    Note

    Due to the chunked encoding specification, empty chunks
    yielded by an iterator body will be ignored by the chunk-encoder.
    This is to avoid premature termination of the read of the request by
    the target server due to malformed encoding.

    Changed in version 3.6: Added chunked encoding support and the *encode\_chunked* parameter.

HTTPConnection.send(*data*)[¶](#http.client.HTTPConnection.send "Link to this definition")
:   Send data to the server. This should be used directly only after the
    [`endheaders()`](#http.client.HTTPConnection.endheaders "http.client.HTTPConnection.endheaders") method has been called and before [`getresponse()`](#http.client.HTTPConnection.getresponse "http.client.HTTPConnection.getresponse") is
    called.

    Raises an [auditing event](sys.html#auditing) `http.client.send` with arguments `self`, `data`.

## HTTPResponse Objects[¶](#httpresponse-objects "Link to this heading")

An [`HTTPResponse`](#http.client.HTTPResponse "http.client.HTTPResponse") instance wraps the HTTP response from the
server. It provides access to the request headers and the entity
body. The response is an iterable object and can be used in a with
statement.

Changed in version 3.5: The [`io.BufferedIOBase`](io.html#io.BufferedIOBase "io.BufferedIOBase") interface is now implemented and
all of its reader operations are supported.

HTTPResponse.read([*amt*])[¶](#http.client.HTTPResponse.read "Link to this definition")
:   Reads and returns the response body, or up to the next *amt* bytes.

HTTPResponse.readinto(*b*)[¶](#http.client.HTTPResponse.readinto "Link to this definition")
:   Reads up to the next len(b) bytes of the response body into the buffer *b*.
    Returns the number of bytes read.

    Added in version 3.3.

HTTPResponse.getheader(*name*, *default=None*)[¶](#http.client.HTTPResponse.getheader "Link to this definition")
:   Return the value of the header *name*, or *default* if there is no header
    matching *name*. If there is more than one header with the name *name*,
    return all of the values joined by ‘, ‘. If *default* is any iterable other
    than a single string, its elements are similarly returned joined by commas.

HTTPResponse.getheaders()[¶](#http.client.HTTPResponse.getheaders "Link to this definition")
:   Return a list of (header, value) tuples.

HTTPResponse.fileno()[¶](#http.client.HTTPResponse.fileno "Link to this definition")
:   Return the `fileno` of the underlying socket.

HTTPResponse.msg[¶](#http.client.HTTPResponse.msg "Link to this definition")
:   A [`http.client.HTTPMessage`](#http.client.HTTPMessage "http.client.HTTPMessage") instance containing the response
    headers. [`http.client.HTTPMessage`](#http.client.HTTPMessage "http.client.HTTPMessage") is a subclass of
    [`email.message.Message`](email.compat32-message.html#email.message.Message "email.message.Message").

HTTPResponse.version[¶](#http.client.HTTPResponse.version "Link to this definition")
:   HTTP protocol version used by server. 10 for HTTP/1.0, 11 for HTTP/1.1.

HTTPResponse.url[¶](#http.client.HTTPResponse.url "Link to this definition")
:   URL of the resource retrieved, commonly used to determine if a redirect was followed.

HTTPResponse.headers[¶](#http.client.HTTPResponse.headers "Link to this definition")
:   Headers of the response in the form of an [`email.message.EmailMessage`](email.message.html#email.message.EmailMessage "email.message.EmailMessage") instance.

HTTPResponse.status[¶](#http.client.HTTPResponse.status "Link to this definition")
:   Status code returned by server.

HTTPResponse.reason[¶](#http.client.HTTPResponse.reason "Link to this definition")
:   Reason phrase returned by server.

HTTPResponse.debuglevel[¶](#http.client.HTTPResponse.debuglevel "Link to this definition")
:   A debugging hook. If [`debuglevel`](#http.client.HTTPResponse.debuglevel "http.client.HTTPResponse.debuglevel") is greater than zero, messages
    will be printed to stdout as the response is read and parsed.

HTTPResponse.closed[¶](#http.client.HTTPResponse.closed "Link to this definition")
:   Is `True` if the stream is closed.

HTTPResponse.geturl()[¶](#http.client.HTTPResponse.geturl "Link to this definition")
:   Deprecated since version 3.9: Deprecated in favor of [`url`](#http.client.HTTPResponse.url "http.client.HTTPResponse.url").

HTTPResponse.info()[¶](#http.client.HTTPResponse.info "Link to this definition")
:   Deprecated since version 3.9: Deprecated in favor of [`headers`](#http.client.HTTPResponse.headers "http.client.HTTPResponse.headers").

HTTPResponse.getcode()[¶](#http.client.HTTPResponse.getcode "Link to this definition")
:   Deprecated since version 3.9: Deprecated in favor of [`status`](#http.client.HTTPResponse.status "http.client.HTTPResponse.status").

## Examples[¶](#examples "Link to this heading")

Here is an example session that uses the `GET` method:

```
>>> import http.client
>>> conn = http.client.HTTPSConnection("www.python.org")
>>> conn.request("GET", "/")
>>> r1 = conn.getresponse()
>>> print(r1.status, r1.reason)
200 OK
>>> data1 = r1.read()  # This will return entire content.
>>> # The following example demonstrates reading data in chunks.
>>> conn.request("GET", "/")
>>> r1 = conn.getresponse()
>>> while chunk := r1.read(200):
...     print(repr(chunk))
b'<!doctype html>\n<!--[if"...
...
>>> # Example of an invalid request
>>> conn = http.client.HTTPSConnection("docs.python.org")
>>> conn.request("GET", "/parrot.spam")
>>> r2 = conn.getresponse()
>>> print(r2.status, r2.reason)
404 Not Found
>>> data2 = r2.read()
>>> conn.close()
```

Here is an example session that uses the `HEAD` method. Note that the
`HEAD` method never returns any data.

```
>>> import http.client
>>> conn = http.client.HTTPSConnection("www.python.org")
>>> conn.request("HEAD", "/")
>>> res = conn.getresponse()
>>> print(res.status, res.reason)
200 OK
>>> data = res.read()
>>> print(len(data))
0
>>> data == b''
True
```

Here is an example session that uses the `POST` method:

```
>>> import http.client, urllib.parse
>>> params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
>>> headers = {"Content-type": "application/x-www-form-urlencoded",
...            "Accept": "text/plain"}
>>> conn = http.client.HTTPConnection("bugs.python.org")
>>> conn.request("POST", "", params, headers)
>>> response = conn.getresponse()
>>> print(response.status, response.reason)
302 Found
>>> data = response.read()
>>> data
b'Redirecting to <a href="https://bugs.python.org/issue12524">https://bugs.python.org/issue12524</a>'
>>> conn.close()
```

Client side HTTP `PUT` requests are very similar to `POST` requests. The
difference lies only on the server side where HTTP servers will allow resources to
be created via `PUT` requests. It should be noted that custom HTTP methods
are also handled in [`urllib.request.Request`](urllib.request.html#urllib.request.Request "urllib.request.Request") by setting the appropriate
method attribute. Here is an example session that uses the `PUT` method:

```
>>> # This creates an HTTP request
>>> # with the content of BODY as the enclosed representation
>>> # for the resource http://localhost:8080/file
...
>>> import http.client
>>> BODY = "***filecontents***"
>>> conn = http.client.HTTPConnection("localhost", 8080)
>>> conn.request("PUT", "/file", BODY)
>>> response = conn.getresponse()
>>> print(response.status, response.reason)
200, OK
```

## HTTPMessage Objects[¶](#httpmessage-objects "Link to this heading")

*class* http.client.HTTPMessage(*email.message.Message*)[¶](#http.client.HTTPMessage "Link to this definition")

An [`http.client.HTTPMessage`](#http.client.HTTPMessage "http.client.HTTPMessage") instance holds the headers from an HTTP
response. It is implemented using the [`email.message.Message`](email.compat32-message.html#email.message.Message "email.message.Message") class.

### [Table of Contents](../contents.html)

* [`http.client` — HTTP protocol client](#)
  + [HTTPConnection Objects](#httpconnection-objects)
  + [HTTPResponse Objects](#httpresponse-objects)
  + [Examples](#examples)
  + [HTTPMessage Objects](#httpmessage-objects)

#### Previous topic

[`http` — HTTP modules](http.html "previous chapter")

#### Next topic

[`ftplib` — FTP protocol client](ftplib.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/http.client.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](ftplib.html "ftplib — FTP protocol client") |
* [previous](http.html "http — HTTP modules") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `http.client` — HTTP protocol client
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