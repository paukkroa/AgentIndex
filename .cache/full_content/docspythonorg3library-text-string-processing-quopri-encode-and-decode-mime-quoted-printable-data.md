### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](markup.html "Structured Markup Processing Tools") |
* [previous](binascii.html "binascii — Convert between binary and ASCII") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `quopri` — Encode and decode MIME quoted-printable data
* |
* Theme
  Auto
  Light
  Dark
   |

# `quopri` — Encode and decode MIME quoted-printable data[¶](#module-quopri "Link to this heading")

**Source code:** [Lib/quopri.py](https://github.com/python/cpython/tree/3.14/Lib/quopri.py)

---

This module performs quoted-printable transport encoding and decoding, as
defined in [**RFC 1521**](https://datatracker.ietf.org/doc/html/rfc1521.html): “MIME (Multipurpose Internet Mail Extensions) Part One:
Mechanisms for Specifying and Describing the Format of Internet Message Bodies”.
The quoted-printable encoding is designed for data where there are relatively
few nonprintable characters; the base64 encoding scheme available via the
[`base64`](base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85") module is more compact if there are many such characters, as when
sending a graphics file.

quopri.decode(*input*, *output*, *header=False*)[¶](#quopri.decode "Link to this definition")
:   Decode the contents of the *input* file and write the resulting decoded binary
    data to the *output* file. *input* and *output* must be [binary file objects](../glossary.html#term-file-object). If the optional argument *header* is present and true, underscore
    will be decoded as space. This is used to decode “Q”-encoded headers as
    described in [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html): “MIME (Multipurpose Internet Mail Extensions)
    Part Two: Message Header Extensions for Non-ASCII Text”.

quopri.encode(*input*, *output*, *quotetabs*, *header=False*)[¶](#quopri.encode "Link to this definition")
:   Encode the contents of the *input* file and write the resulting quoted-printable
    data to the *output* file. *input* and *output* must be
    [binary file objects](../glossary.html#term-file-object). *quotetabs*, a
    non-optional flag which controls whether to encode embedded spaces
    and tabs; when true it encodes such embedded whitespace, and when
    false it leaves them unencoded.
    Note that spaces and tabs appearing at the end of lines are always encoded,
    as per [**RFC 1521**](https://datatracker.ietf.org/doc/html/rfc1521.html). *header* is a flag which controls if spaces are encoded
    as underscores as per [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html).

quopri.decodestring(*s*, *header=False*)[¶](#quopri.decodestring "Link to this definition")
:   Like [`decode()`](#quopri.decode "quopri.decode"), except that it accepts a source [`bytes`](stdtypes.html#bytes "bytes") and
    returns the corresponding decoded [`bytes`](stdtypes.html#bytes "bytes").

quopri.encodestring(*s*, *quotetabs=False*, *header=False*)[¶](#quopri.encodestring "Link to this definition")
:   Like [`encode()`](#quopri.encode "quopri.encode"), except that it accepts a source [`bytes`](stdtypes.html#bytes "bytes") and
    returns the corresponding encoded [`bytes`](stdtypes.html#bytes "bytes"). By default, it sends a
    `False` value to *quotetabs* parameter of the [`encode()`](#quopri.encode "quopri.encode") function.

See also

Module [`base64`](base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
:   Encode and decode MIME base64 data

#### Previous topic

[`binascii` — Convert between binary and ASCII](binascii.html "previous chapter")

#### Next topic

[Structured Markup Processing Tools](markup.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/quopri.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](markup.html "Structured Markup Processing Tools") |
* [previous](binascii.html "binascii — Convert between binary and ASCII") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `quopri` — Encode and decode MIME quoted-printable data
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