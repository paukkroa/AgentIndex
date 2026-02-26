### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](http.server.html "http.server — HTTP servers") |
* [previous](uuid.html "uuid — UUID objects according to RFC 9562") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `socketserver` — A framework for network servers
* |
* Theme
  Auto
  Light
  Dark
   |

# `socketserver` — A framework for network servers[¶](#module-socketserver "Link to this heading")

**Source code:** [Lib/socketserver.py](https://github.com/python/cpython/tree/3.14/Lib/socketserver.py)

---

The `socketserver` module simplifies the task of writing network servers.

[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

There are four basic concrete server classes:

*class* socketserver.TCPServer(*server\_address*, *RequestHandlerClass*, *bind\_and\_activate=True*)[¶](#socketserver.TCPServer "Link to this definition")
:   This uses the internet TCP protocol, which provides for
    continuous streams of data between the client and server.
    If *bind\_and\_activate* is true, the constructor automatically attempts to
    invoke [`server_bind()`](#socketserver.BaseServer.server_bind "socketserver.BaseServer.server_bind") and
    [`server_activate()`](#socketserver.BaseServer.server_activate "socketserver.BaseServer.server_activate"). The other parameters are passed to
    the [`BaseServer`](#socketserver.BaseServer "socketserver.BaseServer") base class.

*class* socketserver.UDPServer(*server\_address*, *RequestHandlerClass*, *bind\_and\_activate=True*)[¶](#socketserver.UDPServer "Link to this definition")
:   This uses datagrams, which are discrete packets of information that may
    arrive out of order or be lost while in transit. The parameters are
    the same as for [`TCPServer`](#socketserver.TCPServer "socketserver.TCPServer").

*class* socketserver.UnixStreamServer(*server\_address*, *RequestHandlerClass*, *bind\_and\_activate=True*)[¶](#socketserver.UnixStreamServer "Link to this definition")

*class* socketserver.UnixDatagramServer(*server\_address*, *RequestHandlerClass*, *bind\_and\_activate=True*)[¶](#socketserver.UnixDatagramServer "Link to this definition")
:   These more infrequently used classes are similar to the TCP and
    UDP classes, but use Unix domain sockets; they’re not available on
    non-Unix platforms. The parameters are the same as for
    [`TCPServer`](#socketserver.TCPServer "socketserver.TCPServer").

These four classes process requests *synchronously*; each request must be
completed before the next request can be started. This isn’t suitable if each
request takes a long time to complete, because it requires a lot of computation,
or because it returns a lot of data which the client is slow to process. The
solution is to create a separate process or thread to handle each request; the
[`ForkingMixIn`](#socketserver.ForkingMixIn "socketserver.ForkingMixIn") and [`ThreadingMixIn`](#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn") mix-in classes can be used to
support asynchronous behaviour.

Creating a server requires several steps. First, you must create a request
handler class by subclassing the [`BaseRequestHandler`](#socketserver.BaseRequestHandler "socketserver.BaseRequestHandler") class and
overriding its [`handle()`](#socketserver.BaseRequestHandler.handle "socketserver.BaseRequestHandler.handle") method;
this method will process incoming
requests. Second, you must instantiate one of the server classes, passing it
the server’s address and the request handler class. It is recommended to use
the server in a [`with`](../reference/compound_stmts.html#with) statement. Then call the
[`handle_request()`](#socketserver.BaseServer.handle_request "socketserver.BaseServer.handle_request") or
[`serve_forever()`](#socketserver.BaseServer.serve_forever "socketserver.BaseServer.serve_forever") method of the server object to
process one or many requests. Finally, call [`server_close()`](#socketserver.BaseServer.server_close "socketserver.BaseServer.server_close")
to close the socket (unless you used a `with` statement).

When inheriting from [`ThreadingMixIn`](#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn") for threaded connection behavior,
you should explicitly declare how you want your threads to behave on an abrupt
shutdown. The [`ThreadingMixIn`](#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn") class defines an attribute
*daemon\_threads*, which indicates whether or not the server should wait for
thread termination. You should set the flag explicitly if you would like
threads to behave autonomously; the default is [`False`](constants.html#False "False"), meaning that
Python will not exit until all threads created by [`ThreadingMixIn`](#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn") have
exited.

Server classes have the same external methods and attributes, no matter what
network protocol they use.

## Server Creation Notes[¶](#server-creation-notes "Link to this heading")

There are five classes in an inheritance diagram, four of which represent
synchronous servers of four types:

```
+------------+
| BaseServer |
+------------+
      |
      v
+-----------+        +------------------+
| TCPServer |------->| UnixStreamServer |
+-----------+        +------------------+
      |
      v
+-----------+        +--------------------+
| UDPServer |------->| UnixDatagramServer |
+-----------+        +--------------------+
```

Note that [`UnixDatagramServer`](#socketserver.UnixDatagramServer "socketserver.UnixDatagramServer") derives from [`UDPServer`](#socketserver.UDPServer "socketserver.UDPServer"), not from
[`UnixStreamServer`](#socketserver.UnixStreamServer "socketserver.UnixStreamServer") — the only difference between an IP and a Unix
server is the address family.

*class* socketserver.ForkingMixIn[¶](#socketserver.ForkingMixIn "Link to this definition")

*class* socketserver.ThreadingMixIn[¶](#socketserver.ThreadingMixIn "Link to this definition")
:   Forking and threading versions of each type of server can be created
    using these mix-in classes. For instance, [`ThreadingUDPServer`](#socketserver.ThreadingUDPServer "socketserver.ThreadingUDPServer")
    is created as follows:

    ```
    class ThreadingUDPServer(ThreadingMixIn, UDPServer):
        pass
    ```

    The mix-in class comes first, since it overrides a method defined in
    [`UDPServer`](#socketserver.UDPServer "socketserver.UDPServer"). Setting the various attributes also changes the
    behavior of the underlying server mechanism.

    [`ForkingMixIn`](#socketserver.ForkingMixIn "socketserver.ForkingMixIn") and the Forking classes mentioned below are
    only available on POSIX platforms that support [`fork()`](os.html#os.fork "os.fork").

    block\_on\_close[¶](#socketserver.ThreadingMixIn.block_on_close "Link to this definition")
    :   [`ForkingMixIn.server_close`](#socketserver.BaseServer.server_close "socketserver.BaseServer.server_close")
        waits until all child processes complete, except if
        [`block_on_close`](#socketserver.ThreadingMixIn.block_on_close "socketserver.ThreadingMixIn.block_on_close") attribute is `False`.

        [`ThreadingMixIn.server_close`](#socketserver.BaseServer.server_close "socketserver.BaseServer.server_close")
        waits until all non-daemon threads complete, except if
        [`block_on_close`](#socketserver.ThreadingMixIn.block_on_close "socketserver.ThreadingMixIn.block_on_close") attribute is `False`.

    max\_children[¶](#socketserver.ThreadingMixIn.max_children "Link to this definition")
    :   Specify how many child processes will exist to handle requests at a time
        for [`ForkingMixIn`](#socketserver.ForkingMixIn "socketserver.ForkingMixIn"). If the limit is reached,
        new requests will wait until one child process has finished.

    daemon\_threads[¶](#socketserver.ThreadingMixIn.daemon_threads "Link to this definition")
    :   For [`ThreadingMixIn`](#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn") use daemonic threads by setting
        [`ThreadingMixIn.daemon_threads`](#socketserver.ThreadingMixIn.daemon_threads "socketserver.ThreadingMixIn.daemon_threads")
        to `True` to not wait until threads complete.

    Changed in version 3.7: [`ForkingMixIn.server_close`](#socketserver.BaseServer.server_close "socketserver.BaseServer.server_close") and
    [`ThreadingMixIn.server_close`](#socketserver.BaseServer.server_close "socketserver.BaseServer.server_close") now waits until all
    child processes and non-daemonic threads complete.
    Add a new [`ForkingMixIn.block_on_close`](#socketserver.ThreadingMixIn.block_on_close "socketserver.ThreadingMixIn.block_on_close") class
    attribute to opt-in for the pre-3.7 behaviour.

*class* socketserver.ForkingTCPServer[¶](#socketserver.ForkingTCPServer "Link to this definition")

*class* socketserver.ForkingUDPServer[¶](#socketserver.ForkingUDPServer "Link to this definition")

*class* socketserver.ThreadingTCPServer[¶](#socketserver.ThreadingTCPServer "Link to this definition")

*class* socketserver.ThreadingUDPServer[¶](#socketserver.ThreadingUDPServer "Link to this definition")

*class* socketserver.ForkingUnixStreamServer[¶](#socketserver.ForkingUnixStreamServer "Link to this definition")

*class* socketserver.ForkingUnixDatagramServer[¶](#socketserver.ForkingUnixDatagramServer "Link to this definition")

*class* socketserver.ThreadingUnixStreamServer[¶](#socketserver.ThreadingUnixStreamServer "Link to this definition")

*class* socketserver.ThreadingUnixDatagramServer[¶](#socketserver.ThreadingUnixDatagramServer "Link to this definition")
:   These classes are pre-defined using the mix-in classes.

Added in version 3.12: The `ForkingUnixStreamServer` and `ForkingUnixDatagramServer` classes
were added.

To implement a service, you must derive a class from [`BaseRequestHandler`](#socketserver.BaseRequestHandler "socketserver.BaseRequestHandler")
and redefine its [`handle()`](#socketserver.BaseRequestHandler.handle "socketserver.BaseRequestHandler.handle") method.
You can then run various versions of
the service by combining one of the server classes with your request handler
class. The request handler class must be different for datagram or stream
services. This can be hidden by using the handler subclasses
[`StreamRequestHandler`](#socketserver.StreamRequestHandler "socketserver.StreamRequestHandler") or [`DatagramRequestHandler`](#socketserver.DatagramRequestHandler "socketserver.DatagramRequestHandler").

Of course, you still have to use your head! For instance, it makes no sense to
use a forking server if the service contains state in memory that can be
modified by different requests, since the modifications in the child process
would never reach the initial state kept in the parent process and passed to
each child. In this case, you can use a threading server, but you will probably
have to use locks to protect the integrity of the shared data.

On the other hand, if you are building an HTTP server where all data is stored
externally (for instance, in the file system), a synchronous class will
essentially render the service “deaf” while one request is being handled –
which may be for a very long time if a client is slow to receive all the data it
has requested. Here a threading or forking server is appropriate.

In some cases, it may be appropriate to process part of a request synchronously,
but to finish processing in a forked child depending on the request data. This
can be implemented by using a synchronous server and doing an explicit fork in
the request handler class [`handle()`](#socketserver.BaseRequestHandler.handle "socketserver.BaseRequestHandler.handle") method.

Another approach to handling multiple simultaneous requests in an environment
that supports neither threads nor [`fork()`](os.html#os.fork "os.fork") (or where these are too
expensive or inappropriate for the service) is to maintain an explicit table of
partially finished requests and to use [`selectors`](selectors.html#module-selectors "selectors: High-level I/O multiplexing.") to decide which
request to work on next (or whether to handle a new incoming request). This is
particularly important for stream services where each client can potentially be
connected for a long time (if threads or subprocesses cannot be used).

## Server Objects[¶](#server-objects "Link to this heading")

*class* socketserver.BaseServer(*server\_address*, *RequestHandlerClass*)[¶](#socketserver.BaseServer "Link to this definition")
:   This is the superclass of all Server objects in the module. It defines the
    interface, given below, but does not implement most of the methods, which is
    done in subclasses. The two parameters are stored in the respective
    [`server_address`](#socketserver.BaseServer.server_address "socketserver.BaseServer.server_address") and [`RequestHandlerClass`](#socketserver.BaseServer.RequestHandlerClass "socketserver.BaseServer.RequestHandlerClass") attributes.

    fileno()[¶](#socketserver.BaseServer.fileno "Link to this definition")
    :   Return an integer file descriptor for the socket on which the server is
        listening. This function is most commonly passed to [`selectors`](selectors.html#module-selectors "selectors: High-level I/O multiplexing."), to
        allow monitoring multiple servers in the same process.

    handle\_request()[¶](#socketserver.BaseServer.handle_request "Link to this definition")
    :   Process a single request. This function calls the following methods in
        order: [`get_request()`](#socketserver.BaseServer.get_request "socketserver.BaseServer.get_request"), [`verify_request()`](#socketserver.BaseServer.verify_request "socketserver.BaseServer.verify_request"), and
        [`process_request()`](#socketserver.BaseServer.process_request "socketserver.BaseServer.process_request"). If the user-provided
        [`handle()`](#socketserver.BaseRequestHandler.handle "socketserver.BaseRequestHandler.handle") method of the
        handler class raises an exception, the server’s [`handle_error()`](#socketserver.BaseServer.handle_error "socketserver.BaseServer.handle_error") method
        will be called. If no request is received within [`timeout`](#socketserver.BaseServer.timeout "socketserver.BaseServer.timeout")
        seconds, [`handle_timeout()`](#socketserver.BaseServer.handle_timeout "socketserver.BaseServer.handle_timeout") will be called and [`handle_request()`](#socketserver.BaseServer.handle_request "socketserver.BaseServer.handle_request")
        will return.

    serve\_forever(*poll\_interval=0.5*)[¶](#socketserver.BaseServer.serve_forever "Link to this definition")
    :   Handle requests until an explicit [`shutdown()`](#socketserver.BaseServer.shutdown "socketserver.BaseServer.shutdown") request. Poll for
        shutdown every *poll\_interval* seconds.
        Ignores the [`timeout`](#socketserver.BaseServer.timeout "socketserver.BaseServer.timeout") attribute. It
        also calls [`service_actions()`](#socketserver.BaseServer.service_actions "socketserver.BaseServer.service_actions"), which may be used by a subclass or mixin
        to provide actions specific to a given service. For example, the
        [`ForkingMixIn`](#socketserver.ForkingMixIn "socketserver.ForkingMixIn") class uses [`service_actions()`](#socketserver.BaseServer.service_actions "socketserver.BaseServer.service_actions") to clean up zombie
        child processes.

        Changed in version 3.3: Added `service_actions` call to the `serve_forever` method.

    service\_actions()[¶](#socketserver.BaseServer.service_actions "Link to this definition")
    :   This is called in the [`serve_forever()`](#socketserver.BaseServer.serve_forever "socketserver.BaseServer.serve_forever") loop. This method can be
        overridden by subclasses or mixin classes to perform actions specific to
        a given service, such as cleanup actions.

        Added in version 3.3.

    shutdown()[¶](#socketserver.BaseServer.shutdown "Link to this definition")
    :   Tell the [`serve_forever()`](#socketserver.BaseServer.serve_forever "socketserver.BaseServer.serve_forever") loop to stop and wait until it does.
        [`shutdown()`](#socketserver.BaseServer.shutdown "socketserver.BaseServer.shutdown") must be called while [`serve_forever()`](#socketserver.BaseServer.serve_forever "socketserver.BaseServer.serve_forever") is running in a
        different thread otherwise it will deadlock.

    server\_close()[¶](#socketserver.BaseServer.server_close "Link to this definition")
    :   Clean up the server. May be overridden.

    address\_family[¶](#socketserver.BaseServer.address_family "Link to this definition")
    :   The family of protocols to which the server’s socket belongs. Common
        examples are [`socket.AF_INET`](socket.html#socket.AF_INET "socket.AF_INET"), [`socket.AF_INET6`](socket.html#socket.AF_INET6 "socket.AF_INET6"), and
        [`socket.AF_UNIX`](socket.html#socket.AF_UNIX "socket.AF_UNIX"). Subclass the TCP or UDP server classes in this
        module with class attribute `address_family = AF_INET6` set if you
        want IPv6 server classes.

    RequestHandlerClass[¶](#socketserver.BaseServer.RequestHandlerClass "Link to this definition")
    :   The user-provided request handler class; an instance of this class is created
        for each request.

    server\_address[¶](#socketserver.BaseServer.server_address "Link to this definition")
    :   The address on which the server is listening. The format of addresses varies
        depending on the protocol family;
        see the documentation for the [`socket`](socket.html#module-socket "socket: Low-level networking interface.") module
        for details. For internet protocols, this is a tuple containing a string giving
        the address, and an integer port number: `('127.0.0.1', 80)`, for example.

    socket[¶](#socketserver.BaseServer.socket "Link to this definition")
    :   The socket object on which the server will listen for incoming requests.

    The server classes support the following class variables:

    allow\_reuse\_address[¶](#socketserver.BaseServer.allow_reuse_address "Link to this definition")
    :   Whether the server will allow the reuse of an address. This defaults to
        [`False`](constants.html#False "False"), and can be set in subclasses to change the policy.

    request\_queue\_size[¶](#socketserver.BaseServer.request_queue_size "Link to this definition")
    :   The size of the request queue. If it takes a long time to process a single
        request, any requests that arrive while the server is busy are placed into a
        queue, up to [`request_queue_size`](#socketserver.BaseServer.request_queue_size "socketserver.BaseServer.request_queue_size") requests. Once the queue is full,
        further requests from clients will get a “Connection denied” error. The default
        value is usually 5, but this can be overridden by subclasses.

    socket\_type[¶](#socketserver.BaseServer.socket_type "Link to this definition")
    :   The type of socket used by the server; [`socket.SOCK_STREAM`](socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM") and
        [`socket.SOCK_DGRAM`](socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM") are two common values.

    timeout[¶](#socketserver.BaseServer.timeout "Link to this definition")
    :   Timeout duration, measured in seconds, or [`None`](constants.html#None "None") if no timeout is
        desired. If [`handle_request()`](#socketserver.BaseServer.handle_request "socketserver.BaseServer.handle_request") receives no incoming requests within the
        timeout period, the [`handle_timeout()`](#socketserver.BaseServer.handle_timeout "socketserver.BaseServer.handle_timeout") method is called.

    There are various server methods that can be overridden by subclasses of base
    server classes like [`TCPServer`](#socketserver.TCPServer "socketserver.TCPServer"); these methods aren’t useful to external
    users of the server object.

    finish\_request(*request*, *client\_address*)[¶](#socketserver.BaseServer.finish_request "Link to this definition")
    :   Actually processes the request by instantiating [`RequestHandlerClass`](#socketserver.BaseServer.RequestHandlerClass "socketserver.BaseServer.RequestHandlerClass") and
        calling its [`handle()`](#socketserver.BaseRequestHandler.handle "socketserver.BaseRequestHandler.handle") method.

    get\_request()[¶](#socketserver.BaseServer.get_request "Link to this definition")
    :   Must accept a request from the socket, and return a 2-tuple containing the *new*
        socket object to be used to communicate with the client, and the client’s
        address.

    handle\_error(*request*, *client\_address*)[¶](#socketserver.BaseServer.handle_error "Link to this definition")
    :   This function is called if the [`handle()`](#socketserver.BaseRequestHandler.handle "socketserver.BaseRequestHandler.handle")
        method of a [`RequestHandlerClass`](#socketserver.BaseServer.RequestHandlerClass "socketserver.BaseServer.RequestHandlerClass") instance raises
        an exception. The default action is to print the traceback to
        standard error and continue handling further requests.

        Changed in version 3.6: Now only called for exceptions derived from the [`Exception`](exceptions.html#Exception "Exception")
        class.

    handle\_timeout()[¶](#socketserver.BaseServer.handle_timeout "Link to this definition")
    :   This function is called when the [`timeout`](#socketserver.BaseServer.timeout "socketserver.BaseServer.timeout") attribute has been set to a
        value other than [`None`](constants.html#None "None") and the timeout period has passed with no
        requests being received. The default action for forking servers is
        to collect the status of any child processes that have exited, while
        in threading servers this method does nothing.

    process\_request(*request*, *client\_address*)[¶](#socketserver.BaseServer.process_request "Link to this definition")
    :   Calls [`finish_request()`](#socketserver.BaseServer.finish_request "socketserver.BaseServer.finish_request") to create an instance of the
        [`RequestHandlerClass`](#socketserver.BaseServer.RequestHandlerClass "socketserver.BaseServer.RequestHandlerClass"). If desired, this function can create a new process
        or thread to handle the request; the [`ForkingMixIn`](#socketserver.ForkingMixIn "socketserver.ForkingMixIn") and
        [`ThreadingMixIn`](#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn") classes do this.

    server\_activate()[¶](#socketserver.BaseServer.server_activate "Link to this definition")
    :   Called by the server’s constructor to activate the server. The default behavior
        for a TCP server just invokes [`listen()`](socket.html#socket.socket.listen "socket.socket.listen")
        on the server’s socket. May be overridden.

    server\_bind()[¶](#socketserver.BaseServer.server_bind "Link to this definition")
    :   Called by the server’s constructor to bind the socket to the desired address.
        May be overridden.

    verify\_request(*request*, *client\_address*)[¶](#socketserver.BaseServer.verify_request "Link to this definition")
    :   Must return a Boolean value; if the value is [`True`](constants.html#True "True"), the request will
        be processed, and if it’s [`False`](constants.html#False "False"), the request will be denied. This
        function can be overridden to implement access controls for a server. The
        default implementation always returns [`True`](constants.html#True "True").

    Changed in version 3.6: Support for the [context manager](../glossary.html#term-context-manager) protocol was added. Exiting the
    context manager is equivalent to calling [`server_close()`](#socketserver.BaseServer.server_close "socketserver.BaseServer.server_close").

## Request Handler Objects[¶](#request-handler-objects "Link to this heading")

*class* socketserver.BaseRequestHandler[¶](#socketserver.BaseRequestHandler "Link to this definition")
:   This is the superclass of all request handler objects. It defines
    the interface, given below. A concrete request handler subclass must
    define a new [`handle()`](#socketserver.BaseRequestHandler.handle "socketserver.BaseRequestHandler.handle") method, and can override any of
    the other methods. A new instance of the subclass is created for each
    request.

    setup()[¶](#socketserver.BaseRequestHandler.setup "Link to this definition")
    :   Called before the [`handle()`](#socketserver.BaseRequestHandler.handle "socketserver.BaseRequestHandler.handle") method to perform any initialization actions
        required. The default implementation does nothing.

    handle()[¶](#socketserver.BaseRequestHandler.handle "Link to this definition")
    :   This function must do all the work required to service a request. The
        default implementation does nothing. Several instance attributes are
        available to it; the request is available as [`request`](#socketserver.BaseRequestHandler.request "socketserver.BaseRequestHandler.request"); the client
        address as [`client_address`](#socketserver.BaseRequestHandler.client_address "socketserver.BaseRequestHandler.client_address"); and the server instance as
        [`server`](#socketserver.BaseRequestHandler.server "socketserver.BaseRequestHandler.server"), in case it needs access to per-server information.

        The type of [`request`](#socketserver.BaseRequestHandler.request "socketserver.BaseRequestHandler.request") is different for datagram or stream
        services. For stream services, [`request`](#socketserver.BaseRequestHandler.request "socketserver.BaseRequestHandler.request") is a socket object; for
        datagram services, [`request`](#socketserver.BaseRequestHandler.request "socketserver.BaseRequestHandler.request") is a pair of string and socket.

    finish()[¶](#socketserver.BaseRequestHandler.finish "Link to this definition")
    :   Called after the [`handle()`](#socketserver.BaseRequestHandler.handle "socketserver.BaseRequestHandler.handle") method to perform any clean-up actions
        required. The default implementation does nothing. If [`setup()`](#socketserver.BaseRequestHandler.setup "socketserver.BaseRequestHandler.setup")
        raises an exception, this function will not be called.

    request[¶](#socketserver.BaseRequestHandler.request "Link to this definition")
    :   The *new* [`socket.socket`](socket.html#socket.socket "socket.socket") object
        to be used to communicate with the client.

    client\_address[¶](#socketserver.BaseRequestHandler.client_address "Link to this definition")
    :   Client address returned by [`BaseServer.get_request()`](#socketserver.BaseServer.get_request "socketserver.BaseServer.get_request").

    server[¶](#socketserver.BaseRequestHandler.server "Link to this definition")
    :   [`BaseServer`](#socketserver.BaseServer "socketserver.BaseServer") object used for handling the request.

*class* socketserver.StreamRequestHandler[¶](#socketserver.StreamRequestHandler "Link to this definition")

*class* socketserver.DatagramRequestHandler[¶](#socketserver.DatagramRequestHandler "Link to this definition")
:   These [`BaseRequestHandler`](#socketserver.BaseRequestHandler "socketserver.BaseRequestHandler") subclasses override the
    [`setup()`](#socketserver.BaseRequestHandler.setup "socketserver.BaseRequestHandler.setup") and [`finish()`](#socketserver.BaseRequestHandler.finish "socketserver.BaseRequestHandler.finish")
    methods, and provide [`rfile`](#socketserver.DatagramRequestHandler.rfile "socketserver.DatagramRequestHandler.rfile") and [`wfile`](#socketserver.DatagramRequestHandler.wfile "socketserver.DatagramRequestHandler.wfile") attributes.

    rfile[¶](#socketserver.DatagramRequestHandler.rfile "Link to this definition")
    :   A file object from which receives the request is read.
        Support the [`io.BufferedIOBase`](io.html#io.BufferedIOBase "io.BufferedIOBase") readable interface.

    wfile[¶](#socketserver.DatagramRequestHandler.wfile "Link to this definition")
    :   A file object to which the reply is written.
        Support the [`io.BufferedIOBase`](io.html#io.BufferedIOBase "io.BufferedIOBase") writable interface

    Changed in version 3.6: [`wfile`](#socketserver.DatagramRequestHandler.wfile "socketserver.DatagramRequestHandler.wfile") also supports the
    [`io.BufferedIOBase`](io.html#io.BufferedIOBase "io.BufferedIOBase") writable interface.

## Examples[¶](#examples "Link to this heading")

### [`socketserver.TCPServer`](#socketserver.TCPServer "socketserver.TCPServer") Example[¶](#socketserver-tcpserver-example "Link to this heading")

This is the server side:

```
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        pieces = [b'']
        total = 0
        while b'\n' not in pieces[-1] and total < 10_000:
            pieces.append(self.request.recv(2000))
            total += len(pieces[-1])
        self.data = b''.join(pieces)
        print(f"Received from {self.client_address[0]}:")
        print(self.data.decode("utf-8"))
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
        # after we return, the socket will be closed.

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
```

An alternative request handler class that makes use of streams (file-like
objects that simplify communication by providing the standard file interface):

```
class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler.
        # We can now use e.g. readline() instead of raw recv() calls.
        # We limit ourselves to 10000 bytes to avoid abuse by the sender.
        self.data = self.rfile.readline(10000).rstrip()
        print(f"{self.client_address[0]} wrote:")
        print(self.data.decode("utf-8"))
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(self.data.upper())
```

The difference is that the `readline()` call in the second handler will call
`recv()` multiple times until it encounters a newline character, while the
first handler had to use a `recv()` loop to accumulate data until a
newline itself. If it had just used a single `recv()` without the loop it
would just have returned what has been received so far from the client.
TCP is stream based: data arrives in the order it was sent, but there is no
correlation between client `send()` or `sendall()` calls and the number
of `recv()` calls on the server required to receive it.

This is the client side:

```
import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data, "utf-8"))
    sock.sendall(b"\n")

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("Sent:    ", data)
print("Received:", received)
```

The output of the example should look something like this:

Server:

```
$ python TCPServer.py
127.0.0.1 wrote:
b'hello world with TCP'
127.0.0.1 wrote:
b'python is nice'
```

Client:

```
$ python TCPClient.py hello world with TCP
Sent:     hello world with TCP
Received: HELLO WORLD WITH TCP
$ python TCPClient.py python is nice
Sent:     python is nice
Received: PYTHON IS NICE
```

### [`socketserver.UDPServer`](#socketserver.UDPServer "socketserver.UDPServer") Example[¶](#socketserver-udpserver-example "Link to this heading")

This is the server side:

```
import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print(f"{self.client_address[0]} wrote:")
        print(data)
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
```

This is the client side:

```
import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
received = str(sock.recv(1024), "utf-8")

print("Sent:    ", data)
print("Received:", received)
```

The output of the example should look exactly like for the TCP server example.

### Asynchronous Mixins[¶](#asynchronous-mixins "Link to this heading")

To build asynchronous handlers, use the [`ThreadingMixIn`](#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn") and
[`ForkingMixIn`](#socketserver.ForkingMixIn "socketserver.ForkingMixIn") classes.

An example for the [`ThreadingMixIn`](#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn") class:

```
import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)

        client(ip, port, "Hello World 1")
        client(ip, port, "Hello World 2")
        client(ip, port, "Hello World 3")

        server.shutdown()
```

The output of the example should look something like this:

```
$ python ThreadedTCPServer.py
Server loop running in thread: Thread-1
Received: Thread-2: Hello World 1
Received: Thread-3: Hello World 2
Received: Thread-4: Hello World 3
```

The [`ForkingMixIn`](#socketserver.ForkingMixIn "socketserver.ForkingMixIn") class is used in the same way, except that the server
will spawn a new process for each request.
Available only on POSIX platforms that support [`fork()`](os.html#os.fork "os.fork").

### [Table of Contents](../contents.html)

* [`socketserver` — A framework for network servers](#)
  + [Server Creation Notes](#server-creation-notes)
  + [Server Objects](#server-objects)
  + [Request Handler Objects](#request-handler-objects)
  + [Examples](#examples)
    - [`socketserver.TCPServer` Example](#socketserver-tcpserver-example)
    - [`socketserver.UDPServer` Example](#socketserver-udpserver-example)
    - [Asynchronous Mixins](#asynchronous-mixins)

#### Previous topic

[`uuid` — UUID objects according to **RFC 9562**](uuid.html "previous chapter")

#### Next topic

[`http.server` — HTTP servers](http.server.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/socketserver.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](http.server.html "http.server — HTTP servers") |
* [previous](uuid.html "uuid — UUID objects according to RFC 9562") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `socketserver` — A framework for network servers
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