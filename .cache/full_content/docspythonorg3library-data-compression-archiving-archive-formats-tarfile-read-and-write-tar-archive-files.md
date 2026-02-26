### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](fileformats.html "File Formats") |
* [previous](zipfile.html "zipfile — Work with ZIP archives") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Compression and Archiving](archiving.html) »
* `tarfile` — Read and write tar archive files
* |
* Theme
  Auto
  Light
  Dark
   |

# `tarfile` — Read and write tar archive files[¶](#module-tarfile "Link to this heading")

**Source code:** [Lib/tarfile.py](https://github.com/python/cpython/tree/3.14/Lib/tarfile.py)

---

The `tarfile` module makes it possible to read and write tar
archives, including those using gzip, bz2 and lzma compression.
Use the [`zipfile`](zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") module to read or write `.zip` files, or the
higher-level functions in [shutil](shutil.html#archiving-operations).

Some facts and figures:

* reads and writes [`gzip`](gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects."), [`bz2`](bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression."), [`compression.zstd`](compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library."), and
  [`lzma`](lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") compressed archives if the respective modules are available.

  If any of these [optional modules](../glossary.html#term-optional-module) are missing from
  your copy of CPython, look for documentation from your distributor (that is,
  whoever provided Python to you).
  If you are the distributor, see [Requirements for optional modules](../using/configure.html#optional-module-requirements).
* read/write support for the POSIX.1-1988 (ustar) format.
* read/write support for the GNU tar format including *longname* and *longlink*
  extensions, read-only support for all variants of the *sparse* extension
  including restoration of sparse files.
* read/write support for the POSIX.1-2001 (pax) format.
* handles directories, regular files, hardlinks, symbolic links, fifos,
  character devices and block devices and is able to acquire and restore file
  information like timestamp, access permissions and owner.

Changed in version 3.3: Added support for [`lzma`](lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") compression.

Changed in version 3.12: Archives are extracted using a [filter](#tarfile-extraction-filter),
which makes it possible to either limit surprising/dangerous features,
or to acknowledge that they are expected and the archive is fully trusted.

Changed in version 3.14: Set the default extraction filter to [`data`](#tarfile.data_filter "tarfile.data_filter"),
which disallows some dangerous features such as links to absolute paths
or paths outside of the destination. Previously, the filter strategy
was equivalent to [`fully_trusted`](#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter").

Changed in version 3.14: Added support for Zstandard compression using [`compression.zstd`](compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.").

tarfile.open(*name=None*, *mode='r'*, *fileobj=None*, *bufsize=10240*, *\*\*kwargs*)[¶](#tarfile.open "Link to this definition")
:   Return a [`TarFile`](#tarfile.TarFile "tarfile.TarFile") object for the pathname *name*. For detailed
    information on [`TarFile`](#tarfile.TarFile "tarfile.TarFile") objects and the keyword arguments that are
    allowed, see [TarFile Objects](#tarfile-objects).

    *mode* has to be a string of the form `'filemode[:compression]'`, it defaults
    to `'r'`. Here is a full list of mode combinations:

    | mode | action |
    | --- | --- |
    | `'r'` or `'r:*'` | Open for reading with transparent compression (recommended). |
    | `'r:'` | Open for reading exclusively without compression. |
    | `'r:gz'` | Open for reading with gzip compression. |
    | `'r:bz2'` | Open for reading with bzip2 compression. |
    | `'r:xz'` | Open for reading with lzma compression. |
    | `'r:zst'` | Open for reading with Zstandard compression. |
    | `'x'` or `'x:'` | Create a tarfile exclusively without compression. Raise a [`FileExistsError`](exceptions.html#FileExistsError "FileExistsError") exception if it already exists. |
    | `'x:gz'` | Create a tarfile with gzip compression. Raise a [`FileExistsError`](exceptions.html#FileExistsError "FileExistsError") exception if it already exists. |
    | `'x:bz2'` | Create a tarfile with bzip2 compression. Raise a [`FileExistsError`](exceptions.html#FileExistsError "FileExistsError") exception if it already exists. |
    | `'x:xz'` | Create a tarfile with lzma compression. Raise a [`FileExistsError`](exceptions.html#FileExistsError "FileExistsError") exception if it already exists. |
    | `'x:zst'` | Create a tarfile with Zstandard compression. Raise a [`FileExistsError`](exceptions.html#FileExistsError "FileExistsError") exception if it already exists. |
    | `'a'` or `'a:'` | Open for appending with no compression. The file is created if it does not exist. |
    | `'w'` or `'w:'` | Open for uncompressed writing. |
    | `'w:gz'` | Open for gzip compressed writing. |
    | `'w:bz2'` | Open for bzip2 compressed writing. |
    | `'w:xz'` | Open for lzma compressed writing. |
    | `'w:zst'` | Open for Zstandard compressed writing. |

    Note that `'a:gz'`, `'a:bz2'` or `'a:xz'` is not possible. If *mode*
    is not suitable to open a certain (compressed) file for reading,
    [`ReadError`](#tarfile.ReadError "tarfile.ReadError") is raised. Use *mode* `'r'` to avoid this. If a
    compression method is not supported, [`CompressionError`](#tarfile.CompressionError "tarfile.CompressionError") is raised.

    If *fileobj* is specified, it is used as an alternative to a [file object](../glossary.html#term-file-object)
    opened in binary mode for *name*. It is supposed to be at position 0.

    For modes `'w:gz'`, `'x:gz'`, `'w|gz'`, `'w:bz2'`, `'x:bz2'`,
    `'w|bz2'`, [`tarfile.open()`](#tarfile.open "tarfile.open") accepts the keyword argument
    *compresslevel* (default `9`) to specify the compression level of the file.

    For modes `'w:xz'`, `'x:xz'` and `'w|xz'`, [`tarfile.open()`](#tarfile.open "tarfile.open") accepts the
    keyword argument *preset* to specify the compression level of the file.

    For modes `'w:zst'`, `'x:zst'` and `'w|zst'`, [`tarfile.open()`](#tarfile.open "tarfile.open")
    accepts the keyword argument *level* to specify the compression level of
    the file. The keyword argument *options* may also be passed, providing
    advanced Zstandard compression parameters described by
    [`CompressionParameter`](compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter"). The keyword argument
    *zstd\_dict* can be passed to provide a [`ZstdDict`](compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict"),
    a Zstandard dictionary used to improve compression of smaller amounts of
    data.

    For special purposes, there is a second format for *mode*:
    `'filemode|[compression]'`. [`tarfile.open()`](#tarfile.open "tarfile.open") will return a [`TarFile`](#tarfile.TarFile "tarfile.TarFile")
    object that processes its data as a stream of blocks. No random seeking will
    be done on the file. If given, *fileobj* may be any object that has a
    [`read()`](io.html#io.RawIOBase.read "io.RawIOBase.read") or [`write()`](io.html#io.RawIOBase.write "io.RawIOBase.write") method
    (depending on the *mode*) that works with bytes.
    *bufsize* specifies the blocksize and defaults to `20 * 512` bytes.
    Use this variant in combination with e.g. `sys.stdin.buffer`, a socket
    [file object](../glossary.html#term-file-object) or a tape device.
    However, such a [`TarFile`](#tarfile.TarFile "tarfile.TarFile") object is limited in that it does
    not allow random access, see [Examples](#tar-examples). The currently
    possible modes:

    | Mode | Action |
    | --- | --- |
    | `'r|*'` | Open a *stream* of tar blocks for reading with transparent compression. |
    | `'r|'` | Open a *stream* of uncompressed tar blocks for reading. |
    | `'r|gz'` | Open a gzip compressed *stream* for reading. |
    | `'r|bz2'` | Open a bzip2 compressed *stream* for reading. |
    | `'r|xz'` | Open an lzma compressed *stream* for reading. |
    | `'r|zst'` | Open a Zstandard compressed *stream* for reading. |
    | `'w|'` | Open an uncompressed *stream* for writing. |
    | `'w|gz'` | Open a gzip compressed *stream* for writing. |
    | `'w|bz2'` | Open a bzip2 compressed *stream* for writing. |
    | `'w|xz'` | Open an lzma compressed *stream* for writing. |
    | `'w|zst'` | Open a Zstandard compressed *stream* for writing. |

    Changed in version 3.5: The `'x'` (exclusive creation) mode was added.

    Changed in version 3.6: The *name* parameter accepts a [path-like object](../glossary.html#term-path-like-object).

    Changed in version 3.12: The *compresslevel* keyword argument also works for streams.

    Changed in version 3.14: The *preset* keyword argument also works for streams.

*class* tarfile.TarFile
:   Class for reading and writing tar archives. Do not use this class directly:
    use [`tarfile.open()`](#tarfile.open "tarfile.open") instead. See [TarFile Objects](#tarfile-objects).

tarfile.is\_tarfile(*name*)[¶](#tarfile.is_tarfile "Link to this definition")
:   Return [`True`](constants.html#True "True") if *name* is a tar archive file, that the `tarfile`
    module can read. *name* may be a [`str`](stdtypes.html#str "str"), file, or file-like object.

    Changed in version 3.9: Support for file and file-like objects.

The `tarfile` module defines the following exceptions:

*exception* tarfile.TarError[¶](#tarfile.TarError "Link to this definition")
:   Base class for all `tarfile` exceptions.

*exception* tarfile.ReadError[¶](#tarfile.ReadError "Link to this definition")
:   Is raised when a tar archive is opened, that either cannot be handled by the
    `tarfile` module or is somehow invalid.

*exception* tarfile.CompressionError[¶](#tarfile.CompressionError "Link to this definition")
:   Is raised when a compression method is not supported or when the data cannot be
    decoded properly.

*exception* tarfile.StreamError[¶](#tarfile.StreamError "Link to this definition")
:   Is raised for the limitations that are typical for stream-like [`TarFile`](#tarfile.TarFile "tarfile.TarFile")
    objects.

*exception* tarfile.ExtractError[¶](#tarfile.ExtractError "Link to this definition")
:   Is raised for *non-fatal* errors when using [`TarFile.extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract"), but only if
    [`TarFile.errorlevel`](#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel")`== 2`.

*exception* tarfile.HeaderError[¶](#tarfile.HeaderError "Link to this definition")
:   Is raised by [`TarInfo.frombuf()`](#tarfile.TarInfo.frombuf "tarfile.TarInfo.frombuf") if the buffer it gets is invalid.

*exception* tarfile.FilterError[¶](#tarfile.FilterError "Link to this definition")
:   Base class for members [refused](#tarfile-extraction-refuse) by
    filters.

    tarinfo[¶](#tarfile.FilterError.tarinfo "Link to this definition")
    :   Information about the member that the filter refused to extract,
        as [TarInfo](#tarinfo-objects).

*exception* tarfile.AbsolutePathError[¶](#tarfile.AbsolutePathError "Link to this definition")
:   Raised to refuse extracting a member with an absolute path.

*exception* tarfile.OutsideDestinationError[¶](#tarfile.OutsideDestinationError "Link to this definition")
:   Raised to refuse extracting a member outside the destination directory.

*exception* tarfile.SpecialFileError[¶](#tarfile.SpecialFileError "Link to this definition")
:   Raised to refuse extracting a special file (e.g. a device or pipe).

*exception* tarfile.AbsoluteLinkError[¶](#tarfile.AbsoluteLinkError "Link to this definition")
:   Raised to refuse extracting a symbolic link with an absolute path.

*exception* tarfile.LinkOutsideDestinationError[¶](#tarfile.LinkOutsideDestinationError "Link to this definition")
:   Raised to refuse extracting a symbolic link pointing outside the destination
    directory.

*exception* tarfile.LinkFallbackError[¶](#tarfile.LinkFallbackError "Link to this definition")
:   Raised to refuse emulating a link (hard or symbolic) by extracting another
    archive member, when that member would be rejected by the filter location.
    The exception that was raised to reject the replacement member is available
    as `BaseException.__context__`.

    Added in version 3.14.

The following constants are available at the module level:

tarfile.ENCODING[¶](#tarfile.ENCODING "Link to this definition")
:   The default character encoding: `'utf-8'` on Windows, the value returned by
    [`sys.getfilesystemencoding()`](sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") otherwise.

tarfile.REGTYPE[¶](#tarfile.REGTYPE "Link to this definition")

tarfile.AREGTYPE[¶](#tarfile.AREGTYPE "Link to this definition")
:   A regular file [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.LNKTYPE[¶](#tarfile.LNKTYPE "Link to this definition")
:   A link (inside tarfile) [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.SYMTYPE[¶](#tarfile.SYMTYPE "Link to this definition")
:   A symbolic link [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.CHRTYPE[¶](#tarfile.CHRTYPE "Link to this definition")
:   A character special device [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.BLKTYPE[¶](#tarfile.BLKTYPE "Link to this definition")
:   A block special device [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.DIRTYPE[¶](#tarfile.DIRTYPE "Link to this definition")
:   A directory [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.FIFOTYPE[¶](#tarfile.FIFOTYPE "Link to this definition")
:   A FIFO special device [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.CONTTYPE[¶](#tarfile.CONTTYPE "Link to this definition")
:   A contiguous file [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.GNUTYPE\_LONGNAME[¶](#tarfile.GNUTYPE_LONGNAME "Link to this definition")
:   A GNU tar longname [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.GNUTYPE\_LONGLINK[¶](#tarfile.GNUTYPE_LONGLINK "Link to this definition")
:   A GNU tar longlink [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.GNUTYPE\_SPARSE[¶](#tarfile.GNUTYPE_SPARSE "Link to this definition")
:   A GNU tar sparse file [`type`](#tarfile.TarInfo.type "tarfile.TarInfo.type").

Each of the following constants defines a tar archive format that the
`tarfile` module is able to create. See section [Supported tar formats](#tar-formats) for
details.

tarfile.USTAR\_FORMAT[¶](#tarfile.USTAR_FORMAT "Link to this definition")
:   POSIX.1-1988 (ustar) format.

tarfile.GNU\_FORMAT[¶](#tarfile.GNU_FORMAT "Link to this definition")
:   GNU tar format.

tarfile.PAX\_FORMAT[¶](#tarfile.PAX_FORMAT "Link to this definition")
:   POSIX.1-2001 (pax) format.

tarfile.DEFAULT\_FORMAT[¶](#tarfile.DEFAULT_FORMAT "Link to this definition")
:   The default format for creating archives. This is currently [`PAX_FORMAT`](#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT").

    Changed in version 3.8: The default format for new archives was changed to
    [`PAX_FORMAT`](#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT") from [`GNU_FORMAT`](#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT").

See also

Module [`zipfile`](zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.")
:   Documentation of the [`zipfile`](zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") standard module.

[Archiving operations](shutil.html#archiving-operations)
:   Documentation of the higher-level archiving facilities provided by the
    standard [`shutil`](shutil.html#module-shutil "shutil: High-level file operations, including copying.") module.

[GNU tar manual, Basic Tar Format](https://www.gnu.org/software/tar/manual/html_node/Standard.html)
:   Documentation for tar archive files, including GNU tar extensions.

## TarFile Objects[¶](#tarfile-objects "Link to this heading")

The [`TarFile`](#tarfile.TarFile "tarfile.TarFile") object provides an interface to a tar archive. A tar
archive is a sequence of blocks. An archive member (a stored file) is made up of
a header block followed by data blocks. It is possible to store a file in a tar
archive several times. Each archive member is represented by a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo")
object, see [TarInfo Objects](#tarinfo-objects) for details.

A [`TarFile`](#tarfile.TarFile "tarfile.TarFile") object can be used as a context manager in a [`with`](../reference/compound_stmts.html#with)
statement. It will automatically be closed when the block is completed. Please
note that in the event of an exception an archive opened for writing will not
be finalized; only the internally used file object will be closed. See the
[Examples](#tar-examples) section for a use case.

Added in version 3.2: Added support for the context management protocol.

*class* tarfile.TarFile(*name=None*, *mode='r'*, *fileobj=None*, *format=DEFAULT\_FORMAT*, *tarinfo=TarInfo*, *dereference=False*, *ignore\_zeros=False*, *encoding=ENCODING*, *errors='surrogateescape'*, *pax\_headers=None*, *debug=0*, *errorlevel=1*, *stream=False*)[¶](#tarfile.TarFile "Link to this definition")
:   All following arguments are optional and can be accessed as instance attributes
    as well.

    *name* is the pathname of the archive. *name* may be a [path-like object](../glossary.html#term-path-like-object).
    It can be omitted if *fileobj* is given.
    In this case, the file object’s `name` attribute is used if it exists.

    *mode* is either `'r'` to read from an existing archive, `'a'` to append
    data to an existing file, `'w'` to create a new file overwriting an existing
    one, or `'x'` to create a new file only if it does not already exist.

    If *fileobj* is given, it is used for reading or writing data. If it can be
    determined, *mode* is overridden by *fileobj*’s mode. *fileobj* will be used
    from position 0.

    Note

    *fileobj* is not closed, when [`TarFile`](#tarfile.TarFile "tarfile.TarFile") is closed.

    *format* controls the archive format for writing. It must be one of the constants
    [`USTAR_FORMAT`](#tarfile.USTAR_FORMAT "tarfile.USTAR_FORMAT"), [`GNU_FORMAT`](#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT") or [`PAX_FORMAT`](#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT") that are
    defined at module level. When reading, format will be automatically detected, even
    if different formats are present in a single archive.

    The *tarinfo* argument can be used to replace the default [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") class
    with a different one.

    If *dereference* is [`False`](constants.html#False "False"), add symbolic and hard links to the archive. If it
    is [`True`](constants.html#True "True"), add the content of the target files to the archive. This has no
    effect on systems that do not support symbolic links.

    If *ignore\_zeros* is [`False`](constants.html#False "False"), treat an empty block as the end of the archive.
    If it is [`True`](constants.html#True "True"), skip empty (and invalid) blocks and try to get as many members
    as possible. This is only useful for reading concatenated or damaged archives.

    *debug* can be set from `0` (no debug messages) up to `3` (all debug
    messages). The messages are written to `sys.stderr`.

    *errorlevel* controls how extraction errors are handled,
    see [`the corresponding attribute`](#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel").

    The *encoding* and *errors* arguments define the character encoding to be
    used for reading or writing the archive and how conversion errors are going
    to be handled. The default settings will work for most users.
    See section [Unicode issues](#tar-unicode) for in-depth information.

    The *pax\_headers* argument is an optional dictionary of strings which
    will be added as a pax global header if *format* is [`PAX_FORMAT`](#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT").

    If *stream* is set to [`True`](constants.html#True "True") then while reading the archive info about files
    in the archive are not cached, saving memory.

    Changed in version 3.2: Use `'surrogateescape'` as the default for the *errors* argument.

    Changed in version 3.5: The `'x'` (exclusive creation) mode was added.

    Changed in version 3.6: The *name* parameter accepts a [path-like object](../glossary.html#term-path-like-object).

    Changed in version 3.13: Add the *stream* parameter.

*classmethod* TarFile.open(*...*)[¶](#tarfile.TarFile.open "Link to this definition")
:   Alternative constructor. The [`tarfile.open()`](#tarfile.open "tarfile.open") function is actually a
    shortcut to this classmethod.

TarFile.getmember(*name*)[¶](#tarfile.TarFile.getmember "Link to this definition")
:   Return a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object for member *name*. If *name* can not be found
    in the archive, [`KeyError`](exceptions.html#KeyError "KeyError") is raised.

    Note

    If a member occurs more than once in the archive, its last occurrence is assumed
    to be the most up-to-date version.

TarFile.getmembers()[¶](#tarfile.TarFile.getmembers "Link to this definition")
:   Return the members of the archive as a list of [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") objects. The
    list has the same order as the members in the archive.

TarFile.getnames()[¶](#tarfile.TarFile.getnames "Link to this definition")
:   Return the members as a list of their names. It has the same order as the list
    returned by [`getmembers()`](#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers").

TarFile.list(*verbose=True*, *\**, *members=None*)[¶](#tarfile.TarFile.list "Link to this definition")
:   Print a table of contents to `sys.stdout`. If *verbose* is [`False`](constants.html#False "False"),
    only the names of the members are printed. If it is [`True`](constants.html#True "True"), output
    similar to that of **ls -l** is produced. If optional *members* is
    given, it must be a subset of the list returned by [`getmembers()`](#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers").

    Changed in version 3.5: Added the *members* parameter.

TarFile.next()[¶](#tarfile.TarFile.next "Link to this definition")
:   Return the next member of the archive as a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object, when
    [`TarFile`](#tarfile.TarFile "tarfile.TarFile") is opened for reading. Return [`None`](constants.html#None "None") if there is no more
    available.

TarFile.extractall(*path='.'*, *members=None*, *\**, *numeric\_owner=False*, *filter=None*)[¶](#tarfile.TarFile.extractall "Link to this definition")
:   Extract all members from the archive to the current working directory or
    directory *path*. If optional *members* is given, it must be a subset of the
    list returned by [`getmembers()`](#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers"). Directory information like owner,
    modification time and permissions are set after all members have been extracted.
    This is done to work around two problems: A directory’s modification time is
    reset each time a file is created in it. And, if a directory’s permissions do
    not allow writing, extracting files to it will fail.

    If *numeric\_owner* is [`True`](constants.html#True "True"), the uid and gid numbers from the tarfile
    are used to set the owner/group for the extracted files. Otherwise, the named
    values from the tarfile are used.

    The *filter* argument specifies how `members` are modified or rejected
    before extraction.
    See [Extraction filters](#tarfile-extraction-filter) for details.
    It is recommended to set this explicitly only if specific *tar* features
    are required, or as `filter='data'` to support Python versions with a less
    secure default (3.13 and lower).

    Warning

    Never extract archives from untrusted sources without prior inspection.

    Since Python 3.14, the default ([`data`](#tarfile.data_filter "tarfile.data_filter")) will prevent
    the most dangerous security issues.
    However, it will not prevent *all* unintended or insecure behavior.
    Read the [Extraction filters](#tarfile-extraction-filter) section for details.

    Changed in version 3.5: Added the *numeric\_owner* parameter.

    Changed in version 3.6: The *path* parameter accepts a [path-like object](../glossary.html#term-path-like-object).

    Changed in version 3.12: Added the *filter* parameter.

    Changed in version 3.14: The *filter* parameter now defaults to `'data'`.

TarFile.extract(*member*, *path=''*, *set\_attrs=True*, *\**, *numeric\_owner=False*, *filter=None*)[¶](#tarfile.TarFile.extract "Link to this definition")
:   Extract a member from the archive to the current working directory, using its
    full name. Its file information is extracted as accurately as possible. *member*
    may be a filename or a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object. You can specify a different
    directory using *path*. *path* may be a [path-like object](../glossary.html#term-path-like-object).
    File attributes (owner, mtime, mode) are set unless *set\_attrs* is false.

    The *numeric\_owner* and *filter* arguments are the same as
    for [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall").

    Note

    The [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract") method does not take care of several extraction issues.
    In most cases you should consider using the [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall") method.

    Warning

    Never extract archives from untrusted sources without prior inspection.
    See the warning for [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall") for details.

    Changed in version 3.2: Added the *set\_attrs* parameter.

    Changed in version 3.5: Added the *numeric\_owner* parameter.

    Changed in version 3.6: The *path* parameter accepts a [path-like object](../glossary.html#term-path-like-object).

    Changed in version 3.12: Added the *filter* parameter.

TarFile.extractfile(*member*)[¶](#tarfile.TarFile.extractfile "Link to this definition")
:   Extract a member from the archive as a file object. *member* may be
    a filename or a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object. If *member* is a regular file or
    a link, an [`io.BufferedReader`](io.html#io.BufferedReader "io.BufferedReader") object is returned. For all other
    existing members, [`None`](constants.html#None "None") is returned. If *member* does not appear
    in the archive, [`KeyError`](exceptions.html#KeyError "KeyError") is raised.

    Changed in version 3.3: Return an [`io.BufferedReader`](io.html#io.BufferedReader "io.BufferedReader") object.

    Changed in version 3.13: The returned [`io.BufferedReader`](io.html#io.BufferedReader "io.BufferedReader") object has the `mode`
    attribute which is always equal to `'rb'`.

TarFile.errorlevel*: [int](functions.html#int "int")*[¶](#tarfile.TarFile.errorlevel "Link to this definition")
:   If *errorlevel* is `0`, errors are ignored when using [`TarFile.extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract")
    and [`TarFile.extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall").
    Nevertheless, they appear as error messages in the debug output when
    *debug* is greater than 0.
    If `1` (the default), all *fatal* errors are raised as [`OSError`](exceptions.html#OSError "OSError") or
    [`FilterError`](#tarfile.FilterError "tarfile.FilterError") exceptions. If `2`, all *non-fatal* errors are raised
    as [`TarError`](#tarfile.TarError "tarfile.TarError") exceptions as well.

    Some exceptions, e.g. ones caused by wrong argument types or data
    corruption, are always raised.

    Custom [extraction filters](#tarfile-extraction-filter)
    should raise [`FilterError`](#tarfile.FilterError "tarfile.FilterError") for *fatal* errors
    and [`ExtractError`](#tarfile.ExtractError "tarfile.ExtractError") for *non-fatal* ones.

    Note that when an exception is raised, the archive may be partially
    extracted. It is the user’s responsibility to clean up.

TarFile.extraction\_filter[¶](#tarfile.TarFile.extraction_filter "Link to this definition")
:   Added in version 3.12.

    The [extraction filter](#tarfile-extraction-filter) used
    as a default for the *filter* argument of [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract")
    and [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall").

    The attribute may be `None` or a callable.
    String names are not allowed for this attribute, unlike the *filter*
    argument to [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract").

    If `extraction_filter` is `None` (the default), extraction methods
    will use the [`data`](#tarfile.data_filter "tarfile.data_filter") filter by default.

    The attribute may be set on instances or overridden in subclasses.
    It also is possible to set it on the `TarFile` class itself to set a
    global default, although, since it affects all uses of *tarfile*,
    it is best practice to only do so in top-level applications or
    [`site configuration`](site.html#module-site "site: Module responsible for site-specific configuration.").
    To set a global default this way, a filter function needs to be wrapped in
    [`staticmethod()`](functions.html#staticmethod "staticmethod") to prevent injection of a `self` argument.

    Changed in version 3.14: The default filter is set to [`data`](#tarfile.data_filter "tarfile.data_filter"),
    which disallows some dangerous features such as links to absolute paths
    or paths outside of the destination.
    Previously, the default was equivalent to
    [`fully_trusted`](#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter").

TarFile.add(*name*, *arcname=None*, *recursive=True*, *\**, *filter=None*)[¶](#tarfile.TarFile.add "Link to this definition")
:   Add the file *name* to the archive. *name* may be any type of file
    (directory, fifo, symbolic link, etc.). If given, *arcname* specifies an
    alternative name for the file in the archive. Directories are added
    recursively by default. This can be avoided by setting *recursive* to
    [`False`](constants.html#False "False"). Recursion adds entries in sorted order.
    If *filter* is given, it
    should be a function that takes a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object argument and
    returns the changed [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object. If it instead returns
    [`None`](constants.html#None "None") the [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object will be excluded from the
    archive. See [Examples](#tar-examples) for an example.

    Changed in version 3.2: Added the *filter* parameter.

    Changed in version 3.7: Recursion adds entries in sorted order.

TarFile.addfile(*tarinfo*, *fileobj=None*)[¶](#tarfile.TarFile.addfile "Link to this definition")
:   Add the [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object *tarinfo* to the archive. If *tarinfo* represents
    a non zero-size regular file, the *fileobj* argument should be a [binary file](../glossary.html#term-binary-file),
    and `tarinfo.size` bytes are read from it and added to the archive. You can
    create [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") objects directly, or by using [`gettarinfo()`](#tarfile.TarFile.gettarinfo "tarfile.TarFile.gettarinfo").

    Changed in version 3.13: *fileobj* must be given for non-zero-sized regular files.

TarFile.gettarinfo(*name=None*, *arcname=None*, *fileobj=None*)[¶](#tarfile.TarFile.gettarinfo "Link to this definition")
:   Create a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object from the result of [`os.stat()`](os.html#os.stat "os.stat") or
    equivalent on an existing file. The file is either named by *name*, or
    specified as a [file object](../glossary.html#term-file-object) *fileobj* with a file descriptor.
    *name* may be a [path-like object](../glossary.html#term-path-like-object). If
    given, *arcname* specifies an alternative name for the file in the
    archive, otherwise, the name is taken from *fileobj*’s
    [`name`](io.html#io.FileIO.name "io.FileIO.name") attribute, or the *name* argument. The name
    should be a text string.

    You can modify
    some of the [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo")’s attributes before you add it using [`addfile()`](#tarfile.TarFile.addfile "tarfile.TarFile.addfile").
    If the file object is not an ordinary file object positioned at the
    beginning of the file, attributes such as [`size`](#tarfile.TarInfo.size "tarfile.TarInfo.size") may need
    modifying. This is the case for objects such as [`GzipFile`](gzip.html#gzip.GzipFile "gzip.GzipFile").
    The [`name`](#tarfile.TarInfo.name "tarfile.TarInfo.name") may also be modified, in which case *arcname*
    could be a dummy string.

    Changed in version 3.6: The *name* parameter accepts a [path-like object](../glossary.html#term-path-like-object).

TarFile.close()[¶](#tarfile.TarFile.close "Link to this definition")
:   Close the [`TarFile`](#tarfile.TarFile "tarfile.TarFile"). In write mode, two finishing zero blocks are
    appended to the archive.

TarFile.pax\_headers*: [dict](stdtypes.html#dict "dict")*[¶](#tarfile.TarFile.pax_headers "Link to this definition")
:   A dictionary containing key-value pairs of pax global headers.

## TarInfo Objects[¶](#tarinfo-objects "Link to this heading")

A [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object represents one member in a [`TarFile`](#tarfile.TarFile "tarfile.TarFile"). Aside
from storing all required attributes of a file (like file type, size, time,
permissions, owner etc.), it provides some useful methods to determine its type.
It does *not* contain the file’s data itself.

[`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") objects are returned by [`TarFile`](#tarfile.TarFile "tarfile.TarFile")’s methods
[`getmember()`](#tarfile.TarFile.getmember "tarfile.TarFile.getmember"), [`getmembers()`](#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers") and
[`gettarinfo()`](#tarfile.TarFile.gettarinfo "tarfile.TarFile.gettarinfo").

Modifying the objects returned by [`getmember()`](#tarfile.TarFile.getmember "tarfile.TarFile.getmember") or
[`getmembers()`](#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers") will affect all subsequent
operations on the archive.
For cases where this is unwanted, you can use [`copy.copy()`](copy.html#module-copy "copy: Shallow and deep copy operations.") or
call the [`replace()`](#tarfile.TarInfo.replace "tarfile.TarInfo.replace") method to create a modified copy in one step.

Several attributes can be set to `None` to indicate that a piece of metadata
is unused or unknown.
Different [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") methods handle `None` differently:

* The [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract") or [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall") methods will
  ignore the corresponding metadata, leaving it set to a default.
* [`addfile()`](#tarfile.TarFile.addfile "tarfile.TarFile.addfile") will fail.
* [`list()`](#tarfile.TarFile.list "tarfile.TarFile.list") will print a placeholder string.

*class* tarfile.TarInfo(*name=''*)[¶](#tarfile.TarInfo "Link to this definition")
:   Create a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object.

*classmethod* TarInfo.frombuf(*buf*, *encoding*, *errors*)[¶](#tarfile.TarInfo.frombuf "Link to this definition")
:   Create and return a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object from string buffer *buf*.

    Raises [`HeaderError`](#tarfile.HeaderError "tarfile.HeaderError") if the buffer is invalid.

*classmethod* TarInfo.fromtarfile(*tarfile*)[¶](#tarfile.TarInfo.fromtarfile "Link to this definition")
:   Read the next member from the [`TarFile`](#tarfile.TarFile "tarfile.TarFile") object *tarfile* and return it as
    a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object.

TarInfo.tobuf(*format=DEFAULT\_FORMAT*, *encoding=ENCODING*, *errors='surrogateescape'*)[¶](#tarfile.TarInfo.tobuf "Link to this definition")
:   Create a string buffer from a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object. For information on the
    arguments see the constructor of the [`TarFile`](#tarfile.TarFile "tarfile.TarFile") class.

    Changed in version 3.2: Use `'surrogateescape'` as the default for the *errors* argument.

A `TarInfo` object has the following public data attributes:

TarInfo.name*: [str](stdtypes.html#str "str")*[¶](#tarfile.TarInfo.name "Link to this definition")
:   Name of the archive member.

TarInfo.size*: [int](functions.html#int "int")*[¶](#tarfile.TarInfo.size "Link to this definition")
:   Size in bytes.

TarInfo.mtime*: [int](functions.html#int "int") | [float](functions.html#float "float")*[¶](#tarfile.TarInfo.mtime "Link to this definition")
:   Time of last modification in seconds since the [epoch](time.html#epoch),
    as in [`os.stat_result.st_mtime`](os.html#os.stat_result.st_mtime "os.stat_result.st_mtime").

    Changed in version 3.12: Can be set to `None` for [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract") and
    [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this
    attribute.

TarInfo.mode*: [int](functions.html#int "int")*[¶](#tarfile.TarInfo.mode "Link to this definition")
:   Permission bits, as for [`os.chmod()`](os.html#os.chmod "os.chmod").

    Changed in version 3.12: Can be set to `None` for [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract") and
    [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this
    attribute.

TarInfo.type[¶](#tarfile.TarInfo.type "Link to this definition")
:   File type. *type* is usually one of these constants: [`REGTYPE`](#tarfile.REGTYPE "tarfile.REGTYPE"),
    [`AREGTYPE`](#tarfile.AREGTYPE "tarfile.AREGTYPE"), [`LNKTYPE`](#tarfile.LNKTYPE "tarfile.LNKTYPE"), [`SYMTYPE`](#tarfile.SYMTYPE "tarfile.SYMTYPE"), [`DIRTYPE`](#tarfile.DIRTYPE "tarfile.DIRTYPE"),
    [`FIFOTYPE`](#tarfile.FIFOTYPE "tarfile.FIFOTYPE"), [`CONTTYPE`](#tarfile.CONTTYPE "tarfile.CONTTYPE"), [`CHRTYPE`](#tarfile.CHRTYPE "tarfile.CHRTYPE"), [`BLKTYPE`](#tarfile.BLKTYPE "tarfile.BLKTYPE"),
    [`GNUTYPE_SPARSE`](#tarfile.GNUTYPE_SPARSE "tarfile.GNUTYPE_SPARSE"). To determine the type of a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object
    more conveniently, use the `is*()` methods below.

TarInfo.linkname*: [str](stdtypes.html#str "str")*[¶](#tarfile.TarInfo.linkname "Link to this definition")
:   Name of the target file name, which is only present in [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") objects
    of type [`LNKTYPE`](#tarfile.LNKTYPE "tarfile.LNKTYPE") and [`SYMTYPE`](#tarfile.SYMTYPE "tarfile.SYMTYPE").

    For symbolic links (`SYMTYPE`), the *linkname* is relative to the directory
    that contains the link.
    For hard links (`LNKTYPE`), the *linkname* is relative to the root of
    the archive.

TarInfo.uid*: [int](functions.html#int "int")*[¶](#tarfile.TarInfo.uid "Link to this definition")
:   User ID of the user who originally stored this member.

    Changed in version 3.12: Can be set to `None` for [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract") and
    [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this
    attribute.

TarInfo.gid*: [int](functions.html#int "int")*[¶](#tarfile.TarInfo.gid "Link to this definition")
:   Group ID of the user who originally stored this member.

    Changed in version 3.12: Can be set to `None` for [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract") and
    [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this
    attribute.

TarInfo.uname*: [str](stdtypes.html#str "str")*[¶](#tarfile.TarInfo.uname "Link to this definition")
:   User name.

    Changed in version 3.12: Can be set to `None` for [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract") and
    [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this
    attribute.

TarInfo.gname*: [str](stdtypes.html#str "str")*[¶](#tarfile.TarInfo.gname "Link to this definition")
:   Group name.

    Changed in version 3.12: Can be set to `None` for [`extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract") and
    [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this
    attribute.

TarInfo.chksum*: [int](functions.html#int "int")*[¶](#tarfile.TarInfo.chksum "Link to this definition")
:   Header checksum.

TarInfo.devmajor*: [int](functions.html#int "int")*[¶](#tarfile.TarInfo.devmajor "Link to this definition")
:   Device major number.

TarInfo.devminor*: [int](functions.html#int "int")*[¶](#tarfile.TarInfo.devminor "Link to this definition")
:   Device minor number.

TarInfo.offset*: [int](functions.html#int "int")*[¶](#tarfile.TarInfo.offset "Link to this definition")
:   The tar header starts here.

TarInfo.offset\_data*: [int](functions.html#int "int")*[¶](#tarfile.TarInfo.offset_data "Link to this definition")
:   The file’s data starts here.

TarInfo.sparse[¶](#tarfile.TarInfo.sparse "Link to this definition")
:   Sparse member information.

TarInfo.pax\_headers*: [dict](stdtypes.html#dict "dict")*[¶](#tarfile.TarInfo.pax_headers "Link to this definition")
:   A dictionary containing key-value pairs of an associated pax extended header.

TarInfo.replace(*name=...*, *mtime=...*, *mode=...*, *linkname=...*, *uid=...*, *gid=...*, *uname=...*, *gname=...*, *deep=True*)[¶](#tarfile.TarInfo.replace "Link to this definition")
:   Added in version 3.12.

    Return a *new* copy of the `TarInfo` object with the given attributes
    changed. For example, to return a `TarInfo` with the group name set to
    `'staff'`, use:

    ```
    new_tarinfo = old_tarinfo.replace(gname='staff')
    ```

    By default, a deep copy is made.
    If *deep* is false, the copy is shallow, i.e. `pax_headers`
    and any custom attributes are shared with the original `TarInfo` object.

A [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object also provides some convenient query methods:

TarInfo.isfile()[¶](#tarfile.TarInfo.isfile "Link to this definition")
:   Return [`True`](constants.html#True "True") if the [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object is a regular file.

TarInfo.isreg()[¶](#tarfile.TarInfo.isreg "Link to this definition")
:   Same as [`isfile()`](#tarfile.TarInfo.isfile "tarfile.TarInfo.isfile").

TarInfo.isdir()[¶](#tarfile.TarInfo.isdir "Link to this definition")
:   Return [`True`](constants.html#True "True") if it is a directory.

TarInfo.issym()[¶](#tarfile.TarInfo.issym "Link to this definition")
:   Return [`True`](constants.html#True "True") if it is a symbolic link.

TarInfo.islnk()[¶](#tarfile.TarInfo.islnk "Link to this definition")
:   Return [`True`](constants.html#True "True") if it is a hard link.

TarInfo.ischr()[¶](#tarfile.TarInfo.ischr "Link to this definition")
:   Return [`True`](constants.html#True "True") if it is a character device.

TarInfo.isblk()[¶](#tarfile.TarInfo.isblk "Link to this definition")
:   Return [`True`](constants.html#True "True") if it is a block device.

TarInfo.isfifo()[¶](#tarfile.TarInfo.isfifo "Link to this definition")
:   Return [`True`](constants.html#True "True") if it is a FIFO.

TarInfo.isdev()[¶](#tarfile.TarInfo.isdev "Link to this definition")
:   Return [`True`](constants.html#True "True") if it is one of character device, block device or FIFO.

## Extraction filters[¶](#extraction-filters "Link to this heading")

Added in version 3.12.

The *tar* format is designed to capture all details of a UNIX-like filesystem,
which makes it very powerful.
Unfortunately, the features make it easy to create tar files that have
unintended – and possibly malicious – effects when extracted.
For example, extracting a tar file can overwrite arbitrary files in various
ways (e.g. by using absolute paths, `..` path components, or symlinks that
affect later members).

In most cases, the full functionality is not needed.
Therefore, *tarfile* supports extraction filters: a mechanism to limit
functionality, and thus mitigate some of the security issues.

Warning

None of the available filters blocks *all* dangerous archive features.
Never extract archives from untrusted sources without prior inspection.
See also [Hints for further verification](#tarfile-further-verification).

See also

[**PEP 706**](https://peps.python.org/pep-0706/)
:   Contains further motivation and rationale behind the design.

The *filter* argument to [`TarFile.extract()`](#tarfile.TarFile.extract "tarfile.TarFile.extract") or [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
can be:

* the string `'fully_trusted'`: Honor all metadata as specified in the
  archive.
  Should be used if the user trusts the archive completely, or implements
  their own complex verification.
* the string `'tar'`: Honor most *tar*-specific features (i.e. features of
  UNIX-like filesystems), but block features that are very likely to be
  surprising or malicious. See [`tar_filter()`](#tarfile.tar_filter "tarfile.tar_filter") for details.
* the string `'data'`: Ignore or block most features specific to UNIX-like
  filesystems. Intended for extracting cross-platform data archives.
  See [`data_filter()`](#tarfile.data_filter "tarfile.data_filter") for details.
* `None` (default): Use [`TarFile.extraction_filter`](#tarfile.TarFile.extraction_filter "tarfile.TarFile.extraction_filter").

  If that is also `None` (the default), the `'data'` filter will be used.

  > Changed in version 3.14: The default filter is set to [`data`](#tarfile.data_filter "tarfile.data_filter").
  > Previously, the default was equivalent to
  > [`fully_trusted`](#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter").
* A callable which will be called for each extracted member with a
  [TarInfo](#tarinfo-objects) describing the member and the destination
  path to where the archive is extracted (i.e. the same path is used for all
  members):

  ```
  filter(member: TarInfo, path: str, /) -> TarInfo | None
  ```

  The callable is called just before each member is extracted, so it can
  take the current state of the disk into account.
  It can:

  + return a [`TarInfo`](#tarfile.TarInfo "tarfile.TarInfo") object which will be used instead of the metadata
    in the archive, or
  + return `None`, in which case the member will be skipped, or
  + raise an exception to abort the operation or skip the member,
    depending on [`errorlevel`](#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel").
    Note that when extraction is aborted, [`extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall") may leave
    the archive partially extracted. It does not attempt to clean up.

### Default named filters[¶](#default-named-filters "Link to this heading")

The pre-defined, named filters are available as functions, so they can be
reused in custom filters:

tarfile.fully\_trusted\_filter(*member*, *path*)[¶](#tarfile.fully_trusted_filter "Link to this definition")
:   Return *member* unchanged.

    This implements the `'fully_trusted'` filter.

tarfile.tar\_filter(*member*, *path*)[¶](#tarfile.tar_filter "Link to this definition")
:   Implements the `'tar'` filter.

    * Strip leading slashes (`/` and [`os.sep`](os.html#os.sep "os.sep")) from filenames.
    * [Refuse](#tarfile-extraction-refuse) to extract files with absolute
      paths (in case the name is absolute
      even after stripping slashes, e.g. `C:/foo` on Windows).
      This raises [`AbsolutePathError`](#tarfile.AbsolutePathError "tarfile.AbsolutePathError").
    * [Refuse](#tarfile-extraction-refuse) to extract files whose absolute
      path (after following symlinks) would end up outside the destination.
      This raises [`OutsideDestinationError`](#tarfile.OutsideDestinationError "tarfile.OutsideDestinationError").
    * Clear high mode bits (setuid, setgid, sticky) and group/other write bits
      ([`S_IWGRP`](stat.html#stat.S_IWGRP "stat.S_IWGRP") | [`S_IWOTH`](stat.html#stat.S_IWOTH "stat.S_IWOTH")).

    Return the modified `TarInfo` member.

tarfile.data\_filter(*member*, *path*)[¶](#tarfile.data_filter "Link to this definition")
:   Implements the `'data'` filter.
    In addition to what `tar_filter` does:

    * Normalize link targets ([`TarInfo.linkname`](#tarfile.TarInfo.linkname "tarfile.TarInfo.linkname")) using
      [`os.path.normpath()`](os.path.html#os.path.normpath "os.path.normpath").
      Note that this removes internal `..` components, which may change the
      meaning of the link if the path in `TarInfo.linkname` traverses
      symbolic links.
    * [Refuse](#tarfile-extraction-refuse) to extract links (hard or soft)
      that link to absolute paths, or ones that link outside the destination.

      This raises [`AbsoluteLinkError`](#tarfile.AbsoluteLinkError "tarfile.AbsoluteLinkError") or
      [`LinkOutsideDestinationError`](#tarfile.LinkOutsideDestinationError "tarfile.LinkOutsideDestinationError").

      Note that such files are refused even on platforms that do not support
      symbolic links.
    * [Refuse](#tarfile-extraction-refuse) to extract device files
      (including pipes).
      This raises [`SpecialFileError`](#tarfile.SpecialFileError "tarfile.SpecialFileError").
    * For regular files, including hard links:

      + Set the owner read and write permissions
        ([`S_IRUSR`](stat.html#stat.S_IRUSR "stat.S_IRUSR") | [`S_IWUSR`](stat.html#stat.S_IWUSR "stat.S_IWUSR")).
      + Remove the group & other executable permission
        ([`S_IXGRP`](stat.html#stat.S_IXGRP "stat.S_IXGRP") | [`S_IXOTH`](stat.html#stat.S_IXOTH "stat.S_IXOTH"))
        if the owner doesn’t have it ([`S_IXUSR`](stat.html#stat.S_IXUSR "stat.S_IXUSR")).
    * For other files (directories), set `mode` to `None`, so
      that extraction methods skip applying permission bits.
    * Set user and group info (`uid`, `gid`, `uname`, `gname`)
      to `None`, so that extraction methods skip setting it.

    Return the modified `TarInfo` member.

    Note that this filter does not block *all* dangerous archive features.
    See [Hints for further verification](#tarfile-further-verification) for details.

    Changed in version 3.14: Link targets are now normalized.

### Filter errors[¶](#filter-errors "Link to this heading")

When a filter refuses to extract a file, it will raise an appropriate exception,
a subclass of [`FilterError`](#tarfile.FilterError "tarfile.FilterError").
This will abort the extraction if [`TarFile.errorlevel`](#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel") is 1 or more.
With `errorlevel=0` the error will be logged and the member will be skipped,
but extraction will continue.

### Hints for further verification[¶](#hints-for-further-verification "Link to this heading")

Even with `filter='data'`, *tarfile* is not suited for extracting untrusted
files without prior inspection.
Among other issues, the pre-defined filters do not prevent denial-of-service
attacks. Users should do additional checks.

Here is an incomplete list of things to consider:

* Extract to a [`new temporary directory`](tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp")
  to prevent e.g. exploiting pre-existing links, and to make it easier to
  clean up after a failed extraction.
* Disallow symbolic links if you do not need the functionality.
* When working with untrusted data, use external (e.g. OS-level) limits on
  disk, memory and CPU usage.
* Check filenames against an allow-list of characters
  (to filter out control characters, confusables, foreign path separators,
  and so on).
* Check that filenames have expected extensions (discouraging files that
  execute when you “click on them”, or extension-less files like Windows
  special device names).
* Limit the number of extracted files, total size of extracted data,
  filename length (including symlink length), and size of individual files.
* Check for files that would be shadowed on case-insensitive filesystems.

Also note that:

* Tar files may contain multiple versions of the same file.
  Later ones are expected to overwrite any earlier ones.
  This feature is crucial to allow updating tape archives, but can be abused
  maliciously.
* *tarfile* does not protect against issues with “live” data,
  e.g. an attacker tinkering with the destination (or source) directory while
  extraction (or archiving) is in progress.

### Supporting older Python versions[¶](#supporting-older-python-versions "Link to this heading")

Extraction filters were added to Python 3.12, but may be backported to older
versions as security updates.
To check whether the feature is available, use e.g.
`hasattr(tarfile, 'data_filter')` rather than checking the Python version.

The following examples show how to support Python versions with and without
the feature.
Note that setting `extraction_filter` will affect any subsequent operations.

* Fully trusted archive:

  ```
  my_tarfile.extraction_filter = (lambda member, path: member)
  my_tarfile.extractall()
  ```
* Use the `'data'` filter if available, but revert to Python 3.11 behavior
  (`'fully_trusted'`) if this feature is not available:

  ```
  my_tarfile.extraction_filter = getattr(tarfile, 'data_filter',
                                         (lambda member, path: member))
  my_tarfile.extractall()
  ```
* Use the `'data'` filter; *fail* if it is not available:

  ```
  my_tarfile.extractall(filter=tarfile.data_filter)
  ```

  or:

  ```
  my_tarfile.extraction_filter = tarfile.data_filter
  my_tarfile.extractall()
  ```
* Use the `'data'` filter; *warn* if it is not available:

  ```
  if hasattr(tarfile, 'data_filter'):
      my_tarfile.extractall(filter='data')
  else:
      # remove this when no longer needed
      warn_the_user('Extracting may be unsafe; consider updating Python')
      my_tarfile.extractall()
  ```

### Stateful extraction filter example[¶](#stateful-extraction-filter-example "Link to this heading")

While *tarfile*’s extraction methods take a simple *filter* callable,
custom filters may be more complex objects with an internal state.
It may be useful to write these as context managers, to be used like this:

```
with StatefulFilter() as filter_func:
    tar.extractall(path, filter=filter_func)
```

Such a filter can be written as, for example:

```
class StatefulFilter:
    def __init__(self):
        self.file_count = 0

    def __enter__(self):
        return self

    def __call__(self, member, path):
        self.file_count += 1
        return member

    def __exit__(self, *exc_info):
        print(f'{self.file_count} files extracted')
```

## Command-Line Interface[¶](#command-line-interface "Link to this heading")

Added in version 3.4.

The `tarfile` module provides a simple command-line interface to interact
with tar archives.

If you want to create a new tar archive, specify its name after the [`-c`](#cmdoption-tarfile-c)
option and then list the filename(s) that should be included:

```
$ python -m tarfile -c monty.tar  spam.txt eggs.txt
```

Passing a directory is also acceptable:

```
$ python -m tarfile -c monty.tar life-of-brian_1979/
```

If you want to extract a tar archive into the current directory, use
the [`-e`](#cmdoption-tarfile-e) option:

```
$ python -m tarfile -e monty.tar
```

You can also extract a tar archive into a different directory by passing the
directory’s name:

```
$ python -m tarfile -e monty.tar  other-dir/
```

For a list of the files in a tar archive, use the [`-l`](#cmdoption-tarfile-l) option:

```
$ python -m tarfile -l monty.tar
```

### Command-line options[¶](#command-line-options "Link to this heading")

-l <tarfile>[¶](#cmdoption-tarfile-l "Link to this definition")

--list <tarfile>[¶](#cmdoption-tarfile-list "Link to this definition")
:   List files in a tarfile.

-c <tarfile> <source1> ... <sourceN>[¶](#cmdoption-tarfile-c "Link to this definition")

--create <tarfile> <source1> ... <sourceN>[¶](#cmdoption-tarfile-create "Link to this definition")
:   Create tarfile from source files.

-e <tarfile> [<output\_dir>][¶](#cmdoption-tarfile-e "Link to this definition")

--extract <tarfile> [<output\_dir>][¶](#cmdoption-tarfile-extract "Link to this definition")
:   Extract tarfile into the current directory if *output\_dir* is not specified.

-t <tarfile>[¶](#cmdoption-tarfile-t "Link to this definition")

--test <tarfile>[¶](#cmdoption-tarfile-test "Link to this definition")
:   Test whether the tarfile is valid or not.

-v, --verbose[¶](#cmdoption-tarfile-v "Link to this definition")
:   Verbose output.

--filter <filtername>[¶](#cmdoption-tarfile-filter "Link to this definition")
:   Specifies the *filter* for `--extract`.
    See [Extraction filters](#tarfile-extraction-filter) for details.
    Only string names are accepted (that is, `fully_trusted`, `tar`,
    and `data`).

## Examples[¶](#examples "Link to this heading")

### Reading examples[¶](#reading-examples "Link to this heading")

How to extract an entire tar archive to the current working directory:

```
import tarfile
tar = tarfile.open("sample.tar.gz")
tar.extractall(filter='data')
tar.close()
```

How to extract a subset of a tar archive with [`TarFile.extractall()`](#tarfile.TarFile.extractall "tarfile.TarFile.extractall") using
a generator function instead of a list:

```
import os
import tarfile

def py_files(members):
    for tarinfo in members:
        if os.path.splitext(tarinfo.name)[1] == ".py":
            yield tarinfo

tar = tarfile.open("sample.tar.gz")
tar.extractall(members=py_files(tar))
tar.close()
```

How to read a gzip compressed tar archive and display some member information:

```
import tarfile
tar = tarfile.open("sample.tar.gz", "r:gz")
for tarinfo in tar:
    print(tarinfo.name, "is", tarinfo.size, "bytes in size and is ", end="")
    if tarinfo.isreg():
        print("a regular file.")
    elif tarinfo.isdir():
        print("a directory.")
    else:
        print("something else.")
tar.close()
```

### Writing examples[¶](#writing-examples "Link to this heading")

How to create an uncompressed tar archive from a list of filenames:

```
import tarfile
tar = tarfile.open("sample.tar", "w")
for name in ["foo", "bar", "quux"]:
    tar.add(name)
tar.close()
```

The same example using the [`with`](../reference/compound_stmts.html#with) statement:

```
import tarfile
with tarfile.open("sample.tar", "w") as tar:
    for name in ["foo", "bar", "quux"]:
        tar.add(name)
```

How to create and write an archive to stdout using
[`sys.stdout.buffer`](sys.html#sys.stdout "sys.stdout") in the *fileobj* parameter
in [`TarFile.add()`](#tarfile.TarFile.add "tarfile.TarFile.add"):

```
import sys
import tarfile
with tarfile.open("sample.tar.gz", "w|gz", fileobj=sys.stdout.buffer) as tar:
    for name in ["foo", "bar", "quux"]:
        tar.add(name)
```

How to create an archive and reset the user information using the *filter*
parameter in [`TarFile.add()`](#tarfile.TarFile.add "tarfile.TarFile.add"):

```
import tarfile
def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    return tarinfo
tar = tarfile.open("sample.tar.gz", "w:gz")
tar.add("foo", filter=reset)
tar.close()
```

## Supported tar formats[¶](#supported-tar-formats "Link to this heading")

There are three tar formats that can be created with the `tarfile` module:

* The POSIX.1-1988 ustar format ([`USTAR_FORMAT`](#tarfile.USTAR_FORMAT "tarfile.USTAR_FORMAT")). It supports filenames
  up to a length of at best 256 characters and linknames up to 100 characters.
  The maximum file size is 8 GiB. This is an old and limited but widely
  supported format.
* The GNU tar format ([`GNU_FORMAT`](#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT")). It supports long filenames and
  linknames, files bigger than 8 GiB and sparse files. It is the de facto
  standard on GNU/Linux systems. `tarfile` fully supports the GNU tar
  extensions for long names, sparse file support is read-only.
* The POSIX.1-2001 pax format ([`PAX_FORMAT`](#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT")). It is the most flexible
  format with virtually no limits. It supports long filenames and linknames, large
  files and stores pathnames in a portable way. Modern tar implementations,
  including GNU tar, bsdtar/libarchive and star, fully support extended *pax*
  features; some old or unmaintained libraries may not, but should treat
  *pax* archives as if they were in the universally supported *ustar* format.
  It is the current default format for new archives.

  It extends the existing *ustar* format with extra headers for information
  that cannot be stored otherwise. There are two flavours of pax headers:
  Extended headers only affect the subsequent file header, global
  headers are valid for the complete archive and affect all following files.
  All the data in a pax header is encoded in *UTF-8* for portability reasons.

There are some more variants of the tar format which can be read, but not
created:

* The ancient V7 format. This is the first tar format from Unix Seventh Edition,
  storing only regular files and directories. Names must not be longer than 100
  characters, there is no user/group name information. Some archives have
  miscalculated header checksums in case of fields with non-ASCII characters.
* The SunOS tar extended format. This format is a variant of the POSIX.1-2001
  pax format, but is not compatible.

## Unicode issues[¶](#unicode-issues "Link to this heading")

The tar format was originally conceived to make backups on tape drives with the
main focus on preserving file system information. Nowadays tar archives are
commonly used for file distribution and exchanging archives over networks. One
problem of the original format (which is the basis of all other formats) is
that there is no concept of supporting different character encodings. For
example, an ordinary tar archive created on a *UTF-8* system cannot be read
correctly on a *Latin-1* system if it contains non-*ASCII* characters. Textual
metadata (like filenames, linknames, user/group names) will appear damaged.
Unfortunately, there is no way to autodetect the encoding of an archive. The
pax format was designed to solve this problem. It stores non-ASCII metadata
using the universal character encoding *UTF-8*.

The details of character conversion in `tarfile` are controlled by the
*encoding* and *errors* keyword arguments of the [`TarFile`](#tarfile.TarFile "tarfile.TarFile") class.

*encoding* defines the character encoding to use for the metadata in the
archive. The default value is [`sys.getfilesystemencoding()`](sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") or `'ascii'`
as a fallback. Depending on whether the archive is read or written, the
metadata must be either decoded or encoded. If *encoding* is not set
appropriately, this conversion may fail.

The *errors* argument defines how characters are treated that cannot be
converted. Possible values are listed in section [Error Handlers](codecs.html#error-handlers).
The default scheme is `'surrogateescape'` which Python also uses for its
file system calls, see [File Names, Command Line Arguments, and Environment Variables](os.html#os-filenames).

For [`PAX_FORMAT`](#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT") archives (the default), *encoding* is generally not needed
because all the metadata is stored using *UTF-8*. *encoding* is only used in
the rare cases when binary pax headers are decoded or when strings with
surrogate characters are stored.

### [Table of Contents](../contents.html)

* [`tarfile` — Read and write tar archive files](#)
  + [TarFile Objects](#tarfile-objects)
  + [TarInfo Objects](#tarinfo-objects)
  + [Extraction filters](#extraction-filters)
    - [Default named filters](#default-named-filters)
    - [Filter errors](#filter-errors)
    - [Hints for further verification](#hints-for-further-verification)
    - [Supporting older Python versions](#supporting-older-python-versions)
    - [Stateful extraction filter example](#stateful-extraction-filter-example)
  + [Command-Line Interface](#command-line-interface)
    - [Command-line options](#command-line-options)
  + [Examples](#examples)
    - [Reading examples](#reading-examples)
    - [Writing examples](#writing-examples)
  + [Supported tar formats](#supported-tar-formats)
  + [Unicode issues](#unicode-issues)

#### Previous topic

[`zipfile` — Work with ZIP archives](zipfile.html "previous chapter")

#### Next topic

[File Formats](fileformats.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/tarfile.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](fileformats.html "File Formats") |
* [previous](zipfile.html "zipfile — Work with ZIP archives") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Compression and Archiving](archiving.html) »
* `tarfile` — Read and write tar archive files
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