### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](plistlib.html "plistlib — Generate and parse Apple .plist files") |
* [previous](tomllib.html "tomllib — Parse TOML files") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File Formats](fileformats.html) »
* `netrc` — netrc file processing
* |
* Theme
  Auto
  Light
  Dark
   |

# `netrc` — netrc file processing[¶](#module-netrc "Link to this heading")

**Source code:** [Lib/netrc.py](https://github.com/python/cpython/tree/3.14/Lib/netrc.py)

---

The [`netrc`](#netrc.netrc "netrc.netrc") class parses and encapsulates the netrc file format used by
the Unix **ftp** program and other FTP clients.

*class* netrc.netrc([*file*])[¶](#netrc.netrc "Link to this definition")
:   A [`netrc`](#netrc.netrc "netrc.netrc") instance or subclass instance encapsulates data from a netrc
    file. The initialization argument, if present, specifies the file to parse. If
    no argument is given, the file `.netrc` in the user’s home directory –
    as determined by [`os.path.expanduser()`](os.path.html#os.path.expanduser "os.path.expanduser") – will be read. Otherwise,
    a [`FileNotFoundError`](exceptions.html#FileNotFoundError "FileNotFoundError") exception will be raised.
    Parse errors will raise [`NetrcParseError`](#netrc.NetrcParseError "netrc.NetrcParseError") with diagnostic
    information including the file name, line number, and terminating token.

    If no argument is specified on a POSIX system, the presence of passwords in
    the `.netrc` file will raise a [`NetrcParseError`](#netrc.NetrcParseError "netrc.NetrcParseError") if the file
    ownership or permissions are insecure (owned by a user other than the user
    running the process, or accessible for read or write by any other user).
    This implements security behavior equivalent to that of ftp and other
    programs that use `.netrc`. Such security checks are not available
    on platforms that do not support [`os.getuid()`](os.html#os.getuid "os.getuid").

    Changed in version 3.4: Added the POSIX permission check.

    Changed in version 3.7: [`os.path.expanduser()`](os.path.html#os.path.expanduser "os.path.expanduser") is used to find the location of the
    `.netrc` file when *file* is not passed as argument.

    Changed in version 3.10: [`netrc`](#module-netrc "netrc: Loading of .netrc files.") try UTF-8 encoding before using locale specific
    encoding.
    The entry in the netrc file no longer needs to contain all tokens. The missing
    tokens’ value default to an empty string. All the tokens and their values now
    can contain arbitrary characters, like whitespace and non-ASCII characters.
    If the login name is anonymous, it won’t trigger the security check.

*exception* netrc.NetrcParseError[¶](#netrc.NetrcParseError "Link to this definition")
:   Exception raised by the [`netrc`](#netrc.netrc "netrc.netrc") class when syntactical errors are
    encountered in source text. Instances of this exception provide three
    interesting attributes:

    msg[¶](#netrc.NetrcParseError.msg "Link to this definition")
    :   Textual explanation of the error.

    filename[¶](#netrc.NetrcParseError.filename "Link to this definition")
    :   The name of the source file.

    lineno[¶](#netrc.NetrcParseError.lineno "Link to this definition")
    :   The line number on which the error was found.

## netrc Objects[¶](#netrc-objects "Link to this heading")

A [`netrc`](#netrc.netrc "netrc.netrc") instance has the following methods:

netrc.authenticators(*host*)[¶](#netrc.netrc.authenticators "Link to this definition")
:   Return a 3-tuple `(login, account, password)` of authenticators for *host*.
    If the netrc file did not contain an entry for the given host, return the tuple
    associated with the ‘default’ entry. If neither matching host nor default entry
    is available, return `None`.

netrc.\_\_repr\_\_()[¶](#netrc.netrc.__repr__ "Link to this definition")
:   Dump the class data as a string in the format of a netrc file. (This discards
    comments and may reorder the entries.)

Instances of [`netrc`](#netrc.netrc "netrc.netrc") have public instance variables:

netrc.hosts[¶](#netrc.netrc.hosts "Link to this definition")
:   Dictionary mapping host names to `(login, account, password)` tuples. The
    ‘default’ entry, if any, is represented as a pseudo-host by that name.

netrc.macros[¶](#netrc.netrc.macros "Link to this definition")
:   Dictionary mapping macro names to string lists.

### [Table of Contents](../contents.html)

* [`netrc` — netrc file processing](#)
  + [netrc Objects](#netrc-objects)

#### Previous topic

[`tomllib` — Parse TOML files](tomllib.html "previous chapter")

#### Next topic

[`plistlib` — Generate and parse Apple `.plist` files](plistlib.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/netrc.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](plistlib.html "plistlib — Generate and parse Apple .plist files") |
* [previous](tomllib.html "tomllib — Parse TOML files") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File Formats](fileformats.html) »
* `netrc` — netrc file processing
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