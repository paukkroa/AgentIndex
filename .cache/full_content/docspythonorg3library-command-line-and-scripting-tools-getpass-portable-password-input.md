### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](fileinput.html "fileinput — Iterate over lines from multiple input streams") |
* [previous](optparse.html "optparse — Parser for command line options") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `getpass` — Portable password input
* |
* Theme
  Auto
  Light
  Dark
   |

# `getpass` — Portable password input[¶](#module-getpass "Link to this heading")

**Source code:** [Lib/getpass.py](https://github.com/python/cpython/tree/3.14/Lib/getpass.py)

---

[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

The `getpass` module provides two functions:

getpass.getpass(*prompt='Password: '*, *stream=None*, *\**, *echo\_char=None*)[¶](#getpass.getpass "Link to this definition")
:   Prompt the user for a password without echoing. The user is prompted using
    the string *prompt*, which defaults to `'Password: '`. On Unix, the
    prompt is written to the file-like object *stream* using the replace error
    handler if needed. *stream* defaults to the controlling terminal
    (`/dev/tty`) or if that is unavailable to `sys.stderr` (this
    argument is ignored on Windows).

    The *echo\_char* argument controls how user input is displayed while typing.
    If *echo\_char* is `None` (default), input remains hidden. Otherwise,
    *echo\_char* must be a single printable ASCII character and each
    typed character is replaced by it. For example, `echo_char='*'` will
    display asterisks instead of the actual input.

    If echo free input is unavailable getpass() falls back to printing
    a warning message to *stream* and reading from `sys.stdin` and
    issuing a [`GetPassWarning`](#getpass.GetPassWarning "getpass.GetPassWarning").

    Note

    If you call getpass from within IDLE, the input may be done in the
    terminal you launched IDLE from rather than the idle window itself.

    Note

    On Unix systems, when *echo\_char* is set, the terminal will be
    configured to operate in
    *[noncanonical mode](https://manpages.debian.org/termios(3)#Canonical_and_noncanonical_mode)*.
    In particular, this means that line editing shortcuts such as
    `Ctrl`+`U` will not work and may insert unexpected characters into
    the input.

    Changed in version 3.14: Added the *echo\_char* parameter for keyboard feedback.

*exception* getpass.GetPassWarning[¶](#getpass.GetPassWarning "Link to this definition")
:   A [`UserWarning`](exceptions.html#UserWarning "UserWarning") subclass issued when password input may be echoed.

getpass.getuser()[¶](#getpass.getuser "Link to this definition")
:   Return the “login name” of the user.

    This function checks the environment variables `LOGNAME`,
    `USER`, `LNAME` and `USERNAME`, in order, and
    returns the value of the first one which is set to a non-empty string. If
    none are set, the login name from the password database is returned on
    systems which support the [`pwd`](pwd.html#module-pwd "pwd: The password database (getpwnam() and friends).") module, otherwise, an [`OSError`](exceptions.html#OSError "OSError")
    is raised.

    In general, this function should be preferred over [`os.getlogin()`](os.html#os.getlogin "os.getlogin").

    Changed in version 3.13: Previously, various exceptions beyond just [`OSError`](exceptions.html#OSError "OSError") were raised.

#### Previous topic

[`optparse` — Parser for command line options](optparse.html "previous chapter")

#### Next topic

[`fileinput` — Iterate over lines from multiple input streams](fileinput.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/getpass.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](fileinput.html "fileinput — Iterate over lines from multiple input streams") |
* [previous](optparse.html "optparse — Parser for command line options") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `getpass` — Portable password input
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