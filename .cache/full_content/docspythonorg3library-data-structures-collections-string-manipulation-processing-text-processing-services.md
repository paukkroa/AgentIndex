### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](string.html "string — Common string operations") |
* [previous](exceptions.html "Built-in Exceptions") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Text Processing Services
* |
* Theme
  Auto
  Light
  Dark
   |

# Text Processing Services[¶](#text-processing-services "Link to this heading")

The modules described in this chapter provide a wide range of string
manipulation operations and other text processing services.

The [`codecs`](codecs.html#module-codecs "codecs: Encode and decode data and streams.") module described under [Binary Data Services](binary.html#binaryservices) is also
highly relevant to text processing. In addition, see the documentation for
Python’s built-in string type in [Text Sequence Type — str](stdtypes.html#textseq).

* [`string` — Common string operations](string.html)
  + [String constants](string.html#string-constants)
  + [Custom String Formatting](string.html#custom-string-formatting)
  + [Format String Syntax](string.html#format-string-syntax)
    - [Format Specification Mini-Language](string.html#format-specification-mini-language)
    - [Format examples](string.html#format-examples)
  + [Template strings ($-strings)](string.html#template-strings-strings)
  + [Helper functions](string.html#helper-functions)
* [`string.templatelib` — Support for template string literals](string.templatelib.html)
  + [Template strings](string.templatelib.html#template-strings)
  + [Types](string.templatelib.html#types)
  + [Helper functions](string.templatelib.html#helper-functions)
* [`re` — Regular expression operations](re.html)
  + [Regular Expression Syntax](re.html#regular-expression-syntax)
  + [Module Contents](re.html#module-contents)
    - [Flags](re.html#flags)
    - [Functions](re.html#functions)
    - [Exceptions](re.html#exceptions)
  + [Regular Expression Objects](re.html#regular-expression-objects)
  + [Match Objects](re.html#match-objects)
  + [Regular Expression Examples](re.html#regular-expression-examples)
    - [Checking for a Pair](re.html#checking-for-a-pair)
    - [Simulating scanf()](re.html#simulating-scanf)
    - [search() vs. match()](re.html#search-vs-match)
    - [Making a Phonebook](re.html#making-a-phonebook)
    - [Text Munging](re.html#text-munging)
    - [Finding all Adverbs](re.html#finding-all-adverbs)
    - [Finding all Adverbs and their Positions](re.html#finding-all-adverbs-and-their-positions)
    - [Raw String Notation](re.html#raw-string-notation)
    - [Writing a Tokenizer](re.html#writing-a-tokenizer)
* [`difflib` — Helpers for computing deltas](difflib.html)
  + [SequenceMatcher Objects](difflib.html#sequencematcher-objects)
  + [SequenceMatcher Examples](difflib.html#sequencematcher-examples)
  + [Differ Objects](difflib.html#differ-objects)
  + [Differ Example](difflib.html#differ-example)
  + [A command-line interface to difflib](difflib.html#a-command-line-interface-to-difflib)
  + [ndiff example](difflib.html#ndiff-example)
* [`textwrap` — Text wrapping and filling](textwrap.html)
* [`unicodedata` — Unicode Database](unicodedata.html)
* [`stringprep` — Internet String Preparation](stringprep.html)
* [`readline` — GNU readline interface](readline.html)
  + [Init file](readline.html#init-file)
  + [Line buffer](readline.html#line-buffer)
  + [History file](readline.html#history-file)
  + [History list](readline.html#history-list)
  + [Startup hooks](readline.html#startup-hooks)
  + [Completion](readline.html#completion)
  + [Example](readline.html#example)
* [`rlcompleter` — Completion function for GNU readline](rlcompleter.html)

#### Previous topic

[Built-in Exceptions](exceptions.html "previous chapter")

#### Next topic

[`string` — Common string operations](string.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/text.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](string.html "string — Common string operations") |
* [previous](exceptions.html "Built-in Exceptions") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Text Processing Services
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