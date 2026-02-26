### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](time.html "time — Time access and conversions") |
* [previous](os.html "os — Miscellaneous operating system interfaces") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Generic Operating System Services](allos.html) »
* `io` — Core tools for working with streams
* |
* Theme
  Auto
  Light
  Dark
   |

# `io` — Core tools for working with streams[¶](#module-io "Link to this heading")

**Source code:** [Lib/io.py](https://github.com/python/cpython/tree/3.14/Lib/io.py)

---

## Overview[¶](#overview "Link to this heading")

The `io` module provides Python’s main facilities for dealing with various
types of I/O. There are three main types of I/O: *text I/O*, *binary I/O*
and *raw I/O*. These are generic categories, and various backing stores can
be used for each of them. A concrete object belonging to any of these
categories is called a [file object](../glossary.html#term-file-object). Other common terms are *stream*
and *file-like object*.

Independent of its category, each concrete stream object will also have
various capabilities: it can be read-only, write-only, or read-write. It can
also allow arbitrary random access (seeking forwards or backwards to any
location), or only sequential access (for example in the case of a socket or
pipe).

All streams are careful about the type of data you give to them. For example
giving a [`str`](stdtypes.html#str "str") object to the `write()` method of a binary stream
will raise a [`TypeError`](exceptions.html#TypeError "TypeError"). So will giving a [`bytes`](stdtypes.html#bytes "bytes") object to the
`write()` method of a text stream.

Changed in version 3.3: Operations that used to raise [`IOError`](exceptions.html#IOError "IOError") now raise [`OSError`](exceptions.html#OSError "OSError"), since
[`IOError`](exceptions.html#IOError "IOError") is now an alias of [`OSError`](exceptions.html#OSError "OSError").

### Text I/O[¶](#text-i-o "Link to this heading")

Text I/O expects and produces [`str`](stdtypes.html#str "str") objects. This means that whenever
the backing store is natively made of bytes (such as in the case of a file),
encoding and decoding of data is made transparently as well as optional
translation of platform-specific newline characters.

The easiest way to create a text stream is with [`open()`](functions.html#open "open"), optionally
specifying an encoding:

```
f = open("myfile.txt", "r", encoding="utf-8")
```

In-memory text streams are also available as [`StringIO`](#io.StringIO "io.StringIO") objects:

```
f = io.StringIO("some initial text data")
```

Note

When working with a non-blocking stream, be aware that read operations on text I/O objects
might raise a [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError") if the stream cannot perform the operation
immediately.

The text stream API is described in detail in the documentation of
[`TextIOBase`](#io.TextIOBase "io.TextIOBase").

### Binary I/O[¶](#binary-i-o "Link to this heading")

Binary I/O (also called *buffered I/O*) expects
[bytes-like objects](../glossary.html#term-bytes-like-object) and produces [`bytes`](stdtypes.html#bytes "bytes")
objects. No encoding, decoding, or newline translation is performed. This
category of streams can be used for all kinds of non-text data, and also when
manual control over the handling of text data is desired.

The easiest way to create a binary stream is with [`open()`](functions.html#open "open") with `'b'` in
the mode string:

```
f = open("myfile.jpg", "rb")
```

In-memory binary streams are also available as [`BytesIO`](#io.BytesIO "io.BytesIO") objects:

```
f = io.BytesIO(b"some initial binary data: \x00\x01")
```

The binary stream API is described in detail in the docs of
[`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase").

Other library modules may provide additional ways to create text or binary
streams. See [`socket.socket.makefile()`](socket.html#socket.socket.makefile "socket.socket.makefile") for example.

### Raw I/O[¶](#raw-i-o "Link to this heading")

Raw I/O (also called *unbuffered I/O*) is generally used as a low-level
building-block for binary and text streams; it is rarely useful to directly
manipulate a raw stream from user code. Nevertheless, you can create a raw
stream by opening a file in binary mode with buffering disabled:

```
f = open("myfile.jpg", "rb", buffering=0)
```

The raw stream API is described in detail in the docs of [`RawIOBase`](#io.RawIOBase "io.RawIOBase").

## Text Encoding[¶](#text-encoding "Link to this heading")

The default encoding of [`TextIOWrapper`](#io.TextIOWrapper "io.TextIOWrapper") and [`open()`](functions.html#open "open") is
locale-specific ([`locale.getencoding()`](locale.html#locale.getencoding "locale.getencoding")).

However, many developers forget to specify the encoding when opening text files
encoded in UTF-8 (e.g. JSON, TOML, Markdown, etc…) since most Unix
platforms use UTF-8 locale by default. This causes bugs because the locale
encoding is not UTF-8 for most Windows users. For example:

```
# May not work on Windows when non-ASCII characters in the file.
with open("README.md") as f:
    long_description = f.read()
```

Accordingly, it is highly recommended that you specify the encoding
explicitly when opening text files. If you want to use UTF-8, pass
`encoding="utf-8"`. To use the current locale encoding,
`encoding="locale"` is supported since Python 3.10.

See also

[Python UTF-8 Mode](os.html#utf8-mode)
:   Python UTF-8 Mode can be used to change the default encoding to
    UTF-8 from locale-specific encoding.

[**PEP 686**](https://peps.python.org/pep-0686/)
:   Python 3.15 will make [Python UTF-8 Mode](os.html#utf8-mode) default.

### Opt-in EncodingWarning[¶](#opt-in-encodingwarning "Link to this heading")

Added in version 3.10: See [**PEP 597**](https://peps.python.org/pep-0597/) for more details.

To find where the default locale encoding is used, you can enable
the [`-X warn_default_encoding`](../using/cmdline.html#cmdoption-X) command line option or set the
[`PYTHONWARNDEFAULTENCODING`](../using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING) environment variable, which will
emit an [`EncodingWarning`](exceptions.html#EncodingWarning "EncodingWarning") when the default encoding is used.

If you are providing an API that uses [`open()`](functions.html#open "open") or
[`TextIOWrapper`](#io.TextIOWrapper "io.TextIOWrapper") and passes `encoding=None` as a parameter, you
can use [`text_encoding()`](#io.text_encoding "io.text_encoding") so that callers of the API will emit an
[`EncodingWarning`](exceptions.html#EncodingWarning "EncodingWarning") if they don’t pass an `encoding`. However,
please consider using UTF-8 by default (i.e. `encoding="utf-8"`) for
new APIs.

## High-level Module Interface[¶](#high-level-module-interface "Link to this heading")

io.DEFAULT\_BUFFER\_SIZE[¶](#io.DEFAULT_BUFFER_SIZE "Link to this definition")
:   An int containing the default buffer size used by the module’s buffered I/O
    classes. [`open()`](functions.html#open "open") uses the file’s blksize (as obtained by
    [`os.stat()`](os.html#os.stat "os.stat")) if possible.

io.open(*file*, *mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*, *closefd=True*, *opener=None*)[¶](#io.open "Link to this definition")
:   This is an alias for the builtin [`open()`](functions.html#open "open") function.

    This function raises an [auditing event](sys.html#auditing) `open` with
    arguments *path*, *mode* and *flags*. The *mode* and *flags*
    arguments may have been modified or inferred from the original call.

io.open\_code(*path*)[¶](#io.open_code "Link to this definition")
:   Opens the provided file with mode `'rb'`. This function should be used
    when the intent is to treat the contents as executable code.

    *path* should be a [`str`](stdtypes.html#str "str") and an absolute path.

    The behavior of this function may be overridden by an earlier call to the
    [`PyFile_SetOpenCodeHook()`](../c-api/file.html#c.PyFile_SetOpenCodeHook "PyFile_SetOpenCodeHook"). However, assuming that *path* is a
    [`str`](stdtypes.html#str "str") and an absolute path, `open_code(path)` should always behave
    the same as `open(path, 'rb')`. Overriding the behavior is intended for
    additional validation or preprocessing of the file.

    Added in version 3.8.

io.text\_encoding(*encoding*, *stacklevel=2*, */*)[¶](#io.text_encoding "Link to this definition")
:   This is a helper function for callables that use [`open()`](functions.html#open "open") or
    [`TextIOWrapper`](#io.TextIOWrapper "io.TextIOWrapper") and have an `encoding=None` parameter.

    This function returns *encoding* if it is not `None`.
    Otherwise, it returns `"locale"` or `"utf-8"` depending on
    [UTF-8 Mode](os.html#utf8-mode).

    This function emits an [`EncodingWarning`](exceptions.html#EncodingWarning "EncodingWarning") if
    [`sys.flags.warn_default_encoding`](sys.html#sys.flags "sys.flags") is true and *encoding*
    is `None`. *stacklevel* specifies where the warning is emitted.
    For example:

    ```
    def read_text(path, encoding=None):
        encoding = io.text_encoding(encoding)  # stacklevel=2
        with open(path, encoding) as f:
            return f.read()
    ```

    In this example, an [`EncodingWarning`](exceptions.html#EncodingWarning "EncodingWarning") is emitted for the caller of
    `read_text()`.

    See [Text Encoding](#io-text-encoding) for more information.

    Added in version 3.10.

    Changed in version 3.11: [`text_encoding()`](#io.text_encoding "io.text_encoding") returns “utf-8” when UTF-8 mode is enabled and
    *encoding* is `None`.

*exception* io.BlockingIOError[¶](#io.BlockingIOError "Link to this definition")
:   This is a compatibility alias for the builtin [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError")
    exception.

*exception* io.UnsupportedOperation[¶](#io.UnsupportedOperation "Link to this definition")
:   An exception inheriting [`OSError`](exceptions.html#OSError "OSError") and [`ValueError`](exceptions.html#ValueError "ValueError") that is raised
    when an unsupported operation is called on a stream.

See also

[`sys`](sys.html#module-sys "sys: Access system-specific parameters and functions.")
:   contains the standard IO streams: [`sys.stdin`](sys.html#sys.stdin "sys.stdin"), [`sys.stdout`](sys.html#sys.stdout "sys.stdout"),
    and [`sys.stderr`](sys.html#sys.stderr "sys.stderr").

## Class hierarchy[¶](#class-hierarchy "Link to this heading")

The implementation of I/O streams is organized as a hierarchy of classes. First
[abstract base classes](../glossary.html#term-abstract-base-class) (ABCs), which are used to
specify the various categories of streams, then concrete classes providing the
standard stream implementations.

Note

The abstract base classes also provide default implementations of some
methods in order to help implementation of concrete stream classes. For
example, [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") provides unoptimized implementations of
`readinto()` and `readline()`.

At the top of the I/O hierarchy is the abstract base class [`IOBase`](#io.IOBase "io.IOBase"). It
defines the basic interface to a stream. Note, however, that there is no
separation between reading and writing to streams; implementations are allowed
to raise [`UnsupportedOperation`](#io.UnsupportedOperation "io.UnsupportedOperation") if they do not support a given operation.

The [`RawIOBase`](#io.RawIOBase "io.RawIOBase") ABC extends [`IOBase`](#io.IOBase "io.IOBase"). It deals with the reading
and writing of bytes to a stream. [`FileIO`](#io.FileIO "io.FileIO") subclasses [`RawIOBase`](#io.RawIOBase "io.RawIOBase")
to provide an interface to files in the machine’s file system.

The [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") ABC extends [`IOBase`](#io.IOBase "io.IOBase"). It deals with
buffering on a raw binary stream ([`RawIOBase`](#io.RawIOBase "io.RawIOBase")). Its subclasses,
[`BufferedWriter`](#io.BufferedWriter "io.BufferedWriter"), [`BufferedReader`](#io.BufferedReader "io.BufferedReader"), and [`BufferedRWPair`](#io.BufferedRWPair "io.BufferedRWPair")
buffer raw binary streams that are writable, readable, and both readable and writable,
respectively. [`BufferedRandom`](#io.BufferedRandom "io.BufferedRandom") provides a buffered interface to seekable streams.
Another [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") subclass, [`BytesIO`](#io.BytesIO "io.BytesIO"), is a stream of
in-memory bytes.

The [`TextIOBase`](#io.TextIOBase "io.TextIOBase") ABC extends [`IOBase`](#io.IOBase "io.IOBase"). It deals with
streams whose bytes represent text, and handles encoding and decoding to and
from strings. [`TextIOWrapper`](#io.TextIOWrapper "io.TextIOWrapper"), which extends [`TextIOBase`](#io.TextIOBase "io.TextIOBase"), is a buffered text
interface to a buffered raw stream ([`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase")). Finally,
[`StringIO`](#io.StringIO "io.StringIO") is an in-memory stream for text.

Argument names are not part of the specification, and only the arguments of
[`open()`](functions.html#open "open") are intended to be used as keyword arguments.

The following table summarizes the ABCs provided by the `io` module:

| ABC | Inherits | Stub Methods | Mixin Methods and Properties |
| --- | --- | --- | --- |
| [`IOBase`](#io.IOBase "io.IOBase") |  | `fileno`, `seek`, and `truncate` | `close`, `closed`, `__enter__`, `__exit__`, `flush`, `isatty`, `__iter__`, `__next__`, `readable`, `readline`, `readlines`, `seekable`, `tell`, `writable`, and `writelines` |
| [`RawIOBase`](#io.RawIOBase "io.RawIOBase") | [`IOBase`](#io.IOBase "io.IOBase") | `readinto` and `write` | Inherited [`IOBase`](#io.IOBase "io.IOBase") methods, `read`, and `readall` |
| [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") | [`IOBase`](#io.IOBase "io.IOBase") | `detach`, `read`, `read1`, and `write` | Inherited [`IOBase`](#io.IOBase "io.IOBase") methods, `readinto`, and `readinto1` |
| [`TextIOBase`](#io.TextIOBase "io.TextIOBase") | [`IOBase`](#io.IOBase "io.IOBase") | `detach`, `read`, `readline`, and `write` | Inherited [`IOBase`](#io.IOBase "io.IOBase") methods, `encoding`, `errors`, and `newlines` |

### I/O Base Classes[¶](#i-o-base-classes "Link to this heading")

*class* io.IOBase[¶](#io.IOBase "Link to this definition")
:   The abstract base class for all I/O classes.

    This class provides empty abstract implementations for many methods
    that derived classes can override selectively; the default
    implementations represent a file that cannot be read, written or
    seeked.

    Even though [`IOBase`](#io.IOBase "io.IOBase") does not declare `read()`
    or `write()` because their signatures will vary, implementations and
    clients should consider those methods part of the interface. Also,
    implementations may raise a [`ValueError`](exceptions.html#ValueError "ValueError") (or [`UnsupportedOperation`](#io.UnsupportedOperation "io.UnsupportedOperation"))
    when operations they do not support are called.

    The basic type used for binary data read from or written to a file is
    [`bytes`](stdtypes.html#bytes "bytes"). Other [bytes-like objects](../glossary.html#term-bytes-like-object) are
    accepted as method arguments too. Text I/O classes work with [`str`](stdtypes.html#str "str") data.

    Note that calling any method (even inquiries) on a closed stream is
    undefined. Implementations may raise [`ValueError`](exceptions.html#ValueError "ValueError") in this case.

    [`IOBase`](#io.IOBase "io.IOBase") (and its subclasses) supports the iterator protocol, meaning
    that an [`IOBase`](#io.IOBase "io.IOBase") object can be iterated over yielding the lines in a
    stream. Lines are defined slightly differently depending on whether the
    stream is a binary stream (yielding bytes), or a text stream (yielding
    character strings). See [`readline()`](#io.IOBase.readline "io.IOBase.readline") below.

    [`IOBase`](#io.IOBase "io.IOBase") is also a context manager and therefore supports the
    [`with`](../reference/compound_stmts.html#with) statement. In this example, *file* is closed after the
    `with` statement’s suite is finished—even if an exception occurs:

    ```
    with open('spam.txt', 'w') as file:
        file.write('Spam and eggs!')
    ```

    [`IOBase`](#io.IOBase "io.IOBase") provides these data attributes and methods:

    close()[¶](#io.IOBase.close "Link to this definition")
    :   Flush and close this stream. This method has no effect if the file is
        already closed. Once the file is closed, any operation on the file
        (e.g. reading or writing) will raise a [`ValueError`](exceptions.html#ValueError "ValueError").

        As a convenience, it is allowed to call this method more than once;
        only the first call, however, will have an effect.

    closed[¶](#io.IOBase.closed "Link to this definition")
    :   `True` if the stream is closed.

    fileno()[¶](#io.IOBase.fileno "Link to this definition")
    :   Return the underlying file descriptor (an integer) of the stream if it
        exists. An [`OSError`](exceptions.html#OSError "OSError") is raised if the IO object does not use a file
        descriptor.

    flush()[¶](#io.IOBase.flush "Link to this definition")
    :   Flush the write buffers of the stream if applicable. This does nothing
        for read-only and non-blocking streams.

    isatty()[¶](#io.IOBase.isatty "Link to this definition")
    :   Return `True` if the stream is interactive (i.e., connected to
        a terminal/tty device).

    readable()[¶](#io.IOBase.readable "Link to this definition")
    :   Return `True` if the stream can be read from.
        If `False`, `read()` will raise [`OSError`](exceptions.html#OSError "OSError").

    readline(*size=-1*, */*)[¶](#io.IOBase.readline "Link to this definition")
    :   Read and return one line from the stream. If *size* is specified, at
        most *size* bytes will be read.

        The line terminator is always `b'\n'` for binary files; for text files,
        the *newline* argument to [`open()`](functions.html#open "open") can be used to select the line
        terminator(s) recognized.

    readlines(*hint=-1*, */*)[¶](#io.IOBase.readlines "Link to this definition")
    :   Read and return a list of lines from the stream. *hint* can be specified
        to control the number of lines read: no more lines will be read if the
        total size (in bytes/characters) of all lines so far exceeds *hint*.

        *hint* values of `0` or less, as well as `None`, are treated as no
        hint.

        Note that it’s already possible to iterate on file objects using `for
        line in file: ...` without calling `file.readlines()`.

    seek(*offset*, *whence=os.SEEK\_SET*, */*)[¶](#io.IOBase.seek "Link to this definition")
    :   Change the stream position to the given byte *offset*,
        interpreted relative to the position indicated by *whence*,
        and return the new absolute position.
        Values for *whence* are:

        * [`os.SEEK_SET`](os.html#os.SEEK_SET "os.SEEK_SET") or `0` – start of the stream (the default);
          *offset* should be zero or positive
        * [`os.SEEK_CUR`](os.html#os.SEEK_CUR "os.SEEK_CUR") or `1` – current stream position;
          *offset* may be negative
        * [`os.SEEK_END`](os.html#os.SEEK_END "os.SEEK_END") or `2` – end of the stream;
          *offset* is usually negative

        Added in version 3.1: The `SEEK_*` constants.

        Added in version 3.3: Some operating systems could support additional values, like
        [`os.SEEK_HOLE`](os.html#os.SEEK_HOLE "os.SEEK_HOLE") or [`os.SEEK_DATA`](os.html#os.SEEK_DATA "os.SEEK_DATA"). The valid values
        for a file could depend on it being open in text or binary mode.

    seekable()[¶](#io.IOBase.seekable "Link to this definition")
    :   Return `True` if the stream supports random access. If `False`,
        [`seek()`](#io.IOBase.seek "io.IOBase.seek"), [`tell()`](#io.IOBase.tell "io.IOBase.tell") and [`truncate()`](#io.IOBase.truncate "io.IOBase.truncate") will raise [`OSError`](exceptions.html#OSError "OSError").

    tell()[¶](#io.IOBase.tell "Link to this definition")
    :   Return the current stream position.

    truncate(*size=None*, */*)[¶](#io.IOBase.truncate "Link to this definition")
    :   Resize the stream to the given *size* in bytes (or the current position
        if *size* is not specified). The current stream position isn’t changed.
        This resizing can extend or reduce the current file size. In case of
        extension, the contents of the new file area depend on the platform
        (on most systems, additional bytes are zero-filled). The new file size
        is returned.

        Changed in version 3.5: Windows will now zero-fill files when extending.

    writable()[¶](#io.IOBase.writable "Link to this definition")
    :   Return `True` if the stream supports writing. If `False`,
        `write()` and [`truncate()`](#io.IOBase.truncate "io.IOBase.truncate") will raise [`OSError`](exceptions.html#OSError "OSError").

    writelines(*lines*, */*)[¶](#io.IOBase.writelines "Link to this definition")
    :   Write a list of lines to the stream. Line separators are not added, so it
        is usual for each of the lines provided to have a line separator at the
        end.

    \_\_del\_\_()[¶](#io.IOBase.__del__ "Link to this definition")
    :   Prepare for object destruction. [`IOBase`](#io.IOBase "io.IOBase") provides a default
        implementation of this method that calls the instance’s
        [`close()`](#io.IOBase.close "io.IOBase.close") method.

*class* io.RawIOBase[¶](#io.RawIOBase "Link to this definition")
:   Base class for raw binary streams. It inherits from [`IOBase`](#io.IOBase "io.IOBase").

    Raw binary streams typically provide low-level access to an underlying OS
    device or API, and do not try to encapsulate it in high-level primitives
    (this functionality is done at a higher-level in buffered binary streams and text streams, described later
    in this page).

    [`RawIOBase`](#io.RawIOBase "io.RawIOBase") provides these methods in addition to those from
    [`IOBase`](#io.IOBase "io.IOBase"):

    read(*size=-1*, */*)[¶](#io.RawIOBase.read "Link to this definition")
    :   Read up to *size* bytes from the object and return them. As a convenience,
        if *size* is unspecified or -1, all bytes until EOF are returned.
        Otherwise, only one system call is ever made. Fewer than *size* bytes may
        be returned if the operating system call returns fewer than *size* bytes.

        If 0 bytes are returned, and *size* was not 0, this indicates end of file.
        If the object is in non-blocking mode and no bytes are available,
        `None` is returned.

        The default implementation defers to [`readall()`](#io.RawIOBase.readall "io.RawIOBase.readall") and
        [`readinto()`](#io.RawIOBase.readinto "io.RawIOBase.readinto").

    readall()[¶](#io.RawIOBase.readall "Link to this definition")
    :   Read and return all the bytes from the stream until EOF, using multiple
        calls to the stream if necessary.

    readinto(*b*, */*)[¶](#io.RawIOBase.readinto "Link to this definition")
    :   Read bytes into a pre-allocated, writable
        [bytes-like object](../glossary.html#term-bytes-like-object) *b*, and return the
        number of bytes read. For example, *b* might be a [`bytearray`](stdtypes.html#bytearray "bytearray").
        If the object is in non-blocking mode and no bytes
        are available, `None` is returned.

    write(*b*, */*)[¶](#io.RawIOBase.write "Link to this definition")
    :   Write the given [bytes-like object](../glossary.html#term-bytes-like-object), *b*, to the
        underlying raw stream, and return the number of
        bytes written. This can be less than the length of *b* in
        bytes, depending on specifics of the underlying raw
        stream, and especially if it is in non-blocking mode. `None` is
        returned if the raw stream is set not to block and no single byte could
        be readily written to it. The caller may release or mutate *b* after
        this method returns, so the implementation should only access *b*
        during the method call.

*class* io.BufferedIOBase[¶](#io.BufferedIOBase "Link to this definition")
:   Base class for binary streams that support some kind of buffering.
    It inherits from [`IOBase`](#io.IOBase "io.IOBase").

    The main difference with [`RawIOBase`](#io.RawIOBase "io.RawIOBase") is that methods [`read()`](#io.BufferedIOBase.read "io.BufferedIOBase.read"),
    [`readinto()`](#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto") and [`write()`](#io.BufferedIOBase.write "io.BufferedIOBase.write") will try (respectively) to read
    as much input as requested or to emit all provided data.

    In addition, if the underlying raw stream is in non-blocking mode, when the
    system returns would block [`write()`](#io.BufferedIOBase.write "io.BufferedIOBase.write") will raise [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError")
    with [`BlockingIOError.characters_written`](exceptions.html#BlockingIOError.characters_written "BlockingIOError.characters_written") and [`read()`](#io.BufferedIOBase.read "io.BufferedIOBase.read") will return
    data read so far or `None` if no data is available.

    Besides, the [`read()`](#io.BufferedIOBase.read "io.BufferedIOBase.read") method does not have a default
    implementation that defers to [`readinto()`](#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto").

    A typical [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") implementation should not inherit from a
    [`RawIOBase`](#io.RawIOBase "io.RawIOBase") implementation, but wrap one, like
    [`BufferedWriter`](#io.BufferedWriter "io.BufferedWriter") and [`BufferedReader`](#io.BufferedReader "io.BufferedReader") do.

    [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") provides or overrides these data attributes and
    methods in addition to those from [`IOBase`](#io.IOBase "io.IOBase"):

    raw[¶](#io.BufferedIOBase.raw "Link to this definition")
    :   The underlying raw stream (a [`RawIOBase`](#io.RawIOBase "io.RawIOBase") instance) that
        [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") deals with. This is not part of the
        [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") API and may not exist on some implementations.

    detach()[¶](#io.BufferedIOBase.detach "Link to this definition")
    :   Separate the underlying raw stream from the buffer and return it.

        After the raw stream has been detached, the buffer is in an unusable
        state.

        Some buffers, like [`BytesIO`](#io.BytesIO "io.BytesIO"), do not have the concept of a single
        raw stream to return from this method. They raise
        [`UnsupportedOperation`](#io.UnsupportedOperation "io.UnsupportedOperation").

        Added in version 3.1.

    read(*size=-1*, */*)[¶](#io.BufferedIOBase.read "Link to this definition")
    :   Read and return up to *size* bytes. If the argument is omitted, `None`,
        or negative read as much as possible.

        Fewer bytes may be returned than requested. An empty [`bytes`](stdtypes.html#bytes "bytes") object
        is returned if the stream is already at EOF. More than one read may be
        made and calls may be retried if specific errors are encountered, see
        [`os.read()`](os.html#os.read "os.read") and [**PEP 475**](https://peps.python.org/pep-0475/) for more details. Less than size bytes
        being returned does not imply that EOF is imminent.

        When reading as much as possible the default implementation will use
        `raw.readall` if available (which should implement
        [`RawIOBase.readall()`](#io.RawIOBase.readall "io.RawIOBase.readall")), otherwise will read in a loop until read
        returns `None`, an empty [`bytes`](stdtypes.html#bytes "bytes"), or a non-retryable error. For
        most streams this is to EOF, but for non-blocking streams more data may
        become available.

        Note

        When the underlying raw stream is non-blocking, implementations may
        either raise [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError") or return `None` if no data is
        available. `io` implementations return `None`.

    read1(*size=-1*, */*)[¶](#io.BufferedIOBase.read1 "Link to this definition")
    :   Read and return up to *size* bytes, calling [`readinto()`](#io.RawIOBase.readinto "io.RawIOBase.readinto")
        which may retry if [`EINTR`](errno.html#errno.EINTR "errno.EINTR") is encountered per
        [**PEP 475**](https://peps.python.org/pep-0475/). If *size* is `-1` or not provided, the implementation will
        choose an arbitrary value for *size*.

        Note

        When the underlying raw stream is non-blocking, implementations may
        either raise [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError") or return `None` if no data is
        available. `io` implementations return `None`.

    readinto(*b*, */*)[¶](#io.BufferedIOBase.readinto "Link to this definition")
    :   Read bytes into a pre-allocated, writable
        [bytes-like object](../glossary.html#term-bytes-like-object) *b* and return the number of bytes read.
        For example, *b* might be a [`bytearray`](stdtypes.html#bytearray "bytearray").

        Like [`read()`](#io.BufferedIOBase.read "io.BufferedIOBase.read"), multiple reads may be issued to the underlying raw
        stream, unless the latter is interactive.

        A [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError") is raised if the underlying raw stream is in non
        blocking-mode, and has no data available at the moment.

    readinto1(*b*, */*)[¶](#io.BufferedIOBase.readinto1 "Link to this definition")
    :   Read bytes into a pre-allocated, writable
        [bytes-like object](../glossary.html#term-bytes-like-object) *b*, using at most one call to
        the underlying raw stream’s [`read()`](#io.RawIOBase.read "io.RawIOBase.read") (or
        [`readinto()`](#io.RawIOBase.readinto "io.RawIOBase.readinto")) method. Return the number of bytes read.

        A [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError") is raised if the underlying raw stream is in non
        blocking-mode, and has no data available at the moment.

        Added in version 3.5.

    write(*b*, */*)[¶](#io.BufferedIOBase.write "Link to this definition")
    :   Write the given [bytes-like object](../glossary.html#term-bytes-like-object), *b*, and return the number
        of bytes written (always equal to the length of *b* in bytes, since if
        the write fails an [`OSError`](exceptions.html#OSError "OSError") will be raised). Depending on the
        actual implementation, these bytes may be readily written to the
        underlying stream, or held in a buffer for performance and latency
        reasons.

        When in non-blocking mode, a [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError") is raised if the
        data needed to be written to the raw stream but it couldn’t accept
        all the data without blocking.

        The caller may release or mutate *b* after this method returns,
        so the implementation should only access *b* during the method call.

### Raw File I/O[¶](#raw-file-i-o "Link to this heading")

*class* io.FileIO(*name*, *mode='r'*, *closefd=True*, *opener=None*)[¶](#io.FileIO "Link to this definition")
:   A raw binary stream representing an OS-level file containing bytes data. It
    inherits from [`RawIOBase`](#io.RawIOBase "io.RawIOBase").

    The *name* can be one of two things:

    * a character string or [`bytes`](stdtypes.html#bytes "bytes") object representing the path to the
      file which will be opened. In this case closefd must be `True` (the default)
      otherwise an error will be raised.
    * an integer representing the number of an existing OS-level file descriptor
      to which the resulting [`FileIO`](#io.FileIO "io.FileIO") object will give access. When the
      FileIO object is closed this fd will be closed as well, unless *closefd*
      is set to `False`.

    The *mode* can be `'r'`, `'w'`, `'x'` or `'a'` for reading
    (default), writing, exclusive creation or appending. The file will be
    created if it doesn’t exist when opened for writing or appending; it will be
    truncated when opened for writing. [`FileExistsError`](exceptions.html#FileExistsError "FileExistsError") will be raised if
    it already exists when opened for creating. Opening a file for creating
    implies writing, so this mode behaves in a similar way to `'w'`. Add a
    `'+'` to the mode to allow simultaneous reading and writing.

    The [`read()`](#io.RawIOBase.read "io.RawIOBase.read") (when called with a positive argument),
    [`readinto()`](#io.RawIOBase.readinto "io.RawIOBase.readinto") and [`write()`](#io.RawIOBase.write "io.RawIOBase.write") methods on this
    class will only make one system call.

    A custom opener can be used by passing a callable as *opener*. The underlying
    file descriptor for the file object is then obtained by calling *opener* with
    (*name*, *flags*). *opener* must return an open file descriptor (passing
    [`os.open`](os.html#os.open "os.open") as *opener* results in functionality similar to passing
    `None`).

    The newly created file is [non-inheritable](os.html#fd-inheritance).

    See the [`open()`](functions.html#open "open") built-in function for examples on using the *opener*
    parameter.

    Changed in version 3.3: The *opener* parameter was added.
    The `'x'` mode was added.

    Changed in version 3.4: The file is now non-inheritable.

    [`FileIO`](#io.FileIO "io.FileIO") provides these data attributes in addition to those from
    [`RawIOBase`](#io.RawIOBase "io.RawIOBase") and [`IOBase`](#io.IOBase "io.IOBase"):

    mode[¶](#io.FileIO.mode "Link to this definition")
    :   The mode as given in the constructor.

    name[¶](#io.FileIO.name "Link to this definition")
    :   The file name. This is the file descriptor of the file when no name is
        given in the constructor.

### Buffered Streams[¶](#buffered-streams "Link to this heading")

Buffered I/O streams provide a higher-level interface to an I/O device
than raw I/O does.

*class* io.BytesIO(*initial\_bytes=b''*)[¶](#io.BytesIO "Link to this definition")
:   A binary stream using an in-memory bytes buffer. It inherits from
    [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase"). The buffer is discarded when the
    [`close()`](#io.IOBase.close "io.IOBase.close") method is called.

    The optional argument *initial\_bytes* is a [bytes-like object](../glossary.html#term-bytes-like-object) that
    contains initial data.

    [`BytesIO`](#io.BytesIO "io.BytesIO") provides or overrides these methods in addition to those
    from [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](#io.IOBase "io.IOBase"):

    getbuffer()[¶](#io.BytesIO.getbuffer "Link to this definition")
    :   Return a readable and writable view over the contents of the buffer
        without copying them. Also, mutating the view will transparently
        update the contents of the buffer:

        ```
        >>> b = io.BytesIO(b"abcdef")
        >>> view = b.getbuffer()
        >>> view[2:4] = b"56"
        >>> b.getvalue()
        b'ab56ef'
        ```

        Note

        As long as the view exists, the [`BytesIO`](#io.BytesIO "io.BytesIO") object cannot be
        resized or closed.

        Added in version 3.2.

    getvalue()[¶](#io.BytesIO.getvalue "Link to this definition")
    :   Return [`bytes`](stdtypes.html#bytes "bytes") containing the entire contents of the buffer.

    read1(*size=-1*, */*)[¶](#io.BytesIO.read1 "Link to this definition")
    :   In [`BytesIO`](#io.BytesIO "io.BytesIO"), this is the same as [`read()`](#io.BufferedIOBase.read "io.BufferedIOBase.read").

        Changed in version 3.7: The *size* argument is now optional.

    readinto1(*b*, */*)[¶](#io.BytesIO.readinto1 "Link to this definition")
    :   In [`BytesIO`](#io.BytesIO "io.BytesIO"), this is the same as [`readinto()`](#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto").

        Added in version 3.5.

*class* io.BufferedReader(*raw*, *buffer\_size=DEFAULT\_BUFFER\_SIZE*)[¶](#io.BufferedReader "Link to this definition")
:   A buffered binary stream providing higher-level access to a readable, non
    seekable [`RawIOBase`](#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from
    [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase").

    When reading data from this object, a larger amount of data may be
    requested from the underlying raw stream, and kept in an internal buffer.
    The buffered data can then be returned directly on subsequent reads.

    The constructor creates a [`BufferedReader`](#io.BufferedReader "io.BufferedReader") for the given readable
    *raw* stream and *buffer\_size*. If *buffer\_size* is omitted,
    [`DEFAULT_BUFFER_SIZE`](#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE") is used.

    [`BufferedReader`](#io.BufferedReader "io.BufferedReader") provides or overrides these methods in addition to
    those from [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](#io.IOBase "io.IOBase"):

    peek(*size=0*, */*)[¶](#io.BufferedReader.peek "Link to this definition")
    :   Return bytes from the stream without advancing the position. The number of
        bytes returned may be less or more than requested. If the underlying raw
        stream is non-blocking and the operation would block, returns empty bytes.

    read(*size=-1*, */*)[¶](#io.BufferedReader.read "Link to this definition")
    :   In [`BufferedReader`](#io.BufferedReader "io.BufferedReader") this is the same as [`io.BufferedIOBase.read()`](#io.BufferedIOBase.read "io.BufferedIOBase.read")

    read1(*size=-1*, */*)[¶](#io.BufferedReader.read1 "Link to this definition")
    :   In [`BufferedReader`](#io.BufferedReader "io.BufferedReader") this is the same as [`io.BufferedIOBase.read1()`](#io.BufferedIOBase.read1 "io.BufferedIOBase.read1")

        Changed in version 3.7: The *size* argument is now optional.

*class* io.BufferedWriter(*raw*, *buffer\_size=DEFAULT\_BUFFER\_SIZE*)[¶](#io.BufferedWriter "Link to this definition")
:   A buffered binary stream providing higher-level access to a writeable, non
    seekable [`RawIOBase`](#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from
    [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase").

    When writing to this object, data is normally placed into an internal
    buffer. The buffer will be written out to the underlying [`RawIOBase`](#io.RawIOBase "io.RawIOBase")
    object under various conditions, including:

    * when the buffer gets too small for all pending data;
    * when [`flush()`](#io.BufferedWriter.flush "io.BufferedWriter.flush") is called;
    * when a [`seek()`](#io.IOBase.seek "io.IOBase.seek") is requested (for [`BufferedRandom`](#io.BufferedRandom "io.BufferedRandom") objects);
    * when the [`BufferedWriter`](#io.BufferedWriter "io.BufferedWriter") object is closed or destroyed.

    The constructor creates a [`BufferedWriter`](#io.BufferedWriter "io.BufferedWriter") for the given writeable
    *raw* stream. If the *buffer\_size* is not given, it defaults to
    [`DEFAULT_BUFFER_SIZE`](#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE").

    [`BufferedWriter`](#io.BufferedWriter "io.BufferedWriter") provides or overrides these methods in addition to
    those from [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](#io.IOBase "io.IOBase"):

    flush()[¶](#io.BufferedWriter.flush "Link to this definition")
    :   Force bytes held in the buffer into the raw stream. A
        [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError") should be raised if the raw stream blocks.

    write(*b*, */*)[¶](#io.BufferedWriter.write "Link to this definition")
    :   Write the [bytes-like object](../glossary.html#term-bytes-like-object), *b*, and return the
        number of bytes written. When in non-blocking mode, a
        [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError") with [`BlockingIOError.characters_written`](exceptions.html#BlockingIOError.characters_written "BlockingIOError.characters_written") set
        is raised if the buffer needs to be written out but the raw stream blocks.

*class* io.BufferedRandom(*raw*, *buffer\_size=DEFAULT\_BUFFER\_SIZE*)[¶](#io.BufferedRandom "Link to this definition")
:   A buffered binary stream providing higher-level access to a seekable
    [`RawIOBase`](#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from [`BufferedReader`](#io.BufferedReader "io.BufferedReader")
    and [`BufferedWriter`](#io.BufferedWriter "io.BufferedWriter").

    The constructor creates a reader and writer for a seekable raw stream, given
    in the first argument. If the *buffer\_size* is omitted it defaults to
    [`DEFAULT_BUFFER_SIZE`](#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE").

    [`BufferedRandom`](#io.BufferedRandom "io.BufferedRandom") is capable of anything [`BufferedReader`](#io.BufferedReader "io.BufferedReader") or
    [`BufferedWriter`](#io.BufferedWriter "io.BufferedWriter") can do. In addition, [`seek()`](#io.IOBase.seek "io.IOBase.seek") and
    [`tell()`](#io.IOBase.tell "io.IOBase.tell") are guaranteed to be implemented.

*class* io.BufferedRWPair(*reader*, *writer*, *buffer\_size=DEFAULT\_BUFFER\_SIZE*, */*)[¶](#io.BufferedRWPair "Link to this definition")
:   A buffered binary stream providing higher-level access to two non seekable
    [`RawIOBase`](#io.RawIOBase "io.RawIOBase") raw binary streams—one readable, the other writeable.
    It inherits from [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase").

    *reader* and *writer* are [`RawIOBase`](#io.RawIOBase "io.RawIOBase") objects that are readable and
    writeable respectively. If the *buffer\_size* is omitted it defaults to
    [`DEFAULT_BUFFER_SIZE`](#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE").

    [`BufferedRWPair`](#io.BufferedRWPair "io.BufferedRWPair") implements all of [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase")'s methods
    except for [`detach()`](#io.BufferedIOBase.detach "io.BufferedIOBase.detach"), which raises
    [`UnsupportedOperation`](#io.UnsupportedOperation "io.UnsupportedOperation").

    Warning

    [`BufferedRWPair`](#io.BufferedRWPair "io.BufferedRWPair") does not attempt to synchronize accesses to
    its underlying raw streams. You should not pass it the same object
    as reader and writer; use [`BufferedRandom`](#io.BufferedRandom "io.BufferedRandom") instead.

### Text I/O[¶](#id1 "Link to this heading")

*class* io.TextIOBase[¶](#io.TextIOBase "Link to this definition")
:   Base class for text streams. This class provides a character and line based
    interface to stream I/O. It inherits from [`IOBase`](#io.IOBase "io.IOBase").

    [`TextIOBase`](#io.TextIOBase "io.TextIOBase") provides or overrides these data attributes and
    methods in addition to those from [`IOBase`](#io.IOBase "io.IOBase"):

    encoding[¶](#io.TextIOBase.encoding "Link to this definition")
    :   The name of the encoding used to decode the stream’s bytes into
        strings, and to encode strings into bytes.

    errors[¶](#io.TextIOBase.errors "Link to this definition")
    :   The error setting of the decoder or encoder.

    newlines[¶](#io.TextIOBase.newlines "Link to this definition")
    :   A string, a tuple of strings, or `None`, indicating the newlines
        translated so far. Depending on the implementation and the initial
        constructor flags, this may not be available.

    buffer[¶](#io.TextIOBase.buffer "Link to this definition")
    :   The underlying binary buffer (a [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase")
        or [`RawIOBase`](#io.RawIOBase "io.RawIOBase") instance) that [`TextIOBase`](#io.TextIOBase "io.TextIOBase") deals with.
        This is not part of the [`TextIOBase`](#io.TextIOBase "io.TextIOBase") API and may not exist
        in some implementations.

    detach()[¶](#io.TextIOBase.detach "Link to this definition")
    :   Separate the underlying binary buffer from the [`TextIOBase`](#io.TextIOBase "io.TextIOBase") and
        return it.

        After the underlying buffer has been detached, the [`TextIOBase`](#io.TextIOBase "io.TextIOBase") is
        in an unusable state.

        Some [`TextIOBase`](#io.TextIOBase "io.TextIOBase") implementations, like [`StringIO`](#io.StringIO "io.StringIO"), may not
        have the concept of an underlying buffer and calling this method will
        raise [`UnsupportedOperation`](#io.UnsupportedOperation "io.UnsupportedOperation").

        Added in version 3.1.

    read(*size=-1*, */*)[¶](#io.TextIOBase.read "Link to this definition")
    :   Read and return at most *size* characters from the stream as a single
        [`str`](stdtypes.html#str "str"). If *size* is negative or `None`, reads until EOF.

    readline(*size=-1*, */*)[¶](#io.TextIOBase.readline "Link to this definition")
    :   Read until newline or EOF and return a single [`str`](stdtypes.html#str "str"). If the stream is
        already at EOF, an empty string is returned.

        If *size* is specified, at most *size* characters will be read.

    seek(*offset*, *whence=SEEK\_SET*, */*)[¶](#io.TextIOBase.seek "Link to this definition")
    :   Change the stream position to the given *offset*. Behaviour depends on
        the *whence* parameter. The default value for *whence* is
        `SEEK_SET`.

        * `SEEK_SET` or `0`: seek from the start of the stream
          (the default); *offset* must either be a number returned by
          [`TextIOBase.tell()`](#io.TextIOBase.tell "io.TextIOBase.tell"), or zero. Any other *offset* value
          produces undefined behaviour.
        * `SEEK_CUR` or `1`: “seek” to the current position;
          *offset* must be zero, which is a no-operation (all other values
          are unsupported).
        * `SEEK_END` or `2`: seek to the end of the stream;
          *offset* must be zero (all other values are unsupported).

        Return the new absolute position as an opaque number.

        Added in version 3.1: The `SEEK_*` constants.

    tell()[¶](#io.TextIOBase.tell "Link to this definition")
    :   Return the current stream position as an opaque number. The number
        does not usually represent a number of bytes in the underlying
        binary storage.

    write(*s*, */*)[¶](#io.TextIOBase.write "Link to this definition")
    :   Write the string *s* to the stream and return the number of characters
        written.

*class* io.TextIOWrapper(*buffer*, *encoding=None*, *errors=None*, *newline=None*, *line\_buffering=False*, *write\_through=False*)[¶](#io.TextIOWrapper "Link to this definition")
:   A buffered text stream providing higher-level access to a
    [`BufferedIOBase`](#io.BufferedIOBase "io.BufferedIOBase") buffered binary stream. It inherits from
    [`TextIOBase`](#io.TextIOBase "io.TextIOBase").

    *encoding* gives the name of the encoding that the stream will be decoded or
    encoded with. In [UTF-8 Mode](os.html#utf8-mode), this defaults to UTF-8.
    Otherwise, it defaults to [`locale.getencoding()`](locale.html#locale.getencoding "locale.getencoding").
    `encoding="locale"` can be used to specify the current locale’s encoding
    explicitly. See [Text Encoding](#io-text-encoding) for more information.

    *errors* is an optional string that specifies how encoding and decoding
    errors are to be handled. Pass `'strict'` to raise a [`ValueError`](exceptions.html#ValueError "ValueError")
    exception if there is an encoding error (the default of `None` has the same
    effect), or pass `'ignore'` to ignore errors. (Note that ignoring encoding
    errors can lead to data loss.) `'replace'` causes a replacement marker
    (such as `'?'`) to be inserted where there is malformed data.
    `'backslashreplace'` causes malformed data to be replaced by a
    backslashed escape sequence. When writing, `'xmlcharrefreplace'`
    (replace with the appropriate XML character reference) or `'namereplace'`
    (replace with `\N{...}` escape sequences) can be used. Any other error
    handling name that has been registered with
    [`codecs.register_error()`](codecs.html#codecs.register_error "codecs.register_error") is also valid.

    *newline* controls how line endings are handled. It can be `None`,
    `''`, `'\n'`, `'\r'`, and `'\r\n'`. It works as follows:

    * When reading input from the stream, if *newline* is `None`,
      [universal newlines](../glossary.html#term-universal-newlines) mode is enabled. Lines in the input can end in
      `'\n'`, `'\r'`, or `'\r\n'`, and these are translated into `'\n'`
      before being returned to the caller. If *newline* is `''`, universal
      newlines mode is enabled, but line endings are returned to the caller
      untranslated. If *newline* has any of the other legal values, input lines
      are only terminated by the given string, and the line ending is returned to
      the caller untranslated.
    * When writing output to the stream, if *newline* is `None`, any `'\n'`
      characters written are translated to the system default line separator,
      [`os.linesep`](os.html#os.linesep "os.linesep"). If *newline* is `''` or `'\n'`, no translation
      takes place. If *newline* is any of the other legal values, any `'\n'`
      characters written are translated to the given string.

    If *line\_buffering* is `True`, [`flush()`](#io.IOBase.flush "io.IOBase.flush") is implied when a call to
    write contains a newline character or a carriage return.

    If *write\_through* is `True`, calls to [`write()`](#io.BufferedIOBase.write "io.BufferedIOBase.write") are guaranteed
    not to be buffered: any data written on the [`TextIOWrapper`](#io.TextIOWrapper "io.TextIOWrapper")
    object is immediately handled to its underlying binary *buffer*.

    Changed in version 3.3: The *write\_through* argument has been added.

    Changed in version 3.3: The default *encoding* is now `locale.getpreferredencoding(False)`
    instead of `locale.getpreferredencoding()`. Don’t change temporary the
    locale encoding using [`locale.setlocale()`](locale.html#locale.setlocale "locale.setlocale"), use the current locale
    encoding instead of the user preferred encoding.

    Changed in version 3.10: The *encoding* argument now supports the `"locale"` dummy encoding name.

    Note

    When the underlying raw stream is non-blocking, a [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError")
    may be raised if a read operation cannot be completed immediately.

    [`TextIOWrapper`](#io.TextIOWrapper "io.TextIOWrapper") provides these data attributes and methods in
    addition to those from [`TextIOBase`](#io.TextIOBase "io.TextIOBase") and [`IOBase`](#io.IOBase "io.IOBase"):

    line\_buffering[¶](#io.TextIOWrapper.line_buffering "Link to this definition")
    :   Whether line buffering is enabled.

    write\_through[¶](#io.TextIOWrapper.write_through "Link to this definition")
    :   Whether writes are passed immediately to the underlying binary
        buffer.

        Added in version 3.7.

    reconfigure(*\**, *encoding=None*, *errors=None*, *newline=None*, *line\_buffering=None*, *write\_through=None*)[¶](#io.TextIOWrapper.reconfigure "Link to this definition")
    :   Reconfigure this text stream using new settings for *encoding*,
        *errors*, *newline*, *line\_buffering* and *write\_through*.

        Parameters not specified keep current settings, except
        `errors='strict'` is used when *encoding* is specified but
        *errors* is not specified.

        It is not possible to change the encoding or newline if some data
        has already been read from the stream. On the other hand, changing
        encoding after write is possible.

        This method does an implicit stream flush before setting the
        new parameters.

        Added in version 3.7.

        Changed in version 3.11: The method supports `encoding="locale"` option.

    seek(*cookie*, *whence=os.SEEK\_SET*, */*)[¶](#io.TextIOWrapper.seek "Link to this definition")
    :   Set the stream position.
        Return the new stream position as an [`int`](functions.html#int "int").

        Four operations are supported,
        given by the following argument combinations:

        * `seek(0, SEEK_SET)`: Rewind to the start of the stream.
        * `seek(cookie, SEEK_SET)`: Restore a previous position;
          *cookie* **must be** a number returned by [`tell()`](#io.TextIOWrapper.tell "io.TextIOWrapper.tell").
        * `seek(0, SEEK_END)`: Fast-forward to the end of the stream.
        * `seek(0, SEEK_CUR)`: Leave the current stream position unchanged.

        Any other argument combinations are invalid,
        and may raise exceptions.

        See also

        [`os.SEEK_SET`](os.html#os.SEEK_SET "os.SEEK_SET"), [`os.SEEK_CUR`](os.html#os.SEEK_CUR "os.SEEK_CUR"), and [`os.SEEK_END`](os.html#os.SEEK_END "os.SEEK_END").

    tell()[¶](#io.TextIOWrapper.tell "Link to this definition")
    :   Return the stream position as an opaque number.
        The return value of `tell()` can be given as input to [`seek()`](#io.TextIOWrapper.seek "io.TextIOWrapper.seek"),
        to restore a previous stream position.

*class* io.StringIO(*initial\_value=''*, *newline='\n'*)[¶](#io.StringIO "Link to this definition")
:   A text stream using an in-memory text buffer. It inherits from
    [`TextIOBase`](#io.TextIOBase "io.TextIOBase").

    The text buffer is discarded when the [`close()`](#io.IOBase.close "io.IOBase.close") method is
    called.

    The initial value of the buffer can be set by providing *initial\_value*.
    If newline translation is enabled, newlines will be encoded as if by
    [`write()`](#io.TextIOBase.write "io.TextIOBase.write"). The stream is positioned at the start of the
    buffer which emulates opening an existing file in a `w+` mode, making it
    ready for an immediate write from the beginning or for a write that
    would overwrite the initial value. To emulate opening a file in an `a+`
    mode ready for appending, use `f.seek(0, io.SEEK_END)` to reposition the
    stream at the end of the buffer.

    The *newline* argument works like that of [`TextIOWrapper`](#io.TextIOWrapper "io.TextIOWrapper"),
    except that when writing output to the stream, if *newline* is `None`,
    newlines are written as `\n` on all platforms.

    [`StringIO`](#io.StringIO "io.StringIO") provides this method in addition to those from
    [`TextIOBase`](#io.TextIOBase "io.TextIOBase") and [`IOBase`](#io.IOBase "io.IOBase"):

    getvalue()[¶](#io.StringIO.getvalue "Link to this definition")
    :   Return a [`str`](stdtypes.html#str "str") containing the entire contents of the buffer.
        Newlines are decoded as if by [`read()`](#io.TextIOBase.read "io.TextIOBase.read"), although
        the stream position is not changed.

    Example usage:

    ```
    import io

    output = io.StringIO()
    output.write('First line.\n')
    print('Second line.', file=output)

    # Retrieve file contents -- this will be
    # 'First line.\nSecond line.\n'
    contents = output.getvalue()

    # Close object and discard memory buffer --
    # .getvalue() will now raise an exception.
    output.close()
    ```

*class* io.IncrementalNewlineDecoder[¶](#io.IncrementalNewlineDecoder "Link to this definition")
:   A helper codec that decodes newlines for [universal newlines](../glossary.html#term-universal-newlines) mode.
    It inherits from [`codecs.IncrementalDecoder`](codecs.html#codecs.IncrementalDecoder "codecs.IncrementalDecoder").

## Static Typing[¶](#static-typing "Link to this heading")

The following protocols can be used for annotating function and method
arguments for simple stream reading or writing operations. They are decorated
with [`@typing.runtime_checkable`](typing.html#typing.runtime_checkable "typing.runtime_checkable").

*class* io.Reader[*T*][¶](#io.Reader "Link to this definition")
:   Generic protocol for reading from a file or other input stream. `T` will
    usually be [`str`](stdtypes.html#str "str") or [`bytes`](stdtypes.html#bytes "bytes"), but can be any type that is
    read from the stream.

    Added in version 3.14.

    read()[¶](#io.Reader.read "Link to this definition")

    read(*size*, */*)
    :   Read data from the input stream and return it. If *size* is
        specified, it should be an integer, and at most *size* items
        (bytes/characters) will be read.

    For example:

    ```
    def read_it(reader: Reader[str]):
        data = reader.read(11)
        assert isinstance(data, str)
    ```

*class* io.Writer[*T*][¶](#io.Writer "Link to this definition")
:   Generic protocol for writing to a file or other output stream. `T` will
    usually be [`str`](stdtypes.html#str "str") or [`bytes`](stdtypes.html#bytes "bytes"), but can be any type that can be
    written to the stream.

    Added in version 3.14.

    write(*data*, */*)[¶](#io.Writer.write "Link to this definition")
    :   Write *data* to the output stream and return the number of items
        (bytes/characters) written.

    For example:

    ```
    def write_binary(writer: Writer[bytes]):
        writer.write(b"Hello world!\n")
    ```

See [ABCs and Protocols for working with I/O](typing.html#typing-io) for other I/O related protocols and classes that can be
used for static type checking.

## Performance[¶](#performance "Link to this heading")

This section discusses the performance of the provided concrete I/O
implementations.

### Binary I/O[¶](#id2 "Link to this heading")

By reading and writing only large chunks of data even when the user asks for a
single byte, buffered I/O hides any inefficiency in calling and executing the
operating system’s unbuffered I/O routines. The gain depends on the OS and the
kind of I/O which is performed. For example, on some modern OSes such as Linux,
unbuffered disk I/O can be as fast as buffered I/O. The bottom line, however,
is that buffered I/O offers predictable performance regardless of the platform
and the backing device. Therefore, it is almost always preferable to use
buffered I/O rather than unbuffered I/O for binary data.

### Text I/O[¶](#id3 "Link to this heading")

Text I/O over a binary storage (such as a file) is significantly slower than
binary I/O over the same storage, because it requires conversions between
unicode and binary data using a character codec. This can become noticeable
handling huge amounts of text data like large log files. Also,
[`tell()`](#io.TextIOBase.tell "io.TextIOBase.tell") and [`seek()`](#io.TextIOBase.seek "io.TextIOBase.seek") are both quite slow
due to the reconstruction algorithm used.

[`StringIO`](#io.StringIO "io.StringIO"), however, is a native in-memory unicode container and will
exhibit similar speed to [`BytesIO`](#io.BytesIO "io.BytesIO").

### Multi-threading[¶](#multi-threading "Link to this heading")

[`FileIO`](#io.FileIO "io.FileIO") objects are thread-safe to the extent that the operating system
calls (such as *[read(2)](https://manpages.debian.org/read(2))* under Unix) they wrap are thread-safe too.

Binary buffered objects (instances of [`BufferedReader`](#io.BufferedReader "io.BufferedReader"),
[`BufferedWriter`](#io.BufferedWriter "io.BufferedWriter"), [`BufferedRandom`](#io.BufferedRandom "io.BufferedRandom") and [`BufferedRWPair`](#io.BufferedRWPair "io.BufferedRWPair"))
protect their internal structures using a lock; it is therefore safe to call
them from multiple threads at once.

[`TextIOWrapper`](#io.TextIOWrapper "io.TextIOWrapper") objects are not thread-safe.

### Reentrancy[¶](#reentrancy "Link to this heading")

Binary buffered objects (instances of [`BufferedReader`](#io.BufferedReader "io.BufferedReader"),
[`BufferedWriter`](#io.BufferedWriter "io.BufferedWriter"), [`BufferedRandom`](#io.BufferedRandom "io.BufferedRandom") and [`BufferedRWPair`](#io.BufferedRWPair "io.BufferedRWPair"))
are not reentrant. While reentrant calls will not happen in normal situations,
they can arise from doing I/O in a [`signal`](signal.html#module-signal "signal: Set handlers for asynchronous events.") handler. If a thread tries to
re-enter a buffered object which it is already accessing, a [`RuntimeError`](exceptions.html#RuntimeError "RuntimeError")
is raised. Note this doesn’t prohibit a different thread from entering the
buffered object.

The above implicitly extends to text files, since the [`open()`](functions.html#open "open") function
will wrap a buffered object inside a [`TextIOWrapper`](#io.TextIOWrapper "io.TextIOWrapper"). This includes
standard streams and therefore affects the built-in [`print()`](functions.html#print "print") function as
well.

### [Table of Contents](../contents.html)

* [`io` — Core tools for working with streams](#)
  + [Overview](#overview)
    - [Text I/O](#text-i-o)
    - [Binary I/O](#binary-i-o)
    - [Raw I/O](#raw-i-o)
  + [Text Encoding](#text-encoding)
    - [Opt-in EncodingWarning](#opt-in-encodingwarning)
  + [High-level Module Interface](#high-level-module-interface)
  + [Class hierarchy](#class-hierarchy)
    - [I/O Base Classes](#i-o-base-classes)
    - [Raw File I/O](#raw-file-i-o)
    - [Buffered Streams](#buffered-streams)
    - [Text I/O](#id1)
  + [Static Typing](#static-typing)
  + [Performance](#performance)
    - [Binary I/O](#id2)
    - [Text I/O](#id3)
    - [Multi-threading](#multi-threading)
    - [Reentrancy](#reentrancy)

#### Previous topic

[`os` — Miscellaneous operating system interfaces](os.html "previous chapter")

#### Next topic

[`time` — Time access and conversions](time.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/io.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](time.html "time — Time access and conversions") |
* [previous](os.html "os — Miscellaneous operating system interfaces") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Generic Operating System Services](allos.html) »
* `io` — Core tools for working with streams
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