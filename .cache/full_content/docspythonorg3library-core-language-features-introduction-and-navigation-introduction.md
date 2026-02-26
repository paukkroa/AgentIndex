### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](functions.html "Built-in Functions") |
* [previous](index.html "The Python Standard Library") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Introduction
* |
* Theme
  Auto
  Light
  Dark
   |

# Introduction[¶](#introduction "Link to this heading")

The “Python library” contains several different kinds of components.

It contains data types that would normally be considered part of the “core” of a
language, such as numbers and lists. For these types, the Python language core
defines the form of literals and places some constraints on their semantics, but
does not fully define the semantics. (On the other hand, the language core does
define syntactic properties like the spelling and priorities of operators.)

The library also contains built-in functions and exceptions — objects that can
be used by all Python code without the need of an [`import`](../reference/simple_stmts.html#import) statement.
Some of these are defined by the core language, but many are not essential for
the core semantics and are only described here.

The bulk of the library, however, consists of a collection of modules. There are
many ways to dissect this collection. Some modules are written in C and built
in to the Python interpreter; others are written in Python and imported in
source form. Some modules provide interfaces that are highly specific to
Python, like printing a stack trace; some provide interfaces that are specific
to particular operating systems, such as access to specific hardware; others
provide interfaces that are specific to a particular application domain, like
the World Wide Web. Some modules are available in all versions and ports of
Python; others are only available when the underlying system supports or
requires them; yet others are available only when a particular configuration
option was chosen at the time when Python was compiled and installed.

This manual is organized “from the inside out:” it first describes the built-in
functions, data types and exceptions, and finally the modules, grouped in
chapters of related modules.

This means that if you start reading this manual from the start, and skip to the
next chapter when you get bored, you will get a reasonable overview of the
available modules and application areas that are supported by the Python
library. Of course, you don’t *have* to read it like a novel — you can also
browse the table of contents (in front of the manual), or look for a specific
function, module or term in the index (in the back). And finally, if you enjoy
learning about random subjects, you choose a random page number (see module
[`random`](random.html#module-random "random: Generate pseudo-random numbers with various common distributions.")) and read a section or two. Regardless of the order in which you
read the sections of this manual, it helps to start with chapter
[Built-in Functions](functions.html#built-in-funcs), as the remainder of the manual assumes familiarity with
this material.

Let the show begin!

## Notes on availability[¶](#notes-on-availability "Link to this heading")

* An “Availability: Unix” note means that this function is commonly found on
  Unix systems. It does not make any claims about its existence on a specific
  operating system.
* If not separately noted, all functions that claim “Availability: Unix” are
  supported on macOS, iOS and Android, all of which build on a Unix core.
* If an availability note contains both a minimum Kernel version and a minimum
  libc version, then both conditions must hold. For example a feature with note
  *Availability: Linux >= 3.17 with glibc >= 2.27* requires both Linux 3.17 or
  newer and glibc 2.27 or newer.

### WebAssembly platforms[¶](#webassembly-platforms "Link to this heading")

The [WebAssembly](https://webassembly.org/) platforms `wasm32-emscripten` ([Emscripten](https://emscripten.org/)) and
`wasm32-wasi` ([WASI](https://wasi.dev/)) provide a subset of POSIX APIs. WebAssembly runtimes
and browsers are sandboxed and have limited access to the host and external
resources. Any Python standard library module that uses processes, threading,
networking, signals, or other forms of inter-process communication (IPC), is
either not available or may not work as on other Unix-like systems. File I/O,
file system, and Unix permission-related functions are restricted, too.
Emscripten does not permit blocking I/O. Other blocking operations like
[`sleep()`](time.html#time.sleep "time.sleep") block the browser event loop.

The properties and behavior of Python on WebAssembly platforms depend on the
[Emscripten](https://emscripten.org/)-SDK or [WASI](https://wasi.dev/)-SDK version, WASM runtimes (browser, NodeJS,
[wasmtime](https://wasmtime.dev/)), and Python build time flags. WebAssembly, Emscripten, and WASI
are evolving standards; some features like networking may be
supported in the future.

For Python in the browser, users should consider [Pyodide](https://pyodide.org/) or [PyScript](https://pyscript.net/).
PyScript is built on top of Pyodide, which itself is built on top of
CPython and Emscripten. Pyodide provides access to browsers’ JavaScript and
DOM APIs as well as limited networking capabilities with JavaScript’s
`XMLHttpRequest` and `Fetch` APIs.

* Process-related APIs are not available or always fail with an error. That
  includes APIs that spawn new processes ([`fork()`](os.html#os.fork "os.fork"),
  [`execve()`](os.html#os.execve "os.execve")), wait for processes ([`waitpid()`](os.html#os.waitpid "os.waitpid")), send signals
  ([`kill()`](os.html#os.kill "os.kill")), or otherwise interact with processes. The
  [`subprocess`](subprocess.html#module-subprocess "subprocess: Subprocess management.") is importable but does not work.
* The [`socket`](socket.html#module-socket "socket: Low-level networking interface.") module is available, but is limited and behaves
  differently from other platforms. On Emscripten, sockets are always
  non-blocking and require additional JavaScript code and helpers on the
  server to proxy TCP through WebSockets; see [Emscripten Networking](https://emscripten.org/docs/porting/networking.html)
  for more information. WASI snapshot preview 1 only permits sockets from an
  existing file descriptor.
* Some functions are stubs that either don’t do anything and always return
  hardcoded values.
* Functions related to file descriptors, file permissions, file ownership, and
  links are limited and don’t support some operations. For example, WASI does
  not permit symlinks with absolute file names.

### Mobile platforms[¶](#mobile-platforms "Link to this heading")

Android and iOS are, in most respects, POSIX operating systems. File I/O, socket handling,
and threading all behave as they would on any POSIX operating system. However,
there are several major differences:

* Mobile platforms can only use Python in “embedded” mode. There is no Python
  REPL, and no ability to use separate executables such as **python** or
  **pip**. To add Python code to your mobile app, you must use
  the [Python embedding API](../extending/embedding.html#embedding). For more details, see
  [Using Python on Android](../using/android.html#using-android) and [Using Python on iOS](../using/ios.html#using-ios).
* Subprocesses:

  + On Android, creating subprocesses is possible but [officially unsupported](https://issuetracker.google.com/issues/128554619#comment4).
    In particular, Android does not support any part of the System V IPC API,
    so [`multiprocessing`](multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") is not available.
  + An iOS app cannot use any form of subprocessing, multiprocessing, or
    inter-process communication. If an iOS app attempts to create a subprocess,
    the process creating the subprocess will either lock up, or crash. An iOS app
    has no visibility of other applications that are running, nor any ability to
    communicate with other running applications, outside of the iOS-specific APIs
    that exist for this purpose.
* Mobile apps have limited access to modify system resources (such as the system
  clock). These resources will often be *readable*, but attempts to modify
  those resources will usually fail.
* Console input and output:

  + On Android, the native `stdout` and `stderr` are not connected to
    anything, so Python installs its own streams which redirect messages to the
    system log. These can be seen under the tags `python.stdout` and
    `python.stderr` respectively.
  + iOS apps have a limited concept of console output. `stdout` and
    `stderr` *exist*, and content written to `stdout` and `stderr` will be
    visible in logs when running in Xcode, but this content *won’t* be recorded
    in the system log. If a user who has installed your app provides their app
    logs as a diagnostic aid, they will not include any detail written to
    `stdout` or `stderr`.
  + Mobile apps have no usable `stdin` at all. While apps can display an on-screen
    keyboard, this is a software feature, not something that is attached to
    `stdin`.

    As a result, Python modules that involve console manipulation (such as
    [`curses`](curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling.") and [`readline`](readline.html#module-readline "readline: GNU readline support for Python.")) are not available on mobile platforms.

### [Table of Contents](../contents.html)

* [Introduction](#)
  + [Notes on availability](#notes-on-availability)
    - [WebAssembly platforms](#webassembly-platforms)
    - [Mobile platforms](#mobile-platforms)

#### Previous topic

[The Python Standard Library](index.html "previous chapter")

#### Next topic

[Built-in Functions](functions.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/intro.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](functions.html "Built-in Functions") |
* [previous](index.html "The Python Standard Library") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Introduction
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