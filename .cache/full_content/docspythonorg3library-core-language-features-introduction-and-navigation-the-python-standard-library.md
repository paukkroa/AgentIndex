### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](intro.html "Introduction") |
* [previous](../reference/grammar.html "10. Full Grammar specification") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* The Python Standard Library
* |
* Theme
  Auto
  Light
  Dark
   |

# The Python Standard Library[¶](#the-python-standard-library "Link to this heading")

While [The Python Language Reference](../reference/index.html#reference-index) describes the exact syntax and
semantics of the Python language, this library reference manual
describes the standard library that is distributed with Python. It also
describes some of the optional components that are commonly included
in Python distributions.

Python’s standard library is very extensive, offering a wide range of
facilities as indicated by the long table of contents listed below. The
library contains built-in modules (written in C) that provide access to
system functionality such as file I/O that would otherwise be
inaccessible to Python programmers, as well as modules written in Python
that provide standardized solutions for many problems that occur in
everyday programming. Some of these modules are explicitly designed to
encourage and enhance the portability of Python programs by abstracting
away platform-specifics into platform-neutral APIs.

The Python installers for the Windows platform usually include
the entire standard library and often also include many additional
components. For Unix-like operating systems Python is normally provided
as a collection of packages, so it may be necessary to use the packaging
tools provided with the operating system to obtain some or all of the
optional components.

In addition to the standard library, there is an active collection of
hundreds of thousands of components (from individual programs and modules to
packages and entire application development frameworks), available from
the [Python Package Index](https://pypi.org).

* [Introduction](intro.html)
  + [Notes on availability](intro.html#notes-on-availability)
* [Built-in Functions](functions.html)
* [Built-in Constants](constants.html)
  + [Constants added by the `site` module](constants.html#constants-added-by-the-site-module)
* [Built-in Types](stdtypes.html)
  + [Truth Value Testing](stdtypes.html#truth-value-testing)
  + [Boolean Operations — `and`, `or`, `not`](stdtypes.html#boolean-operations-and-or-not)
  + [Comparisons](stdtypes.html#comparisons)
  + [Numeric Types — `int`, `float`, `complex`](stdtypes.html#numeric-types-int-float-complex)
  + [Boolean Type - `bool`](stdtypes.html#boolean-type-bool)
  + [Iterator Types](stdtypes.html#iterator-types)
  + [Sequence Types — `list`, `tuple`, `range`](stdtypes.html#sequence-types-list-tuple-range)
  + [Text and Binary Sequence Type Methods Summary](stdtypes.html#text-and-binary-sequence-type-methods-summary)
  + [Text Sequence Type — `str`](stdtypes.html#text-sequence-type-str)
  + [Binary Sequence Types — `bytes`, `bytearray`, `memoryview`](stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)
  + [Set Types — `set`, `frozenset`](stdtypes.html#set-types-set-frozenset)
  + [Mapping Types — `dict`](stdtypes.html#mapping-types-dict)
  + [Context Manager Types](stdtypes.html#context-manager-types)
  + [Type Annotation Types — Generic Alias, Union](stdtypes.html#type-annotation-types-generic-alias-union)
  + [Other Built-in Types](stdtypes.html#other-built-in-types)
  + [Special Attributes](stdtypes.html#special-attributes)
  + [Integer string conversion length limitation](stdtypes.html#integer-string-conversion-length-limitation)
* [Built-in Exceptions](exceptions.html)
  + [Exception context](exceptions.html#exception-context)
  + [Inheriting from built-in exceptions](exceptions.html#inheriting-from-built-in-exceptions)
  + [Base classes](exceptions.html#base-classes)
  + [Concrete exceptions](exceptions.html#concrete-exceptions)
  + [Warnings](exceptions.html#warnings)
  + [Exception groups](exceptions.html#exception-groups)
  + [Exception hierarchy](exceptions.html#exception-hierarchy)
* [Text Processing Services](text.html)
  + [`string` — Common string operations](string.html)
  + [`string.templatelib` — Support for template string literals](string.templatelib.html)
  + [`re` — Regular expression operations](re.html)
  + [`difflib` — Helpers for computing deltas](difflib.html)
  + [`textwrap` — Text wrapping and filling](textwrap.html)
  + [`unicodedata` — Unicode Database](unicodedata.html)
  + [`stringprep` — Internet String Preparation](stringprep.html)
  + [`readline` — GNU readline interface](readline.html)
  + [`rlcompleter` — Completion function for GNU readline](rlcompleter.html)
* [Binary Data Services](binary.html)
  + [`struct` — Interpret bytes as packed binary data](struct.html)
  + [`codecs` — Codec registry and base classes](codecs.html)
* [Data Types](datatypes.html)
  + [`datetime` — Basic date and time types](datetime.html)
  + [`zoneinfo` — IANA time zone support](zoneinfo.html)
  + [`calendar` — General calendar-related functions](calendar.html)
  + [`collections` — Container datatypes](collections.html)
  + [`collections.abc` — Abstract Base Classes for Containers](collections.abc.html)
  + [`heapq` — Heap queue algorithm](heapq.html)
  + [`bisect` — Array bisection algorithm](bisect.html)
  + [`array` — Efficient arrays of numeric values](array.html)
  + [`weakref` — Weak references](weakref.html)
  + [`types` — Dynamic type creation and names for built-in types](types.html)
  + [`copy` — Shallow and deep copy operations](copy.html)
  + [`pprint` — Data pretty printer](pprint.html)
  + [`reprlib` — Alternate `repr()` implementation](reprlib.html)
  + [`enum` — Support for enumerations](enum.html)
  + [`graphlib` — Functionality to operate with graph-like structures](graphlib.html)
* [Numeric and Mathematical Modules](numeric.html)
  + [`numbers` — Numeric abstract base classes](numbers.html)
  + [`math` — Mathematical functions](math.html)
  + [`cmath` — Mathematical functions for complex numbers](cmath.html)
  + [`decimal` — Decimal fixed-point and floating-point arithmetic](decimal.html)
  + [`fractions` — Rational numbers](fractions.html)
  + [`random` — Generate pseudo-random numbers](random.html)
  + [`statistics` — Mathematical statistics functions](statistics.html)
* [Functional Programming Modules](functional.html)
  + [`itertools` — Functions creating iterators for efficient looping](itertools.html)
  + [`functools` — Higher-order functions and operations on callable objects](functools.html)
  + [`operator` — Standard operators as functions](operator.html)
* [File and Directory Access](filesys.html)
  + [`pathlib` — Object-oriented filesystem paths](pathlib.html)
  + [`os.path` — Common pathname manipulations](os.path.html)
  + [`stat` — Interpreting `stat()` results](stat.html)
  + [`filecmp` — File and Directory Comparisons](filecmp.html)
  + [`tempfile` — Generate temporary files and directories](tempfile.html)
  + [`glob` — Unix style pathname pattern expansion](glob.html)
  + [`fnmatch` — Unix filename pattern matching](fnmatch.html)
  + [`linecache` — Random access to text lines](linecache.html)
  + [`shutil` — High-level file operations](shutil.html)
* [Data Persistence](persistence.html)
  + [`pickle` — Python object serialization](pickle.html)
  + [`copyreg` — Register `pickle` support functions](copyreg.html)
  + [`shelve` — Python object persistence](shelve.html)
  + [`marshal` — Internal Python object serialization](marshal.html)
  + [`dbm` — Interfaces to Unix “databases”](dbm.html)
  + [`sqlite3` — DB-API 2.0 interface for SQLite databases](sqlite3.html)
* [Data Compression and Archiving](archiving.html)
  + [The `compression` package](compression.html)
  + [`compression.zstd` — Compression compatible with the Zstandard format](compression.zstd.html)
  + [`zlib` — Compression compatible with **gzip**](zlib.html)
  + [`gzip` — Support for **gzip** files](gzip.html)
  + [`bz2` — Support for **bzip2** compression](bz2.html)
  + [`lzma` — Compression using the LZMA algorithm](lzma.html)
  + [`zipfile` — Work with ZIP archives](zipfile.html)
  + [`tarfile` — Read and write tar archive files](tarfile.html)
* [File Formats](fileformats.html)
  + [`csv` — CSV File Reading and Writing](csv.html)
  + [`configparser` — Configuration file parser](configparser.html)
  + [`tomllib` — Parse TOML files](tomllib.html)
  + [`netrc` — netrc file processing](netrc.html)
  + [`plistlib` — Generate and parse Apple `.plist` files](plistlib.html)
* [Cryptographic Services](crypto.html)
  + [`hashlib` — Secure hashes and message digests](hashlib.html)
  + [`hmac` — Keyed-Hashing for Message Authentication](hmac.html)
  + [`secrets` — Generate secure random numbers for managing secrets](secrets.html)
* [Generic Operating System Services](allos.html)
  + [`os` — Miscellaneous operating system interfaces](os.html)
  + [`io` — Core tools for working with streams](io.html)
  + [`time` — Time access and conversions](time.html)
  + [`logging` — Logging facility for Python](logging.html)
  + [`logging.config` — Logging configuration](logging.config.html)
  + [`logging.handlers` — Logging handlers](logging.handlers.html)
  + [`platform` — Access to underlying platform’s identifying data](platform.html)
  + [`errno` — Standard errno system symbols](errno.html)
  + [`ctypes` — A foreign function library for Python](ctypes.html)
* [Command-line interface libraries](cmdlinelibs.html)
  + [`argparse` — Parser for command-line options, arguments and subcommands](argparse.html)
  + [`optparse` — Parser for command line options](optparse.html)
  + [`getpass` — Portable password input](getpass.html)
  + [`fileinput` — Iterate over lines from multiple input streams](fileinput.html)
  + [`curses` — Terminal handling for character-cell displays](curses.html)
  + [`curses.textpad` — Text input widget for curses programs](curses.html#module-curses.textpad)
  + [`curses.ascii` — Utilities for ASCII characters](curses.ascii.html)
  + [`curses.panel` — A panel stack extension for curses](curses.panel.html)
  + [`cmd` — Support for line-oriented command interpreters](cmd.html)
* [Concurrent Execution](concurrency.html)
  + [`threading` — Thread-based parallelism](threading.html)
  + [`multiprocessing` — Process-based parallelism](multiprocessing.html)
  + [`multiprocessing.shared_memory` — Shared memory for direct access across processes](multiprocessing.shared_memory.html)
  + [The `concurrent` package](concurrent.html)
  + [`concurrent.futures` — Launching parallel tasks](concurrent.futures.html)
  + [`concurrent.interpreters` — Multiple interpreters in the same process](concurrent.interpreters.html)
  + [`subprocess` — Subprocess management](subprocess.html)
  + [`sched` — Event scheduler](sched.html)
  + [`queue` — A synchronized queue class](queue.html)
  + [`contextvars` — Context Variables](contextvars.html)
  + [`_thread` — Low-level threading API](_thread.html)
* [Networking and Interprocess Communication](ipc.html)
  + [`asyncio` — Asynchronous I/O](asyncio.html)
  + [`socket` — Low-level networking interface](socket.html)
  + [`ssl` — TLS/SSL wrapper for socket objects](ssl.html)
  + [`select` — Waiting for I/O completion](select.html)
  + [`selectors` — High-level I/O multiplexing](selectors.html)
  + [`signal` — Set handlers for asynchronous events](signal.html)
  + [`mmap` — Memory-mapped file support](mmap.html)
* [Internet Data Handling](netdata.html)
  + [`email` — An email and MIME handling package](email.html)
  + [`json` — JSON encoder and decoder](json.html)
  + [`mailbox` — Manipulate mailboxes in various formats](mailbox.html)
  + [`mimetypes` — Map filenames to MIME types](mimetypes.html)
  + [`base64` — Base16, Base32, Base64, Base85 Data Encodings](base64.html)
  + [`binascii` — Convert between binary and ASCII](binascii.html)
  + [`quopri` — Encode and decode MIME quoted-printable data](quopri.html)
* [Structured Markup Processing Tools](markup.html)
  + [`html` — HyperText Markup Language support](html.html)
  + [`html.parser` — Simple HTML and XHTML parser](html.parser.html)
  + [`html.entities` — Definitions of HTML general entities](html.entities.html)
  + [XML Processing Modules](xml.html)
  + [`xml.etree.ElementTree` — The ElementTree XML API](xml.etree.elementtree.html)
  + [`xml.dom` — The Document Object Model API](xml.dom.html)
  + [`xml.dom.minidom` — Minimal DOM implementation](xml.dom.minidom.html)
  + [`xml.dom.pulldom` — Support for building partial DOM trees](xml.dom.pulldom.html)
  + [`xml.sax` — Support for SAX2 parsers](xml.sax.html)
  + [`xml.sax.handler` — Base classes for SAX handlers](xml.sax.handler.html)
  + [`xml.sax.saxutils` — SAX Utilities](xml.sax.utils.html)
  + [`xml.sax.xmlreader` — Interface for XML parsers](xml.sax.reader.html)
  + [`xml.parsers.expat` — Fast XML parsing using Expat](pyexpat.html)
* [Internet Protocols and Support](internet.html)
  + [`webbrowser` — Convenient web-browser controller](webbrowser.html)
  + [`wsgiref` — WSGI Utilities and Reference Implementation](wsgiref.html)
  + [`urllib` — URL handling modules](urllib.html)
  + [`urllib.request` — Extensible library for opening URLs](urllib.request.html)
  + [`urllib.response` — Response classes used by urllib](urllib.request.html#module-urllib.response)
  + [`urllib.parse` — Parse URLs into components](urllib.parse.html)
  + [`urllib.error` — Exception classes raised by urllib.request](urllib.error.html)
  + [`urllib.robotparser` — Parser for robots.txt](urllib.robotparser.html)
  + [`http` — HTTP modules](http.html)
  + [`http.client` — HTTP protocol client](http.client.html)
  + [`ftplib` — FTP protocol client](ftplib.html)
  + [`poplib` — POP3 protocol client](poplib.html)
  + [`imaplib` — IMAP4 protocol client](imaplib.html)
  + [`smtplib` — SMTP protocol client](smtplib.html)
  + [`uuid` — UUID objects according to **RFC 9562**](uuid.html)
  + [`socketserver` — A framework for network servers](socketserver.html)
  + [`http.server` — HTTP servers](http.server.html)
  + [`http.cookies` — HTTP state management](http.cookies.html)
  + [`http.cookiejar` — Cookie handling for HTTP clients](http.cookiejar.html)
  + [`xmlrpc` — XMLRPC server and client modules](xmlrpc.html)
  + [`xmlrpc.client` — XML-RPC client access](xmlrpc.client.html)
  + [`xmlrpc.server` — Basic XML-RPC servers](xmlrpc.server.html)
  + [`ipaddress` — IPv4/IPv6 manipulation library](ipaddress.html)
* [Multimedia Services](mm.html)
  + [`wave` — Read and write WAV files](wave.html)
  + [`colorsys` — Conversions between color systems](colorsys.html)
* [Internationalization](i18n.html)
  + [`gettext` — Multilingual internationalization services](gettext.html)
  + [`locale` — Internationalization services](locale.html)
* [Graphical user interfaces with Tk](tk.html)
  + [`tkinter` — Python interface to Tcl/Tk](tkinter.html)
  + [`tkinter.colorchooser` — Color choosing dialog](tkinter.colorchooser.html)
  + [`tkinter.font` — Tkinter font wrapper](tkinter.font.html)
  + [Tkinter Dialogs](dialog.html)
  + [`tkinter.messagebox` — Tkinter message prompts](tkinter.messagebox.html)
  + [`tkinter.scrolledtext` — Scrolled Text Widget](tkinter.scrolledtext.html)
  + [`tkinter.dnd` — Drag and drop support](tkinter.dnd.html)
  + [`tkinter.ttk` — Tk themed widgets](tkinter.ttk.html)
  + [IDLE — Python editor and shell](idle.html)
  + [`turtle` — Turtle graphics](turtle.html)
* [Development Tools](development.html)
  + [`typing` — Support for type hints](typing.html)
  + [`pydoc` — Documentation generator and online help system](pydoc.html)
  + [Python Development Mode](devmode.html)
  + [`doctest` — Test interactive Python examples](doctest.html)
  + [`unittest` — Unit testing framework](unittest.html)
  + [`unittest.mock` — mock object library](unittest.mock.html)
  + [`unittest.mock` — getting started](unittest.mock-examples.html)
  + [`test` — Regression tests package for Python](test.html)
  + [`test.support` — Utilities for the Python test suite](test.html#module-test.support)
  + [`test.support.socket_helper` — Utilities for socket tests](test.html#module-test.support.socket_helper)
  + [`test.support.script_helper` — Utilities for the Python execution tests](test.html#module-test.support.script_helper)
  + [`test.support.bytecode_helper` — Support tools for testing correct bytecode generation](test.html#module-test.support.bytecode_helper)
  + [`test.support.threading_helper` — Utilities for threading tests](test.html#module-test.support.threading_helper)
  + [`test.support.os_helper` — Utilities for os tests](test.html#module-test.support.os_helper)
  + [`test.support.import_helper` — Utilities for import tests](test.html#module-test.support.import_helper)
  + [`test.support.warnings_helper` — Utilities for warnings tests](test.html#module-test.support.warnings_helper)
* [Debugging and Profiling](debug.html)
  + [Audit events table](audit_events.html)
  + [`bdb` — Debugger framework](bdb.html)
  + [`faulthandler` — Dump the Python traceback](faulthandler.html)
  + [`pdb` — The Python Debugger](pdb.html)
  + [The Python Profilers](profile.html)
  + [`timeit` — Measure execution time of small code snippets](timeit.html)
  + [`trace` — Trace or track Python statement execution](trace.html)
  + [`tracemalloc` — Trace memory allocations](tracemalloc.html)
* [Software Packaging and Distribution](distribution.html)
  + [`ensurepip` — Bootstrapping the `pip` installer](ensurepip.html)
  + [`venv` — Creation of virtual environments](venv.html)
  + [`zipapp` — Manage executable Python zip archives](zipapp.html)
* [Python Runtime Services](python.html)
  + [`sys` — System-specific parameters and functions](sys.html)
  + [`sys.monitoring` — Execution event monitoring](sys.monitoring.html)
  + [`sysconfig` — Provide access to Python’s configuration information](sysconfig.html)
  + [`builtins` — Built-in objects](builtins.html)
  + [`__main__` — Top-level code environment](__main__.html)
  + [`warnings` — Warning control](warnings.html)
  + [`dataclasses` — Data Classes](dataclasses.html)
  + [`contextlib` — Utilities for `with`-statement contexts](contextlib.html)
  + [`abc` — Abstract Base Classes](abc.html)
  + [`atexit` — Exit handlers](atexit.html)
  + [`traceback` — Print or retrieve a stack traceback](traceback.html)
  + [`__future__` — Future statement definitions](__future__.html)
  + [`gc` — Garbage Collector interface](gc.html)
  + [`inspect` — Inspect live objects](inspect.html)
  + [`annotationlib` — Functionality for introspecting annotations](annotationlib.html)
  + [`site` — Site-specific configuration hook](site.html)
* [Custom Python Interpreters](custominterp.html)
  + [`code` — Interpreter base classes](code.html)
  + [`codeop` — Compile Python code](codeop.html)
* [Importing Modules](modules.html)
  + [`zipimport` — Import modules from Zip archives](zipimport.html)
  + [`pkgutil` — Package extension utility](pkgutil.html)
  + [`modulefinder` — Find modules used by a script](modulefinder.html)
  + [`runpy` — Locating and executing Python modules](runpy.html)
  + [`importlib` — The implementation of `import`](importlib.html)
  + [`importlib.resources` – Package resource reading, opening and access](importlib.resources.html)
  + [`importlib.resources.abc` – Abstract base classes for resources](importlib.resources.abc.html)
  + [`importlib.metadata` – Accessing package metadata](importlib.metadata.html)
  + [The initialization of the `sys.path` module search path](sys_path_init.html)
* [Python Language Services](language.html)
  + [`ast` — Abstract syntax trees](ast.html)
  + [`symtable` — Access to the compiler’s symbol tables](symtable.html)
  + [`token` — Constants used with Python parse trees](token.html)
  + [`keyword` — Testing for Python keywords](keyword.html)
  + [`tokenize` — Tokenizer for Python source](tokenize.html)
  + [`tabnanny` — Detection of ambiguous indentation](tabnanny.html)
  + [`pyclbr` — Python module browser support](pyclbr.html)
  + [`py_compile` — Compile Python source files](py_compile.html)
  + [`compileall` — Byte-compile Python libraries](compileall.html)
  + [`dis` — Disassembler for Python bytecode](dis.html)
  + [`pickletools` — Tools for pickle developers](pickletools.html)
* [MS Windows Specific Services](windows.html)
  + [`msvcrt` — Useful routines from the MS VC++ runtime](msvcrt.html)
  + [`winreg` — Windows registry access](winreg.html)
  + [`winsound` — Sound-playing interface for Windows](winsound.html)
* [Unix-specific services](unix.html)
  + [`shlex` — Simple lexical analysis](shlex.html)
  + [`posix` — The most common POSIX system calls](posix.html)
  + [`pwd` — The password database](pwd.html)
  + [`grp` — The group database](grp.html)
  + [`termios` — POSIX style tty control](termios.html)
  + [`tty` — Terminal control functions](tty.html)
  + [`pty` — Pseudo-terminal utilities](pty.html)
  + [`fcntl` — The `fcntl` and `ioctl` system calls](fcntl.html)
  + [`resource` — Resource usage information](resource.html)
  + [`syslog` — Unix syslog library routines](syslog.html)
* [Modules command-line interface (CLI)](cmdline.html)
* [Superseded Modules](superseded.html)
  + [`getopt` — C-style parser for command line options](getopt.html)
* [Removed Modules](removed.html)
* [Security Considerations](security_warnings.html)

#### Previous topic

[10. Full Grammar specification](../reference/grammar.html "previous chapter")

#### Next topic

[Introduction](intro.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/index.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](intro.html "Introduction") |
* [previous](../reference/grammar.html "10. Full Grammar specification") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* The Python Standard Library
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