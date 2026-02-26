### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](curses.html "curses — Terminal handling for character-cell displays") |
* [previous](getpass.html "getpass — Portable password input") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `fileinput` — Iterate over lines from multiple input streams
* |
* Theme
  Auto
  Light
  Dark
   |

# `fileinput` — Iterate over lines from multiple input streams[¶](#module-fileinput "Link to this heading")

**Source code:** [Lib/fileinput.py](https://github.com/python/cpython/tree/3.14/Lib/fileinput.py)

---

This module implements a helper class and functions to quickly write a
loop over standard input or a list of files. If you just want to read or
write one file see [`open()`](functions.html#open "open").

The typical use is:

```
import fileinput
for line in fileinput.input(encoding="utf-8"):
    process(line)
```

This iterates over the lines of all files listed in `sys.argv[1:]`, defaulting
to `sys.stdin` if the list is empty. If a filename is `'-'`, it is also
replaced by `sys.stdin` and the optional arguments *mode* and *openhook*
are ignored. To specify an alternative list of filenames, pass it as the
first argument to [`input()`](#fileinput.input "fileinput.input"). A single file name is also allowed.

All files are opened in text mode by default, but you can override this by
specifying the *mode* parameter in the call to [`input()`](#fileinput.input "fileinput.input") or
[`FileInput`](#fileinput.FileInput "fileinput.FileInput"). If an I/O error occurs during opening or reading a file,
[`OSError`](exceptions.html#OSError "OSError") is raised.

Changed in version 3.3: [`IOError`](exceptions.html#IOError "IOError") used to be raised; it is now an alias of [`OSError`](exceptions.html#OSError "OSError").

If `sys.stdin` is used more than once, the second and further use will return
no lines, except perhaps for interactive use, or if it has been explicitly reset
(e.g. using `sys.stdin.seek(0)`).

Empty files are opened and immediately closed; the only time their presence in
the list of filenames is noticeable at all is when the last file opened is
empty.

Lines are returned with any newlines intact, which means that the last line in
a file may not have one.

You can control how files are opened by providing an opening hook via the
*openhook* parameter to [`fileinput.input()`](#fileinput.input "fileinput.input") or [`FileInput()`](#fileinput.FileInput "fileinput.FileInput"). The
hook must be a function that takes two arguments, *filename* and *mode*, and
returns an accordingly opened file-like object. If *encoding* and/or *errors*
are specified, they will be passed to the hook as additional keyword arguments.
This module provides a [`hook_compressed()`](#fileinput.hook_compressed "fileinput.hook_compressed") to support compressed files.

The following function is the primary interface of this module:

fileinput.input(*files=None*, *inplace=False*, *backup=''*, *\**, *mode='r'*, *openhook=None*, *encoding=None*, *errors=None*)[¶](#fileinput.input "Link to this definition")
:   Create an instance of the [`FileInput`](#fileinput.FileInput "fileinput.FileInput") class. The instance will be used
    as global state for the functions of this module, and is also returned to use
    during iteration. The parameters to this function will be passed along to the
    constructor of the [`FileInput`](#fileinput.FileInput "fileinput.FileInput") class.

    The [`FileInput`](#fileinput.FileInput "fileinput.FileInput") instance can be used as a context manager in the
    [`with`](../reference/compound_stmts.html#with) statement. In this example, *input* is closed after the
    `with` statement is exited, even if an exception occurs:

    ```
    with fileinput.input(files=('spam.txt', 'eggs.txt'), encoding="utf-8") as f:
        for line in f:
            process(line)
    ```

    Changed in version 3.2: Can be used as a context manager.

    Changed in version 3.8: The keyword parameters *mode* and *openhook* are now keyword-only.

    Changed in version 3.10: The keyword-only parameter *encoding* and *errors* are added.

The following functions use the global state created by [`fileinput.input()`](#fileinput.input "fileinput.input");
if there is no active state, [`RuntimeError`](exceptions.html#RuntimeError "RuntimeError") is raised.

fileinput.filename()[¶](#fileinput.filename "Link to this definition")
:   Return the name of the file currently being read. Before the first line has
    been read, returns `None`.

fileinput.fileno()[¶](#fileinput.fileno "Link to this definition")
:   Return the integer “file descriptor” for the current file. When no file is
    opened (before the first line and between files), returns `-1`.

fileinput.lineno()[¶](#fileinput.lineno "Link to this definition")
:   Return the cumulative line number of the line that has just been read. Before
    the first line has been read, returns `0`. After the last line of the last
    file has been read, returns the line number of that line.

fileinput.filelineno()[¶](#fileinput.filelineno "Link to this definition")
:   Return the line number in the current file. Before the first line has been
    read, returns `0`. After the last line of the last file has been read,
    returns the line number of that line within the file.

fileinput.isfirstline()[¶](#fileinput.isfirstline "Link to this definition")
:   Return `True` if the line just read is the first line of its file, otherwise
    return `False`.

fileinput.isstdin()[¶](#fileinput.isstdin "Link to this definition")
:   Return `True` if the last line was read from `sys.stdin`, otherwise return
    `False`.

fileinput.nextfile()[¶](#fileinput.nextfile "Link to this definition")
:   Close the current file so that the next iteration will read the first line from
    the next file (if any); lines not read from the file will not count towards the
    cumulative line count. The filename is not changed until after the first line
    of the next file has been read. Before the first line has been read, this
    function has no effect; it cannot be used to skip the first file. After the
    last line of the last file has been read, this function has no effect.

fileinput.close()[¶](#fileinput.close "Link to this definition")
:   Close the sequence.

The class which implements the sequence behavior provided by the module is
available for subclassing as well:

*class* fileinput.FileInput(*files=None*, *inplace=False*, *backup=''*, *\**, *mode='r'*, *openhook=None*, *encoding=None*, *errors=None*)[¶](#fileinput.FileInput "Link to this definition")
:   Class [`FileInput`](#fileinput.FileInput "fileinput.FileInput") is the implementation; its methods [`filename()`](#fileinput.filename "fileinput.filename"),
    [`fileno()`](#fileinput.fileno "fileinput.fileno"), [`lineno()`](#fileinput.lineno "fileinput.lineno"), [`filelineno()`](#fileinput.filelineno "fileinput.filelineno"), [`isfirstline()`](#fileinput.isfirstline "fileinput.isfirstline"),
    [`isstdin()`](#fileinput.isstdin "fileinput.isstdin"), [`nextfile()`](#fileinput.nextfile "fileinput.nextfile") and [`close()`](#fileinput.close "fileinput.close") correspond to the
    functions of the same name in the module. In addition it is [iterable](../glossary.html#term-iterable)
    and has a [`readline()`](io.html#io.TextIOBase.readline "io.TextIOBase.readline") method which returns the next
    input line. The sequence must be accessed in strictly sequential order;
    random access and [`readline()`](io.html#io.TextIOBase.readline "io.TextIOBase.readline") cannot be mixed.

    With *mode* you can specify which file mode will be passed to [`open()`](functions.html#open "open"). It
    must be one of `'r'` and `'rb'`.

    The *openhook*, when given, must be a function that takes two arguments,
    *filename* and *mode*, and returns an accordingly opened file-like object. You
    cannot use *inplace* and *openhook* together.

    You can specify *encoding* and *errors* that is passed to [`open()`](functions.html#open "open") or *openhook*.

    A [`FileInput`](#fileinput.FileInput "fileinput.FileInput") instance can be used as a context manager in the
    [`with`](../reference/compound_stmts.html#with) statement. In this example, *input* is closed after the
    `with` statement is exited, even if an exception occurs:

    ```
    with FileInput(files=('spam.txt', 'eggs.txt')) as input:
        process(input)
    ```

    Changed in version 3.2: Can be used as a context manager.

    Changed in version 3.8: The keyword parameter *mode* and *openhook* are now keyword-only.

    Changed in version 3.10: The keyword-only parameter *encoding* and *errors* are added.

    Changed in version 3.11: The `'rU'` and `'U'` modes and the `__getitem__()` method have
    been removed.

**Optional in-place filtering:** if the keyword argument `inplace=True` is
passed to [`fileinput.input()`](#fileinput.input "fileinput.input") or to the [`FileInput`](#fileinput.FileInput "fileinput.FileInput") constructor, the
file is moved to a backup file and standard output is directed to the input file
(if a file of the same name as the backup file already exists, it will be
replaced silently). This makes it possible to write a filter that rewrites its
input file in place. If the *backup* parameter is given (typically as
`backup='.<some extension>'`), it specifies the extension for the backup file,
and the backup file remains around; by default, the extension is `'.bak'` and
it is deleted when the output file is closed. In-place filtering is disabled
when standard input is read.

The two following opening hooks are provided by this module:

fileinput.hook\_compressed(*filename*, *mode*, *\**, *encoding=None*, *errors=None*)[¶](#fileinput.hook_compressed "Link to this definition")
:   Transparently opens files compressed with gzip and bzip2 (recognized by the
    extensions `'.gz'` and `'.bz2'`) using the [`gzip`](gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.") and [`bz2`](bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
    modules. If the filename extension is not `'.gz'` or `'.bz2'`, the file is
    opened normally (ie, using [`open()`](functions.html#open "open") without any decompression).

    The *encoding* and *errors* values are passed to [`io.TextIOWrapper`](io.html#io.TextIOWrapper "io.TextIOWrapper")
    for compressed files and open for normal files.

    Usage example: `fi = fileinput.FileInput(openhook=fileinput.hook_compressed, encoding="utf-8")`

    Changed in version 3.10: The keyword-only parameter *encoding* and *errors* are added.

fileinput.hook\_encoded(*encoding*, *errors=None*)[¶](#fileinput.hook_encoded "Link to this definition")
:   Returns a hook which opens each file with [`open()`](functions.html#open "open"), using the given
    *encoding* and *errors* to read the file.

    Usage example: `fi =
    fileinput.FileInput(openhook=fileinput.hook_encoded("utf-8",
    "surrogateescape"))`

    Changed in version 3.6: Added the optional *errors* parameter.

    Deprecated since version 3.10: This function is deprecated since [`fileinput.input()`](#fileinput.input "fileinput.input") and [`FileInput`](#fileinput.FileInput "fileinput.FileInput")
    now have *encoding* and *errors* parameters.

#### Previous topic

[`getpass` — Portable password input](getpass.html "previous chapter")

#### Next topic

[`curses` — Terminal handling for character-cell displays](curses.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/fileinput.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](curses.html "curses — Terminal handling for character-cell displays") |
* [previous](getpass.html "getpass — Portable password input") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `fileinput` — Iterate over lines from multiple input streams
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