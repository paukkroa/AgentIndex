### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](datatypes.html "Data Types") |
* [previous](struct.html "struct — Interpret bytes as packed binary data") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Binary Data Services](binary.html) »
* `codecs` — Codec registry and base classes
* |
* Theme
  Auto
  Light
  Dark
   |

# `codecs` — Codec registry and base classes[¶](#module-codecs "Link to this heading")

**Source code:** [Lib/codecs.py](https://github.com/python/cpython/tree/3.14/Lib/codecs.py)

---

This module defines base classes for standard Python codecs (encoders and
decoders) and provides access to the internal Python codec registry, which
manages the codec and error handling lookup process. Most standard codecs
are [text encodings](../glossary.html#term-text-encoding), which encode text to bytes (and
decode bytes to text), but there are also codecs provided that encode text to
text, and bytes to bytes. Custom codecs may encode and decode between arbitrary
types, but some module features are restricted to be used specifically with
[text encodings](../glossary.html#term-text-encoding) or with codecs that encode to
[`bytes`](stdtypes.html#bytes "bytes").

The module defines the following functions for encoding and decoding with
any codec:

codecs.encode(*obj*, *encoding='utf-8'*, *errors='strict'*)[¶](#codecs.encode "Link to this definition")
:   Encodes *obj* using the codec registered for *encoding*.

    *Errors* may be given to set the desired error handling scheme. The
    default error handler is `'strict'` meaning that encoding errors raise
    [`ValueError`](exceptions.html#ValueError "ValueError") (or a more codec specific subclass, such as
    [`UnicodeEncodeError`](exceptions.html#UnicodeEncodeError "UnicodeEncodeError")). Refer to [Codec Base Classes](#codec-base-classes) for more
    information on codec error handling.

codecs.decode(*obj*, *encoding='utf-8'*, *errors='strict'*)[¶](#codecs.decode "Link to this definition")
:   Decodes *obj* using the codec registered for *encoding*.

    *Errors* may be given to set the desired error handling scheme. The
    default error handler is `'strict'` meaning that decoding errors raise
    [`ValueError`](exceptions.html#ValueError "ValueError") (or a more codec specific subclass, such as
    [`UnicodeDecodeError`](exceptions.html#UnicodeDecodeError "UnicodeDecodeError")). Refer to [Codec Base Classes](#codec-base-classes) for more
    information on codec error handling.

codecs.charmap\_build(*string*)[¶](#codecs.charmap_build "Link to this definition")
:   Return a mapping suitable for encoding with a custom single-byte encoding.
    Given a [`str`](stdtypes.html#str "str") *string* of up to 256 characters representing a
    decoding table, returns either a compact internal mapping object
    `EncodingMap` or a [`dictionary`](stdtypes.html#dict "dict") mapping character ordinals
    to byte values. Raises a [`TypeError`](exceptions.html#TypeError "TypeError") on invalid input.

The full details for each codec can also be looked up directly:

codecs.lookup(*encoding*, */*)[¶](#codecs.lookup "Link to this definition")
:   Looks up the codec info in the Python codec registry and returns a
    [`CodecInfo`](#codecs.CodecInfo "codecs.CodecInfo") object as defined below.

    Encodings are first looked up in the registry’s cache. If not found, the list of
    registered search functions is scanned. If no [`CodecInfo`](#codecs.CodecInfo "codecs.CodecInfo") object is
    found, a [`LookupError`](exceptions.html#LookupError "LookupError") is raised. Otherwise, the [`CodecInfo`](#codecs.CodecInfo "codecs.CodecInfo") object
    is stored in the cache and returned to the caller.

*class* codecs.CodecInfo(*encode*, *decode*, *streamreader=None*, *streamwriter=None*, *incrementalencoder=None*, *incrementaldecoder=None*, *name=None*)[¶](#codecs.CodecInfo "Link to this definition")
:   Codec details when looking up the codec registry. The constructor
    arguments are stored in attributes of the same name:

    name[¶](#codecs.CodecInfo.name "Link to this definition")
    :   The name of the encoding.

    encode[¶](#codecs.CodecInfo.encode "Link to this definition")

    decode[¶](#codecs.CodecInfo.decode "Link to this definition")
    :   The stateless encoding and decoding functions. These must be
        functions or methods which have the same interface as
        the [`encode()`](#codecs.Codec.encode "codecs.Codec.encode") and [`decode()`](#codecs.Codec.decode "codecs.Codec.decode") methods of Codec
        instances (see [Codec Interface](#codec-objects)).
        The functions or methods are expected to work in a stateless mode.

    incrementalencoder[¶](#codecs.CodecInfo.incrementalencoder "Link to this definition")

    incrementaldecoder[¶](#codecs.CodecInfo.incrementaldecoder "Link to this definition")
    :   Incremental encoder and decoder classes or factory functions.
        These have to provide the interface defined by the base classes
        [`IncrementalEncoder`](#codecs.IncrementalEncoder "codecs.IncrementalEncoder") and [`IncrementalDecoder`](#codecs.IncrementalDecoder "codecs.IncrementalDecoder"),
        respectively. Incremental codecs can maintain state.

    streamwriter[¶](#codecs.CodecInfo.streamwriter "Link to this definition")

    streamreader[¶](#codecs.CodecInfo.streamreader "Link to this definition")
    :   Stream writer and reader classes or factory functions. These have to
        provide the interface defined by the base classes
        [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") and [`StreamReader`](#codecs.StreamReader "codecs.StreamReader"), respectively.
        Stream codecs can maintain state.

To simplify access to the various codec components, the module provides
these additional functions which use [`lookup()`](#codecs.lookup "codecs.lookup") for the codec lookup:

codecs.getencoder(*encoding*)[¶](#codecs.getencoder "Link to this definition")
:   Look up the codec for the given encoding and return its encoder function.

    Raises a [`LookupError`](exceptions.html#LookupError "LookupError") in case the encoding cannot be found.

codecs.getdecoder(*encoding*)[¶](#codecs.getdecoder "Link to this definition")
:   Look up the codec for the given encoding and return its decoder function.

    Raises a [`LookupError`](exceptions.html#LookupError "LookupError") in case the encoding cannot be found.

codecs.getincrementalencoder(*encoding*)[¶](#codecs.getincrementalencoder "Link to this definition")
:   Look up the codec for the given encoding and return its incremental encoder
    class or factory function.

    Raises a [`LookupError`](exceptions.html#LookupError "LookupError") in case the encoding cannot be found or the codec
    doesn’t support an incremental encoder.

codecs.getincrementaldecoder(*encoding*)[¶](#codecs.getincrementaldecoder "Link to this definition")
:   Look up the codec for the given encoding and return its incremental decoder
    class or factory function.

    Raises a [`LookupError`](exceptions.html#LookupError "LookupError") in case the encoding cannot be found or the codec
    doesn’t support an incremental decoder.

codecs.getreader(*encoding*)[¶](#codecs.getreader "Link to this definition")
:   Look up the codec for the given encoding and return its [`StreamReader`](#codecs.StreamReader "codecs.StreamReader")
    class or factory function.

    Raises a [`LookupError`](exceptions.html#LookupError "LookupError") in case the encoding cannot be found.

codecs.getwriter(*encoding*)[¶](#codecs.getwriter "Link to this definition")
:   Look up the codec for the given encoding and return its [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter")
    class or factory function.

    Raises a [`LookupError`](exceptions.html#LookupError "LookupError") in case the encoding cannot be found.

Custom codecs are made available by registering a suitable codec search
function:

codecs.register(*search\_function*, */*)[¶](#codecs.register "Link to this definition")
:   Register a codec search function. Search functions are expected to take one
    argument, being the encoding name in all lower case letters with hyphens
    and spaces converted to underscores, and return a [`CodecInfo`](#codecs.CodecInfo "codecs.CodecInfo") object.
    In case a search function cannot find a given encoding, it should return
    `None`.

    Changed in version 3.9: Hyphens and spaces are converted to underscore.

codecs.unregister(*search\_function*, */*)[¶](#codecs.unregister "Link to this definition")
:   Unregister a codec search function and clear the registry’s cache.
    If the search function is not registered, do nothing.

    Added in version 3.10.

While the builtin [`open()`](functions.html#open "open") and the associated [`io`](io.html#module-io "io: Core tools for working with streams.") module are the
recommended approach for working with encoded text files, this module
provides additional utility functions and classes that allow the use of a
wider range of codecs when working with binary files:

codecs.open(*filename*, *mode='r'*, *encoding=None*, *errors='strict'*, *buffering=-1*)[¶](#codecs.open "Link to this definition")
:   Open an encoded file using the given *mode* and return an instance of
    [`StreamReaderWriter`](#codecs.StreamReaderWriter "codecs.StreamReaderWriter"), providing transparent encoding/decoding.
    The default file mode is `'r'`, meaning to open the file in read mode.

    Note

    If *encoding* is not `None`, then the
    underlying encoded files are always opened in binary mode.
    No automatic conversion of `'\n'` is done on reading and writing.
    The *mode* argument may be any binary mode acceptable to the built-in
    [`open()`](functions.html#open "open") function; the `'b'` is automatically added.

    *encoding* specifies the encoding which is to be used for the file.
    Any encoding that encodes to and decodes from bytes is allowed, and
    the data types supported by the file methods depend on the codec used.

    *errors* may be given to define the error handling. It defaults to `'strict'`
    which causes a [`ValueError`](exceptions.html#ValueError "ValueError") to be raised in case an encoding error occurs.

    *buffering* has the same meaning as for the built-in [`open()`](functions.html#open "open") function.
    It defaults to -1 which means that the default buffer size will be used.

    Changed in version 3.11: The `'U'` mode has been removed.

    Deprecated since version 3.14: [`codecs.open()`](#codecs.open "codecs.open") has been superseded by [`open()`](functions.html#open "open").

codecs.EncodedFile(*file*, *data\_encoding*, *file\_encoding=None*, *errors='strict'*)[¶](#codecs.EncodedFile "Link to this definition")
:   Return a [`StreamRecoder`](#codecs.StreamRecoder "codecs.StreamRecoder") instance, a wrapped version of *file*
    which provides transparent transcoding. The original file is closed
    when the wrapped version is closed.

    Data written to the wrapped file is decoded according to the given
    *data\_encoding* and then written to the original file as bytes using
    *file\_encoding*. Bytes read from the original file are decoded
    according to *file\_encoding*, and the result is encoded
    using *data\_encoding*.

    If *file\_encoding* is not given, it defaults to *data\_encoding*.

    *errors* may be given to define the error handling. It defaults to
    `'strict'`, which causes [`ValueError`](exceptions.html#ValueError "ValueError") to be raised in case an encoding
    error occurs.

codecs.iterencode(*iterator*, *encoding*, *errors='strict'*, *\*\*kwargs*)[¶](#codecs.iterencode "Link to this definition")
:   Uses an incremental encoder to iteratively encode the input provided by
    *iterator*. *iterator* must yield [`str`](stdtypes.html#str "str") objects.
    This function is a [generator](../glossary.html#term-generator). The *errors* argument (as well as any
    other keyword argument) is passed through to the incremental encoder.

    This function requires that the codec accept text [`str`](stdtypes.html#str "str") objects
    to encode. Therefore it does not support bytes-to-bytes encoders such as
    `base64_codec`.

codecs.iterdecode(*iterator*, *encoding*, *errors='strict'*, *\*\*kwargs*)[¶](#codecs.iterdecode "Link to this definition")
:   Uses an incremental decoder to iteratively decode the input provided by
    *iterator*. *iterator* must yield [`bytes`](stdtypes.html#bytes "bytes") objects.
    This function is a [generator](../glossary.html#term-generator). The *errors* argument (as well as any
    other keyword argument) is passed through to the incremental decoder.

    This function requires that the codec accept [`bytes`](stdtypes.html#bytes "bytes") objects
    to decode. Therefore it does not support text-to-text encoders such as
    `rot_13`, although `rot_13` may be used equivalently with
    [`iterencode()`](#codecs.iterencode "codecs.iterencode").

codecs.readbuffer\_encode(*buffer*, *errors=None*, */*)[¶](#codecs.readbuffer_encode "Link to this definition")
:   Return a [`tuple`](stdtypes.html#tuple "tuple") containing the raw bytes of *buffer*, a
    [buffer-compatible object](../c-api/buffer.html#bufferobjects) or [`str`](stdtypes.html#str "str")
    (encoded to UTF-8 before processing), and their length in bytes.

    The *errors* argument is ignored.

    ```
    >>> codecs.readbuffer_encode(b"Zito")
    (b'Zito', 4)
    ```

The module also provides the following constants which are useful for reading
and writing to platform dependent files:

codecs.BOM[¶](#codecs.BOM "Link to this definition")

codecs.BOM\_BE[¶](#codecs.BOM_BE "Link to this definition")

codecs.BOM\_LE[¶](#codecs.BOM_LE "Link to this definition")

codecs.BOM\_UTF8[¶](#codecs.BOM_UTF8 "Link to this definition")

codecs.BOM\_UTF16[¶](#codecs.BOM_UTF16 "Link to this definition")

codecs.BOM\_UTF16\_BE[¶](#codecs.BOM_UTF16_BE "Link to this definition")

codecs.BOM\_UTF16\_LE[¶](#codecs.BOM_UTF16_LE "Link to this definition")

codecs.BOM\_UTF32[¶](#codecs.BOM_UTF32 "Link to this definition")

codecs.BOM\_UTF32\_BE[¶](#codecs.BOM_UTF32_BE "Link to this definition")

codecs.BOM\_UTF32\_LE[¶](#codecs.BOM_UTF32_LE "Link to this definition")
:   These constants define various byte sequences,
    being Unicode byte order marks (BOMs) for several encodings. They are
    used in UTF-16 and UTF-32 data streams to indicate the byte order used,
    and in UTF-8 as a Unicode signature. [`BOM_UTF16`](#codecs.BOM_UTF16 "codecs.BOM_UTF16") is either
    [`BOM_UTF16_BE`](#codecs.BOM_UTF16_BE "codecs.BOM_UTF16_BE") or [`BOM_UTF16_LE`](#codecs.BOM_UTF16_LE "codecs.BOM_UTF16_LE") depending on the platform’s
    native byte order, [`BOM`](#codecs.BOM "codecs.BOM") is an alias for [`BOM_UTF16`](#codecs.BOM_UTF16 "codecs.BOM_UTF16"),
    [`BOM_LE`](#codecs.BOM_LE "codecs.BOM_LE") for [`BOM_UTF16_LE`](#codecs.BOM_UTF16_LE "codecs.BOM_UTF16_LE") and [`BOM_BE`](#codecs.BOM_BE "codecs.BOM_BE") for
    [`BOM_UTF16_BE`](#codecs.BOM_UTF16_BE "codecs.BOM_UTF16_BE"). The others represent the BOM in UTF-8 and UTF-32
    encodings.

## Codec Base Classes[¶](#codec-base-classes "Link to this heading")

The `codecs` module defines a set of base classes which define the
interfaces for working with codec objects, and can also be used as the basis
for custom codec implementations.

Each codec has to define four interfaces to make it usable as codec in Python:
stateless encoder, stateless decoder, stream reader and stream writer. The
stream reader and writers typically reuse the stateless encoder/decoder to
implement the file protocols. Codec authors also need to define how the
codec will handle encoding and decoding errors.

### Error Handlers[¶](#error-handlers "Link to this heading")

To simplify and standardize error handling, codecs may implement different
error handling schemes by accepting the *errors* string argument:

```
>>> 'German ß, ♬'.encode(encoding='ascii', errors='backslashreplace')
b'German \\xdf, \\u266c'
>>> 'German ß, ♬'.encode(encoding='ascii', errors='xmlcharrefreplace')
b'German &#223;, &#9836;'
```

The following error handlers can be used with all Python
[Standard Encodings](#standard-encodings) codecs:

| Value | Meaning |
| --- | --- |
| `'strict'` | Raise [`UnicodeError`](exceptions.html#UnicodeError "UnicodeError") (or a subclass), this is the default. Implemented in [`strict_errors()`](#codecs.strict_errors "codecs.strict_errors"). |
| `'ignore'` | Ignore the malformed data and continue without further notice. Implemented in [`ignore_errors()`](#codecs.ignore_errors "codecs.ignore_errors"). |
| `'replace'` | Replace with a replacement marker. On encoding, use `?` (ASCII character). On decoding, use `�` (U+FFFD, the official REPLACEMENT CHARACTER). Implemented in [`replace_errors()`](#codecs.replace_errors "codecs.replace_errors"). |
| `'backslashreplace'` | Replace with backslashed escape sequences. On encoding, use hexadecimal form of Unicode code point with formats `\xhh` `\uxxxx` `\Uxxxxxxxx`. On decoding, use hexadecimal form of byte value with format `\xhh`. Implemented in [`backslashreplace_errors()`](#codecs.backslashreplace_errors "codecs.backslashreplace_errors"). |
| `'surrogateescape'` | On decoding, replace byte with individual surrogate code ranging from `U+DC80` to `U+DCFF`. This code will then be turned back into the same byte when the `'surrogateescape'` error handler is used when encoding the data. (See [**PEP 383**](https://peps.python.org/pep-0383/) for more.) |

The following error handlers are only applicable to encoding (within
[text encodings](../glossary.html#term-text-encoding)):

| Value | Meaning |
| --- | --- |
| `'xmlcharrefreplace'` | Replace with XML/HTML numeric character reference, which is a decimal form of Unicode code point with format `&#num;`. Implemented in [`xmlcharrefreplace_errors()`](#codecs.xmlcharrefreplace_errors "codecs.xmlcharrefreplace_errors"). |
| `'namereplace'` | Replace with `\N{...}` escape sequences, what appears in the braces is the Name property from Unicode Character Database. Implemented in [`namereplace_errors()`](#codecs.namereplace_errors "codecs.namereplace_errors"). |

In addition, the following error handler is specific to the given codecs:

| Value | Codecs | Meaning |
| --- | --- | --- |
| `'surrogatepass'` | utf-8, utf-16, utf-32, utf-16-be, utf-16-le, utf-32-be, utf-32-le | Allow encoding and decoding surrogate code point (`U+D800` - `U+DFFF`) as normal code point. Otherwise these codecs treat the presence of surrogate code point in [`str`](stdtypes.html#str "str") as an error. |

Added in version 3.1: The `'surrogateescape'` and `'surrogatepass'` error handlers.

Changed in version 3.4: The `'surrogatepass'` error handler now works with utf-16\* and utf-32\*
codecs.

Added in version 3.5: The `'namereplace'` error handler.

Changed in version 3.5: The `'backslashreplace'` error handler now works with decoding and
translating.

The set of allowed values can be extended by registering a new named error
handler:

codecs.register\_error(*name*, *error\_handler*, */*)[¶](#codecs.register_error "Link to this definition")
:   Register the error handling function *error\_handler* under the name *name*.
    The *error\_handler* argument will be called during encoding and decoding
    in case of an error, when *name* is specified as the errors parameter.

    For encoding, *error\_handler* will be called with a [`UnicodeEncodeError`](exceptions.html#UnicodeEncodeError "UnicodeEncodeError")
    instance, which contains information about the location of the error. The
    error handler must either raise this or a different exception, or return a
    tuple with a replacement for the unencodable part of the input and a position
    where encoding should continue. The replacement may be either [`str`](stdtypes.html#str "str") or
    [`bytes`](stdtypes.html#bytes "bytes"). If the replacement is bytes, the encoder will simply copy
    them into the output buffer. If the replacement is a string, the encoder will
    encode the replacement. Encoding continues on original input at the
    specified position. Negative position values will be treated as being
    relative to the end of the input string. If the resulting position is out of
    bound an [`IndexError`](exceptions.html#IndexError "IndexError") will be raised.

    Decoding and translating works similarly, except [`UnicodeDecodeError`](exceptions.html#UnicodeDecodeError "UnicodeDecodeError") or
    [`UnicodeTranslateError`](exceptions.html#UnicodeTranslateError "UnicodeTranslateError") will be passed to the handler and that the
    replacement from the error handler will be put into the output directly.

Previously registered error handlers (including the standard error handlers)
can be looked up by name:

codecs.lookup\_error(*name*, */*)[¶](#codecs.lookup_error "Link to this definition")
:   Return the error handler previously registered under the name *name*.

    Raises a [`LookupError`](exceptions.html#LookupError "LookupError") in case the handler cannot be found.

The following standard error handlers are also made available as module level
functions:

codecs.strict\_errors(*exception*)[¶](#codecs.strict_errors "Link to this definition")
:   Implements the `'strict'` error handling.

    Each encoding or decoding error raises a [`UnicodeError`](exceptions.html#UnicodeError "UnicodeError").

codecs.ignore\_errors(*exception*)[¶](#codecs.ignore_errors "Link to this definition")
:   Implements the `'ignore'` error handling.

    Malformed data is ignored; encoding or decoding is continued without
    further notice.

codecs.replace\_errors(*exception*)[¶](#codecs.replace_errors "Link to this definition")
:   Implements the `'replace'` error handling.

    Substitutes `?` (ASCII character) for encoding errors or `�` (U+FFFD,
    the official REPLACEMENT CHARACTER) for decoding errors.

codecs.backslashreplace\_errors(*exception*)[¶](#codecs.backslashreplace_errors "Link to this definition")
:   Implements the `'backslashreplace'` error handling.

    Malformed data is replaced by a backslashed escape sequence.
    On encoding, use the hexadecimal form of Unicode code point with formats
    `\xhh` `\uxxxx` `\Uxxxxxxxx`.
    On decoding, use the hexadecimal form of
    byte value with format `\xhh`.

    Changed in version 3.5: Works with decoding and translating.

codecs.xmlcharrefreplace\_errors(*exception*)[¶](#codecs.xmlcharrefreplace_errors "Link to this definition")
:   Implements the `'xmlcharrefreplace'` error handling (for encoding within
    [text encoding](../glossary.html#term-text-encoding) only).

    The unencodable character is replaced by an appropriate XML/HTML numeric
    character reference, which is a decimal form of Unicode code point with
    format `&#num;` .

codecs.namereplace\_errors(*exception*)[¶](#codecs.namereplace_errors "Link to this definition")
:   Implements the `'namereplace'` error handling (for encoding within
    [text encoding](../glossary.html#term-text-encoding) only).

    The unencodable character is replaced by a `\N{...}` escape sequence. The
    set of characters that appear in the braces is the Name property from
    Unicode Character Database. For example, the German lowercase letter `'ß'`
    will be converted to byte sequence `\N{LATIN SMALL LETTER SHARP S}` .

    Added in version 3.5.

### Stateless Encoding and Decoding[¶](#stateless-encoding-and-decoding "Link to this heading")

The base [`Codec`](#codecs.Codec "codecs.Codec") class defines these methods which also define the
function interfaces of the stateless encoder and decoder:

*class* codecs.Codec[¶](#codecs.Codec "Link to this definition")
:   encode(*input*, *errors='strict'*)[¶](#codecs.Codec.encode "Link to this definition")
    :   Encodes the object *input* and returns a tuple (output object, length consumed).
        For instance, [text encoding](../glossary.html#term-text-encoding) converts
        a string object to a bytes object using a particular
        character set encoding (e.g., `cp1252` or `iso-8859-1`).

        The *errors* argument defines the error handling to apply.
        It defaults to `'strict'` handling.

        The method may not store state in the [`Codec`](#codecs.Codec "codecs.Codec") instance. Use
        [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") for codecs which have to keep state in order to make
        encoding efficient.

        The encoder must be able to handle zero length input and return an empty object
        of the output object type in this situation.

    decode(*input*, *errors='strict'*)[¶](#codecs.Codec.decode "Link to this definition")
    :   Decodes the object *input* and returns a tuple (output object, length
        consumed). For instance, for a [text encoding](../glossary.html#term-text-encoding), decoding converts
        a bytes object encoded using a particular
        character set encoding to a string object.

        For text encodings and bytes-to-bytes codecs,
        *input* must be a bytes object or one which provides the read-only
        buffer interface – for example, buffer objects and memory mapped files.

        The *errors* argument defines the error handling to apply.
        It defaults to `'strict'` handling.

        The method may not store state in the [`Codec`](#codecs.Codec "codecs.Codec") instance. Use
        [`StreamReader`](#codecs.StreamReader "codecs.StreamReader") for codecs which have to keep state in order to make
        decoding efficient.

        The decoder must be able to handle zero length input and return an empty object
        of the output object type in this situation.

### Incremental Encoding and Decoding[¶](#incremental-encoding-and-decoding "Link to this heading")

The [`IncrementalEncoder`](#codecs.IncrementalEncoder "codecs.IncrementalEncoder") and [`IncrementalDecoder`](#codecs.IncrementalDecoder "codecs.IncrementalDecoder") classes provide
the basic interface for incremental encoding and decoding. Encoding/decoding the
input isn’t done with one call to the stateless encoder/decoder function, but
with multiple calls to the
[`encode()`](#codecs.IncrementalEncoder.encode "codecs.IncrementalEncoder.encode")/[`decode()`](#codecs.IncrementalDecoder.decode "codecs.IncrementalDecoder.decode") method of
the incremental encoder/decoder. The incremental encoder/decoder keeps track of
the encoding/decoding process during method calls.

The joined output of calls to the
[`encode()`](#codecs.IncrementalEncoder.encode "codecs.IncrementalEncoder.encode")/[`decode()`](#codecs.IncrementalDecoder.decode "codecs.IncrementalDecoder.decode") method is
the same as if all the single inputs were joined into one, and this input was
encoded/decoded with the stateless encoder/decoder.

#### IncrementalEncoder Objects[¶](#incrementalencoder-objects "Link to this heading")

The [`IncrementalEncoder`](#codecs.IncrementalEncoder "codecs.IncrementalEncoder") class is used for encoding an input in multiple
steps. It defines the following methods which every incremental encoder must
define in order to be compatible with the Python codec registry.

*class* codecs.IncrementalEncoder(*errors='strict'*)[¶](#codecs.IncrementalEncoder "Link to this definition")
:   Constructor for an [`IncrementalEncoder`](#codecs.IncrementalEncoder "codecs.IncrementalEncoder") instance.

    All incremental encoders must provide this constructor interface. They are free
    to add additional keyword arguments, but only the ones defined here are used by
    the Python codec registry.

    The [`IncrementalEncoder`](#codecs.IncrementalEncoder "codecs.IncrementalEncoder") may implement different error handling schemes
    by providing the *errors* keyword argument. See [Error Handlers](#error-handlers) for
    possible values.

    The *errors* argument will be assigned to an attribute of the same name.
    Assigning to this attribute makes it possible to switch between different error
    handling strategies during the lifetime of the [`IncrementalEncoder`](#codecs.IncrementalEncoder "codecs.IncrementalEncoder")
    object.

    encode(*object*, *final=False*)[¶](#codecs.IncrementalEncoder.encode "Link to this definition")
    :   Encodes *object* (taking the current state of the encoder into account)
        and returns the resulting encoded object. If this is the last call to
        [`encode()`](#codecs.encode "codecs.encode") *final* must be true (the default is false).

    reset()[¶](#codecs.IncrementalEncoder.reset "Link to this definition")
    :   Reset the encoder to the initial state. The output is discarded: call
        `.encode(object, final=True)`, passing an empty byte or text string
        if necessary, to reset the encoder and to get the output.

    getstate()[¶](#codecs.IncrementalEncoder.getstate "Link to this definition")
    :   Return the current state of the encoder which must be an integer. The
        implementation should make sure that `0` is the most common
        state. (States that are more complicated than integers can be converted
        into an integer by marshaling/pickling the state and encoding the bytes
        of the resulting string into an integer.)

    setstate(*state*)[¶](#codecs.IncrementalEncoder.setstate "Link to this definition")
    :   Set the state of the encoder to *state*. *state* must be an encoder state
        returned by [`getstate()`](#codecs.IncrementalEncoder.getstate "codecs.IncrementalEncoder.getstate").

#### IncrementalDecoder Objects[¶](#incrementaldecoder-objects "Link to this heading")

The [`IncrementalDecoder`](#codecs.IncrementalDecoder "codecs.IncrementalDecoder") class is used for decoding an input in multiple
steps. It defines the following methods which every incremental decoder must
define in order to be compatible with the Python codec registry.

*class* codecs.IncrementalDecoder(*errors='strict'*)[¶](#codecs.IncrementalDecoder "Link to this definition")
:   Constructor for an [`IncrementalDecoder`](#codecs.IncrementalDecoder "codecs.IncrementalDecoder") instance.

    All incremental decoders must provide this constructor interface. They are free
    to add additional keyword arguments, but only the ones defined here are used by
    the Python codec registry.

    The [`IncrementalDecoder`](#codecs.IncrementalDecoder "codecs.IncrementalDecoder") may implement different error handling schemes
    by providing the *errors* keyword argument. See [Error Handlers](#error-handlers) for
    possible values.

    The *errors* argument will be assigned to an attribute of the same name.
    Assigning to this attribute makes it possible to switch between different error
    handling strategies during the lifetime of the [`IncrementalDecoder`](#codecs.IncrementalDecoder "codecs.IncrementalDecoder")
    object.

    decode(*object*, *final=False*)[¶](#codecs.IncrementalDecoder.decode "Link to this definition")
    :   Decodes *object* (taking the current state of the decoder into account)
        and returns the resulting decoded object. If this is the last call to
        [`decode()`](#codecs.decode "codecs.decode") *final* must be true (the default is false). If *final* is
        true the decoder must decode the input completely and must flush all
        buffers. If this isn’t possible (e.g. because of incomplete byte sequences
        at the end of the input) it must initiate error handling just like in the
        stateless case (which might raise an exception).

    reset()[¶](#codecs.IncrementalDecoder.reset "Link to this definition")
    :   Reset the decoder to the initial state.

    getstate()[¶](#codecs.IncrementalDecoder.getstate "Link to this definition")
    :   Return the current state of the decoder. This must be a tuple with two
        items, the first must be the buffer containing the still undecoded
        input. The second must be an integer and can be additional state
        info. (The implementation should make sure that `0` is the most common
        additional state info.) If this additional state info is `0` it must be
        possible to set the decoder to the state which has no input buffered and
        `0` as the additional state info, so that feeding the previously
        buffered input to the decoder returns it to the previous state without
        producing any output. (Additional state info that is more complicated than
        integers can be converted into an integer by marshaling/pickling the info
        and encoding the bytes of the resulting string into an integer.)

    setstate(*state*)[¶](#codecs.IncrementalDecoder.setstate "Link to this definition")
    :   Set the state of the decoder to *state*. *state* must be a decoder state
        returned by [`getstate()`](#codecs.IncrementalDecoder.getstate "codecs.IncrementalDecoder.getstate").

### Stream Encoding and Decoding[¶](#stream-encoding-and-decoding "Link to this heading")

The [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") and [`StreamReader`](#codecs.StreamReader "codecs.StreamReader") classes provide generic
working interfaces which can be used to implement new encoding submodules very
easily. See `encodings.utf_8` for an example of how this is done.

#### StreamWriter Objects[¶](#streamwriter-objects "Link to this heading")

The [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") class is a subclass of [`Codec`](#codecs.Codec "codecs.Codec") and defines the
following methods which every stream writer must define in order to be
compatible with the Python codec registry.

*class* codecs.StreamWriter(*stream*, *errors='strict'*)[¶](#codecs.StreamWriter "Link to this definition")
:   Constructor for a [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") instance.

    All stream writers must provide this constructor interface. They are free to add
    additional keyword arguments, but only the ones defined here are used by the
    Python codec registry.

    The *stream* argument must be a file-like object open for writing
    text or binary data, as appropriate for the specific codec.

    The [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") may implement different error handling schemes by
    providing the *errors* keyword argument. See [Error Handlers](#error-handlers) for
    the standard error handlers the underlying stream codec may support.

    The *errors* argument will be assigned to an attribute of the same name.
    Assigning to this attribute makes it possible to switch between different error
    handling strategies during the lifetime of the [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") object.

    write(*object*)[¶](#codecs.StreamWriter.write "Link to this definition")
    :   Writes the object’s contents encoded to the stream.

    writelines(*list*)[¶](#codecs.StreamWriter.writelines "Link to this definition")
    :   Writes the concatenated iterable of strings to the stream (possibly by reusing
        the [`write()`](#codecs.StreamWriter.write "codecs.StreamWriter.write") method). Infinite or
        very large iterables are not supported. The standard bytes-to-bytes codecs
        do not support this method.

    reset()[¶](#codecs.StreamWriter.reset "Link to this definition")
    :   Resets the codec buffers used for keeping internal state.

        Calling this method should ensure that the data on the output is put into
        a clean state that allows appending of new fresh data without having to
        rescan the whole stream to recover state.

In addition to the above methods, the [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") must also inherit
all other methods and attributes from the underlying stream.

#### StreamReader Objects[¶](#streamreader-objects "Link to this heading")

The [`StreamReader`](#codecs.StreamReader "codecs.StreamReader") class is a subclass of [`Codec`](#codecs.Codec "codecs.Codec") and defines the
following methods which every stream reader must define in order to be
compatible with the Python codec registry.

*class* codecs.StreamReader(*stream*, *errors='strict'*)[¶](#codecs.StreamReader "Link to this definition")
:   Constructor for a [`StreamReader`](#codecs.StreamReader "codecs.StreamReader") instance.

    All stream readers must provide this constructor interface. They are free to add
    additional keyword arguments, but only the ones defined here are used by the
    Python codec registry.

    The *stream* argument must be a file-like object open for reading
    text or binary data, as appropriate for the specific codec.

    The [`StreamReader`](#codecs.StreamReader "codecs.StreamReader") may implement different error handling schemes by
    providing the *errors* keyword argument. See [Error Handlers](#error-handlers) for
    the standard error handlers the underlying stream codec may support.

    The *errors* argument will be assigned to an attribute of the same name.
    Assigning to this attribute makes it possible to switch between different error
    handling strategies during the lifetime of the [`StreamReader`](#codecs.StreamReader "codecs.StreamReader") object.

    The set of allowed values for the *errors* argument can be extended with
    [`register_error()`](#codecs.register_error "codecs.register_error").

    read(*size=-1*, *chars=-1*, *firstline=False*)[¶](#codecs.StreamReader.read "Link to this definition")
    :   Decodes data from the stream and returns the resulting object.

        The *chars* argument indicates the number of decoded
        code points or bytes to return. The [`read()`](#codecs.StreamReader.read "codecs.StreamReader.read") method will
        never return more data than requested, but it might return less,
        if there is not enough available.

        The *size* argument indicates the approximate maximum
        number of encoded bytes or code points to read
        for decoding. The decoder can modify this setting as
        appropriate. The default value -1 indicates to read and decode as much as
        possible. This parameter is intended to
        prevent having to decode huge files in one step.

        The *firstline* flag indicates that
        it would be sufficient to only return the first
        line, if there are decoding errors on later lines.

        The method should use a greedy read strategy meaning that it should read
        as much data as is allowed within the definition of the encoding and the
        given size, e.g. if optional encoding endings or state markers are
        available on the stream, these should be read too.

    readline(*size=None*, *keepends=True*)[¶](#codecs.StreamReader.readline "Link to this definition")
    :   Read one line from the input stream and return the decoded data.

        *size*, if given, is passed as size argument to the stream’s
        [`read()`](#codecs.StreamReader.read "codecs.StreamReader.read") method.

        If *keepends* is false line-endings will be stripped from the lines
        returned.

    readlines(*sizehint=None*, *keepends=True*)[¶](#codecs.StreamReader.readlines "Link to this definition")
    :   Read all lines available on the input stream and return them as a list of
        lines.

        Line-endings are implemented using the codec’s [`decode()`](#codecs.decode "codecs.decode") method and
        are included in the list entries if *keepends* is true.

        *sizehint*, if given, is passed as the *size* argument to the stream’s
        [`read()`](#codecs.StreamReader.read "codecs.StreamReader.read") method.

    reset()[¶](#codecs.StreamReader.reset "Link to this definition")
    :   Resets the codec buffers used for keeping internal state.

        Note that no stream repositioning should take place. This method is
        primarily intended to be able to recover from decoding errors.

In addition to the above methods, the [`StreamReader`](#codecs.StreamReader "codecs.StreamReader") must also inherit
all other methods and attributes from the underlying stream.

#### StreamReaderWriter Objects[¶](#streamreaderwriter-objects "Link to this heading")

The [`StreamReaderWriter`](#codecs.StreamReaderWriter "codecs.StreamReaderWriter") is a convenience class that allows wrapping
streams which work in both read and write modes.

The design is such that one can use the factory functions returned by the
[`lookup()`](#codecs.lookup "codecs.lookup") function to construct the instance.

*class* codecs.StreamReaderWriter(*stream*, *Reader*, *Writer*, *errors='strict'*)[¶](#codecs.StreamReaderWriter "Link to this definition")
:   Creates a [`StreamReaderWriter`](#codecs.StreamReaderWriter "codecs.StreamReaderWriter") instance. *stream* must be a file-like
    object. *Reader* and *Writer* must be factory functions or classes providing the
    [`StreamReader`](#codecs.StreamReader "codecs.StreamReader") and [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") interface resp. Error handling
    is done in the same way as defined for the stream readers and writers.

[`StreamReaderWriter`](#codecs.StreamReaderWriter "codecs.StreamReaderWriter") instances define the combined interfaces of
[`StreamReader`](#codecs.StreamReader "codecs.StreamReader") and [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") classes. They inherit all other
methods and attributes from the underlying stream.

#### StreamRecoder Objects[¶](#streamrecoder-objects "Link to this heading")

The [`StreamRecoder`](#codecs.StreamRecoder "codecs.StreamRecoder") translates data from one encoding to another,
which is sometimes useful when dealing with different encoding environments.

The design is such that one can use the factory functions returned by the
[`lookup()`](#codecs.lookup "codecs.lookup") function to construct the instance.

*class* codecs.StreamRecoder(*stream*, *encode*, *decode*, *Reader*, *Writer*, *errors='strict'*)[¶](#codecs.StreamRecoder "Link to this definition")
:   Creates a [`StreamRecoder`](#codecs.StreamRecoder "codecs.StreamRecoder") instance which implements a two-way conversion:
    *encode* and *decode* work on the frontend — the data visible to
    code calling [`read()`](#codecs.StreamReader.read "codecs.StreamReader.read") and [`write()`](#codecs.StreamWriter.write "codecs.StreamWriter.write"),
    while *Reader* and *Writer*
    work on the backend — the data in *stream*.

    You can use these objects to do transparent transcodings, e.g., from Latin-1
    to UTF-8 and back.

    The *stream* argument must be a file-like object.

    The *encode* and *decode* arguments must
    adhere to the [`Codec`](#codecs.Codec "codecs.Codec") interface. *Reader* and
    *Writer* must be factory functions or classes providing objects of the
    [`StreamReader`](#codecs.StreamReader "codecs.StreamReader") and [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") interface respectively.

    Error handling is done in the same way as defined for the stream readers and
    writers.

[`StreamRecoder`](#codecs.StreamRecoder "codecs.StreamRecoder") instances define the combined interfaces of
[`StreamReader`](#codecs.StreamReader "codecs.StreamReader") and [`StreamWriter`](#codecs.StreamWriter "codecs.StreamWriter") classes. They inherit all other
methods and attributes from the underlying stream.

## Encodings and Unicode[¶](#encodings-and-unicode "Link to this heading")

Strings are stored internally as sequences of code points in
range `U+0000`–`U+10FFFF`. (See [**PEP 393**](https://peps.python.org/pep-0393/) for
more details about the implementation.)
Once a string object is used outside of CPU and memory, endianness
and how these arrays are stored as bytes become an issue. As with other
codecs, serialising a string into a sequence of bytes is known as *encoding*,
and recreating the string from the sequence of bytes is known as *decoding*.
There are a variety of different text serialisation codecs, which are
collectivity referred to as [text encodings](../glossary.html#term-text-encoding).

The simplest text encoding (called `'latin-1'` or `'iso-8859-1'`) maps
the code points 0–255 to the bytes `0x0`–`0xff`, which means that a string
object that contains code points above `U+00FF` can’t be encoded with this
codec. Doing so will raise a [`UnicodeEncodeError`](exceptions.html#UnicodeEncodeError "UnicodeEncodeError") that looks
like the following (although the details of the error message may differ):
`UnicodeEncodeError: 'latin-1' codec can't encode character '\u1234' in
position 3: ordinal not in range(256)`.

There’s another group of encodings (the so called charmap encodings) that choose
a different subset of all Unicode code points and how these code points are
mapped to the bytes `0x0`–`0xff`. To see how this is done simply open
e.g. `encodings/cp1252.py` (which is an encoding that is used primarily on
Windows). There’s a string constant with 256 characters that shows you which
character is mapped to which byte value.

All of these encodings can only encode 256 of the 1114112 code points
defined in Unicode. A simple and straightforward way that can store each Unicode
code point, is to store each code point as four consecutive bytes. There are two
possibilities: store the bytes in big endian or in little endian order. These
two encodings are called `UTF-32-BE` and `UTF-32-LE` respectively. Their
disadvantage is that if, for example, you use `UTF-32-BE` on a little endian
machine you will always have to swap bytes on encoding and decoding.
Python’s `UTF-16` and `UTF-32` codecs avoid this problem by using the
platform’s native byte order when no BOM is present.
Python follows prevailing platform
practice, so native-endian data round-trips without redundant byte swapping,
even though the Unicode Standard defaults to big-endian when the byte order is
unspecified. When these bytes are read by a CPU with a different endianness,
the bytes have to be swapped. To be able to detect the endianness of a
`UTF-16` or `UTF-32` byte sequence, a BOM (“Byte Order Mark”) is used.
This is the Unicode character `U+FEFF`. This character can be prepended to every
`UTF-16` or `UTF-32` byte sequence. The byte swapped version of this character
(`0xFFFE`) is an illegal character that may not appear in a Unicode text.
When the first character of a `UTF-16` or `UTF-32` byte sequence is
`U+FFFE`, the bytes have to be swapped on decoding.

Unfortunately the character `U+FEFF` had a second purpose as
a `ZERO WIDTH NO-BREAK SPACE`: a character that has no width and doesn’t allow
a word to be split. It can e.g. be used to give hints to a ligature algorithm.
With Unicode 4.0 using `U+FEFF` as a `ZERO WIDTH NO-BREAK SPACE` has been
deprecated (with `U+2060` (`WORD JOINER`) assuming this role). Nevertheless
Unicode software still must be able to handle `U+FEFF` in both roles: as a BOM
it’s a device to determine the storage layout of the encoded bytes, and vanishes
once the byte sequence has been decoded into a string; as a `ZERO WIDTH
NO-BREAK SPACE` it’s a normal character that will be decoded like any other.

There’s another encoding that is able to encode the full range of Unicode
characters: UTF-8. UTF-8 is an 8-bit encoding, which means there are no issues
with byte order in UTF-8. Each byte in a UTF-8 byte sequence consists of two
parts: marker bits (the most significant bits) and payload bits. The marker bits
are a sequence of zero to four `1` bits followed by a `0` bit. Unicode characters are
encoded like this (with x being payload bits, which when concatenated give the
Unicode character):

| Range | Encoding |
| --- | --- |
| `U-00000000` … `U-0000007F` | 0xxxxxxx |
| `U-00000080` … `U-000007FF` | 110xxxxx 10xxxxxx |
| `U-00000800` … `U-0000FFFF` | 1110xxxx 10xxxxxx 10xxxxxx |
| `U-00010000` … `U-0010FFFF` | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

The least significant bit of the Unicode character is the rightmost x bit.

As UTF-8 is an 8-bit encoding no BOM is required and any `U+FEFF` character in
the decoded string (even if it’s the first character) is treated as a `ZERO
WIDTH NO-BREAK SPACE`.

Without external information it’s impossible to reliably determine which
encoding was used for encoding a string. Each charmap encoding can
decode any random byte sequence. However that’s not possible with UTF-8, as
UTF-8 byte sequences have a structure that doesn’t allow arbitrary byte
sequences. To increase the reliability with which a UTF-8 encoding can be
detected, Microsoft invented a variant of UTF-8 (that Python calls
`"utf-8-sig"`) for its Notepad program: Before any of the Unicode characters
is written to the file, a UTF-8 encoded BOM (which looks like this as a byte
sequence: `0xef`, `0xbb`, `0xbf`) is written. As it’s rather improbable
that any charmap encoded file starts with these byte values (which would e.g.
map to

> LATIN SMALL LETTER I WITH DIAERESIS
>
> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
>
> INVERTED QUESTION MARK

in iso-8859-1), this increases the probability that a `utf-8-sig` encoding can be
correctly guessed from the byte sequence. So here the BOM is not used to be able
to determine the byte order used for generating the byte sequence, but as a
signature that helps in guessing the encoding. On encoding the utf-8-sig codec
will write `0xef`, `0xbb`, `0xbf` as the first three bytes to the file. On
decoding `utf-8-sig` will skip those three bytes if they appear as the first
three bytes in the file. In UTF-8, the use of the BOM is discouraged and
should generally be avoided.

## Standard Encodings[¶](#standard-encodings "Link to this heading")

Python comes with a number of codecs built-in, either implemented as C functions
or with dictionaries as mapping tables. The following table lists the codecs by
name, together with a few common aliases, and the languages for which the
encoding is likely used. Neither the list of aliases nor the list of languages
is meant to be exhaustive. Notice that spelling alternatives that only differ in
case or use a hyphen instead of an underscore are also valid aliases
because they are equivalent when normalized by
[`normalize_encoding()`](#encodings.normalize_encoding "encodings.normalize_encoding"). For example, `'utf-8'` is a valid
alias for the `'utf_8'` codec.

Note

The below table lists the most common aliases, for a complete list
refer to the source [aliases.py](https://github.com/python/cpython/tree/3.14/Lib/encodings/aliases.py) file.

On Windows, `cpXXX` codecs are available for all code pages.
But only codecs listed in the following table are guarantead to exist on
other platforms.

**CPython implementation detail:** Some common encodings can bypass the codecs lookup machinery to
improve performance. These optimization opportunities are only
recognized by CPython for a limited set of (case insensitive)
aliases: utf-8, utf8, latin-1, latin1, iso-8859-1, iso8859-1, mbcs
(Windows only), ascii, us-ascii, utf-16, utf16, utf-32, utf32, and
the same using underscores instead of dashes. Using alternative
aliases for these encodings may result in slower execution.

Changed in version 3.6: Optimization opportunity recognized for us-ascii.

Many of the character sets support the same languages. They vary in individual
characters (e.g. whether the EURO SIGN is supported or not), and in the
assignment of characters to code positions. For the European languages in
particular, the following variants typically exist:

* an ISO 8859 codeset
* a Microsoft Windows code page, which is typically derived from an 8859 codeset,
  but replaces control characters with additional graphic characters
* an IBM EBCDIC code page
* an IBM PC code page, which is ASCII compatible

| Codec | Aliases | Languages |
| --- | --- | --- |
| ascii | 646, us-ascii | English |
| big5 | big5-tw, csbig5 | Traditional Chinese |
| big5hkscs | big5-hkscs, hkscs | Traditional Chinese |
| cp037 | IBM037, IBM039 | English |
| cp273 | 273, IBM273, csIBM273 | German  Added in version 3.4. |
| cp424 | EBCDIC-CP-HE, IBM424 | Hebrew |
| cp437 | 437, IBM437 | English |
| cp500 | EBCDIC-CP-BE, EBCDIC-CP-CH, IBM500 | Western Europe |
| cp720 |  | Arabic |
| cp737 |  | Greek |
| cp775 | IBM775 | Baltic languages |
| cp850 | 850, IBM850 | Western Europe |
| cp852 | 852, IBM852 | Central and Eastern Europe |
| cp855 | 855, IBM855 | Belarusian, Bulgarian, Macedonian, Russian, Serbian |
| cp856 |  | Hebrew |
| cp857 | 857, IBM857 | Turkish |
| cp858 | 858, IBM858 | Western Europe |
| cp860 | 860, IBM860 | Portuguese |
| cp861 | 861, CP-IS, IBM861 | Icelandic |
| cp862 | 862, IBM862 | Hebrew |
| cp863 | 863, IBM863 | Canadian |
| cp864 | IBM864 | Arabic |
| cp865 | 865, IBM865 | Danish, Norwegian |
| cp866 | 866, IBM866 | Russian |
| cp869 | 869, CP-GR, IBM869 | Greek |
| cp874 |  | Thai |
| cp875 |  | Greek |
| cp932 | 932, ms932, mskanji, ms-kanji, windows-31j | Japanese |
| cp949 | 949, ms949, uhc | Korean |
| cp950 | 950, ms950 | Traditional Chinese |
| cp1006 |  | Urdu |
| cp1026 | ibm1026 | Turkish |
| cp1125 | 1125, ibm1125, cp866u, ruscii | Ukrainian  Added in version 3.4. |
| cp1140 | ibm1140 | Western Europe |
| cp1250 | windows-1250 | Central and Eastern Europe |
| cp1251 | windows-1251 | Belarusian, Bulgarian, Macedonian, Russian, Serbian |
| cp1252 | windows-1252 | Western Europe |
| cp1253 | windows-1253 | Greek |
| cp1254 | windows-1254 | Turkish |
| cp1255 | windows-1255 | Hebrew |
| cp1256 | windows-1256 | Arabic |
| cp1257 | windows-1257 | Baltic languages |
| cp1258 | windows-1258 | Vietnamese |
| euc\_jp | eucjp, ujis, u-jis | Japanese |
| euc\_jis\_2004 | jisx0213, eucjis2004 | Japanese |
| euc\_jisx0213 | eucjisx0213 | Japanese |
| euc\_kr | euckr, korean, ksc5601, ks\_c-5601, ks\_c-5601-1987, ksx1001, ks\_x-1001 | Korean |
| gb2312 | chinese, csiso58gb231280, euc-cn, euccn, eucgb2312-cn, gb2312-1980, gb2312-80, iso-ir-58 | Simplified Chinese |
| gbk | 936, cp936, ms936 | Unified Chinese |
| gb18030 | gb18030-2000 | Unified Chinese |
| hz | hzgb, hz-gb, hz-gb-2312 | Simplified Chinese |
| iso2022\_jp | csiso2022jp, iso2022jp, iso-2022-jp | Japanese |
| iso2022\_jp\_1 | iso2022jp-1, iso-2022-jp-1 | Japanese |
| iso2022\_jp\_2 | iso2022jp-2, iso-2022-jp-2 | Japanese, Korean, Simplified Chinese, Western Europe, Greek |
| iso2022\_jp\_2004 | iso2022jp-2004, iso-2022-jp-2004 | Japanese |
| iso2022\_jp\_3 | iso2022jp-3, iso-2022-jp-3 | Japanese |
| iso2022\_jp\_ext | iso2022jp-ext, iso-2022-jp-ext | Japanese |
| iso2022\_kr | csiso2022kr, iso2022kr, iso-2022-kr | Korean |
| latin\_1 | iso-8859-1, iso8859-1, 8859, cp819, latin, latin1, L1 | Western Europe |
| iso8859\_2 | iso-8859-2, latin2, L2 | Central and Eastern Europe |
| iso8859\_3 | iso-8859-3, latin3, L3 | Esperanto, Maltese |
| iso8859\_4 | iso-8859-4, latin4, L4 | Northern Europe |
| iso8859\_5 | iso-8859-5, cyrillic | Belarusian, Bulgarian, Macedonian, Russian, Serbian |
| iso8859\_6 | iso-8859-6, arabic | Arabic |
| iso8859\_7 | iso-8859-7, greek, greek8 | Greek |
| iso8859\_8 | iso-8859-8, hebrew | Hebrew |
| iso8859\_9 | iso-8859-9, latin5, L5 | Turkish |
| iso8859\_10 | iso-8859-10, latin6, L6 | Nordic languages |
| iso8859\_11 | iso-8859-11, thai | Thai languages |
| iso8859\_13 | iso-8859-13, latin7, L7 | Baltic languages |
| iso8859\_14 | iso-8859-14, latin8, L8 | Celtic languages |
| iso8859\_15 | iso-8859-15, latin9, L9 | Western Europe |
| iso8859\_16 | iso-8859-16, latin10, L10 | South-Eastern Europe |
| johab | cp1361, ms1361 | Korean |
| koi8\_r |  | Russian |
| koi8\_t |  | Tajik  Added in version 3.5. |
| koi8\_u |  | Ukrainian |
| kz1048 | kz\_1048, strk1048\_2002, rk1048 | Kazakh  Added in version 3.5. |
| mac\_cyrillic | maccyrillic | Belarusian, Bulgarian, Macedonian, Russian, Serbian |
| mac\_greek | macgreek | Greek |
| mac\_iceland | maciceland | Icelandic |
| mac\_latin2 | maclatin2, maccentraleurope, mac\_centeuro | Central and Eastern Europe |
| mac\_roman | macroman, macintosh | Western Europe |
| mac\_turkish | macturkish | Turkish |
| ptcp154 | csptcp154, pt154, cp154, cyrillic-asian | Kazakh |
| shift\_jis | csshiftjis, shiftjis, sjis, s\_jis | Japanese |
| shift\_jis\_2004 | shiftjis2004, sjis\_2004, sjis2004 | Japanese |
| shift\_jisx0213 | shiftjisx0213, sjisx0213, s\_jisx0213 | Japanese |
| utf\_32 | U32, utf32 | all languages |
| utf\_32\_be | UTF-32BE | all languages |
| utf\_32\_le | UTF-32LE | all languages |
| utf\_16 | U16, utf16 | all languages |
| utf\_16\_be | UTF-16BE | all languages |
| utf\_16\_le | UTF-16LE | all languages |
| utf\_7 | U7, unicode-1-1-utf-7 | all languages |
| utf\_8 | U8, UTF, utf8, cp65001 | all languages |
| utf\_8\_sig |  | all languages |

Changed in version 3.4: The utf-16\* and utf-32\* encoders no longer allow surrogate code points
(`U+D800`–`U+DFFF`) to be encoded.
The utf-32\* decoders no longer decode
byte sequences that correspond to surrogate code points.

Changed in version 3.8: `cp65001` is now an alias to `utf_8`.

Changed in version 3.14: On Windows, `cpXXX` codecs are now available for all code pages.

## Python Specific Encodings[¶](#python-specific-encodings "Link to this heading")

A number of predefined codecs are specific to Python, so their codec names have
no meaning outside Python. These are listed in the tables below based on the
expected input and output types (note that while text encodings are the most
common use case for codecs, the underlying codec infrastructure supports
arbitrary data transforms rather than just text encodings). For asymmetric
codecs, the stated meaning describes the encoding direction.

### Text Encodings[¶](#text-encodings "Link to this heading")

The following codecs provide [`str`](stdtypes.html#str "str") to [`bytes`](stdtypes.html#bytes "bytes") encoding and
[bytes-like object](../glossary.html#term-bytes-like-object) to [`str`](stdtypes.html#str "str") decoding, similar to the Unicode text
encodings.

| Codec | Aliases | Meaning |
| --- | --- | --- |
| idna |  | Implement [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html), see also [`encodings.idna`](#module-encodings.idna "encodings.idna: Internationalized Domain Names implementation"). Only `errors='strict'` is supported. |
| mbcs | ansi, dbcs | Windows only: Encode the operand according to the ANSI codepage (CP\_ACP). |
| oem |  | Windows only: Encode the operand according to the OEM codepage (CP\_OEMCP).  Added in version 3.6. |
| palmos |  | Encoding of PalmOS 3.5. |
| punycode |  | Implement [**RFC 3492**](https://datatracker.ietf.org/doc/html/rfc3492.html). Stateful codecs are not supported. |
| raw\_unicode\_escape |  | Latin-1 encoding with `\uXXXX` and `\UXXXXXXXX` for other code points. Existing backslashes are not escaped in any way. It is used in the Python pickle protocol. |
| undefined |  | This Codec should only be used for testing purposes.  Raise an exception for all conversions, even empty strings. The error handler is ignored. |
| unicode\_escape |  | Encoding suitable as the contents of a Unicode literal in ASCII-encoded Python source code, except that quotes are not escaped. Decode from Latin-1 source code. Beware that Python source code actually uses UTF-8 by default. |

Changed in version 3.8: “unicode\_internal” codec is removed.

### Binary Transforms[¶](#binary-transforms "Link to this heading")

The following codecs provide binary transforms: [bytes-like object](../glossary.html#term-bytes-like-object)
to [`bytes`](stdtypes.html#bytes "bytes") mappings. They are not supported by [`bytes.decode()`](stdtypes.html#bytes.decode "bytes.decode")
(which only produces [`str`](stdtypes.html#str "str") output).

| Codec | Aliases | Meaning | Encoder / decoder |
| --- | --- | --- | --- |
| base64\_codec [[1]](#b64) | base64, base\_64 | Convert the operand to multiline MIME base64 (the result always includes a trailing `'\n'`).  Changed in version 3.4: accepts any [bytes-like object](../glossary.html#term-bytes-like-object) as input for encoding and decoding | [`base64.encodebytes()`](base64.html#base64.encodebytes "base64.encodebytes") / [`base64.decodebytes()`](base64.html#base64.decodebytes "base64.decodebytes") |
| bz2\_codec | bz2 | Compress the operand using bz2. | [`bz2.compress()`](bz2.html#bz2.compress "bz2.compress") / [`bz2.decompress()`](bz2.html#bz2.decompress "bz2.decompress") |
| hex\_codec | hex | Convert the operand to hexadecimal representation, with two digits per byte. | [`binascii.b2a_hex()`](binascii.html#binascii.b2a_hex "binascii.b2a_hex") / [`binascii.a2b_hex()`](binascii.html#binascii.a2b_hex "binascii.a2b_hex") |
| quopri\_codec | quopri, quotedprintable, quoted\_printable | Convert the operand to MIME quoted printable. | [`quopri.encode()`](quopri.html#quopri.encode "quopri.encode") with `quotetabs=True` / [`quopri.decode()`](quopri.html#quopri.decode "quopri.decode") |
| uu\_codec | uu | Convert the operand using uuencode. |  |
| zlib\_codec | zip, zlib | Compress the operand using gzip. | [`zlib.compress()`](zlib.html#zlib.compress "zlib.compress") / [`zlib.decompress()`](zlib.html#zlib.decompress "zlib.decompress") |

[[1](#id5)]

In addition to [bytes-like objects](../glossary.html#term-bytes-like-object),
`'base64_codec'` also accepts ASCII-only instances of [`str`](stdtypes.html#str "str") for
decoding

Added in version 3.2: Restoration of the binary transforms.

Changed in version 3.4: Restoration of the aliases for the binary transforms.

### Standalone Codec Functions[¶](#standalone-codec-functions "Link to this heading")

The following functions provide encoding and decoding functionality similar to codecs,
but are not available as named codecs through [`codecs.encode()`](#codecs.encode "codecs.encode") or [`codecs.decode()`](#codecs.decode "codecs.decode").
They are used internally (for example, by [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")) and behave similarly to the
`string_escape` codec that was removed in Python 3.

codecs.escape\_encode(*input*, *errors=None*)[¶](#codecs.codecs.escape_encode "Link to this definition")
:   Encode *input* using escape sequences. Similar to how [`repr()`](functions.html#repr "repr") on bytes
    produces escaped byte values.

    *input* must be a [`bytes`](stdtypes.html#bytes "bytes") object.

    Returns a tuple `(output, length)` where *output* is a [`bytes`](stdtypes.html#bytes "bytes")
    object and *length* is the number of bytes consumed.

codecs.escape\_decode(*input*, *errors=None*)[¶](#codecs.codecs.escape_decode "Link to this definition")
:   Decode *input* from escape sequences back to the original bytes.

    *input* must be a [bytes-like object](../glossary.html#term-bytes-like-object).

    Returns a tuple `(output, length)` where *output* is a [`bytes`](stdtypes.html#bytes "bytes")
    object and *length* is the number of bytes consumed.

### Text Transforms[¶](#text-transforms "Link to this heading")

The following codec provides a text transform: a [`str`](stdtypes.html#str "str") to [`str`](stdtypes.html#str "str")
mapping. It is not supported by [`str.encode()`](stdtypes.html#str.encode "str.encode") (which only produces
[`bytes`](stdtypes.html#bytes "bytes") output).

| Codec | Aliases | Meaning |
| --- | --- | --- |
| rot\_13 | rot13 | Return the Caesar-cypher encryption of the operand. |

Added in version 3.2: Restoration of the `rot_13` text transform.

Changed in version 3.4: Restoration of the `rot13` alias.

## `encodings` — Encodings package[¶](#module-encodings "Link to this heading")

This module implements the following functions:

encodings.normalize\_encoding(*encoding*)[¶](#encodings.normalize_encoding "Link to this definition")
:   Normalize encoding name *encoding*.

    Normalization works as follows: all non-alphanumeric characters except the
    dot used for Python package names are collapsed and replaced with a single
    underscore, leading and trailing underscores are removed.
    For example, `'  -;#'` becomes `'_'`.

    Note that *encoding* should be ASCII only.

Note

The following functions should not be used directly, except for testing
purposes; [`codecs.lookup()`](#codecs.lookup "codecs.lookup") should be used instead.

encodings.search\_function(*encoding*)[¶](#encodings.search_function "Link to this definition")
:   Search for the codec module corresponding to the given encoding name
    *encoding*.

    This function first normalizes the *encoding* using
    [`normalize_encoding()`](#encodings.normalize_encoding "encodings.normalize_encoding"), then looks for a corresponding alias.
    It attempts to import a codec module from the encodings package using either
    the alias or the normalized name. If the module is found and defines a valid
    `getregentry()` function that returns a [`codecs.CodecInfo`](#codecs.CodecInfo "codecs.CodecInfo") object,
    the codec is cached and returned.

    If the codec module defines a `getaliases()` function any returned aliases
    are registered for future use.

encodings.win32\_code\_page\_search\_function(*encoding*)[¶](#encodings.win32_code_page_search_function "Link to this definition")
:   Search for a Windows code page encoding *encoding* of the form `cpXXXX`.

    If the code page is valid and supported, return a [`codecs.CodecInfo`](#codecs.CodecInfo "codecs.CodecInfo")
    object for it.

    [Availability](intro.html#availability): Windows.

    Added in version 3.14.

This module implements the following exception:

*exception* encodings.CodecRegistryError[¶](#encodings.CodecRegistryError "Link to this definition")
:   Raised when a codec is invalid or incompatible.

## `encodings.idna` — Internationalized Domain Names in Applications[¶](#module-encodings.idna "Link to this heading")

This module implements [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html) (Internationalized Domain Names in
Applications) and [**RFC 3492**](https://datatracker.ietf.org/doc/html/rfc3492.html) (Nameprep: A Stringprep Profile for
Internationalized Domain Names (IDN)). It builds upon the `punycode` encoding
and [`stringprep`](stringprep.html#module-stringprep "stringprep: String preparation, as per RFC 3453").

If you need the IDNA 2008 standard from [**RFC 5891**](https://datatracker.ietf.org/doc/html/rfc5891.html) and [**RFC 5895**](https://datatracker.ietf.org/doc/html/rfc5895.html), use the
third-party [idna](https://pypi.org/project/idna/) module.

These RFCs together define a protocol to support non-ASCII characters in domain
names. A domain name containing non-ASCII characters (such as
`www.Alliancefrançaise.nu`) is converted into an ASCII-compatible encoding
(ACE, such as `www.xn--alliancefranaise-npb.nu`). The ACE form of the domain
name is then used in all places where arbitrary characters are not allowed by
the protocol, such as DNS queries, HTTP *Host* fields, and so
on. This conversion is carried out in the application; if possible invisible to
the user: The application should transparently convert Unicode domain labels to
IDNA on the wire, and convert back ACE labels to Unicode before presenting them
to the user.

Python supports this conversion in several ways: the `idna` codec performs
conversion between Unicode and ACE, separating an input string into labels
based on the separator characters defined in [**section 3.1 of RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html#section-3.1)
and converting each label to ACE as required, and conversely separating an input
byte string into labels based on the `.` separator and converting any ACE
labels found into unicode. Furthermore, the [`socket`](socket.html#module-socket "socket: Low-level networking interface.") module
transparently converts Unicode host names to ACE, so that applications need not
be concerned about converting host names themselves when they pass them to the
socket module. On top of that, modules that have host names as function
parameters, such as [`http.client`](http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).") and [`ftplib`](ftplib.html#module-ftplib "ftplib: FTP protocol client (requires sockets)."), accept Unicode host
names ([`http.client`](http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).") then also transparently sends an IDNA hostname in the
*Host* field if it sends that field at all).

When receiving host names from the wire (such as in reverse name lookup), no
automatic conversion to Unicode is performed: applications wishing to present
such host names to the user should decode them to Unicode.

The module `encodings.idna` also implements the nameprep procedure, which
performs certain normalizations on host names, to achieve case-insensitivity of
international domain names, and to unify similar characters. The nameprep
functions can be used directly if desired.

encodings.idna.nameprep(*label*)[¶](#encodings.idna.nameprep "Link to this definition")
:   Return the nameprepped version of *label*. The implementation currently assumes
    query strings, so `AllowUnassigned` is true.

encodings.idna.ToASCII(*label*)[¶](#encodings.idna.ToASCII "Link to this definition")
:   Convert a label to ASCII, as specified in [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html). `UseSTD3ASCIIRules` is
    assumed to be false.

encodings.idna.ToUnicode(*label*)[¶](#encodings.idna.ToUnicode "Link to this definition")
:   Convert a label to Unicode, as specified in [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html).

## `encodings.mbcs` — Windows ANSI codepage[¶](#module-encodings.mbcs "Link to this heading")

This module implements the ANSI codepage (CP\_ACP).

[Availability](intro.html#availability): Windows.

Changed in version 3.2: Before 3.2, the *errors* argument was ignored; `'replace'` was always used
to encode, and `'ignore'` to decode.

Changed in version 3.3: Support any error handler.

## `encodings.utf_8_sig` — UTF-8 codec with BOM signature[¶](#module-encodings.utf_8_sig "Link to this heading")

This module implements a variant of the UTF-8 codec. On encoding, a UTF-8 encoded
BOM will be prepended to the UTF-8 encoded bytes. For the stateful encoder this
is only done once (on the first write to the byte stream). On decoding, an
optional UTF-8 encoded BOM at the start of the data will be skipped.

### [Table of Contents](../contents.html)

* [`codecs` — Codec registry and base classes](#)
  + [Codec Base Classes](#codec-base-classes)
    - [Error Handlers](#error-handlers)
    - [Stateless Encoding and Decoding](#stateless-encoding-and-decoding)
    - [Incremental Encoding and Decoding](#incremental-encoding-and-decoding)
      * [IncrementalEncoder Objects](#incrementalencoder-objects)
      * [IncrementalDecoder Objects](#incrementaldecoder-objects)
    - [Stream Encoding and Decoding](#stream-encoding-and-decoding)
      * [StreamWriter Objects](#streamwriter-objects)
      * [StreamReader Objects](#streamreader-objects)
      * [StreamReaderWriter Objects](#streamreaderwriter-objects)
      * [StreamRecoder Objects](#streamrecoder-objects)
  + [Encodings and Unicode](#encodings-and-unicode)
  + [Standard Encodings](#standard-encodings)
  + [Python Specific Encodings](#python-specific-encodings)
    - [Text Encodings](#text-encodings)
    - [Binary Transforms](#binary-transforms)
    - [Standalone Codec Functions](#standalone-codec-functions)
    - [Text Transforms](#text-transforms)
  + [`encodings` — Encodings package](#module-encodings)
  + [`encodings.idna` — Internationalized Domain Names in Applications](#module-encodings.idna)
  + [`encodings.mbcs` — Windows ANSI codepage](#module-encodings.mbcs)
  + [`encodings.utf_8_sig` — UTF-8 codec with BOM signature](#module-encodings.utf_8_sig)

#### Previous topic

[`struct` — Interpret bytes as packed binary data](struct.html "previous chapter")

#### Next topic

[Data Types](datatypes.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/codecs.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](datatypes.html "Data Types") |
* [previous](struct.html "struct — Interpret bytes as packed binary data") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Binary Data Services](binary.html) »
* `codecs` — Codec registry and base classes
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