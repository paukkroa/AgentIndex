### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](binascii.html "binascii — Convert between binary and ASCII") |
* [previous](mimetypes.html "mimetypes — Map filenames to MIME types") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `base64` — Base16, Base32, Base64, Base85 Data Encodings
* |
* Theme
  Auto
  Light
  Dark
   |

# `base64` — Base16, Base32, Base64, Base85 Data Encodings[¶](#module-base64 "Link to this heading")

**Source code:** [Lib/base64.py](https://github.com/python/cpython/tree/3.14/Lib/base64.py)

---

This module provides functions for encoding binary data to printable
ASCII characters and decoding such encodings back to binary data.
This includes the [encodings specified in](#base64-rfc-4648)
[**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html) (Base64, Base32 and Base16)
and the non-standard [Base85 encodings](#base64-base-85).

There are two interfaces provided by this module. The modern interface
supports encoding [bytes-like objects](../glossary.html#term-bytes-like-object) to ASCII
[`bytes`](stdtypes.html#bytes "bytes"), and decoding [bytes-like objects](../glossary.html#term-bytes-like-object) or
strings containing ASCII to [`bytes`](stdtypes.html#bytes "bytes"). Both base-64 alphabets
defined in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html) (normal, and URL- and filesystem-safe) are supported.

The [legacy interface](#base64-legacy) does not support decoding from strings, but it does
provide functions for encoding and decoding to and from [file objects](../glossary.html#term-file-object). It only supports the Base64 standard alphabet, and it adds
newlines every 76 characters as per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html). Note that if you are looking
for [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) support you probably want to be looking at the [`email`](email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
package instead.

Changed in version 3.3: ASCII-only Unicode strings are now accepted by the decoding functions of
the modern interface.

Changed in version 3.4: Any [bytes-like objects](../glossary.html#term-bytes-like-object) are now accepted by all
encoding and decoding functions in this module. Ascii85/Base85 support added.

## RFC 4648 Encodings[¶](#rfc-4648-encodings "Link to this heading")

The [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html) encodings are suitable for encoding binary data so that it can be
safely sent by email, used as parts of URLs, or included as part of an HTTP
POST request.

base64.b64encode(*s*, *altchars=None*)[¶](#base64.b64encode "Link to this definition")
:   Encode the [bytes-like object](../glossary.html#term-bytes-like-object) *s* using Base64 and return the encoded
    [`bytes`](stdtypes.html#bytes "bytes").

    Optional *altchars* must be a [bytes-like object](../glossary.html#term-bytes-like-object) of length 2 which
    specifies an alternative alphabet for the `+` and `/` characters.
    This allows an application to e.g. generate URL or filesystem safe Base64
    strings. The default is `None`, for which the standard Base64 alphabet is used.

    May assert or raise a [`ValueError`](exceptions.html#ValueError "ValueError") if the length of *altchars* is not 2. Raises a
    [`TypeError`](exceptions.html#TypeError "TypeError") if *altchars* is not a [bytes-like object](../glossary.html#term-bytes-like-object).

base64.b64decode(*s*, *altchars=None*, *validate=False*)[¶](#base64.b64decode "Link to this definition")
:   Decode the Base64 encoded [bytes-like object](../glossary.html#term-bytes-like-object) or ASCII string
    *s* and return the decoded [`bytes`](stdtypes.html#bytes "bytes").

    Optional *altchars* must be a [bytes-like object](../glossary.html#term-bytes-like-object) or ASCII string
    of length 2 which specifies the alternative alphabet used instead of the
    `+` and `/` characters.

    A [`binascii.Error`](binascii.html#binascii.Error "binascii.Error") exception is raised
    if *s* is incorrectly padded.

    If *validate* is `False` (the default), characters that are neither
    in the normal base-64 alphabet nor the alternative alphabet are
    discarded prior to the padding check. If *validate* is `True`,
    these non-alphabet characters in the input result in a
    [`binascii.Error`](binascii.html#binascii.Error "binascii.Error").

    For more information about the strict base64 check, see [`binascii.a2b_base64()`](binascii.html#binascii.a2b_base64 "binascii.a2b_base64")

    May assert or raise a [`ValueError`](exceptions.html#ValueError "ValueError") if the length of *altchars* is not 2.

base64.standard\_b64encode(*s*)[¶](#base64.standard_b64encode "Link to this definition")
:   Encode [bytes-like object](../glossary.html#term-bytes-like-object) *s* using the standard Base64 alphabet
    and return the encoded [`bytes`](stdtypes.html#bytes "bytes").

base64.standard\_b64decode(*s*)[¶](#base64.standard_b64decode "Link to this definition")
:   Decode [bytes-like object](../glossary.html#term-bytes-like-object) or ASCII string *s* using the standard
    Base64 alphabet and return the decoded [`bytes`](stdtypes.html#bytes "bytes").

base64.urlsafe\_b64encode(*s*)[¶](#base64.urlsafe_b64encode "Link to this definition")
:   Encode [bytes-like object](../glossary.html#term-bytes-like-object) *s* using the
    URL- and filesystem-safe alphabet, which
    substitutes `-` instead of `+` and `_` instead of `/` in the
    standard Base64 alphabet, and return the encoded [`bytes`](stdtypes.html#bytes "bytes"). The result
    can still contain `=`.

base64.urlsafe\_b64decode(*s*)[¶](#base64.urlsafe_b64decode "Link to this definition")
:   Decode [bytes-like object](../glossary.html#term-bytes-like-object) or ASCII string *s*
    using the URL- and filesystem-safe
    alphabet, which substitutes `-` instead of `+` and `_` instead of
    `/` in the standard Base64 alphabet, and return the decoded
    [`bytes`](stdtypes.html#bytes "bytes").

base64.b32encode(*s*)[¶](#base64.b32encode "Link to this definition")
:   Encode the [bytes-like object](../glossary.html#term-bytes-like-object) *s* using Base32 and return the
    encoded [`bytes`](stdtypes.html#bytes "bytes").

base64.b32decode(*s*, *casefold=False*, *map01=None*)[¶](#base64.b32decode "Link to this definition")
:   Decode the Base32 encoded [bytes-like object](../glossary.html#term-bytes-like-object) or ASCII string *s* and
    return the decoded [`bytes`](stdtypes.html#bytes "bytes").

    Optional *casefold* is a flag specifying
    whether a lowercase alphabet is acceptable as input. For security purposes,
    the default is `False`.

    [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html) allows for optional mapping of the digit 0 (zero) to the letter O
    (oh), and for optional mapping of the digit 1 (one) to either the letter I (eye)
    or letter L (el). The optional argument *map01* when not `None`, specifies
    which letter the digit 1 should be mapped to (when *map01* is not `None`, the
    digit 0 is always mapped to the letter O). For security purposes the default is
    `None`, so that 0 and 1 are not allowed in the input.

    A [`binascii.Error`](binascii.html#binascii.Error "binascii.Error") is raised if *s* is
    incorrectly padded or if there are non-alphabet characters present in the
    input.

base64.b32hexencode(*s*)[¶](#base64.b32hexencode "Link to this definition")
:   Similar to [`b32encode()`](#base64.b32encode "base64.b32encode") but uses the Extended Hex Alphabet, as defined in
    [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html).

    Added in version 3.10.

base64.b32hexdecode(*s*, *casefold=False*)[¶](#base64.b32hexdecode "Link to this definition")
:   Similar to [`b32decode()`](#base64.b32decode "base64.b32decode") but uses the Extended Hex Alphabet, as defined in
    [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html).

    This version does not allow the digit 0 (zero) to the letter O (oh) and digit
    1 (one) to either the letter I (eye) or letter L (el) mappings, all these
    characters are included in the Extended Hex Alphabet and are not
    interchangeable.

    Added in version 3.10.

base64.b16encode(*s*)[¶](#base64.b16encode "Link to this definition")
:   Encode the [bytes-like object](../glossary.html#term-bytes-like-object) *s* using Base16 and return the
    encoded [`bytes`](stdtypes.html#bytes "bytes").

base64.b16decode(*s*, *casefold=False*)[¶](#base64.b16decode "Link to this definition")
:   Decode the Base16 encoded [bytes-like object](../glossary.html#term-bytes-like-object) or ASCII string *s* and
    return the decoded [`bytes`](stdtypes.html#bytes "bytes").

    Optional *casefold* is a flag specifying whether a
    lowercase alphabet is acceptable as input. For security purposes, the default
    is `False`.

    A [`binascii.Error`](binascii.html#binascii.Error "binascii.Error") is raised if *s* is
    incorrectly padded or if there are non-alphabet characters present in the
    input.

## Base85 Encodings[¶](#base85-encodings "Link to this heading")

Base85 encoding is not formally specified but rather a de facto standard,
thus different systems perform the encoding differently.

The [`a85encode()`](#base64.a85encode "base64.a85encode") and [`b85encode()`](#base64.b85encode "base64.b85encode") functions in this module are two implementations of
the de facto standard. You should call the function with the Base85
implementation used by the software you intend to work with.

The two functions present in this module differ in how they handle the following:

* Whether to include enclosing `<~` and `~>` markers
* Whether to include newline characters
* The set of ASCII characters used for encoding
* Handling of null bytes

Refer to the documentation of the individual functions for more information.

base64.a85encode(*b*, *\**, *foldspaces=False*, *wrapcol=0*, *pad=False*, *adobe=False*)[¶](#base64.a85encode "Link to this definition")
:   Encode the [bytes-like object](../glossary.html#term-bytes-like-object) *b* using Ascii85 and return the
    encoded [`bytes`](stdtypes.html#bytes "bytes").

    *foldspaces* is an optional flag that uses the special short sequence ‘y’
    instead of 4 consecutive spaces (ASCII 0x20) as supported by ‘btoa’. This
    feature is not supported by the “standard” Ascii85 encoding.

    *wrapcol* controls whether the output should have newline (`b'\n'`)
    characters added to it. If this is non-zero, each output line will be
    at most this many characters long, excluding the trailing newline.

    *pad* controls whether the input is padded to a multiple of 4
    before encoding. Note that the `btoa` implementation always pads.

    *adobe* controls whether the encoded byte sequence is framed with `<~`
    and `~>`, which is used by the Adobe implementation.

    Added in version 3.4.

base64.a85decode(*b*, *\**, *foldspaces=False*, *adobe=False*, *ignorechars=b' \t\n\r\x0b'*)[¶](#base64.a85decode "Link to this definition")
:   Decode the Ascii85 encoded [bytes-like object](../glossary.html#term-bytes-like-object) or ASCII string *b* and
    return the decoded [`bytes`](stdtypes.html#bytes "bytes").

    *foldspaces* is a flag that specifies whether the ‘y’ short sequence
    should be accepted as shorthand for 4 consecutive spaces (ASCII 0x20).
    This feature is not supported by the “standard” Ascii85 encoding.

    *adobe* controls whether the input sequence is in Adobe Ascii85 format
    (i.e. is framed with <~ and ~>).

    *ignorechars* should be a byte string containing characters to ignore
    from the input. This should only contain whitespace characters, and by
    default contains all whitespace characters in ASCII.

    Added in version 3.4.

base64.b85encode(*b*, *pad=False*)[¶](#base64.b85encode "Link to this definition")
:   Encode the [bytes-like object](../glossary.html#term-bytes-like-object) *b* using base85 (as used in e.g.
    git-style binary diffs) and return the encoded [`bytes`](stdtypes.html#bytes "bytes").

    If *pad* is true, the input is padded with `b'\0'` so its length is a
    multiple of 4 bytes before encoding.

    Added in version 3.4.

base64.b85decode(*b*)[¶](#base64.b85decode "Link to this definition")
:   Decode the base85-encoded [bytes-like object](../glossary.html#term-bytes-like-object) or ASCII string *b* and
    return the decoded [`bytes`](stdtypes.html#bytes "bytes"). Padding is implicitly removed, if
    necessary.

    Added in version 3.4.

base64.z85encode(*s*)[¶](#base64.z85encode "Link to this definition")
:   Encode the [bytes-like object](../glossary.html#term-bytes-like-object) *s* using Z85 (as used in ZeroMQ)
    and return the encoded [`bytes`](stdtypes.html#bytes "bytes"). See [Z85 specification](https://rfc.zeromq.org/spec/32/) for more information.

    Added in version 3.13.

base64.z85decode(*s*)[¶](#base64.z85decode "Link to this definition")
:   Decode the Z85-encoded [bytes-like object](../glossary.html#term-bytes-like-object) or ASCII string *s* and
    return the decoded [`bytes`](stdtypes.html#bytes "bytes"). See [Z85 specification](https://rfc.zeromq.org/spec/32/) for more information.

    Added in version 3.13.

## Legacy Interface[¶](#legacy-interface "Link to this heading")

base64.decode(*input*, *output*)[¶](#base64.decode "Link to this definition")
:   Decode the contents of the binary *input* file and write the resulting binary
    data to the *output* file. *input* and *output* must be [file objects](../glossary.html#term-file-object). *input* will be read until `input.readline()` returns an
    empty bytes object.

base64.decodebytes(*s*)[¶](#base64.decodebytes "Link to this definition")
:   Decode the [bytes-like object](../glossary.html#term-bytes-like-object) *s*, which must contain one or more
    lines of base64 encoded data, and return the decoded [`bytes`](stdtypes.html#bytes "bytes").

    Added in version 3.1.

base64.encode(*input*, *output*)[¶](#base64.encode "Link to this definition")
:   Encode the contents of the binary *input* file and write the resulting base64
    encoded data to the *output* file. *input* and *output* must be [file
    objects](../glossary.html#term-file-object). *input* will be read until `input.read()` returns
    an empty bytes object. [`encode()`](#base64.encode "base64.encode") inserts a newline character (`b'\n'`)
    after every 76 bytes of the output, as well as ensuring that the output
    always ends with a newline, as per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) (MIME).

base64.encodebytes(*s*)[¶](#base64.encodebytes "Link to this definition")
:   Encode the [bytes-like object](../glossary.html#term-bytes-like-object) *s*, which can contain arbitrary binary
    data, and return [`bytes`](stdtypes.html#bytes "bytes") containing the base64-encoded data, with newlines
    (`b'\n'`) inserted after every 76 bytes of output, and ensuring that
    there is a trailing newline, as per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) (MIME).

    Added in version 3.1.

An example usage of the module:

```
>>> import base64
>>> encoded = base64.b64encode(b'data to be encoded')
>>> encoded
b'ZGF0YSB0byBiZSBlbmNvZGVk'
>>> data = base64.b64decode(encoded)
>>> data
b'data to be encoded'
```

## Security Considerations[¶](#security-considerations "Link to this heading")

A new security considerations section was added to [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html) (section 12); it’s
recommended to review the security section for any code deployed to production.

See also

Module [`binascii`](binascii.html#module-binascii "binascii: Tools for converting between binary and various ASCII-encoded binary representations.")
:   Support module containing ASCII-to-binary and binary-to-ASCII conversions.

[**RFC 1521**](https://datatracker.ietf.org/doc/html/rfc1521.html) - MIME (Multipurpose Internet Mail Extensions) Part One: Mechanisms for Specifying and Describing the Format of Internet Message Bodies
:   Section 5.2, “Base64 Content-Transfer-Encoding,” provides the definition of the
    base64 encoding.

### [Table of Contents](../contents.html)

* [`base64` — Base16, Base32, Base64, Base85 Data Encodings](#)
  + [RFC 4648 Encodings](#rfc-4648-encodings)
  + [Base85 Encodings](#base85-encodings)
  + [Legacy Interface](#legacy-interface)
  + [Security Considerations](#security-considerations)

#### Previous topic

[`mimetypes` — Map filenames to MIME types](mimetypes.html "previous chapter")

#### Next topic

[`binascii` — Convert between binary and ASCII](binascii.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/base64.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](binascii.html "binascii — Convert between binary and ASCII") |
* [previous](mimetypes.html "mimetypes — Map filenames to MIME types") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `base64` — Base16, Base32, Base64, Base85 Data Encodings
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