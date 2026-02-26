### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](bz2.html "bz2 — Support for bzip2 compression") |
* [previous](zlib.html "zlib — Compression compatible with gzip") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Compression and Archiving](archiving.html) »
* `gzip` — Support for **gzip** files
* |
* Theme
  Auto
  Light
  Dark
   |

# `gzip` — Support for **gzip** files[¶](#module-gzip "Link to this heading")

**Source code:** [Lib/gzip.py](https://github.com/python/cpython/tree/3.14/Lib/gzip.py)

---

This module provides a simple interface to compress and decompress files just
like the GNU programs **gzip** and **gunzip** would.

This is an [optional module](../glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](../using/configure.html#optional-module-requirements).

The data compression is provided by the [`zlib`](zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module.

The `gzip` module provides the [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") class, as well as the
[`open()`](#gzip.open "gzip.open"), [`compress()`](#gzip.compress "gzip.compress") and [`decompress()`](#gzip.decompress "gzip.decompress") convenience functions.
The [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") class reads and writes **gzip**-format files,
automatically compressing or decompressing the data so that it looks like an
ordinary [file object](../glossary.html#term-file-object).

Note that additional file formats which can be decompressed by the
**gzip** and **gunzip** programs, such as those produced by
**compress** and **pack**, are not supported by this module.

The module defines the following items:

gzip.open(*filename*, *mode='rb'*, *compresslevel=9*, *encoding=None*, *errors=None*, *newline=None*)[¶](#gzip.open "Link to this definition")
:   Open a gzip-compressed file in binary or text mode, returning a [file
    object](../glossary.html#term-file-object).

    The *filename* argument can be an actual filename (a [`str`](stdtypes.html#str "str") or
    [`bytes`](stdtypes.html#bytes "bytes") object), or an existing file object to read from or write to.

    The *mode* argument can be any of `'r'`, `'rb'`, `'a'`, `'ab'`,
    `'w'`, `'wb'`, `'x'` or `'xb'` for binary mode, or `'rt'`,
    `'at'`, `'wt'`, or `'xt'` for text mode. The default is `'rb'`.

    The *compresslevel* argument is an integer from 0 to 9, as for the
    [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") constructor.

    For binary mode, this function is equivalent to the [`GzipFile`](#gzip.GzipFile "gzip.GzipFile")
    constructor: `GzipFile(filename, mode, compresslevel)`. In this case, the
    *encoding*, *errors* and *newline* arguments must not be provided.

    For text mode, a [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") object is created, and wrapped in an
    [`io.TextIOWrapper`](io.html#io.TextIOWrapper "io.TextIOWrapper") instance with the specified encoding, error
    handling behavior, and line ending(s).

    Changed in version 3.3: Added support for *filename* being a file object, support for text mode,
    and the *encoding*, *errors* and *newline* arguments.

    Changed in version 3.4: Added support for the `'x'`, `'xb'` and `'xt'` modes.

    Changed in version 3.6: Accepts a [path-like object](../glossary.html#term-path-like-object).

*exception* gzip.BadGzipFile[¶](#gzip.BadGzipFile "Link to this definition")
:   An exception raised for invalid gzip files. It inherits from [`OSError`](exceptions.html#OSError "OSError").
    [`EOFError`](exceptions.html#EOFError "EOFError") and [`zlib.error`](zlib.html#zlib.error "zlib.error") can also be raised for invalid gzip
    files.

    Added in version 3.8.

*class* gzip.GzipFile(*filename=None*, *mode=None*, *compresslevel=9*, *fileobj=None*, *mtime=None*)[¶](#gzip.GzipFile "Link to this definition")
:   Constructor for the [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") class, which simulates most of the
    methods of a [file object](../glossary.html#term-file-object), with the exception of the [`truncate()`](io.html#io.IOBase.truncate "io.IOBase.truncate")
    method. At least one of *fileobj* and *filename* must be given a non-trivial
    value.

    The new class instance is based on *fileobj*, which can be a regular file, an
    [`io.BytesIO`](io.html#io.BytesIO "io.BytesIO") object, or any other object which simulates a file. It
    defaults to `None`, in which case *filename* is opened to provide a file
    object.

    When *fileobj* is not `None`, the *filename* argument is only used to be
    included in the **gzip** file header, which may include the original
    filename of the uncompressed file. It defaults to the filename of *fileobj*, if
    discernible; otherwise, it defaults to the empty string, and in this case the
    original filename is not included in the header.

    The *mode* argument can be any of `'r'`, `'rb'`, `'a'`, `'ab'`, `'w'`,
    `'wb'`, `'x'`, or `'xb'`, depending on whether the file will be read or
    written. The default is the mode of *fileobj* if discernible; otherwise, the
    default is `'rb'`. In future Python releases the mode of *fileobj* will
    not be used. It is better to always specify *mode* for writing.

    Note that the file is always opened in binary mode. To open a compressed file
    in text mode, use [`open()`](#gzip.open "gzip.open") (or wrap your [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") with an
    [`io.TextIOWrapper`](io.html#io.TextIOWrapper "io.TextIOWrapper")).

    The *compresslevel* argument is an integer from `0` to `9` controlling
    the level of compression; `1` is fastest and produces the least
    compression, and `9` is slowest and produces the most compression. `0`
    is no compression. The default is `9`.

    The optional *mtime* argument is the timestamp requested by gzip. The time
    is in Unix format, i.e., seconds since 00:00:00 UTC, January 1, 1970.
    If *mtime* is omitted or `None`, the current time is used. Use *mtime* = 0
    to generate a compressed stream that does not depend on creation time.

    See below for the [`mtime`](#gzip.GzipFile.mtime "gzip.GzipFile.mtime") attribute that is set when decompressing.

    Calling a [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") object’s `close()` method does not close
    *fileobj*, since you might wish to append more material after the compressed
    data. This also allows you to pass an [`io.BytesIO`](io.html#io.BytesIO "io.BytesIO") object opened for
    writing as *fileobj*, and retrieve the resulting memory buffer using the
    [`io.BytesIO`](io.html#io.BytesIO "io.BytesIO") object’s [`getvalue()`](io.html#io.BytesIO.getvalue "io.BytesIO.getvalue") method.

    [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") supports the [`io.BufferedIOBase`](io.html#io.BufferedIOBase "io.BufferedIOBase") interface,
    including iteration and the [`with`](../reference/compound_stmts.html#with) statement. Only the
    [`truncate()`](io.html#io.IOBase.truncate "io.IOBase.truncate") method isn’t implemented.

    [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") also provides the following method and attribute:

    peek(*n*)[¶](#gzip.GzipFile.peek "Link to this definition")
    :   Read *n* uncompressed bytes without advancing the file position.
        The number of bytes returned may be more or less than requested.

        Note

        While calling [`peek()`](#gzip.GzipFile.peek "gzip.GzipFile.peek") does not change the file position of
        the [`GzipFile`](#gzip.GzipFile "gzip.GzipFile"), it may change the position of the underlying
        file object (e.g. if the [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") was constructed with the
        *fileobj* parameter).

        Added in version 3.2.

    mode[¶](#gzip.GzipFile.mode "Link to this definition")
    :   `'rb'` for reading and `'wb'` for writing.

        Changed in version 3.13: In previous versions it was an integer `1` or `2`.

    mtime[¶](#gzip.GzipFile.mtime "Link to this definition")
    :   When decompressing, this attribute is set to the last timestamp in the most
        recently read header. It is an integer, holding the number of seconds
        since the Unix epoch (00:00:00 UTC, January 1, 1970).
        The initial value before reading any headers is `None`.

    name[¶](#gzip.GzipFile.name "Link to this definition")
    :   The path to the gzip file on disk, as a [`str`](stdtypes.html#str "str") or [`bytes`](stdtypes.html#bytes "bytes").
        Equivalent to the output of [`os.fspath()`](os.html#os.fspath "os.fspath") on the original input path,
        with no other normalization, resolution or expansion.

    Changed in version 3.1: Support for the [`with`](../reference/compound_stmts.html#with) statement was added, along with the
    *mtime* constructor argument and [`mtime`](#gzip.GzipFile.mtime "gzip.GzipFile.mtime") attribute.

    Changed in version 3.2: Support for zero-padded and unseekable files was added.

    Changed in version 3.3: The [`io.BufferedIOBase.read1()`](io.html#io.BufferedIOBase.read1 "io.BufferedIOBase.read1") method is now implemented.

    Changed in version 3.4: Added support for the `'x'` and `'xb'` modes.

    Changed in version 3.5: Added support for writing arbitrary
    [bytes-like objects](../glossary.html#term-bytes-like-object).
    The [`read()`](io.html#io.BufferedIOBase.read "io.BufferedIOBase.read") method now accepts an argument of
    `None`.

    Changed in version 3.6: Accepts a [path-like object](../glossary.html#term-path-like-object).

    Deprecated since version 3.9: Opening [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") for writing without specifying the *mode*
    argument is deprecated.

    Changed in version 3.12: Remove the `filename` attribute, use the [`name`](#gzip.GzipFile.name "gzip.GzipFile.name")
    attribute instead.

gzip.compress(*data*, *compresslevel=9*, *\**, *mtime=0*)[¶](#gzip.compress "Link to this definition")
:   Compress the *data*, returning a [`bytes`](stdtypes.html#bytes "bytes") object containing
    the compressed data. *compresslevel* and *mtime* have the same meaning as in
    the [`GzipFile`](#gzip.GzipFile "gzip.GzipFile") constructor above,
    but *mtime* defaults to 0 for reproducible output.

    Added in version 3.2.

    Changed in version 3.8: Added the *mtime* parameter for reproducible output.

    Changed in version 3.11: Speed is improved by compressing all data at once instead of in a
    streamed fashion. Calls with *mtime* set to `0` are delegated to
    [`zlib.compress()`](zlib.html#zlib.compress "zlib.compress") for better speed. In this situation the
    output may contain a gzip header “OS” byte value other than 255
    “unknown” as supplied by the underlying zlib implementation.

    Changed in version 3.13: The gzip header OS byte is guaranteed to be set to 255 when this function
    is used as was the case in 3.10 and earlier.

    Changed in version 3.14: The *mtime* parameter now defaults to 0 for reproducible output.
    For the previous behaviour of using the current time,
    pass `None` to *mtime*.

gzip.decompress(*data*)[¶](#gzip.decompress "Link to this definition")
:   Decompress the *data*, returning a [`bytes`](stdtypes.html#bytes "bytes") object containing the
    uncompressed data. This function is capable of decompressing multi-member
    gzip data (multiple gzip blocks concatenated together). When the data is
    certain to contain only one member the [`zlib.decompress()`](zlib.html#zlib.decompress "zlib.decompress") function with
    *wbits* set to 31 is faster.

    Added in version 3.2.

    Changed in version 3.11: Speed is improved by decompressing members at once in memory instead of in
    a streamed fashion.

## Examples of usage[¶](#examples-of-usage "Link to this heading")

Example of how to read a compressed file:

```
import gzip
with gzip.open('/home/joe/file.txt.gz', 'rb') as f:
    file_content = f.read()
```

Example of how to create a compressed GZIP file:

```
import gzip
content = b"Lots of content here"
with gzip.open('/home/joe/file.txt.gz', 'wb') as f:
    f.write(content)
```

Example of how to GZIP compress an existing file:

```
import gzip
import shutil
with open('/home/joe/file.txt', 'rb') as f_in:
    with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
```

Example of how to GZIP compress a binary string:

```
import gzip
s_in = b"Lots of content here"
s_out = gzip.compress(s_in)
```

See also

Module [`zlib`](zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")
:   The basic data compression module needed to support the **gzip** file
    format.

In case gzip (de)compression is a bottleneck, the [python-isal](https://github.com/pycompression/python-isal)
package speeds up (de)compression with a mostly compatible API.

## Command-line interface[¶](#command-line-interface "Link to this heading")

The `gzip` module provides a simple command line interface to compress or
decompress files.

Once executed the `gzip` module keeps the input file(s).

Changed in version 3.8: Add a new command line interface with a usage.
By default, when you will execute the CLI, the default compression level is 6.

### Command-line options[¶](#command-line-options "Link to this heading")

file[¶](#cmdoption-gzip-arg-file "Link to this definition")
:   If *file* is not specified, read from [`sys.stdin`](sys.html#sys.stdin "sys.stdin").

--fast[¶](#cmdoption-gzip-fast "Link to this definition")
:   Indicates the fastest compression method (less compression).

--best[¶](#cmdoption-gzip-best "Link to this definition")
:   Indicates the slowest compression method (best compression).

-d, --decompress[¶](#cmdoption-gzip-d "Link to this definition")
:   Decompress the given file.

-h, --help[¶](#cmdoption-gzip-h "Link to this definition")
:   Show the help message.

### [Table of Contents](../contents.html)

* [`gzip` — Support for **gzip** files](#)
  + [Examples of usage](#examples-of-usage)
  + [Command-line interface](#command-line-interface)
    - [Command-line options](#command-line-options)

#### Previous topic

[`zlib` — Compression compatible with **gzip**](zlib.html "previous chapter")

#### Next topic

[`bz2` — Support for **bzip2** compression](bz2.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/gzip.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](bz2.html "bz2 — Support for bzip2 compression") |
* [previous](zlib.html "zlib — Compression compatible with gzip") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Compression and Archiving](archiving.html) »
* `gzip` — Support for **gzip** files
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