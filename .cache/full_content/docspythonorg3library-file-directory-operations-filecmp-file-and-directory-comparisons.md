### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tempfile.html "tempfile — Generate temporary files and directories") |
* [previous](stat.html "stat — Interpreting stat() results") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File and Directory Access](filesys.html) »
* `filecmp` — File and Directory Comparisons
* |
* Theme
  Auto
  Light
  Dark
   |

# `filecmp` — File and Directory Comparisons[¶](#module-filecmp "Link to this heading")

**Source code:** [Lib/filecmp.py](https://github.com/python/cpython/tree/3.14/Lib/filecmp.py)

---

The `filecmp` module defines functions to compare files and directories,
with various optional time/correctness trade-offs. For comparing files,
see also the [`difflib`](difflib.html#module-difflib "difflib: Helpers for computing differences between objects.") module.

The `filecmp` module defines the following functions:

filecmp.cmp(*f1*, *f2*, *shallow=True*)[¶](#filecmp.cmp "Link to this definition")
:   Compare the files named *f1* and *f2*, returning `True` if they seem equal,
    `False` otherwise.

    If *shallow* is true and the [`os.stat()`](os.html#os.stat "os.stat") signatures (file type, size, and
    modification time) of both files are identical, the files are taken to be
    equal.

    Otherwise, the files are treated as different if their sizes or contents differ.

    Note that no external programs are called from this function, giving it
    portability and efficiency.

    This function uses a cache for past comparisons and the results,
    with cache entries invalidated if the [`os.stat()`](os.html#os.stat "os.stat") information for the
    file changes. The entire cache may be cleared using [`clear_cache()`](#filecmp.clear_cache "filecmp.clear_cache").

filecmp.cmpfiles(*dir1*, *dir2*, *common*, *shallow=True*)[¶](#filecmp.cmpfiles "Link to this definition")
:   Compare the files in the two directories *dir1* and *dir2* whose names are
    given by *common*.

    Returns three lists of file names: *match*, *mismatch*,
    *errors*. *match* contains the list of files that match, *mismatch* contains
    the names of those that don’t, and *errors* lists the names of files which
    could not be compared. Files are listed in *errors* if they don’t exist in
    one of the directories, the user lacks permission to read them or if the
    comparison could not be done for some other reason.

    The *shallow* parameter has the same meaning and default value as for
    [`filecmp.cmp()`](#filecmp.cmp "filecmp.cmp").

    For example, `cmpfiles('a', 'b', ['c', 'd/e'])` will compare `a/c` with
    `b/c` and `a/d/e` with `b/d/e`. `'c'` and `'d/e'` will each be in
    one of the three returned lists.

filecmp.clear\_cache()[¶](#filecmp.clear_cache "Link to this definition")
:   Clear the filecmp cache. This may be useful if a file is compared so quickly
    after it is modified that it is within the mtime resolution of
    the underlying filesystem.

    Added in version 3.4.

## The [`dircmp`](#filecmp.dircmp "filecmp.dircmp") class[¶](#the-dircmp-class "Link to this heading")

*class* filecmp.dircmp(*a*, *b*, *ignore=None*, *hide=None*, *\**, *shallow=True*)[¶](#filecmp.dircmp "Link to this definition")
:   Construct a new directory comparison object, to compare the directories *a*
    and *b*. *ignore* is a list of names to ignore, and defaults to
    [`filecmp.DEFAULT_IGNORES`](#filecmp.DEFAULT_IGNORES "filecmp.DEFAULT_IGNORES"). *hide* is a list of names to hide, and
    defaults to `[os.curdir, os.pardir]`.

    The [`dircmp`](#filecmp.dircmp "filecmp.dircmp") class compares files by doing *shallow* comparisons
    as described for [`filecmp.cmp()`](#filecmp.cmp "filecmp.cmp") by default using the *shallow*
    parameter.

    Changed in version 3.13: Added the *shallow* parameter.

    The [`dircmp`](#filecmp.dircmp "filecmp.dircmp") class provides the following methods:

    report()[¶](#filecmp.dircmp.report "Link to this definition")
    :   Print (to [`sys.stdout`](sys.html#sys.stdout "sys.stdout")) a comparison between *a* and *b*.

    report\_partial\_closure()[¶](#filecmp.dircmp.report_partial_closure "Link to this definition")
    :   Print a comparison between *a* and *b* and common immediate
        subdirectories.

    report\_full\_closure()[¶](#filecmp.dircmp.report_full_closure "Link to this definition")
    :   Print a comparison between *a* and *b* and common subdirectories
        (recursively).

    The [`dircmp`](#filecmp.dircmp "filecmp.dircmp") class offers a number of interesting attributes that may be
    used to get various bits of information about the directory trees being
    compared.

    Note that via [`__getattr__()`](../reference/datamodel.html#object.__getattr__ "object.__getattr__") hooks, all attributes are computed lazily,
    so there is no speed penalty if only those attributes which are lightweight
    to compute are used.

    left[¶](#filecmp.dircmp.left "Link to this definition")
    :   The directory *a*.

    right[¶](#filecmp.dircmp.right "Link to this definition")
    :   The directory *b*.

    left\_list[¶](#filecmp.dircmp.left_list "Link to this definition")
    :   Files and subdirectories in *a*, filtered by *hide* and *ignore*.

    right\_list[¶](#filecmp.dircmp.right_list "Link to this definition")
    :   Files and subdirectories in *b*, filtered by *hide* and *ignore*.

    common[¶](#filecmp.dircmp.common "Link to this definition")
    :   Files and subdirectories in both *a* and *b*.

    left\_only[¶](#filecmp.dircmp.left_only "Link to this definition")
    :   Files and subdirectories only in *a*.

    right\_only[¶](#filecmp.dircmp.right_only "Link to this definition")
    :   Files and subdirectories only in *b*.

    common\_dirs[¶](#filecmp.dircmp.common_dirs "Link to this definition")
    :   Subdirectories in both *a* and *b*.

    common\_files[¶](#filecmp.dircmp.common_files "Link to this definition")
    :   Files in both *a* and *b*.

    common\_funny[¶](#filecmp.dircmp.common_funny "Link to this definition")
    :   Names in both *a* and *b*, such that the type differs between the
        directories, or names for which [`os.stat()`](os.html#os.stat "os.stat") reports an error.

    same\_files[¶](#filecmp.dircmp.same_files "Link to this definition")
    :   Files which are identical in both *a* and *b*, using the class’s
        file comparison operator.

    diff\_files[¶](#filecmp.dircmp.diff_files "Link to this definition")
    :   Files which are in both *a* and *b*, whose contents differ according
        to the class’s file comparison operator.

    funny\_files[¶](#filecmp.dircmp.funny_files "Link to this definition")
    :   Files which are in both *a* and *b*, but could not be compared.

    subdirs[¶](#filecmp.dircmp.subdirs "Link to this definition")
    :   A dictionary mapping names in [`common_dirs`](#filecmp.dircmp.common_dirs "filecmp.dircmp.common_dirs") to [`dircmp`](#filecmp.dircmp "filecmp.dircmp")
        instances (or MyDirCmp instances if this instance is of type MyDirCmp, a
        subclass of [`dircmp`](#filecmp.dircmp "filecmp.dircmp")).

        Changed in version 3.10: Previously entries were always [`dircmp`](#filecmp.dircmp "filecmp.dircmp") instances. Now entries
        are the same type as *self*, if *self* is a subclass of
        [`dircmp`](#filecmp.dircmp "filecmp.dircmp").

filecmp.DEFAULT\_IGNORES[¶](#filecmp.DEFAULT_IGNORES "Link to this definition")
:   Added in version 3.4.

    List of directories ignored by [`dircmp`](#filecmp.dircmp "filecmp.dircmp") by default.

Here is a simplified example of using the `subdirs` attribute to search
recursively through two directories to show common different files:

```
>>> from filecmp import dircmp
>>> def print_diff_files(dcmp):
...     for name in dcmp.diff_files:
...         print("diff_file %s found in %s and %s" % (name, dcmp.left,
...               dcmp.right))
...     for sub_dcmp in dcmp.subdirs.values():
...         print_diff_files(sub_dcmp)
...
>>> dcmp = dircmp('dir1', 'dir2')
>>> print_diff_files(dcmp)
```

### [Table of Contents](../contents.html)

* [`filecmp` — File and Directory Comparisons](#)
  + [The `dircmp` class](#the-dircmp-class)

#### Previous topic

[`stat` — Interpreting `stat()` results](stat.html "previous chapter")

#### Next topic

[`tempfile` — Generate temporary files and directories](tempfile.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/filecmp.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tempfile.html "tempfile — Generate temporary files and directories") |
* [previous](stat.html "stat — Interpreting stat() results") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File and Directory Access](filesys.html) »
* `filecmp` — File and Directory Comparisons
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