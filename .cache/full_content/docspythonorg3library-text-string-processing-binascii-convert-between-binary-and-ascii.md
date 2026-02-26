### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](quopri.html "quopri — Encode and decode MIME quoted-printable data") |
* [previous](base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `binascii` — Convert between binary and ASCII
* |
* Theme
  Auto
  Light
  Dark
   |

# `binascii` — Convert between binary and ASCII[¶](#module-binascii "Link to this heading")

---

The `binascii` module contains a number of methods to convert between
binary and various ASCII-encoded binary representations. Normally, you will not
use these functions directly but use wrapper modules like
[`base64`](base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85") instead. The `binascii` module contains
low-level functions written in C for greater speed that are used by the
higher-level modules.

Note

`a2b_*` functions accept Unicode strings containing only ASCII characters.
Other functions only accept [bytes-like objects](../glossary.html#term-bytes-like-object) (such as
[`bytes`](stdtypes.html#bytes "bytes"), [`bytearray`](stdtypes.html#bytearray "bytearray") and other objects that support the buffer
protocol).

Changed in version 3.3: ASCII-only unicode strings are now accepted by the `a2b_*` functions.

The `binascii` module defines the following functions:

binascii.a2b\_uu(*string*)[¶](#binascii.a2b_uu "Link to this definition")
:   Convert a single line of uuencoded data back to binary and return the binary
    data. Lines normally contain 45 (binary) bytes, except for the last line. Line
    data may be followed by whitespace.

binascii.b2a\_uu(*data*, *\**, *backtick=False*)[¶](#binascii.b2a_uu "Link to this definition")
:   Convert binary data to a line of ASCII characters, the return value is the
    converted line, including a newline char. The length of *data* should be at most
    45. If *backtick* is true, zeros are represented by `` '`' `` instead of spaces.

    Changed in version 3.7: Added the *backtick* parameter.

binascii.a2b\_base64(*string*, */*, *\**, *strict\_mode=False*)[¶](#binascii.a2b_base64 "Link to this definition")
:   Convert a block of base64 data back to binary and return the binary data. More
    than one line may be passed at a time.

    If *strict\_mode* is true, only valid base64 data will be converted. Invalid base64
    data will raise [`binascii.Error`](#binascii.Error "binascii.Error").

    Valid base64:

    * Conforms to [**RFC 3548**](https://datatracker.ietf.org/doc/html/rfc3548.html).
    * Contains only characters from the base64 alphabet.
    * Contains no excess data after padding (including excess padding, newlines, etc.).
    * Does not start with a padding.

    Changed in version 3.11: Added the *strict\_mode* parameter.

binascii.b2a\_base64(*data*, *\**, *newline=True*)[¶](#binascii.b2a_base64 "Link to this definition")
:   Convert binary data to a line of ASCII characters in base64 coding. The return
    value is the converted line, including a newline char if *newline* is
    true. The output of this function conforms to [**RFC 3548**](https://datatracker.ietf.org/doc/html/rfc3548.html).

    Changed in version 3.6: Added the *newline* parameter.

binascii.a2b\_qp(*data*, *header=False*)[¶](#binascii.a2b_qp "Link to this definition")
:   Convert a block of quoted-printable data back to binary and return the binary
    data. More than one line may be passed at a time. If the optional argument
    *header* is present and true, underscores will be decoded as spaces.

binascii.b2a\_qp(*data*, *quotetabs=False*, *istext=True*, *header=False*)[¶](#binascii.b2a_qp "Link to this definition")
:   Convert binary data to a line(s) of ASCII characters in quoted-printable
    encoding. The return value is the converted line(s). If the optional argument
    *quotetabs* is present and true, all tabs and spaces will be encoded. If the
    optional argument *istext* is present and true, newlines are not encoded but
    trailing whitespace will be encoded. If the optional argument *header* is
    present and true, spaces will be encoded as underscores per [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html). If the
    optional argument *header* is present and false, newline characters will be
    encoded as well; otherwise linefeed conversion might corrupt the binary data
    stream.

binascii.crc\_hqx(*data*, *value*)[¶](#binascii.crc_hqx "Link to this definition")
:   Compute a 16-bit CRC value of *data*, starting with *value* as the
    initial CRC, and return the result. This uses the CRC-CCITT polynomial
    *x*16 + *x*12 + *x*5 + 1, often represented as
    0x1021. This CRC is used in the binhex4 format.

binascii.crc32(*data*[, *value*])[¶](#binascii.crc32 "Link to this definition")
:   Compute CRC-32, the unsigned 32-bit checksum of *data*, starting with an
    initial CRC of *value*. The default initial CRC is zero. The algorithm
    is consistent with the ZIP file checksum. Since the algorithm is designed for
    use as a checksum algorithm, it is not suitable for use as a general hash
    algorithm. Use as follows:

    ```
    print(binascii.crc32(b"hello world"))
    # Or, in two pieces:
    crc = binascii.crc32(b"hello")
    crc = binascii.crc32(b" world", crc)
    print('crc32 = {:#010x}'.format(crc))
    ```

    Changed in version 3.0: The result is always unsigned.

binascii.b2a\_hex(*data*[, *sep*[, *bytes\_per\_sep=1*]])[¶](#binascii.b2a_hex "Link to this definition")

binascii.hexlify(*data*[, *sep*[, *bytes\_per\_sep=1*]])[¶](#binascii.hexlify "Link to this definition")
:   Return the hexadecimal representation of the binary *data*. Every byte of
    *data* is converted into the corresponding 2-digit hex representation. The
    returned bytes object is therefore twice as long as the length of *data*.

    Similar functionality (but returning a text string) is also conveniently
    accessible using the [`bytes.hex()`](stdtypes.html#bytes.hex "bytes.hex") method.

    If *sep* is specified, it must be a single character str or bytes object.
    It will be inserted in the output after every *bytes\_per\_sep* input bytes.
    Separator placement is counted from the right end of the output by default,
    if you wish to count from the left, supply a negative *bytes\_per\_sep* value.

    ```
    >>> import binascii
    >>> binascii.b2a_hex(b'\xb9\x01\xef')
    b'b901ef'
    >>> binascii.hexlify(b'\xb9\x01\xef', '-')
    b'b9-01-ef'
    >>> binascii.b2a_hex(b'\xb9\x01\xef', b'_', 2)
    b'b9_01ef'
    >>> binascii.b2a_hex(b'\xb9\x01\xef', b' ', -2)
    b'b901 ef'
    ```

    Changed in version 3.8: The *sep* and *bytes\_per\_sep* parameters were added.

binascii.a2b\_hex(*hexstr*)[¶](#binascii.a2b_hex "Link to this definition")

binascii.unhexlify(*hexstr*)[¶](#binascii.unhexlify "Link to this definition")
:   Return the binary data represented by the hexadecimal string *hexstr*. This
    function is the inverse of [`b2a_hex()`](#binascii.b2a_hex "binascii.b2a_hex"). *hexstr* must contain an even number
    of hexadecimal digits (which can be upper or lower case), otherwise an
    [`Error`](#binascii.Error "binascii.Error") exception is raised.

    Similar functionality (accepting only text string arguments, but more
    liberal towards whitespace) is also accessible using the
    [`bytes.fromhex()`](stdtypes.html#bytes.fromhex "bytes.fromhex") class method.

*exception* binascii.Error[¶](#binascii.Error "Link to this definition")
:   Exception raised on errors. These are usually programming errors.

*exception* binascii.Incomplete[¶](#binascii.Incomplete "Link to this definition")
:   Exception raised on incomplete data. These are usually not programming errors,
    but may be handled by reading a little more data and trying again.

See also

Module [`base64`](base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
:   Support for RFC compliant base64-style encoding in base 16, 32, 64,
    and 85.

Module [`quopri`](quopri.html#module-quopri "quopri: Encode and decode files using the MIME quoted-printable encoding.")
:   Support for quoted-printable encoding used in MIME email messages.

#### Previous topic

[`base64` — Base16, Base32, Base64, Base85 Data Encodings](base64.html "previous chapter")

#### Next topic

[`quopri` — Encode and decode MIME quoted-printable data](quopri.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/binascii.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](quopri.html "quopri — Encode and decode MIME quoted-printable data") |
* [previous](base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `binascii` — Convert between binary and ASCII
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