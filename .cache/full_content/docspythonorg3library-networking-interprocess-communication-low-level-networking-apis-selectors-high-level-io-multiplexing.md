### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](signal.html "signal — Set handlers for asynchronous events") |
* [previous](select.html "select — Waiting for I/O completion") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Networking and Interprocess Communication](ipc.html) »
* `selectors` — High-level I/O multiplexing
* |
* Theme
  Auto
  Light
  Dark
   |

# `selectors` — High-level I/O multiplexing[¶](#module-selectors "Link to this heading")

Added in version 3.4.

**Source code:** [Lib/selectors.py](https://github.com/python/cpython/tree/3.14/Lib/selectors.py)

---

## Introduction[¶](#introduction "Link to this heading")

This module allows high-level and efficient I/O multiplexing, built upon the
[`select`](select.html#module-select "select: Wait for I/O completion on multiple streams.") module primitives. Users are encouraged to use this module
instead, unless they want precise control over the OS-level primitives used.

It defines a [`BaseSelector`](#selectors.BaseSelector "selectors.BaseSelector") abstract base class, along with several
concrete implementations ([`KqueueSelector`](#selectors.KqueueSelector "selectors.KqueueSelector"), [`EpollSelector`](#selectors.EpollSelector "selectors.EpollSelector")…),
that can be used to wait for I/O readiness notification on multiple file
objects. In the following, “file object” refers to any object with a
[`fileno()`](io.html#io.IOBase.fileno "io.IOBase.fileno") method, or a raw file descriptor. See [file object](../glossary.html#term-file-object).

[`DefaultSelector`](#selectors.DefaultSelector "selectors.DefaultSelector") is an alias to the most efficient implementation
available on the current platform: this should be the default choice for most
users.

Note

The type of file objects supported depends on the platform: on Windows,
sockets are supported, but not pipes, whereas on Unix, both are supported
(some other types may be supported as well, such as fifos or special file
devices).

See also

[`select`](select.html#module-select "select: Wait for I/O completion on multiple streams.")
:   Low-level I/O multiplexing module.

[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

## Classes[¶](#classes "Link to this heading")

Classes hierarchy:

```
BaseSelector
+-- SelectSelector
+-- PollSelector
+-- EpollSelector
+-- DevpollSelector
+-- KqueueSelector
```

In the following, *events* is a bitwise mask indicating which I/O events should
be waited for on a given file object. It can be a combination of the module’s
constants below:

> | Constant | Meaning |
> | --- | --- |
> | selectors.EVENT\_READ[¶](#selectors.EVENT_READ "Link to this definition") | Available for read |
> | selectors.EVENT\_WRITE[¶](#selectors.EVENT_WRITE "Link to this definition") | Available for write |

*class* selectors.SelectorKey[¶](#selectors.SelectorKey "Link to this definition")
:   A [`SelectorKey`](#selectors.SelectorKey "selectors.SelectorKey") is a [`namedtuple`](collections.html#collections.namedtuple "collections.namedtuple") used to
    associate a file object to its underlying file descriptor, selected event
    mask and attached data. It is returned by several [`BaseSelector`](#selectors.BaseSelector "selectors.BaseSelector")
    methods.

    fileobj[¶](#selectors.SelectorKey.fileobj "Link to this definition")
    :   File object registered.

    fd[¶](#selectors.SelectorKey.fd "Link to this definition")
    :   Underlying file descriptor.

    events[¶](#selectors.SelectorKey.events "Link to this definition")
    :   Events that must be waited for on this file object.

    data[¶](#selectors.SelectorKey.data "Link to this definition")
    :   Optional opaque data associated to this file object: for example, this
        could be used to store a per-client session ID.

*class* selectors.BaseSelector[¶](#selectors.BaseSelector "Link to this definition")
:   A [`BaseSelector`](#selectors.BaseSelector "selectors.BaseSelector") is used to wait for I/O event readiness on multiple
    file objects. It supports file stream registration, unregistration, and a
    method to wait for I/O events on those streams, with an optional timeout.
    It’s an abstract base class, so cannot be instantiated. Use
    [`DefaultSelector`](#selectors.DefaultSelector "selectors.DefaultSelector") instead, or one of [`SelectSelector`](#selectors.SelectSelector "selectors.SelectSelector"),
    [`KqueueSelector`](#selectors.KqueueSelector "selectors.KqueueSelector") etc. if you want to specifically use an
    implementation, and your platform supports it.
    [`BaseSelector`](#selectors.BaseSelector "selectors.BaseSelector") and its concrete implementations support the
    [context manager](../glossary.html#term-context-manager) protocol.

    *abstractmethod* register(*fileobj*, *events*, *data=None*)[¶](#selectors.BaseSelector.register "Link to this definition")
    :   Register a file object for selection, monitoring it for I/O events.

        *fileobj* is the file object to monitor. It may either be an integer
        file descriptor or an object with a `fileno()` method.
        *events* is a bitwise mask of events to monitor.
        *data* is an opaque object.

        This returns a new [`SelectorKey`](#selectors.SelectorKey "selectors.SelectorKey") instance, or raises a
        [`ValueError`](exceptions.html#ValueError "ValueError") in case of invalid event mask or file descriptor, or
        [`KeyError`](exceptions.html#KeyError "KeyError") if the file object is already registered.

    *abstractmethod* unregister(*fileobj*)[¶](#selectors.BaseSelector.unregister "Link to this definition")
    :   Unregister a file object from selection, removing it from monitoring. A
        file object shall be unregistered prior to being closed.

        *fileobj* must be a file object previously registered.

        This returns the associated [`SelectorKey`](#selectors.SelectorKey "selectors.SelectorKey") instance, or raises a
        [`KeyError`](exceptions.html#KeyError "KeyError") if *fileobj* is not registered. It will raise
        [`ValueError`](exceptions.html#ValueError "ValueError") if *fileobj* is invalid (e.g. it has no `fileno()`
        method or its `fileno()` method has an invalid return value).

    modify(*fileobj*, *events*, *data=None*)[¶](#selectors.BaseSelector.modify "Link to this definition")
    :   Change a registered file object’s monitored events or attached data.

        This is equivalent to `BaseSelector.unregister(fileobj)` followed
        by `BaseSelector.register(fileobj, events, data)`, except that it
        can be implemented more efficiently.

        This returns a new [`SelectorKey`](#selectors.SelectorKey "selectors.SelectorKey") instance, or raises a
        [`ValueError`](exceptions.html#ValueError "ValueError") in case of invalid event mask or file descriptor, or
        [`KeyError`](exceptions.html#KeyError "KeyError") if the file object is not registered.

    *abstractmethod* select(*timeout=None*)[¶](#selectors.BaseSelector.select "Link to this definition")
    :   Wait until some registered file objects become ready, or the timeout
        expires.

        If `timeout > 0`, this specifies the maximum wait time, in seconds.
        If `timeout <= 0`, the call won’t block, and will report the currently
        ready file objects.
        If *timeout* is `None`, the call will block until a monitored file object
        becomes ready.

        This returns a list of `(key, events)` tuples, one for each ready file
        object.

        *key* is the [`SelectorKey`](#selectors.SelectorKey "selectors.SelectorKey") instance corresponding to a ready file
        object.
        *events* is a bitmask of events ready on this file object.

        Note

        This method can return before any file object becomes ready or the
        timeout has elapsed if the current process receives a signal: in this
        case, an empty list will be returned.

        Changed in version 3.5: The selector is now retried with a recomputed timeout when interrupted
        by a signal if the signal handler did not raise an exception (see
        [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale), instead of returning an empty list
        of events before the timeout.

    close()[¶](#selectors.BaseSelector.close "Link to this definition")
    :   Close the selector.

        This must be called to make sure that any underlying resource is freed.
        The selector shall not be used once it has been closed.

    get\_key(*fileobj*)[¶](#selectors.BaseSelector.get_key "Link to this definition")
    :   Return the key associated with a registered file object.

        This returns the [`SelectorKey`](#selectors.SelectorKey "selectors.SelectorKey") instance associated to this file
        object, or raises [`KeyError`](exceptions.html#KeyError "KeyError") if the file object is not registered.

    *abstractmethod* get\_map()[¶](#selectors.BaseSelector.get_map "Link to this definition")
    :   Return a mapping of file objects to selector keys.

        This returns a [`Mapping`](collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") instance mapping
        registered file objects to their associated [`SelectorKey`](#selectors.SelectorKey "selectors.SelectorKey")
        instance.

*class* selectors.DefaultSelector[¶](#selectors.DefaultSelector "Link to this definition")
:   The default selector class, using the most efficient implementation
    available on the current platform. This should be the default choice for
    most users.

*class* selectors.SelectSelector[¶](#selectors.SelectSelector "Link to this definition")
:   [`select.select()`](select.html#select.select "select.select")-based selector.

*class* selectors.PollSelector[¶](#selectors.PollSelector "Link to this definition")
:   [`select.poll()`](select.html#select.poll "select.poll")-based selector.

*class* selectors.EpollSelector[¶](#selectors.EpollSelector "Link to this definition")
:   [`select.epoll()`](select.html#select.epoll "select.epoll")-based selector.

    fileno()[¶](#selectors.EpollSelector.fileno "Link to this definition")
    :   This returns the file descriptor used by the underlying
        [`select.epoll()`](select.html#select.epoll "select.epoll") object.

*class* selectors.DevpollSelector[¶](#selectors.DevpollSelector "Link to this definition")
:   [`select.devpoll()`](select.html#select.devpoll "select.devpoll")-based selector.

    fileno()[¶](#selectors.DevpollSelector.fileno "Link to this definition")
    :   This returns the file descriptor used by the underlying
        [`select.devpoll()`](select.html#select.devpoll "select.devpoll") object.

    Added in version 3.5.

*class* selectors.KqueueSelector[¶](#selectors.KqueueSelector "Link to this definition")
:   [`select.kqueue()`](select.html#select.kqueue "select.kqueue")-based selector.

    fileno()[¶](#selectors.KqueueSelector.fileno "Link to this definition")
    :   This returns the file descriptor used by the underlying
        [`select.kqueue()`](select.html#select.kqueue "select.kqueue") object.

## Examples[¶](#examples "Link to this heading")

Here is a simple echo server implementation:

```
import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
```

### [Table of Contents](../contents.html)

* [`selectors` — High-level I/O multiplexing](#)
  + [Introduction](#introduction)
  + [Classes](#classes)
  + [Examples](#examples)

#### Previous topic

[`select` — Waiting for I/O completion](select.html "previous chapter")

#### Next topic

[`signal` — Set handlers for asynchronous events](signal.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/selectors.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](signal.html "signal — Set handlers for asynchronous events") |
* [previous](select.html "select — Waiting for I/O completion") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Networking and Interprocess Communication](ipc.html) »
* `selectors` — High-level I/O multiplexing
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