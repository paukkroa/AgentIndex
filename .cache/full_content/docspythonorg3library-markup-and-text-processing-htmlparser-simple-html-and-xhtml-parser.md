### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](html.entities.html "html.entities — Definitions of HTML general entities") |
* [previous](html.html "html — HyperText Markup Language support") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `html.parser` — Simple HTML and XHTML parser
* |
* Theme
  Auto
  Light
  Dark
   |

# `html.parser` — Simple HTML and XHTML parser[¶](#module-html.parser "Link to this heading")

**Source code:** [Lib/html/parser.py](https://github.com/python/cpython/tree/3.14/Lib/html/parser.py)

---

This module defines a class [`HTMLParser`](#html.parser.HTMLParser "html.parser.HTMLParser") which serves as the basis for
parsing text files formatted in HTML (HyperText Mark-up Language) and XHTML.

*class* html.parser.HTMLParser(*\**, *convert\_charrefs=True*, *scripting=False*)[¶](#html.parser.HTMLParser "Link to this definition")
:   Create a parser instance able to parse invalid markup.

    If *convert\_charrefs* is true (the default), all character
    references (except the ones in elements like `script` and `style`) are
    automatically converted to the corresponding Unicode characters.

    If *scripting* is false (the default), the content of the `noscript`
    element is parsed normally; if it’s true, it’s returned as is without
    being parsed.

    An [`HTMLParser`](#html.parser.HTMLParser "html.parser.HTMLParser") instance is fed HTML data and calls handler methods
    when start tags, end tags, text, comments, and other markup elements are
    encountered. The user should subclass [`HTMLParser`](#html.parser.HTMLParser "html.parser.HTMLParser") and override its
    methods to implement the desired behavior.

    This parser does not check that end tags match start tags or call the end-tag
    handler for elements which are closed implicitly by closing an outer element.

    Changed in version 3.4: *convert\_charrefs* keyword argument added.

    Changed in version 3.5: The default value for argument *convert\_charrefs* is now `True`.

    Changed in version 3.14.1: Added the *scripting* parameter.

## Example HTML Parser Application[¶](#example-html-parser-application "Link to this heading")

As a basic example, below is a simple HTML parser that uses the
[`HTMLParser`](#html.parser.HTMLParser "html.parser.HTMLParser") class to print out start tags, end tags, and data
as they are encountered:

```
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
```

The output will then be:

```
Encountered a start tag: html
Encountered a start tag: head
Encountered a start tag: title
Encountered some data  : Test
Encountered an end tag : title
Encountered an end tag : head
Encountered a start tag: body
Encountered a start tag: h1
Encountered some data  : Parse me!
Encountered an end tag : h1
Encountered an end tag : body
Encountered an end tag : html
```

## [`HTMLParser`](#html.parser.HTMLParser "html.parser.HTMLParser") Methods[¶](#htmlparser-methods "Link to this heading")

[`HTMLParser`](#html.parser.HTMLParser "html.parser.HTMLParser") instances have the following methods:

HTMLParser.feed(*data*)[¶](#html.parser.HTMLParser.feed "Link to this definition")
:   Feed some text to the parser. It is processed insofar as it consists of
    complete elements; incomplete data is buffered until more data is fed or
    [`close()`](#html.parser.HTMLParser.close "html.parser.HTMLParser.close") is called. *data* must be [`str`](stdtypes.html#str "str").

HTMLParser.close()[¶](#html.parser.HTMLParser.close "Link to this definition")
:   Force processing of all buffered data as if it were followed by an end-of-file
    mark. This method may be redefined by a derived class to define additional
    processing at the end of the input, but the redefined version should always call
    the [`HTMLParser`](#html.parser.HTMLParser "html.parser.HTMLParser") base class method [`close()`](#html.parser.HTMLParser.close "html.parser.HTMLParser.close").

HTMLParser.reset()[¶](#html.parser.HTMLParser.reset "Link to this definition")
:   Reset the instance. Loses all unprocessed data. This is called implicitly at
    instantiation time.

HTMLParser.getpos()[¶](#html.parser.HTMLParser.getpos "Link to this definition")
:   Return current line number and offset.

HTMLParser.get\_starttag\_text()[¶](#html.parser.HTMLParser.get_starttag_text "Link to this definition")
:   Return the text of the most recently opened start tag. This should not normally
    be needed for structured processing, but may be useful in dealing with HTML “as
    deployed” or for re-generating input with minimal changes (whitespace between
    attributes can be preserved, etc.).

The following methods are called when data or markup elements are encountered
and they are meant to be overridden in a subclass. The base class
implementations do nothing (except for [`handle_startendtag()`](#html.parser.HTMLParser.handle_startendtag "html.parser.HTMLParser.handle_startendtag")):

HTMLParser.handle\_starttag(*tag*, *attrs*)[¶](#html.parser.HTMLParser.handle_starttag "Link to this definition")
:   This method is called to handle the start tag of an element (e.g. `<div id="main">`).

    The *tag* argument is the name of the tag converted to lower case. The *attrs*
    argument is a list of `(name, value)` pairs containing the attributes found
    inside the tag’s `<>` brackets. The *name* will be translated to lower case,
    and quotes in the *value* have been removed, and character and entity references
    have been replaced.

    For instance, for the tag `<A HREF="https://www.cwi.nl/">`, this method
    would be called as `handle_starttag('a', [('href', 'https://www.cwi.nl/')])`.

    All entity references from [`html.entities`](html.entities.html#module-html.entities "html.entities: Definitions of HTML general entities.") are replaced in the attribute
    values.

HTMLParser.handle\_endtag(*tag*)[¶](#html.parser.HTMLParser.handle_endtag "Link to this definition")
:   This method is called to handle the end tag of an element (e.g. `</div>`).

    The *tag* argument is the name of the tag converted to lower case.

HTMLParser.handle\_startendtag(*tag*, *attrs*)[¶](#html.parser.HTMLParser.handle_startendtag "Link to this definition")
:   Similar to [`handle_starttag()`](#html.parser.HTMLParser.handle_starttag "html.parser.HTMLParser.handle_starttag"), but called when the parser encounters an
    XHTML-style empty tag (`<img ... />`). This method may be overridden by
    subclasses which require this particular lexical information; the default
    implementation simply calls [`handle_starttag()`](#html.parser.HTMLParser.handle_starttag "html.parser.HTMLParser.handle_starttag") and [`handle_endtag()`](#html.parser.HTMLParser.handle_endtag "html.parser.HTMLParser.handle_endtag").

HTMLParser.handle\_data(*data*)[¶](#html.parser.HTMLParser.handle_data "Link to this definition")
:   This method is called to process arbitrary data (e.g. text nodes and the
    content of elements like `script` and `style`).

HTMLParser.handle\_entityref(*name*)[¶](#html.parser.HTMLParser.handle_entityref "Link to this definition")
:   This method is called to process a named character reference of the form
    `&name;` (e.g. `&gt;`), where *name* is a general entity reference
    (e.g. `'gt'`).
    This method is only called if *convert\_charrefs* is false.

HTMLParser.handle\_charref(*name*)[¶](#html.parser.HTMLParser.handle_charref "Link to this definition")
:   This method is called to process decimal and hexadecimal numeric character
    references of the form `&#NNN;` and `&#xNNN;`. For example, the decimal
    equivalent for `&gt;` is `&#62;`, whereas the hexadecimal is `&#x3E;`;
    in this case the method will receive `'62'` or `'x3E'`.
    This method is only called if *convert\_charrefs* is false.

HTMLParser.handle\_comment(*data*)[¶](#html.parser.HTMLParser.handle_comment "Link to this definition")
:   This method is called when a comment is encountered (e.g. `<!--comment-->`).

    For example, the comment `<!-- comment -->` will cause this method to be
    called with the argument `' comment '`.

    The content of Internet Explorer conditional comments (condcoms) will also be
    sent to this method, so, for `<!--[if IE 9]>IE9-specific content<![endif]-->`,
    this method will receive `'[if IE 9]>IE9-specific content<![endif]'`.

HTMLParser.handle\_decl(*decl*)[¶](#html.parser.HTMLParser.handle_decl "Link to this definition")
:   This method is called to handle an HTML doctype declaration (e.g.
    `<!DOCTYPE html>`).

    The *decl* parameter will be the entire contents of the declaration inside
    the `<!...>` markup (e.g. `'DOCTYPE html'`).

HTMLParser.handle\_pi(*data*)[¶](#html.parser.HTMLParser.handle_pi "Link to this definition")
:   Method called when a processing instruction is encountered. The *data*
    parameter will contain the entire processing instruction. For example, for the
    processing instruction `<?proc color='red'>`, this method would be called as
    `handle_pi("proc color='red'")`. It is intended to be overridden by a derived
    class; the base class implementation does nothing.

    Note

    The [`HTMLParser`](#html.parser.HTMLParser "html.parser.HTMLParser") class uses the SGML syntactic rules for processing
    instructions. An XHTML processing instruction using the trailing `'?'` will
    cause the `'?'` to be included in *data*.

HTMLParser.unknown\_decl(*data*)[¶](#html.parser.HTMLParser.unknown_decl "Link to this definition")
:   This method is called when an unrecognized declaration is read by the parser.

    The *data* parameter will be the entire contents of the declaration inside
    the `<![...]>` markup. It is sometimes useful to be overridden by a
    derived class. The base class implementation does nothing.

## Examples[¶](#examples "Link to this heading")

The following class implements a parser that will be used to illustrate more
examples:

```
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
```

Parsing a doctype:

```
>>> parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
...             '"http://www.w3.org/TR/html4/strict.dtd">')
Decl     : DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"
```

Parsing an element with a few attributes and a title:

```
>>> parser.feed('<img src="python-logo.png" alt="The Python logo">')
Start tag: img
     attr: ('src', 'python-logo.png')
     attr: ('alt', 'The Python logo')
>>>
>>> parser.feed('<h1>Python</h1>')
Start tag: h1
Data     : Python
End tag  : h1
```

The content of elements like `script` and `style` is returned as is,
without further parsing:

```
>>> parser.feed('<style type="text/css">#python { color: green }</style>')
Start tag: style
     attr: ('type', 'text/css')
Data     : #python { color: green }
End tag  : style

>>> parser.feed('<script type="text/javascript">'
...             'alert("<strong>hello! &#9786;</strong>");</script>')
Start tag: script
     attr: ('type', 'text/javascript')
Data     : alert("<strong>hello! &#9786;</strong>");
End tag  : script
```

Parsing comments:

```
>>> parser.feed('<!--a comment-->'
...             '<!--[if IE 9]>IE-specific content<![endif]-->')
Comment  : a comment
Comment  : [if IE 9]>IE-specific content<![endif]
```

Parsing named and numeric character references and converting them to the
correct char (note: these 3 references are all equivalent to `'>'`):

```
>>> parser = MyHTMLParser()
>>> parser.feed('&gt;&#62;&#x3E;')
Data     : >>>

>>> parser = MyHTMLParser(convert_charrefs=False)
>>> parser.feed('&gt;&#62;&#x3E;')
Named ent: >
Num ent  : >
Num ent  : >
```

Feeding incomplete chunks to [`feed()`](#html.parser.HTMLParser.feed "html.parser.HTMLParser.feed") works, but
[`handle_data()`](#html.parser.HTMLParser.handle_data "html.parser.HTMLParser.handle_data") might be called more than once
if *convert\_charrefs* is false:

```
>>> for chunk in ['<sp', 'an>buff', 'ered', ' text</s', 'pan>']:
...     parser.feed(chunk)
...
Start tag: span
Data     : buff
Data     : ered
Data     :  text
End tag  : span
```

Parsing invalid HTML (e.g. unquoted attributes) also works:

```
>>> parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
Start tag: p
Start tag: a
     attr: ('class', 'link')
     attr: ('href', '#main')
Data     : tag soup
End tag  : p
End tag  : a
```

### [Table of Contents](../contents.html)

* [`html.parser` — Simple HTML and XHTML parser](#)
  + [Example HTML Parser Application](#example-html-parser-application)
  + [`HTMLParser` Methods](#htmlparser-methods)
  + [Examples](#examples)

#### Previous topic

[`html` — HyperText Markup Language support](html.html "previous chapter")

#### Next topic

[`html.entities` — Definitions of HTML general entities](html.entities.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/html.parser.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](html.entities.html "html.entities — Definitions of HTML general entities") |
* [previous](html.html "html — HyperText Markup Language support") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `html.parser` — Simple HTML and XHTML parser
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