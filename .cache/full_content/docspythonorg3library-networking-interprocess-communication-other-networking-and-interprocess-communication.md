### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](asyncio.html "asyncio — Asynchronous I/O") |
* [previous](_thread.html "_thread — Low-level threading API") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Networking and Interprocess Communication
* |
* Theme
  Auto
  Light
  Dark
   |

# Networking and Interprocess Communication[¶](#networking-and-interprocess-communication "Link to this heading")

The modules described in this chapter provide mechanisms for
networking and inter-processes communication.

Some modules only work for two processes that are on the same machine, e.g.
[`signal`](signal.html#module-signal "signal: Set handlers for asynchronous events.") and [`mmap`](mmap.html#module-mmap "mmap: Interface to memory-mapped files for Unix and Windows."). Other modules support networking protocols
that two or more processes can use to communicate across machines.

The list of modules described in this chapter is:

* [`asyncio` — Asynchronous I/O](asyncio.html)
* [`socket` — Low-level networking interface](socket.html)
* [`ssl` — TLS/SSL wrapper for socket objects](ssl.html)
* [`select` — Waiting for I/O completion](select.html)
* [`selectors` — High-level I/O multiplexing](selectors.html)
* [`signal` — Set handlers for asynchronous events](signal.html)
* [`mmap` — Memory-mapped file support](mmap.html)

#### Previous topic

[`_thread` — Low-level threading API](_thread.html "previous chapter")

#### Next topic

[`asyncio` — Asynchronous I/O](asyncio.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/ipc.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](asyncio.html "asyncio — Asynchronous I/O") |
* [previous](_thread.html "_thread — Low-level threading API") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Networking and Interprocess Communication
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