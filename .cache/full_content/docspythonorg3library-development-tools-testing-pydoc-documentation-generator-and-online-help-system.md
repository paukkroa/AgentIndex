### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](devmode.html "Python Development Mode") |
* [previous](typing.html "typing — Support for type hints") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Development Tools](development.html) »
* `pydoc` — Documentation generator and online help system
* |
* Theme
  Auto
  Light
  Dark
   |

# `pydoc` — Documentation generator and online help system[¶](#module-pydoc "Link to this heading")

**Source code:** [Lib/pydoc.py](https://github.com/python/cpython/tree/3.14/Lib/pydoc.py)

---

The `pydoc` module automatically generates documentation from Python
modules. The documentation can be presented as pages of text on the console,
served to a web browser, or saved to HTML files.

For modules, classes, functions and methods, the displayed documentation is
derived from the docstring (i.e. the [`__doc__`](stdtypes.html#definition.__doc__ "definition.__doc__") attribute) of the object,
and recursively of its documentable members. If there is no docstring,
`pydoc` tries to obtain a description from the block of comment lines just
above the definition of the class, function or method in the source file, or at
the top of the module (see [`inspect.getcomments()`](inspect.html#inspect.getcomments "inspect.getcomments")).

The built-in function [`help()`](functions.html#help "help") invokes the online help system in the
interactive interpreter, which uses `pydoc` to generate its documentation
as text on the console. The same text documentation can also be viewed from
outside the Python interpreter by running **pydoc** as a script at the
operating system’s command prompt. For example, running

```
python -m pydoc sys
```

at a shell prompt will display documentation on the [`sys`](sys.html#module-sys "sys: Access system-specific parameters and functions.") module, in a
style similar to the manual pages shown by the Unix **man** command. The
argument to **pydoc** can be the name of a function, module, or package,
or a dotted reference to a class, method, or function within a module or module
in a package. If the argument to **pydoc** looks like a path (that is,
it contains the path separator for your operating system, such as a slash in
Unix), and refers to an existing Python source file, then documentation is
produced for that file.

Note

In order to find objects and their documentation, `pydoc` imports the
module(s) to be documented. Therefore, any code on module level will be
executed on that occasion. Use an `if __name__ == '__main__':` guard to
only execute code when a file is invoked as a script and not just imported.

When printing output to the console, **pydoc** attempts to paginate the
output for easier reading. If either the `MANPAGER` or the
`PAGER` environment variable is set, **pydoc** will use its
value as a pagination program. When both are set, `MANPAGER` is used.

Specifying a `-w` flag before the argument will cause HTML documentation
to be written out to a file in the current directory, instead of displaying text
on the console.

Specifying a `-k` flag before the argument will search the synopsis
lines of all available modules for the keyword given as the argument, again in a
manner similar to the Unix **man** command. The synopsis line of a
module is the first line of its documentation string.

You can also use **pydoc** to start an HTTP server on the local machine
that will serve documentation to visiting web browsers. **python -m pydoc -p 1234**
will start a HTTP server on port 1234, allowing you to browse the
documentation at `http://localhost:1234/` in your preferred web browser.
Specifying `0` as the port number will select an arbitrary unused port.

**python -m pydoc -n <hostname>** will start the server listening at the given
hostname. By default the hostname is ‘localhost’ but if you want the server to
be reached from other machines, you may want to change the host name that the
server responds to. During development this is especially useful if you want
to run pydoc from within a container.

**python -m pydoc -b** will start the server and additionally open a web
browser to a module index page. Each served page has a navigation bar at the
top where you can *Get* help on an individual item, *Search* all modules with a
keyword in their synopsis line, and go to the *Module index*, *Topics* and
*Keywords* pages.

When **pydoc** generates documentation, it uses the current environment
and path to locate modules. Thus, invoking **pydoc spam**
documents precisely the version of the module you would get if you started the
Python interpreter and typed `import spam`.

Module docs for core modules are assumed to reside in
`https://docs.python.org/X.Y/library/` where `X` and `Y` are the
major and minor version numbers of the Python interpreter. This can
be overridden by setting the `PYTHONDOCS` environment variable
to a different URL or to a local directory containing the Library
Reference Manual pages.

Changed in version 3.2: Added the `-b` option.

Changed in version 3.3: The `-g` command line option was removed.

Changed in version 3.4: `pydoc` now uses [`inspect.signature()`](inspect.html#inspect.signature "inspect.signature") rather than
[`inspect.getfullargspec()`](inspect.html#inspect.getfullargspec "inspect.getfullargspec") to extract signature information from
callables.

Changed in version 3.7: Added the `-n` option.

#### Previous topic

[`typing` — Support for type hints](typing.html "previous chapter")

#### Next topic

[Python Development Mode](devmode.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/pydoc.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](devmode.html "Python Development Mode") |
* [previous](typing.html "typing — Support for type hints") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Development Tools](development.html) »
* `pydoc` — Documentation generator and online help system
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