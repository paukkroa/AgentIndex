### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](lzma.html "lzma — Compression using the LZMA algorithm") |
* [previous](gzip.html "gzip — Support for gzip files") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Compression and Archiving](archiving.html) »
* `bz2` — Support for **bzip2** compression
* |
* Theme
  Auto
  Light
  Dark
   |

# `bz2` — Support for **bzip2** compression[¶](#module-bz2 "Link to this heading")

**Source code:** [Lib/bz2.py](https://github.com/python/cpython/tree/3.14/Lib/bz2.py)

---

This module provides a comprehensive interface for compressing and
decompressing data using the bzip2 compression algorithm.

The `bz2` module contains:

* The [`open()`](#bz2.open "bz2.open") function and [`BZ2File`](#bz2.BZ2File "bz2.BZ2File") class for reading and
  writing compressed files.
* The [`BZ2Compressor`](#bz2.BZ2Compressor "bz2.BZ2Compressor") and [`BZ2Decompressor`](#bz2.BZ2Decompressor "bz2.BZ2Decompressor") classes for
  incremental (de)compression.
* The [`compress()`](#bz2.compress "bz2.compress") and [`decompress()`](#bz2.decompress "bz2.decompress") functions for one-shot
  (de)compression.

This is an [optional module](../glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](../using/configure.html#optional-module-requirements).

## (De)compression of files[¶](#de-compression-of-files "Link to this heading")

bz2.open(*filename*, *mode='rb'*, *compresslevel=9*, *encoding=None*, *errors=None*, *newline=None*)[¶](#bz2.open "Link to this definition")
:   Open a bzip2-compressed file in binary or text mode, returning a [file
    object](../glossary.html#term-file-object).

    As with the constructor for [`BZ2File`](#bz2.BZ2File "bz2.BZ2File"), the *filename* argument can be
    an actual filename (a [`str`](stdtypes.html#str "str") or [`bytes`](stdtypes.html#bytes "bytes") object), or an existing
    file object to read from or write to.

    The *mode* argument can be any of `'r'`, `'rb'`, `'w'`, `'wb'`,
    `'x'`, `'xb'`, `'a'` or `'ab'` for binary mode, or `'rt'`,
    `'wt'`, `'xt'`, or `'at'` for text mode. The default is `'rb'`.

    The *compresslevel* argument is an integer from 1 to 9, as for the
    [`BZ2File`](#bz2.BZ2File "bz2.BZ2File") constructor.

    For binary mode, this function is equivalent to the [`BZ2File`](#bz2.BZ2File "bz2.BZ2File")
    constructor: `BZ2File(filename, mode, compresslevel=compresslevel)`. In
    this case, the *encoding*, *errors* and *newline* arguments must not be
    provided.

    For text mode, a [`BZ2File`](#bz2.BZ2File "bz2.BZ2File") object is created, and wrapped in an
    [`io.TextIOWrapper`](io.html#io.TextIOWrapper "io.TextIOWrapper") instance with the specified encoding, error
    handling behavior, and line ending(s).

    Added in version 3.3.

    Changed in version 3.4: The `'x'` (exclusive creation) mode was added.

    Changed in version 3.6: Accepts a [path-like object](../glossary.html#term-path-like-object).

*class* bz2.BZ2File(*filename*, *mode='r'*, *\**, *compresslevel=9*)[¶](#bz2.BZ2File "Link to this definition")
:   Open a bzip2-compressed file in binary mode.

    If *filename* is a [`str`](stdtypes.html#str "str") or [`bytes`](stdtypes.html#bytes "bytes") object, open the named file
    directly. Otherwise, *filename* should be a [file object](../glossary.html#term-file-object), which will
    be used to read or write the compressed data.

    The *mode* argument can be either `'r'` for reading (default), `'w'` for
    overwriting, `'x'` for exclusive creation, or `'a'` for appending. These
    can equivalently be given as `'rb'`, `'wb'`, `'xb'` and `'ab'`
    respectively.

    If *filename* is a file object (rather than an actual file name), a mode of
    `'w'` does not truncate the file, and is instead equivalent to `'a'`.

    If *mode* is `'w'` or `'a'`, *compresslevel* can be an integer between
    `1` and `9` specifying the level of compression: `1` produces the
    least compression, and `9` (default) produces the most compression.

    If *mode* is `'r'`, the input file may be the concatenation of multiple
    compressed streams.

    [`BZ2File`](#bz2.BZ2File "bz2.BZ2File") provides all of the members specified by the
    [`io.BufferedIOBase`](io.html#io.BufferedIOBase "io.BufferedIOBase"), except for [`detach()`](io.html#io.BufferedIOBase.detach "io.BufferedIOBase.detach")
    and [`truncate()`](io.html#io.IOBase.truncate "io.IOBase.truncate").
    Iteration and the [`with`](../reference/compound_stmts.html#with) statement are supported.

    [`BZ2File`](#bz2.BZ2File "bz2.BZ2File") also provides the following methods and attributes:

    peek([*n*])[¶](#bz2.BZ2File.peek "Link to this definition")
    :   Return buffered data without advancing the file position. At least one
        byte of data will be returned (unless at EOF). The exact number of bytes
        returned is unspecified.

        Note

        While calling [`peek()`](#bz2.BZ2File.peek "bz2.BZ2File.peek") does not change the file position of
        the [`BZ2File`](#bz2.BZ2File "bz2.BZ2File"), it may change the position of the underlying file
        object (e.g. if the [`BZ2File`](#bz2.BZ2File "bz2.BZ2File") was constructed by passing a file
        object for *filename*).

        Added in version 3.3.

    fileno()[¶](#bz2.BZ2File.fileno "Link to this definition")
    :   Return the file descriptor for the underlying file.

        Added in version 3.3.

    readable()[¶](#bz2.BZ2File.readable "Link to this definition")
    :   Return whether the file was opened for reading.

        Added in version 3.3.

    seekable()[¶](#bz2.BZ2File.seekable "Link to this definition")
    :   Return whether the file supports seeking.

        Added in version 3.3.

    writable()[¶](#bz2.BZ2File.writable "Link to this definition")
    :   Return whether the file was opened for writing.

        Added in version 3.3.

    read1(*size=-1*)[¶](#bz2.BZ2File.read1 "Link to this definition")
    :   Read up to *size* uncompressed bytes, while trying to avoid
        making multiple reads from the underlying stream. Reads up to a
        buffer’s worth of data if size is negative.

        Returns `b''` if the file is at EOF.

        Added in version 3.3.

    readinto(*b*)[¶](#bz2.BZ2File.readinto "Link to this definition")
    :   Read bytes into *b*.

        Returns the number of bytes read (0 for EOF).

        Added in version 3.3.

    mode[¶](#bz2.BZ2File.mode "Link to this definition")
    :   `'rb'` for reading and `'wb'` for writing.

        Added in version 3.13.

    name[¶](#bz2.BZ2File.name "Link to this definition")
    :   The bzip2 file name. Equivalent to the [`name`](io.html#io.FileIO.name "io.FileIO.name")
        attribute of the underlying [file object](../glossary.html#term-file-object).

        Added in version 3.13.

    Changed in version 3.1: Support for the [`with`](../reference/compound_stmts.html#with) statement was added.

    Changed in version 3.3: Support was added for *filename* being a [file object](../glossary.html#term-file-object) instead of an
    actual filename.

    The `'a'` (append) mode was added, along with support for reading
    multi-stream files.

    Changed in version 3.4: The `'x'` (exclusive creation) mode was added.

    Changed in version 3.5: The [`read()`](io.html#io.BufferedIOBase.read "io.BufferedIOBase.read") method now accepts an argument of
    `None`.

    Changed in version 3.6: Accepts a [path-like object](../glossary.html#term-path-like-object).

    Changed in version 3.9: The *buffering* parameter has been removed. It was ignored and deprecated
    since Python 3.0. Pass an open file object to control how the file is
    opened.

    The *compresslevel* parameter became keyword-only.

    Changed in version 3.10: This class is thread unsafe in the face of multiple simultaneous
    readers or writers, just like its equivalent classes in [`gzip`](gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.") and
    [`lzma`](lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") have always been.

## Incremental (de)compression[¶](#incremental-de-compression "Link to this heading")

*class* bz2.BZ2Compressor(*compresslevel=9*)[¶](#bz2.BZ2Compressor "Link to this definition")
:   Create a new compressor object. This object may be used to compress data
    incrementally. For one-shot compression, use the [`compress()`](#bz2.compress "bz2.compress") function
    instead.

    *compresslevel*, if given, must be an integer between `1` and `9`. The
    default is `9`.

    compress(*data*)[¶](#bz2.BZ2Compressor.compress "Link to this definition")
    :   Provide data to the compressor object. Returns a chunk of compressed data
        if possible, or an empty byte string otherwise.

        When you have finished providing data to the compressor, call the
        [`flush()`](#bz2.BZ2Compressor.flush "bz2.BZ2Compressor.flush") method to finish the compression process.

    flush()[¶](#bz2.BZ2Compressor.flush "Link to this definition")
    :   Finish the compression process. Returns the compressed data left in
        internal buffers.

        The compressor object may not be used after this method has been called.

*class* bz2.BZ2Decompressor[¶](#bz2.BZ2Decompressor "Link to this definition")
:   Create a new decompressor object. This object may be used to decompress data
    incrementally. For one-shot compression, use the [`decompress()`](#bz2.decompress "bz2.decompress") function
    instead.

    Note

    This class does not transparently handle inputs containing multiple
    compressed streams, unlike [`decompress()`](#bz2.decompress "bz2.decompress") and [`BZ2File`](#bz2.BZ2File "bz2.BZ2File"). If
    you need to decompress a multi-stream input with [`BZ2Decompressor`](#bz2.BZ2Decompressor "bz2.BZ2Decompressor"),
    you must use a new decompressor for each stream.

    decompress(*data*, *max\_length=-1*)[¶](#bz2.BZ2Decompressor.decompress "Link to this definition")
    :   Decompress *data* (a [bytes-like object](../glossary.html#term-bytes-like-object)), returning
        uncompressed data as bytes. Some of *data* may be buffered
        internally, for use in later calls to [`decompress()`](#bz2.decompress "bz2.decompress"). The
        returned data should be concatenated with the output of any
        previous calls to [`decompress()`](#bz2.decompress "bz2.decompress").

        If *max\_length* is nonnegative, returns at most *max\_length*
        bytes of decompressed data. If this limit is reached and further
        output can be produced, the [`needs_input`](#bz2.BZ2Decompressor.needs_input "bz2.BZ2Decompressor.needs_input") attribute will
        be set to `False`. In this case, the next call to
        [`decompress()`](#bz2.BZ2Decompressor.decompress "bz2.BZ2Decompressor.decompress") may provide *data* as `b''` to obtain
        more of the output.

        If all of the input data was decompressed and returned (either
        because this was less than *max\_length* bytes, or because
        *max\_length* was negative), the [`needs_input`](#bz2.BZ2Decompressor.needs_input "bz2.BZ2Decompressor.needs_input") attribute
        will be set to `True`.

        Attempting to decompress data after the end of stream is reached
        raises an [`EOFError`](exceptions.html#EOFError "EOFError"). Any data found after the end of the
        stream is ignored and saved in the [`unused_data`](#bz2.BZ2Decompressor.unused_data "bz2.BZ2Decompressor.unused_data") attribute.

        Changed in version 3.5: Added the *max\_length* parameter.

    eof[¶](#bz2.BZ2Decompressor.eof "Link to this definition")
    :   `True` if the end-of-stream marker has been reached.

        Added in version 3.3.

    unused\_data[¶](#bz2.BZ2Decompressor.unused_data "Link to this definition")
    :   Data found after the end of the compressed stream.

        If this attribute is accessed before the end of the stream has been
        reached, its value will be `b''`.

    needs\_input[¶](#bz2.BZ2Decompressor.needs_input "Link to this definition")
    :   `False` if the [`decompress()`](#bz2.BZ2Decompressor.decompress "bz2.BZ2Decompressor.decompress") method can provide more
        decompressed data before requiring new uncompressed input.

        Added in version 3.5.

## One-shot (de)compression[¶](#one-shot-de-compression "Link to this heading")

bz2.compress(*data*, *compresslevel=9*)[¶](#bz2.compress "Link to this definition")
:   Compress *data*, a [bytes-like object](../glossary.html#term-bytes-like-object).

    *compresslevel*, if given, must be an integer between `1` and `9`. The
    default is `9`.

    For incremental compression, use a [`BZ2Compressor`](#bz2.BZ2Compressor "bz2.BZ2Compressor") instead.

bz2.decompress(*data*)[¶](#bz2.decompress "Link to this definition")
:   Decompress *data*, a [bytes-like object](../glossary.html#term-bytes-like-object).

    If *data* is the concatenation of multiple compressed streams, decompress
    all of the streams.

    For incremental decompression, use a [`BZ2Decompressor`](#bz2.BZ2Decompressor "bz2.BZ2Decompressor") instead.

    Changed in version 3.3: Support for multi-stream inputs was added.

## Examples of usage[¶](#examples-of-usage "Link to this heading")

Below are some examples of typical usage of the `bz2` module.

Using [`compress()`](#bz2.compress "bz2.compress") and [`decompress()`](#bz2.decompress "bz2.decompress") to demonstrate round-trip compression:

```
>>> import bz2
>>> data = b"""\
... Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
... nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
... sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
... pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
... Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
... felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
... dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""
>>> c = bz2.compress(data)
>>> len(data) / len(c)  # Data compression ratio
1.513595166163142
>>> d = bz2.decompress(c)
>>> data == d  # Check equality to original object after round-trip
True
```

Using [`BZ2Compressor`](#bz2.BZ2Compressor "bz2.BZ2Compressor") for incremental compression:

```
>>> import bz2
>>> def gen_data(chunks=10, chunksize=1000):
...     """Yield incremental blocks of chunksize bytes."""
...     for _ in range(chunks):
...         yield b"z" * chunksize
...
>>> comp = bz2.BZ2Compressor()
>>> out = b""
>>> for chunk in gen_data():
...     # Provide data to the compressor object
...     out = out + comp.compress(chunk)
...
>>> # Finish the compression process.  Call this once you have
>>> # finished providing data to the compressor.
>>> out = out + comp.flush()
```

The example above uses a very “nonrandom” stream of data
(a stream of `b"z"` chunks). Random data tends to compress poorly,
while ordered, repetitive data usually yields a high compression ratio.

Writing and reading a bzip2-compressed file in binary mode:

```
>>> import bz2
>>> data = b"""\
... Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
... nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
... sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
... pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
... Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
... felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
... dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""
>>> with bz2.open("myfile.bz2", "wb") as f:
...     # Write compressed data to file
...     unused = f.write(data)
...
>>> with bz2.open("myfile.bz2", "rb") as f:
...     # Decompress data from file
...     content = f.read()
...
>>> content == data  # Check equality to original object after round-trip
True
```

### [Table of Contents](../contents.html)

* [`bz2` — Support for **bzip2** compression](#)
  + [(De)compression of files](#de-compression-of-files)
  + [Incremental (de)compression](#incremental-de-compression)
  + [One-shot (de)compression](#one-shot-de-compression)
  + [Examples of usage](#examples-of-usage)

#### Previous topic

[`gzip` — Support for **gzip** files](gzip.html "previous chapter")

#### Next topic

[`lzma` — Compression using the LZMA algorithm](lzma.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/bz2.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](lzma.html "lzma — Compression using the LZMA algorithm") |
* [previous](gzip.html "gzip — Support for gzip files") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Compression and Archiving](archiving.html) »
* `bz2` — Support for **bzip2** compression
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