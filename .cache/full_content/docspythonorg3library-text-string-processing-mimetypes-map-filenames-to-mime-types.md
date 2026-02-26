### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings") |
* [previous](mailbox.html "mailbox — Manipulate mailboxes in various formats") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `mimetypes` — Map filenames to MIME types
* |
* Theme
  Auto
  Light
  Dark
   |

# `mimetypes` — Map filenames to MIME types[¶](#module-mimetypes "Link to this heading")

**Source code:** [Lib/mimetypes.py](https://github.com/python/cpython/tree/3.14/Lib/mimetypes.py)

---

The `mimetypes` module converts between a filename or URL and the MIME type
associated with the filename extension. Conversions are provided from filename
to MIME type and from MIME type to filename extension; encodings are not
supported for the latter conversion.

The module provides one class and a number of convenience functions. The
functions are the normal interface to this module, but some applications may be
interested in the class as well.

The functions described below provide the primary interface for this module. If
the module has not been initialized, they will call [`init()`](#mimetypes.init "mimetypes.init") if they rely on
the information [`init()`](#mimetypes.init "mimetypes.init") sets up.

mimetypes.guess\_type(*url*, *strict=True*)[¶](#mimetypes.guess_type "Link to this definition")
:   Guess the type of a file based on its filename, path or URL, given by *url*.
    URL can be a string or a [path-like object](../glossary.html#term-path-like-object).

    The return value is a tuple `(type, encoding)` where *type* is `None` if the
    type can’t be guessed (missing or unknown suffix) or a string of the form
    `'type/subtype'`, usable for a MIME *content-type* header.

    *encoding* is `None` for no encoding or the name of the program used to encode
    (e.g. **compress** or **gzip**). The encoding is suitable for use
    as a *Content-Encoding* header, **not** as a
    *Content-Transfer-Encoding* header. The mappings are table driven.
    Encoding suffixes are case sensitive; type suffixes are first tried case
    sensitively, then case insensitively.

    The optional *strict* argument is a flag specifying whether the list of known MIME types
    is limited to only the official types [registered with IANA](https://www.iana.org/assignments/media-types/media-types.xhtml).
    However, the behavior of this module also depends on the underlying operating
    system. Only file types recognized by the OS or explicitly registered with
    Python’s internal database can be identified. When *strict* is `True` (the
    default), only the IANA types are supported; when *strict* is `False`, some
    additional non-standard but commonly used MIME types are also recognized.

    Changed in version 3.8: Added support for *url* being a [path-like object](../glossary.html#term-path-like-object).

    Deprecated since version 3.13: Passing a file path instead of URL is [soft deprecated](../glossary.html#term-soft-deprecated).
    Use [`guess_file_type()`](#mimetypes.guess_file_type "mimetypes.guess_file_type") for this.

mimetypes.guess\_file\_type(*path*, *\**, *strict=True*)[¶](#mimetypes.guess_file_type "Link to this definition")
:   Guess the type of a file based on its path, given by *path*.
    Similar to the [`guess_type()`](#mimetypes.guess_type "mimetypes.guess_type") function, but accepts a path instead of URL.
    Path can be a string, a bytes object or a [path-like object](../glossary.html#term-path-like-object).

    Added in version 3.13.

mimetypes.guess\_all\_extensions(*type*, *strict=True*)[¶](#mimetypes.guess_all_extensions "Link to this definition")
:   Guess the extensions for a file based on its MIME type, given by *type*. The
    return value is a list of strings giving all possible filename extensions,
    including the leading dot (`'.'`). The extensions are not guaranteed to have
    been associated with any particular data stream, but would be mapped to the MIME
    type *type* by [`guess_type()`](#mimetypes.guess_type "mimetypes.guess_type") and [`guess_file_type()`](#mimetypes.guess_file_type "mimetypes.guess_file_type").

    The optional *strict* argument has the same meaning as with the [`guess_type()`](#mimetypes.guess_type "mimetypes.guess_type") function.

mimetypes.guess\_extension(*type*, *strict=True*)[¶](#mimetypes.guess_extension "Link to this definition")
:   Guess the extension for a file based on its MIME type, given by *type*. The
    return value is a string giving a filename extension, including the leading dot
    (`'.'`). The extension is not guaranteed to have been associated with any
    particular data stream, but would be mapped to the MIME type *type* by
    [`guess_type()`](#mimetypes.guess_type "mimetypes.guess_type") and [`guess_file_type()`](#mimetypes.guess_file_type "mimetypes.guess_file_type").
    If no extension can be guessed for *type*, `None` is returned.

    The optional *strict* argument has the same meaning as with the [`guess_type()`](#mimetypes.guess_type "mimetypes.guess_type") function.

Some additional functions and data items are available for controlling the
behavior of the module.

mimetypes.init(*files=None*)[¶](#mimetypes.init "Link to this definition")
:   Initialize the internal data structures. If given, *files* must be a sequence
    of file names which should be used to augment the default type map. If omitted,
    the file names to use are taken from [`knownfiles`](#mimetypes.knownfiles "mimetypes.knownfiles"); on Windows, the
    current registry settings are loaded. Each file named in *files* or
    [`knownfiles`](#mimetypes.knownfiles "mimetypes.knownfiles") takes precedence over those named before it. Calling
    [`init()`](#mimetypes.init "mimetypes.init") repeatedly is allowed.

    Specifying an empty list for *files* will prevent the system defaults from
    being applied: only the well-known values will be present from a built-in list.

    If *files* is `None` the internal data structure is completely rebuilt to its
    initial default value. This is a stable operation and will produce the same results
    when called multiple times.

    Changed in version 3.2: Previously, Windows registry settings were ignored.

mimetypes.read\_mime\_types(*filename*)[¶](#mimetypes.read_mime_types "Link to this definition")
:   Load the type map given in the file *filename*, if it exists. The type map is
    returned as a dictionary mapping filename extensions, including the leading dot
    (`'.'`), to strings of the form `'type/subtype'`. If the file *filename*
    does not exist or cannot be read, `None` is returned.

mimetypes.add\_type(*type*, *ext*, *strict=True*)[¶](#mimetypes.add_type "Link to this definition")
:   Add a mapping from the MIME type *type* to the extension *ext*. When the
    extension is already known, the new type will replace the old one. When the type
    is already known the extension will be added to the list of known extensions.

    When *strict* is `True` (the default), the mapping will be added to the
    official MIME types, otherwise to the non-standard ones.

mimetypes.inited[¶](#mimetypes.inited "Link to this definition")
:   Flag indicating whether or not the global data structures have been initialized.
    This is set to `True` by [`init()`](#mimetypes.init "mimetypes.init").

mimetypes.knownfiles[¶](#mimetypes.knownfiles "Link to this definition")
:   List of type map file names commonly installed. These files are typically named
    `mime.types` and are installed in different locations by different
    packages.

mimetypes.suffix\_map[¶](#mimetypes.suffix_map "Link to this definition")
:   Dictionary mapping suffixes to suffixes. This is used to allow recognition of
    encoded files for which the encoding and the type are indicated by the same
    extension. For example, the `.tgz` extension is mapped to `.tar.gz`
    to allow the encoding and type to be recognized separately.

mimetypes.encodings\_map[¶](#mimetypes.encodings_map "Link to this definition")
:   Dictionary mapping filename extensions to encoding types.

mimetypes.types\_map[¶](#mimetypes.types_map "Link to this definition")
:   Dictionary mapping filename extensions to MIME types.

mimetypes.common\_types[¶](#mimetypes.common_types "Link to this definition")
:   Dictionary mapping filename extensions to non-standard, but commonly found MIME
    types.

An example usage of the module:

```
>>> import mimetypes
>>> mimetypes.init()
>>> mimetypes.knownfiles
['/etc/mime.types', '/etc/httpd/mime.types', ... ]
>>> mimetypes.suffix_map['.tgz']
'.tar.gz'
>>> mimetypes.encodings_map['.gz']
'gzip'
>>> mimetypes.types_map['.tgz']
'application/x-tar-gz'
```

## MimeTypes objects[¶](#mimetypes-objects "Link to this heading")

The [`MimeTypes`](#mimetypes.MimeTypes "mimetypes.MimeTypes") class may be useful for applications which may want more
than one MIME-type database; it provides an interface similar to the one of the
`mimetypes` module.

*class* mimetypes.MimeTypes(*filenames=()*, *strict=True*)[¶](#mimetypes.MimeTypes "Link to this definition")
:   This class represents a MIME-types database. By default, it provides access to
    the same database as the rest of this module. The initial database is a copy of
    that provided by the module, and may be extended by loading additional
    `mime.types`-style files into the database using the [`read()`](#mimetypes.MimeTypes.read "mimetypes.MimeTypes.read") or
    [`readfp()`](#mimetypes.MimeTypes.readfp "mimetypes.MimeTypes.readfp") methods. The mapping dictionaries may also be cleared before
    loading additional data if the default data is not desired.

    The optional *filenames* parameter can be used to cause additional files to be
    loaded “on top” of the default database.

    suffix\_map[¶](#mimetypes.MimeTypes.suffix_map "Link to this definition")
    :   Dictionary mapping suffixes to suffixes. This is used to allow recognition of
        encoded files for which the encoding and the type are indicated by the same
        extension. For example, the `.tgz` extension is mapped to `.tar.gz`
        to allow the encoding and type to be recognized separately. This is initially a
        copy of the global [`suffix_map`](#mimetypes.suffix_map "mimetypes.suffix_map") defined in the module.

    encodings\_map[¶](#mimetypes.MimeTypes.encodings_map "Link to this definition")
    :   Dictionary mapping filename extensions to encoding types. This is initially a
        copy of the global [`encodings_map`](#mimetypes.encodings_map "mimetypes.encodings_map") defined in the module.

    types\_map[¶](#mimetypes.MimeTypes.types_map "Link to this definition")
    :   Tuple containing two dictionaries, mapping filename extensions to MIME types:
        the first dictionary is for the non-standards types and the second one is for
        the standard types. They are initialized by [`common_types`](#mimetypes.common_types "mimetypes.common_types") and
        [`types_map`](#mimetypes.types_map "mimetypes.types_map").

    types\_map\_inv[¶](#mimetypes.MimeTypes.types_map_inv "Link to this definition")
    :   Tuple containing two dictionaries, mapping MIME types to a list of filename
        extensions: the first dictionary is for the non-standards types and the
        second one is for the standard types. They are initialized by
        [`common_types`](#mimetypes.common_types "mimetypes.common_types") and [`types_map`](#mimetypes.types_map "mimetypes.types_map").

    guess\_extension(*type*, *strict=True*)[¶](#mimetypes.MimeTypes.guess_extension "Link to this definition")
    :   Similar to the [`guess_extension()`](#mimetypes.guess_extension "mimetypes.guess_extension") function, using the tables stored as part
        of the object.

    guess\_type(*url*, *strict=True*)[¶](#mimetypes.MimeTypes.guess_type "Link to this definition")
    :   Similar to the [`guess_type()`](#mimetypes.guess_type "mimetypes.guess_type") function, using the tables stored as part of
        the object.

    guess\_file\_type(*path*, *\**, *strict=True*)[¶](#mimetypes.MimeTypes.guess_file_type "Link to this definition")
    :   Similar to the [`guess_file_type()`](#mimetypes.guess_file_type "mimetypes.guess_file_type") function, using the tables stored
        as part of the object.

        Added in version 3.13.

    guess\_all\_extensions(*type*, *strict=True*)[¶](#mimetypes.MimeTypes.guess_all_extensions "Link to this definition")
    :   Similar to the [`guess_all_extensions()`](#mimetypes.guess_all_extensions "mimetypes.guess_all_extensions") function, using the tables stored
        as part of the object.

    read(*filename*, *strict=True*)[¶](#mimetypes.MimeTypes.read "Link to this definition")
    :   Load MIME information from a file named *filename*. This uses [`readfp()`](#mimetypes.MimeTypes.readfp "mimetypes.MimeTypes.readfp") to
        parse the file.

        If *strict* is `True`, information will be added to list of standard types,
        else to the list of non-standard types.

    readfp(*fp*, *strict=True*)[¶](#mimetypes.MimeTypes.readfp "Link to this definition")
    :   Load MIME type information from an open file *fp*. The file must have the format of
        the standard `mime.types` files.

        If *strict* is `True`, information will be added to the list of standard
        types, else to the list of non-standard types.

    read\_windows\_registry(*strict=True*)[¶](#mimetypes.MimeTypes.read_windows_registry "Link to this definition")
    :   Load MIME type information from the Windows registry.

        [Availability](intro.html#availability): Windows.

        If *strict* is `True`, information will be added to the list of standard
        types, else to the list of non-standard types.

        Added in version 3.2.

    add\_type(*type*, *ext*, *strict=True*)[¶](#mimetypes.MimeTypes.add_type "Link to this definition")
    :   Add a mapping from the MIME type *type* to the extension *ext*.
        Valid extensions start with a ‘.’ or are empty. When the
        extension is already known, the new type will replace the old one. When the type
        is already known the extension will be added to the list of known extensions.

        When *strict* is `True` (the default), the mapping will be added to the
        official MIME types, otherwise to the non-standard ones.

        Deprecated since version 3.14, will be removed in version 3.16: Invalid, undotted extensions will raise a
        [`ValueError`](exceptions.html#ValueError "ValueError") in Python 3.16.

## Command-line usage[¶](#command-line-usage "Link to this heading")

The `mimetypes` module can be executed as a script from the command line.

```
python -m mimetypes [-h] [-e] [-l] type [type ...]
```

The following options are accepted:

-h[¶](#cmdoption-mimetypes-h "Link to this definition")

--help[¶](#cmdoption-mimetypes-help "Link to this definition")
:   Show the help message and exit.

-e[¶](#cmdoption-mimetypes-e "Link to this definition")

--extension[¶](#cmdoption-mimetypes-extension "Link to this definition")
:   Guess extension instead of type.

-l[¶](#cmdoption-mimetypes-l "Link to this definition")

--lenient[¶](#cmdoption-mimetypes-lenient "Link to this definition")
:   Additionally search for some common, but non-standard types.

By default the script converts MIME types to file extensions.
However, if `--extension` is specified,
it converts file extensions to MIME types.

For each `type` entry, the script writes a line into the standard output
stream. If an unknown type occurs, it writes an error message into the
standard error stream and exits with the return code `1`.

## Command-line example[¶](#command-line-example "Link to this heading")

Here are some examples of typical usage of the `mimetypes` command-line
interface:

```
$ # get a MIME type by a file name
$ python -m mimetypes filename.png
type: image/png encoding: None

$ # get a MIME type by a URL
$ python -m mimetypes https://example.com/filename.txt
type: text/plain encoding: None

$ # get a complex MIME type
$ python -m mimetypes filename.tar.gz
type: application/x-tar encoding: gzip

$ # get a MIME type for a rare file extension
$ python -m mimetypes filename.pict
error: unknown extension of filename.pict

$ # now look in the extended database built into Python
$ python -m mimetypes --lenient filename.pict
type: image/pict encoding: None

$ # get a file extension by a MIME type
$ python -m mimetypes --extension text/javascript
.js

$ # get a file extension by a rare MIME type
$ python -m mimetypes --extension text/xul
error: unknown type text/xul

$ # now look in the extended database again
$ python -m mimetypes --extension --lenient text/xul
.xul

$ # try to feed an unknown file extension
$ python -m mimetypes filename.sh filename.nc filename.xxx filename.txt
type: application/x-sh encoding: None
type: application/x-netcdf encoding: None
error: unknown extension of filename.xxx

$ # try to feed an unknown MIME type
$ python -m mimetypes --extension audio/aac audio/opus audio/future audio/x-wav
.aac
.opus
error: unknown type audio/future
```

### [Table of Contents](../contents.html)

* [`mimetypes` — Map filenames to MIME types](#)
  + [MimeTypes objects](#mimetypes-objects)
  + [Command-line usage](#command-line-usage)
  + [Command-line example](#command-line-example)

#### Previous topic

[`mailbox` — Manipulate mailboxes in various formats](mailbox.html "previous chapter")

#### Next topic

[`base64` — Base16, Base32, Base64, Base85 Data Encodings](base64.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/mimetypes.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings") |
* [previous](mailbox.html "mailbox — Manipulate mailboxes in various formats") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `mimetypes` — Map filenames to MIME types
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