### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.sax.html "xml.sax — Support for SAX2 parsers") |
* [previous](xml.dom.minidom.html "xml.dom.minidom — Minimal DOM implementation") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.dom.pulldom` — Support for building partial DOM trees
* |
* Theme
  Auto
  Light
  Dark
   |

# `xml.dom.pulldom` — Support for building partial DOM trees[¶](#module-xml.dom.pulldom "Link to this heading")

**Source code:** [Lib/xml/dom/pulldom.py](https://github.com/python/cpython/tree/3.14/Lib/xml/dom/pulldom.py)

---

The `xml.dom.pulldom` module provides a “pull parser” which can also be
asked to produce DOM-accessible fragments of the document where necessary. The
basic concept involves pulling “events” from a stream of incoming XML and
processing them. In contrast to SAX which also employs an event-driven
processing model together with callbacks, the user of a pull parser is
responsible for explicitly pulling events from the stream, looping over those
events until either processing is finished or an error condition occurs.

Note

If you need to parse untrusted or unauthenticated data, see
[XML security](xml.html#xml-security).

Changed in version 3.7.1: The SAX parser no longer processes general external entities by default to
increase security by default. To enable processing of external entities,
pass a custom parser instance in:

```
from xml.dom.pulldom import parse
from xml.sax import make_parser
from xml.sax.handler import feature_external_ges

parser = make_parser()
parser.setFeature(feature_external_ges, True)
parse(filename, parser=parser)
```

Example:

```
from xml.dom import pulldom

doc = pulldom.parse('sales_items.xml')
for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'item':
        if int(node.getAttribute('price')) > 50:
            doc.expandNode(node)
            print(node.toxml())
```

`event` is a constant and can be one of:

* `START_ELEMENT`
* `END_ELEMENT`
* `COMMENT`
* `START_DOCUMENT`
* `END_DOCUMENT`
* `CHARACTERS`
* `PROCESSING_INSTRUCTION`
* `IGNORABLE_WHITESPACE`

`node` is an object of type `xml.dom.minidom.Document`,
`xml.dom.minidom.Element` or `xml.dom.minidom.Text`.

Since the document is treated as a “flat” stream of events, the document “tree”
is implicitly traversed and the desired elements are found regardless of their
depth in the tree. In other words, one does not need to consider hierarchical
issues such as recursive searching of the document nodes, although if the
context of elements were important, one would either need to maintain some
context-related state (i.e. remembering where one is in the document at any
given point) or to make use of the [`DOMEventStream.expandNode()`](#xml.dom.pulldom.DOMEventStream.expandNode "xml.dom.pulldom.DOMEventStream.expandNode") method
and switch to DOM-related processing.

*class* xml.dom.pulldom.PullDOM(*documentFactory=None*)[¶](#xml.dom.pulldom.PullDOM "Link to this definition")
:   Subclass of [`xml.sax.handler.ContentHandler`](xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler").

*class* xml.dom.pulldom.SAX2DOM(*documentFactory=None*)[¶](#xml.dom.pulldom.SAX2DOM "Link to this definition")
:   Subclass of [`xml.sax.handler.ContentHandler`](xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler").

xml.dom.pulldom.parse(*stream\_or\_string*, *parser=None*, *bufsize=None*)[¶](#xml.dom.pulldom.parse "Link to this definition")
:   Return a [`DOMEventStream`](#xml.dom.pulldom.DOMEventStream "xml.dom.pulldom.DOMEventStream") from the given input. *stream\_or\_string* may be
    either a file name, or a file-like object. *parser*, if given, must be an
    [`XMLReader`](xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") object. This function will change the
    document handler of the
    parser and activate namespace support; other parser configuration (like
    setting an entity resolver) must have been done in advance.

If you have XML in a string, you can use the [`parseString()`](#xml.dom.pulldom.parseString "xml.dom.pulldom.parseString") function instead:

xml.dom.pulldom.parseString(*string*, *parser=None*)[¶](#xml.dom.pulldom.parseString "Link to this definition")
:   Return a [`DOMEventStream`](#xml.dom.pulldom.DOMEventStream "xml.dom.pulldom.DOMEventStream") that represents the (Unicode) *string*.

xml.dom.pulldom.default\_bufsize[¶](#xml.dom.pulldom.default_bufsize "Link to this definition")
:   Default value for the *bufsize* parameter to [`parse()`](#xml.dom.pulldom.parse "xml.dom.pulldom.parse").

    The value of this variable can be changed before calling [`parse()`](#xml.dom.pulldom.parse "xml.dom.pulldom.parse") and
    the new value will take effect.

## DOMEventStream Objects[¶](#domeventstream-objects "Link to this heading")

*class* xml.dom.pulldom.DOMEventStream(*stream*, *parser*, *bufsize*)[¶](#xml.dom.pulldom.DOMEventStream "Link to this definition")
:   Changed in version 3.11: Support for [`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__") method has been removed.

    getEvent()[¶](#xml.dom.pulldom.DOMEventStream.getEvent "Link to this definition")
    :   Return a tuple containing *event* and the current *node* as
        `xml.dom.minidom.Document` if event equals `START_DOCUMENT`,
        `xml.dom.minidom.Element` if event equals `START_ELEMENT` or
        `END_ELEMENT` or `xml.dom.minidom.Text` if event equals
        `CHARACTERS`.
        The current node does not contain information about its children, unless
        [`expandNode()`](#xml.dom.pulldom.DOMEventStream.expandNode "xml.dom.pulldom.DOMEventStream.expandNode") is called.

    expandNode(*node*)[¶](#xml.dom.pulldom.DOMEventStream.expandNode "Link to this definition")
    :   Expands all children of *node* into *node*. Example:

        ```
        from xml.dom import pulldom

        xml = '<html><title>Foo</title> <p>Some text <div>and more</div></p> </html>'
        doc = pulldom.parseString(xml)
        for event, node in doc:
            if event == pulldom.START_ELEMENT and node.tagName == 'p':
                # Following statement only prints '<p/>'
                print(node.toxml())
                doc.expandNode(node)
                # Following statement prints node with all its children '<p>Some text <div>and more</div></p>'
                print(node.toxml())
        ```

    reset()[¶](#xml.dom.pulldom.DOMEventStream.reset "Link to this definition")

### [Table of Contents](../contents.html)

* [`xml.dom.pulldom` — Support for building partial DOM trees](#)
  + [DOMEventStream Objects](#domeventstream-objects)

#### Previous topic

[`xml.dom.minidom` — Minimal DOM implementation](xml.dom.minidom.html "previous chapter")

#### Next topic

[`xml.sax` — Support for SAX2 parsers](xml.sax.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/xml.dom.pulldom.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.sax.html "xml.sax — Support for SAX2 parsers") |
* [previous](xml.dom.minidom.html "xml.dom.minidom — Minimal DOM implementation") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.dom.pulldom` — Support for building partial DOM trees
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