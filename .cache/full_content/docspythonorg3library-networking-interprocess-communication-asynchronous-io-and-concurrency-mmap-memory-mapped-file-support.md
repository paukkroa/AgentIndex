### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](netdata.html "Internet Data Handling") |
* [previous](signal.html "signal — Set handlers for asynchronous events") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Networking and Interprocess Communication](ipc.html) »
* `mmap` — Memory-mapped file support
* |
* Theme
  Auto
  Light
  Dark
   |

# `mmap` — Memory-mapped file support[¶](#module-mmap "Link to this heading")

---

[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

Memory-mapped file objects behave like both [`bytearray`](stdtypes.html#bytearray "bytearray") and like
[file objects](../glossary.html#term-file-object). You can use mmap objects in most places
where [`bytearray`](stdtypes.html#bytearray "bytearray") are expected; for example, you can use the [`re`](re.html#module-re "re: Regular expression operations.")
module to search through a memory-mapped file. You can also change a single
byte by doing `obj[index] = 97`, or change a subsequence by assigning to a
slice: `obj[i1:i2] = b'...'`. You can also read and write data starting at
the current file position, and `seek()` through the file to different positions.

A memory-mapped file is created by the [`mmap`](#mmap.mmap "mmap.mmap") constructor, which is
different on Unix and on Windows. In either case you must provide a file
descriptor for a file opened for update. If you wish to map an existing Python
file object, use its [`fileno()`](io.html#io.IOBase.fileno "io.IOBase.fileno") method to obtain the correct value for the
*fileno* parameter. Otherwise, you can open the file using the
[`os.open()`](os.html#os.open "os.open") function, which returns a file descriptor directly (the file
still needs to be closed when done).

Note

If you want to create a memory-mapping for a writable, buffered file, you
should [`flush()`](io.html#io.IOBase.flush "io.IOBase.flush") the file first. This is necessary to ensure
that local modifications to the buffers are actually available to the
mapping.

For both the Unix and Windows versions of the constructor, *access* may be
specified as an optional keyword parameter. *access* accepts one of four
values: `ACCESS_READ`, `ACCESS_WRITE`, or `ACCESS_COPY` to
specify read-only, write-through or copy-on-write memory respectively, or
`ACCESS_DEFAULT` to defer to *prot*. *access* can be used on both Unix
and Windows. If *access* is not specified, Windows mmap returns a
write-through mapping. The initial memory values for all three access types
are taken from the specified file. Assignment to an `ACCESS_READ`
memory map raises a [`TypeError`](exceptions.html#TypeError "TypeError") exception. Assignment to an
`ACCESS_WRITE` memory map affects both memory and the underlying file.
Assignment to an `ACCESS_COPY` memory map affects memory but does not
update the underlying file.

Changed in version 3.7: Added `ACCESS_DEFAULT` constant.

To map anonymous memory, -1 should be passed as the fileno along with the length.

*class* mmap.mmap(*fileno*, *length*, *tagname=None*, *access=ACCESS\_DEFAULT*, *offset=0*)[¶](#mmap.mmap "Link to this definition")
:   **(Windows version)** Maps *length* bytes from the file specified by the
    file handle *fileno*, and creates a mmap object. If *length* is larger
    than the current size of the file, the file is extended to contain *length*
    bytes. If *length* is `0`, the maximum length of the map is the current
    size of the file, except that if the file is empty Windows raises an
    exception (you cannot create an empty mapping on Windows).

    *tagname*, if specified and not `None`, is a string giving a tag name for
    the mapping. Windows allows you to have many different mappings against
    the same file. If you specify the name of an existing tag, that tag is
    opened, otherwise a new tag of this name is created. If this parameter is
    omitted or `None`, the mapping is created without a name. Avoiding the
    use of the *tagname* parameter will assist in keeping your code portable
    between Unix and Windows.

    *offset* may be specified as a non-negative integer offset. mmap references
    will be relative to the offset from the beginning of the file. *offset*
    defaults to 0. *offset* must be a multiple of the `ALLOCATIONGRANULARITY`.

    Raises an [auditing event](sys.html#auditing) `mmap.__new__` with arguments `fileno`, `length`, `access`, `offset`.

*class* mmap.mmap(*fileno*, *length*, *flags=MAP\_SHARED*, *prot=PROT\_WRITE | PROT\_READ*, *access=ACCESS\_DEFAULT*, *offset=0*, *\**, *trackfd=True*)
:   **(Unix version)** Maps *length* bytes from the file specified by the file
    descriptor *fileno*, and returns a mmap object. If *length* is `0`, the
    maximum length of the map will be the current size of the file when
    [`mmap`](#mmap.mmap "mmap.mmap") is called.

    *flags* specifies the nature of the mapping. [`MAP_PRIVATE`](#mmap.MAP_PRIVATE "mmap.MAP_PRIVATE") creates a
    private copy-on-write mapping, so changes to the contents of the mmap
    object will be private to this process, and [`MAP_SHARED`](#mmap.MAP_SHARED "mmap.MAP_SHARED") creates a
    mapping that’s shared with all other processes mapping the same areas of
    the file. The default value is [`MAP_SHARED`](#mmap.MAP_SHARED "mmap.MAP_SHARED"). Some systems have
    additional possible flags with the full list specified in
    [MAP\_\* constants](#map-constants).

    *prot*, if specified, gives the desired memory protection; the two most
    useful values are `PROT_READ` and `PROT_WRITE`, to specify
    that the pages may be read or written. *prot* defaults to
    `PROT_READ | PROT_WRITE`.

    *access* may be specified in lieu of *flags* and *prot* as an optional
    keyword parameter. It is an error to specify both *flags*, *prot* and
    *access*. See the description of *access* above for information on how to
    use this parameter.

    *offset* may be specified as a non-negative integer offset. mmap references
    will be relative to the offset from the beginning of the file. *offset*
    defaults to 0. *offset* must be a multiple of `ALLOCATIONGRANULARITY`
    which is equal to `PAGESIZE` on Unix systems.

    If *trackfd* is `False`, the file descriptor specified by *fileno* will
    not be duplicated, and the resulting `mmap` object will not
    be associated with the map’s underlying file.
    This means that the [`size()`](#mmap.mmap.size "mmap.mmap.size") and [`resize()`](#mmap.mmap.resize "mmap.mmap.resize")
    methods will fail.
    This mode is useful to limit the number of open file descriptors.

    To ensure validity of the created memory mapping the file specified
    by the descriptor *fileno* is internally automatically synchronized
    with the physical backing store on macOS.

    Changed in version 3.13: The *trackfd* parameter was added.

    This example shows a simple way of using [`mmap`](#mmap.mmap "mmap.mmap"):

    ```
    import mmap

    # write a simple example file
    with open("hello.txt", "wb") as f:
        f.write(b"Hello Python!\n")

    with open("hello.txt", "r+b") as f:
        # memory-map the file, size 0 means whole file
        mm = mmap.mmap(f.fileno(), 0)
        # read content via standard file methods
        print(mm.readline())  # prints b"Hello Python!\n"
        # read content via slice notation
        print(mm[:5])  # prints b"Hello"
        # update content using slice notation;
        # note that new content must have same size
        mm[6:] = b" world!\n"
        # ... and read again using standard file methods
        mm.seek(0)
        print(mm.readline())  # prints b"Hello  world!\n"
        # close the map
        mm.close()
    ```

    [`mmap`](#mmap.mmap "mmap.mmap") can also be used as a context manager in a [`with`](../reference/compound_stmts.html#with)
    statement:

    ```
    import mmap

    with mmap.mmap(-1, 13) as mm:
        mm.write(b"Hello world!")
    ```

    Added in version 3.2: Context manager support.

    The next example demonstrates how to create an anonymous map and exchange
    data between the parent and child processes:

    ```
    import mmap
    import os

    mm = mmap.mmap(-1, 13)
    mm.write(b"Hello world!")

    pid = os.fork()

    if pid == 0:  # In a child process
        mm.seek(0)
        print(mm.readline())

        mm.close()
    ```

    Raises an [auditing event](sys.html#auditing) `mmap.__new__` with arguments `fileno`, `length`, `access`, `offset`.

    Memory-mapped file objects support the following methods:

    close()[¶](#mmap.mmap.close "Link to this definition")
    :   Closes the mmap. Subsequent calls to other methods of the object will
        result in a ValueError exception being raised. This will not close
        the open file.

    closed[¶](#mmap.mmap.closed "Link to this definition")
    :   `True` if the file is closed.

        Added in version 3.2.

    find(*sub*[, *start*[, *end*]])[¶](#mmap.mmap.find "Link to this definition")
    :   Returns the lowest index in the object where the subsequence *sub* is
        found, such that *sub* is contained in the range [*start*, *end*].
        Optional arguments *start* and *end* are interpreted as in slice notation.
        Returns `-1` on failure.

        Changed in version 3.5: Writable [bytes-like object](../glossary.html#term-bytes-like-object) is now accepted.

    flush()[¶](#mmap.mmap.flush "Link to this definition")

    flush(*offset*, *size*, */*)
    :   Flushes changes made to the in-memory copy of a file back to disk. Without
        use of this call there is no guarantee that changes are written back before
        the object is destroyed. If *offset* and *size* are specified, only
        changes to the given range of bytes will be flushed to disk; otherwise, the
        whole extent of the mapping is flushed. *offset* must be a multiple of the
        `PAGESIZE` or `ALLOCATIONGRANULARITY`.

        `None` is returned to indicate success. An exception is raised when the
        call failed.

        Changed in version 3.8: Previously, a nonzero value was returned on success; zero was returned
        on error under Windows. A zero value was returned on success; an
        exception was raised on error under Unix.

    madvise(*option*[, *start*[, *length*]])[¶](#mmap.mmap.madvise "Link to this definition")
    :   Send advice *option* to the kernel about the memory region beginning at
        *start* and extending *length* bytes. *option* must be one of the
        [MADV\_\* constants](#madvise-constants) available on the system. If
        *start* and *length* are omitted, the entire mapping is spanned. On
        some systems (including Linux), *start* must be a multiple of the
        `PAGESIZE`.

        Availability: Systems with the `madvise()` system call.

        Added in version 3.8.

    move(*dest*, *src*, *count*)[¶](#mmap.mmap.move "Link to this definition")
    :   Copy the *count* bytes starting at offset *src* to the destination index
        *dest*. If the mmap was created with `ACCESS_READ`, then calls to
        move will raise a [`TypeError`](exceptions.html#TypeError "TypeError") exception.

    read([*n*])[¶](#mmap.mmap.read "Link to this definition")
    :   Return a [`bytes`](stdtypes.html#bytes "bytes") containing up to *n* bytes starting from the
        current file position. If the argument is omitted, `None` or negative,
        return all bytes from the current file position to the end of the
        mapping. The file position is updated to point after the bytes that were
        returned.

        Changed in version 3.3: Argument can be omitted or `None`.

    read\_byte()[¶](#mmap.mmap.read_byte "Link to this definition")
    :   Returns a byte at the current file position as an integer, and advances
        the file position by 1.

    readline()[¶](#mmap.mmap.readline "Link to this definition")
    :   Returns a single line, starting at the current file position and up to the
        next newline. The file position is updated to point after the bytes that were
        returned.

    resize(*newsize*)[¶](#mmap.mmap.resize "Link to this definition")
    :   Resizes the map and the underlying file, if any.

        Resizing a map created with *access* of `ACCESS_READ` or
        `ACCESS_COPY`, will raise a [`TypeError`](exceptions.html#TypeError "TypeError") exception.
        Resizing a map created with *trackfd* set to `False`,
        will raise a [`ValueError`](exceptions.html#ValueError "ValueError") exception.

        **On Windows**: Resizing the map will raise an [`OSError`](exceptions.html#OSError "OSError") if there are other
        maps against the same named file. Resizing an anonymous map (ie against the
        pagefile) will silently create a new map with the original data copied over
        up to the length of the new size.

        Changed in version 3.11: Correctly fails if attempting to resize when another map is held
        Allows resize against an anonymous map on Windows

    rfind(*sub*[, *start*[, *end*]])[¶](#mmap.mmap.rfind "Link to this definition")
    :   Returns the highest index in the object where the subsequence *sub* is
        found, such that *sub* is contained in the range [*start*, *end*].
        Optional arguments *start* and *end* are interpreted as in slice notation.
        Returns `-1` on failure.

        Changed in version 3.5: Writable [bytes-like object](../glossary.html#term-bytes-like-object) is now accepted.

    seek(*pos*[, *whence*])[¶](#mmap.mmap.seek "Link to this definition")
    :   Set the file’s current position. *whence* argument is optional and
        defaults to `os.SEEK_SET` or `0` (absolute file positioning); other
        values are `os.SEEK_CUR` or `1` (seek relative to the current
        position) and `os.SEEK_END` or `2` (seek relative to the file’s end).

        Changed in version 3.13: Return the new absolute position instead of `None`.

    seekable()[¶](#mmap.mmap.seekable "Link to this definition")
    :   Return whether the file supports seeking, and the return value is always `True`.

        Added in version 3.13.

    size()[¶](#mmap.mmap.size "Link to this definition")
    :   Return the length of the file, which can be larger than the size of the
        memory-mapped area.

    tell()[¶](#mmap.mmap.tell "Link to this definition")
    :   Returns the current position of the file pointer.

    write(*bytes*)[¶](#mmap.mmap.write "Link to this definition")
    :   Write the bytes in *bytes* into memory at the current position of the
        file pointer and return the number of bytes written (never less than
        `len(bytes)`, since if the write fails, a [`ValueError`](exceptions.html#ValueError "ValueError") will be
        raised). The file position is updated to point after the bytes that
        were written. If the mmap was created with `ACCESS_READ`, then
        writing to it will raise a [`TypeError`](exceptions.html#TypeError "TypeError") exception.

        Changed in version 3.5: Writable [bytes-like object](../glossary.html#term-bytes-like-object) is now accepted.

        Changed in version 3.6: The number of bytes written is now returned.

    write\_byte(*byte*)[¶](#mmap.mmap.write_byte "Link to this definition")
    :   Write the integer *byte* into memory at the current
        position of the file pointer; the file position is advanced by `1`. If
        the mmap was created with `ACCESS_READ`, then writing to it will
        raise a [`TypeError`](exceptions.html#TypeError "TypeError") exception.

## MADV\_\* Constants[¶](#madv-constants "Link to this heading")

mmap.MADV\_NORMAL[¶](#mmap.MADV_NORMAL "Link to this definition")

mmap.MADV\_RANDOM[¶](#mmap.MADV_RANDOM "Link to this definition")

mmap.MADV\_SEQUENTIAL[¶](#mmap.MADV_SEQUENTIAL "Link to this definition")

mmap.MADV\_WILLNEED[¶](#mmap.MADV_WILLNEED "Link to this definition")

mmap.MADV\_DONTNEED[¶](#mmap.MADV_DONTNEED "Link to this definition")

mmap.MADV\_REMOVE[¶](#mmap.MADV_REMOVE "Link to this definition")

mmap.MADV\_DONTFORK[¶](#mmap.MADV_DONTFORK "Link to this definition")

mmap.MADV\_DOFORK[¶](#mmap.MADV_DOFORK "Link to this definition")

mmap.MADV\_HWPOISON[¶](#mmap.MADV_HWPOISON "Link to this definition")

mmap.MADV\_MERGEABLE[¶](#mmap.MADV_MERGEABLE "Link to this definition")

mmap.MADV\_UNMERGEABLE[¶](#mmap.MADV_UNMERGEABLE "Link to this definition")

mmap.MADV\_SOFT\_OFFLINE[¶](#mmap.MADV_SOFT_OFFLINE "Link to this definition")

mmap.MADV\_HUGEPAGE[¶](#mmap.MADV_HUGEPAGE "Link to this definition")

mmap.MADV\_NOHUGEPAGE[¶](#mmap.MADV_NOHUGEPAGE "Link to this definition")

mmap.MADV\_DONTDUMP[¶](#mmap.MADV_DONTDUMP "Link to this definition")

mmap.MADV\_DODUMP[¶](#mmap.MADV_DODUMP "Link to this definition")

mmap.MADV\_FREE[¶](#mmap.MADV_FREE "Link to this definition")

mmap.MADV\_NOSYNC[¶](#mmap.MADV_NOSYNC "Link to this definition")

mmap.MADV\_AUTOSYNC[¶](#mmap.MADV_AUTOSYNC "Link to this definition")

mmap.MADV\_NOCORE[¶](#mmap.MADV_NOCORE "Link to this definition")

mmap.MADV\_CORE[¶](#mmap.MADV_CORE "Link to this definition")

mmap.MADV\_PROTECT[¶](#mmap.MADV_PROTECT "Link to this definition")

mmap.MADV\_FREE\_REUSABLE[¶](#mmap.MADV_FREE_REUSABLE "Link to this definition")

mmap.MADV\_FREE\_REUSE[¶](#mmap.MADV_FREE_REUSE "Link to this definition")
:   These options can be passed to [`mmap.madvise()`](#mmap.mmap.madvise "mmap.mmap.madvise"). Not every option will
    be present on every system.

    Availability: Systems with the madvise() system call.

    Added in version 3.8.

## MAP\_\* Constants[¶](#map-constants "Link to this heading")

mmap.MAP\_SHARED[¶](#mmap.MAP_SHARED "Link to this definition")

mmap.MAP\_PRIVATE[¶](#mmap.MAP_PRIVATE "Link to this definition")

mmap.MAP\_32BIT[¶](#mmap.MAP_32BIT "Link to this definition")

mmap.MAP\_ALIGNED\_SUPER[¶](#mmap.MAP_ALIGNED_SUPER "Link to this definition")

mmap.MAP\_ANON[¶](#mmap.MAP_ANON "Link to this definition")

mmap.MAP\_ANONYMOUS[¶](#mmap.MAP_ANONYMOUS "Link to this definition")

mmap.MAP\_CONCEAL[¶](#mmap.MAP_CONCEAL "Link to this definition")

mmap.MAP\_DENYWRITE[¶](#mmap.MAP_DENYWRITE "Link to this definition")

mmap.MAP\_EXECUTABLE[¶](#mmap.MAP_EXECUTABLE "Link to this definition")

mmap.MAP\_HASSEMAPHORE[¶](#mmap.MAP_HASSEMAPHORE "Link to this definition")

mmap.MAP\_JIT[¶](#mmap.MAP_JIT "Link to this definition")

mmap.MAP\_NOCACHE[¶](#mmap.MAP_NOCACHE "Link to this definition")

mmap.MAP\_NOEXTEND[¶](#mmap.MAP_NOEXTEND "Link to this definition")

mmap.MAP\_NORESERVE[¶](#mmap.MAP_NORESERVE "Link to this definition")

mmap.MAP\_POPULATE[¶](#mmap.MAP_POPULATE "Link to this definition")

mmap.MAP\_RESILIENT\_CODESIGN[¶](#mmap.MAP_RESILIENT_CODESIGN "Link to this definition")

mmap.MAP\_RESILIENT\_MEDIA[¶](#mmap.MAP_RESILIENT_MEDIA "Link to this definition")

mmap.MAP\_STACK[¶](#mmap.MAP_STACK "Link to this definition")

mmap.MAP\_TPRO[¶](#mmap.MAP_TPRO "Link to this definition")

mmap.MAP\_TRANSLATED\_ALLOW\_EXECUTE[¶](#mmap.MAP_TRANSLATED_ALLOW_EXECUTE "Link to this definition")

mmap.MAP\_UNIX03[¶](#mmap.MAP_UNIX03 "Link to this definition")
:   These are the various flags that can be passed to [`mmap.mmap()`](#mmap.mmap "mmap.mmap"). [`MAP_ALIGNED_SUPER`](#mmap.MAP_ALIGNED_SUPER "mmap.MAP_ALIGNED_SUPER")
    is only available at FreeBSD and [`MAP_CONCEAL`](#mmap.MAP_CONCEAL "mmap.MAP_CONCEAL") is only available at OpenBSD. Note
    that some options might not be present on some systems.

    Changed in version 3.10: Added [`MAP_POPULATE`](#mmap.MAP_POPULATE "mmap.MAP_POPULATE") constant.

    Added in version 3.11: Added [`MAP_STACK`](#mmap.MAP_STACK "mmap.MAP_STACK") constant.

    Added in version 3.12: Added [`MAP_ALIGNED_SUPER`](#mmap.MAP_ALIGNED_SUPER "mmap.MAP_ALIGNED_SUPER") and [`MAP_CONCEAL`](#mmap.MAP_CONCEAL "mmap.MAP_CONCEAL") constants.

    Added in version 3.13: Added [`MAP_32BIT`](#mmap.MAP_32BIT "mmap.MAP_32BIT"), [`MAP_HASSEMAPHORE`](#mmap.MAP_HASSEMAPHORE "mmap.MAP_HASSEMAPHORE"), [`MAP_JIT`](#mmap.MAP_JIT "mmap.MAP_JIT"),
    [`MAP_NOCACHE`](#mmap.MAP_NOCACHE "mmap.MAP_NOCACHE"), [`MAP_NOEXTEND`](#mmap.MAP_NOEXTEND "mmap.MAP_NOEXTEND"), [`MAP_NORESERVE`](#mmap.MAP_NORESERVE "mmap.MAP_NORESERVE"),
    [`MAP_RESILIENT_CODESIGN`](#mmap.MAP_RESILIENT_CODESIGN "mmap.MAP_RESILIENT_CODESIGN"), [`MAP_RESILIENT_MEDIA`](#mmap.MAP_RESILIENT_MEDIA "mmap.MAP_RESILIENT_MEDIA"),
    [`MAP_TPRO`](#mmap.MAP_TPRO "mmap.MAP_TPRO"), [`MAP_TRANSLATED_ALLOW_EXECUTE`](#mmap.MAP_TRANSLATED_ALLOW_EXECUTE "mmap.MAP_TRANSLATED_ALLOW_EXECUTE"), and
    [`MAP_UNIX03`](#mmap.MAP_UNIX03 "mmap.MAP_UNIX03") constants.

### [Table of Contents](../contents.html)

* [`mmap` — Memory-mapped file support](#)
  + [MADV\_\* Constants](#madv-constants)
  + [MAP\_\* Constants](#map-constants)

#### Previous topic

[`signal` — Set handlers for asynchronous events](signal.html "previous chapter")

#### Next topic

[Internet Data Handling](netdata.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/mmap.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](netdata.html "Internet Data Handling") |
* [previous](signal.html "signal — Set handlers for asynchronous events") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Networking and Interprocess Communication](ipc.html) »
* `mmap` — Memory-mapped file support
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