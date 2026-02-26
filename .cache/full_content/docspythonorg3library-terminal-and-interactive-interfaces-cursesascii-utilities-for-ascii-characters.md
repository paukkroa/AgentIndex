### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](curses.panel.html "curses.panel — A panel stack extension for curses") |
* [previous](curses.html "curses — Terminal handling for character-cell displays") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `curses.ascii` — Utilities for ASCII characters
* |
* Theme
  Auto
  Light
  Dark
   |

# `curses.ascii` — Utilities for ASCII characters[¶](#module-curses.ascii "Link to this heading")

**Source code:** [Lib/curses/ascii.py](https://github.com/python/cpython/tree/3.14/Lib/curses/ascii.py)

---

The `curses.ascii` module supplies name constants for ASCII characters and
functions to test membership in various ASCII character classes. The constants
supplied are names for control characters as follows:

| Name | Meaning |
| --- | --- |
| curses.ascii.NUL[¶](#curses.ascii.NUL "Link to this definition") |  |
| curses.ascii.SOH[¶](#curses.ascii.SOH "Link to this definition") | Start of heading, console interrupt |
| curses.ascii.STX[¶](#curses.ascii.STX "Link to this definition") | Start of text |
| curses.ascii.ETX[¶](#curses.ascii.ETX "Link to this definition") | End of text |
| curses.ascii.EOT[¶](#curses.ascii.EOT "Link to this definition") | End of transmission |
| curses.ascii.ENQ[¶](#curses.ascii.ENQ "Link to this definition") | Enquiry, goes with [`ACK`](#curses.ascii.ACK "curses.ascii.ACK") flow control |
| curses.ascii.ACK[¶](#curses.ascii.ACK "Link to this definition") | Acknowledgement |
| curses.ascii.BEL[¶](#curses.ascii.BEL "Link to this definition") | Bell |
| curses.ascii.BS[¶](#curses.ascii.BS "Link to this definition") | Backspace |
| curses.ascii.TAB[¶](#curses.ascii.TAB "Link to this definition") | Tab |
| curses.ascii.HT[¶](#curses.ascii.HT "Link to this definition") | Alias for [`TAB`](#curses.ascii.TAB "curses.ascii.TAB"): “Horizontal tab” |
| curses.ascii.LF[¶](#curses.ascii.LF "Link to this definition") | Line feed |
| curses.ascii.NL[¶](#curses.ascii.NL "Link to this definition") | Alias for [`LF`](#curses.ascii.LF "curses.ascii.LF"): “New line” |
| curses.ascii.VT[¶](#curses.ascii.VT "Link to this definition") | Vertical tab |
| curses.ascii.FF[¶](#curses.ascii.FF "Link to this definition") | Form feed |
| curses.ascii.CR[¶](#curses.ascii.CR "Link to this definition") | Carriage return |
| curses.ascii.SO[¶](#curses.ascii.SO "Link to this definition") | Shift-out, begin alternate character set |
| curses.ascii.SI[¶](#curses.ascii.SI "Link to this definition") | Shift-in, resume default character set |
| curses.ascii.DLE[¶](#curses.ascii.DLE "Link to this definition") | Data-link escape |
| curses.ascii.DC1[¶](#curses.ascii.DC1 "Link to this definition") | XON, for flow control |
| curses.ascii.DC2[¶](#curses.ascii.DC2 "Link to this definition") | Device control 2, block-mode flow control |
| curses.ascii.DC3[¶](#curses.ascii.DC3 "Link to this definition") | XOFF, for flow control |
| curses.ascii.DC4[¶](#curses.ascii.DC4 "Link to this definition") | Device control 4 |
| curses.ascii.NAK[¶](#curses.ascii.NAK "Link to this definition") | Negative acknowledgement |
| curses.ascii.SYN[¶](#curses.ascii.SYN "Link to this definition") | Synchronous idle |
| curses.ascii.ETB[¶](#curses.ascii.ETB "Link to this definition") | End transmission block |
| curses.ascii.CAN[¶](#curses.ascii.CAN "Link to this definition") | Cancel |
| curses.ascii.EM[¶](#curses.ascii.EM "Link to this definition") | End of medium |
| curses.ascii.SUB[¶](#curses.ascii.SUB "Link to this definition") | Substitute |
| curses.ascii.ESC[¶](#curses.ascii.ESC "Link to this definition") | Escape |
| curses.ascii.FS[¶](#curses.ascii.FS "Link to this definition") | File separator |
| curses.ascii.GS[¶](#curses.ascii.GS "Link to this definition") | Group separator |
| curses.ascii.RS[¶](#curses.ascii.RS "Link to this definition") | Record separator, block-mode terminator |
| curses.ascii.US[¶](#curses.ascii.US "Link to this definition") | Unit separator |
| curses.ascii.SP[¶](#curses.ascii.SP "Link to this definition") | Space |
| curses.ascii.DEL[¶](#curses.ascii.DEL "Link to this definition") | Delete |

Note that many of these have little practical significance in modern usage. The
mnemonics derive from teleprinter conventions that predate digital computers.

The module supplies the following functions, patterned on those in the standard
C library:

curses.ascii.isalnum(*c*)[¶](#curses.ascii.isalnum "Link to this definition")
:   Checks for an ASCII alphanumeric character; it is equivalent to `isalpha(c) or
    isdigit(c)`.

curses.ascii.isalpha(*c*)[¶](#curses.ascii.isalpha "Link to this definition")
:   Checks for an ASCII alphabetic character; it is equivalent to `isupper(c) or
    islower(c)`.

curses.ascii.isascii(*c*)[¶](#curses.ascii.isascii "Link to this definition")
:   Checks for a character value that fits in the 7-bit ASCII set.

curses.ascii.isblank(*c*)[¶](#curses.ascii.isblank "Link to this definition")
:   Checks for an ASCII whitespace character; space or horizontal tab.

curses.ascii.iscntrl(*c*)[¶](#curses.ascii.iscntrl "Link to this definition")
:   Checks for an ASCII control character (in the range 0x00 to 0x1f or 0x7f).

curses.ascii.isdigit(*c*)[¶](#curses.ascii.isdigit "Link to this definition")
:   Checks for an ASCII decimal digit, `'0'` through `'9'`. This is equivalent
    to `c in string.digits`.

curses.ascii.isgraph(*c*)[¶](#curses.ascii.isgraph "Link to this definition")
:   Checks for ASCII any printable character except space.

curses.ascii.islower(*c*)[¶](#curses.ascii.islower "Link to this definition")
:   Checks for an ASCII lower-case character.

curses.ascii.isprint(*c*)[¶](#curses.ascii.isprint "Link to this definition")
:   Checks for any ASCII printable character including space.

curses.ascii.ispunct(*c*)[¶](#curses.ascii.ispunct "Link to this definition")
:   Checks for any printable ASCII character which is not a space or an alphanumeric
    character.

curses.ascii.isspace(*c*)[¶](#curses.ascii.isspace "Link to this definition")
:   Checks for ASCII white-space characters; space, line feed, carriage return, form
    feed, horizontal tab, vertical tab.

curses.ascii.isupper(*c*)[¶](#curses.ascii.isupper "Link to this definition")
:   Checks for an ASCII uppercase letter.

curses.ascii.isxdigit(*c*)[¶](#curses.ascii.isxdigit "Link to this definition")
:   Checks for an ASCII hexadecimal digit. This is equivalent to `c in
    string.hexdigits`.

curses.ascii.isctrl(*c*)[¶](#curses.ascii.isctrl "Link to this definition")
:   Checks for an ASCII control character (ordinal values 0 to 31).

curses.ascii.ismeta(*c*)[¶](#curses.ascii.ismeta "Link to this definition")
:   Checks for a non-ASCII character (ordinal values 0x80 and above).

These functions accept either integers or single-character strings; when the argument is a
string, it is first converted using the built-in function [`ord()`](functions.html#ord "ord").

Note that all these functions check ordinal bit values derived from the
character of the string you pass in; they do not actually know anything about
the host machine’s character encoding.

The following two functions take either a single-character string or integer
byte value; they return a value of the same type.

curses.ascii.ascii(*c*)[¶](#curses.ascii.ascii "Link to this definition")
:   Return the ASCII value corresponding to the low 7 bits of *c*.

curses.ascii.ctrl(*c*)[¶](#curses.ascii.ctrl "Link to this definition")
:   Return the control character corresponding to the given character (the character
    bit value is bitwise-anded with 0x1f).

curses.ascii.alt(*c*)[¶](#curses.ascii.alt "Link to this definition")
:   Return the 8-bit character corresponding to the given ASCII character (the
    character bit value is bitwise-ored with 0x80).

The following function takes either a single-character string or integer value;
it returns a string.

curses.ascii.unctrl(*c*)[¶](#curses.ascii.unctrl "Link to this definition")
:   Return a string representation of the ASCII character *c*. If *c* is printable,
    this string is the character itself. If the character is a control character
    (0x00–0x1f) the string consists of a caret (`'^'`) followed by the
    corresponding uppercase letter. If the character is an ASCII delete (0x7f) the
    string is `'^?'`. If the character has its meta bit (0x80) set, the meta bit
    is stripped, the preceding rules applied, and `'!'` prepended to the result.

curses.ascii.controlnames[¶](#curses.ascii.controlnames "Link to this definition")
:   A 33-element string array that contains the ASCII mnemonics for the thirty-two
    ASCII control characters from 0 (NUL) to 0x1f (US), in order, plus the mnemonic
    `SP` for the space character.

#### Previous topic

[`curses` — Terminal handling for character-cell displays](curses.html "previous chapter")

#### Next topic

[`curses.panel` — A panel stack extension for curses](curses.panel.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/curses.ascii.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](curses.panel.html "curses.panel — A panel stack extension for curses") |
* [previous](curses.html "curses — Terminal handling for character-cell displays") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `curses.ascii` — Utilities for ASCII characters
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