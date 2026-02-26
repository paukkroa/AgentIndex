### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](struct.html "struct — Interpret bytes as packed binary data") |
* [previous](rlcompleter.html "rlcompleter — Completion function for GNU readline") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Binary Data Services
* |
* Theme
  Auto
  Light
  Dark
   |

# Binary Data Services[¶](#binary-data-services "Link to this heading")

The modules described in this chapter provide some basic services operations
for manipulation of binary data. Other operations on binary data, specifically
in relation to file formats and network protocols, are described in the
relevant sections.

Some libraries described under [Text Processing Services](text.html#textservices) also work with either
ASCII-compatible binary formats (for example, [`re`](re.html#module-re "re: Regular expression operations.")) or all binary data
(for example, [`difflib`](difflib.html#module-difflib "difflib: Helpers for computing differences between objects.")).

In addition, see the documentation for Python’s built-in binary data types in
[Binary Sequence Types — bytes, bytearray, memoryview](stdtypes.html#binaryseq).

* [`struct` — Interpret bytes as packed binary data](struct.html)
  + [Functions and Exceptions](struct.html#functions-and-exceptions)
  + [Format Strings](struct.html#format-strings)
    - [Byte Order, Size, and Alignment](struct.html#byte-order-size-and-alignment)
    - [Format Characters](struct.html#format-characters)
    - [Examples](struct.html#examples)
  + [Applications](struct.html#applications)
    - [Native Formats](struct.html#native-formats)
    - [Standard Formats](struct.html#standard-formats)
  + [Classes](struct.html#classes)
* [`codecs` — Codec registry and base classes](codecs.html)
  + [Codec Base Classes](codecs.html#codec-base-classes)
    - [Error Handlers](codecs.html#error-handlers)
    - [Stateless Encoding and Decoding](codecs.html#stateless-encoding-and-decoding)
    - [Incremental Encoding and Decoding](codecs.html#incremental-encoding-and-decoding)
      * [IncrementalEncoder Objects](codecs.html#incrementalencoder-objects)
      * [IncrementalDecoder Objects](codecs.html#incrementaldecoder-objects)
    - [Stream Encoding and Decoding](codecs.html#stream-encoding-and-decoding)
      * [StreamWriter Objects](codecs.html#streamwriter-objects)
      * [StreamReader Objects](codecs.html#streamreader-objects)
      * [StreamReaderWriter Objects](codecs.html#streamreaderwriter-objects)
      * [StreamRecoder Objects](codecs.html#streamrecoder-objects)
  + [Encodings and Unicode](codecs.html#encodings-and-unicode)
  + [Standard Encodings](codecs.html#standard-encodings)
  + [Python Specific Encodings](codecs.html#python-specific-encodings)
    - [Text Encodings](codecs.html#text-encodings)
    - [Binary Transforms](codecs.html#binary-transforms)
    - [Standalone Codec Functions](codecs.html#standalone-codec-functions)
    - [Text Transforms](codecs.html#text-transforms)
  + [`encodings` — Encodings package](codecs.html#module-encodings)
  + [`encodings.idna` — Internationalized Domain Names in Applications](codecs.html#module-encodings.idna)
  + [`encodings.mbcs` — Windows ANSI codepage](codecs.html#module-encodings.mbcs)
  + [`encodings.utf_8_sig` — UTF-8 codec with BOM signature](codecs.html#module-encodings.utf_8_sig)

#### Previous topic

[`rlcompleter` — Completion function for GNU readline](rlcompleter.html "previous chapter")

#### Next topic

[`struct` — Interpret bytes as packed binary data](struct.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/binary.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](struct.html "struct — Interpret bytes as packed binary data") |
* [previous](rlcompleter.html "rlcompleter — Completion function for GNU readline") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Binary Data Services
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