### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](shutil.html "shutil — High-level file operations") |
* [previous](fnmatch.html "fnmatch — Unix filename pattern matching") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File and Directory Access](filesys.html) »
* `linecache` — Random access to text lines
* |
* Theme
  Auto
  Light
  Dark
   |

# `linecache` — Random access to text lines[¶](#module-linecache "Link to this heading")

**Source code:** [Lib/linecache.py](https://github.com/python/cpython/tree/3.14/Lib/linecache.py)

---

The `linecache` module allows one to get any line from a Python source file, while
attempting to optimize internally, using a cache, the common case where many
lines are read from a single file. This is used by the [`traceback`](traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.") module
to retrieve source lines for inclusion in the formatted traceback.

The [`tokenize.open()`](tokenize.html#tokenize.open "tokenize.open") function is used to open files. This
function uses [`tokenize.detect_encoding()`](tokenize.html#tokenize.detect_encoding "tokenize.detect_encoding") to get the encoding of the
file; in the absence of an encoding token, the file encoding defaults to UTF-8.

The `linecache` module defines the following functions:

linecache.getline(*filename*, *lineno*, *module\_globals=None*)[¶](#linecache.getline "Link to this definition")
:   Get line *lineno* from file named *filename*. This function will never raise an
    exception — it will return `''` on errors (the terminating newline character
    will be included for lines that are found).

    If *filename* indicates a frozen module (starting with `'<frozen '`), the function
    will attempt to get the real file name from `module_globals['__file__']` if
    *module\_globals* is not `None`.

    If a file named *filename* is not found, the function first checks
    for a [**PEP 302**](https://peps.python.org/pep-0302/) `__loader__` in *module\_globals*.
    If there is such a loader and it defines a `get_source` method,
    then that determines the source lines
    (if `get_source()` returns `None`, then `''` is returned).
    Finally, if *filename* is a relative filename,
    it is looked up relative to the entries in the module search path, `sys.path`.

    Changed in version 3.14: Support *filename* of frozen modules.

linecache.clearcache()[¶](#linecache.clearcache "Link to this definition")
:   Clear the cache. Use this function if you no longer need lines from files
    previously read using [`getline()`](#linecache.getline "linecache.getline").

linecache.checkcache(*filename=None*)[¶](#linecache.checkcache "Link to this definition")
:   Check the cache for validity. Use this function if files in the cache may have
    changed on disk, and you require the updated version. If *filename* is omitted,
    it will check all the entries in the cache.

linecache.lazycache(*filename*, *module\_globals*)[¶](#linecache.lazycache "Link to this definition")
:   Capture enough detail about a non-file-based module to permit getting its
    lines later via [`getline()`](#linecache.getline "linecache.getline") even if *module\_globals* is `None` in the later
    call. This avoids doing I/O until a line is actually needed, without having
    to carry the module globals around indefinitely.

    Added in version 3.5.

Example:

```
>>> import linecache
>>> linecache.getline(linecache.__file__, 8)
'import sys\n'
```

#### Previous topic

[`fnmatch` — Unix filename pattern matching](fnmatch.html "previous chapter")

#### Next topic

[`shutil` — High-level file operations](shutil.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/linecache.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](shutil.html "shutil — High-level file operations") |
* [previous](fnmatch.html "fnmatch — Unix filename pattern matching") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File and Directory Access](filesys.html) »
* `linecache` — Random access to text lines
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