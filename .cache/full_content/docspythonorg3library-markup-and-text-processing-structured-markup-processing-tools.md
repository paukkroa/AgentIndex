### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](html.html "html — HyperText Markup Language support") |
* [previous](quopri.html "quopri — Encode and decode MIME quoted-printable data") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Structured Markup Processing Tools
* |
* Theme
  Auto
  Light
  Dark
   |

# Structured Markup Processing Tools[¶](#structured-markup-processing-tools "Link to this heading")

Python supports a variety of modules to work with various forms of structured
data markup. This includes modules to work with the Standard Generalized Markup
Language (SGML) and the Hypertext Markup Language (HTML), and several interfaces
for working with the Extensible Markup Language (XML).

* [`html` — HyperText Markup Language support](html.html)
* [`html.parser` — Simple HTML and XHTML parser](html.parser.html)
  + [Example HTML Parser Application](html.parser.html#example-html-parser-application)
  + [`HTMLParser` Methods](html.parser.html#htmlparser-methods)
  + [Examples](html.parser.html#examples)
* [`html.entities` — Definitions of HTML general entities](html.entities.html)
* [XML Processing Modules](xml.html)
  + [XML security](xml.html#xml-vulnerabilities)
* [`xml.etree.ElementTree` — The ElementTree XML API](xml.etree.elementtree.html)
  + [Tutorial](xml.etree.elementtree.html#tutorial)
    - [XML tree and elements](xml.etree.elementtree.html#xml-tree-and-elements)
    - [Parsing XML](xml.etree.elementtree.html#parsing-xml)
    - [Pull API for non-blocking parsing](xml.etree.elementtree.html#pull-api-for-non-blocking-parsing)
    - [Finding interesting elements](xml.etree.elementtree.html#finding-interesting-elements)
    - [Modifying an XML File](xml.etree.elementtree.html#modifying-an-xml-file)
    - [Building XML documents](xml.etree.elementtree.html#building-xml-documents)
    - [Parsing XML with Namespaces](xml.etree.elementtree.html#parsing-xml-with-namespaces)
  + [XPath support](xml.etree.elementtree.html#xpath-support)
    - [Example](xml.etree.elementtree.html#example)
    - [Supported XPath syntax](xml.etree.elementtree.html#supported-xpath-syntax)
  + [Reference](xml.etree.elementtree.html#reference)
    - [Functions](xml.etree.elementtree.html#functions)
  + [XInclude support](xml.etree.elementtree.html#xinclude-support)
    - [Example](xml.etree.elementtree.html#id3)
  + [Reference](xml.etree.elementtree.html#id4)
    - [Functions](xml.etree.elementtree.html#elementinclude-functions)
    - [Element Objects](xml.etree.elementtree.html#element-objects)
    - [ElementTree Objects](xml.etree.elementtree.html#elementtree-objects)
    - [QName Objects](xml.etree.elementtree.html#qname-objects)
    - [TreeBuilder Objects](xml.etree.elementtree.html#treebuilder-objects)
    - [XMLParser Objects](xml.etree.elementtree.html#xmlparser-objects)
    - [XMLPullParser Objects](xml.etree.elementtree.html#xmlpullparser-objects)
    - [Exceptions](xml.etree.elementtree.html#exceptions)
* [`xml.dom` — The Document Object Model API](xml.dom.html)
  + [Module Contents](xml.dom.html#module-contents)
  + [Objects in the DOM](xml.dom.html#objects-in-the-dom)
    - [DOMImplementation Objects](xml.dom.html#domimplementation-objects)
    - [Node Objects](xml.dom.html#node-objects)
    - [NodeList Objects](xml.dom.html#nodelist-objects)
    - [DocumentType Objects](xml.dom.html#documenttype-objects)
    - [Document Objects](xml.dom.html#document-objects)
    - [Element Objects](xml.dom.html#element-objects)
    - [Attr Objects](xml.dom.html#attr-objects)
    - [NamedNodeMap Objects](xml.dom.html#namednodemap-objects)
    - [Comment Objects](xml.dom.html#comment-objects)
    - [Text and CDATASection Objects](xml.dom.html#text-and-cdatasection-objects)
    - [ProcessingInstruction Objects](xml.dom.html#processinginstruction-objects)
    - [Exceptions](xml.dom.html#exceptions)
  + [Conformance](xml.dom.html#conformance)
    - [Type Mapping](xml.dom.html#type-mapping)
    - [Accessor Methods](xml.dom.html#accessor-methods)
* [`xml.dom.minidom` — Minimal DOM implementation](xml.dom.minidom.html)
  + [DOM Objects](xml.dom.minidom.html#dom-objects)
  + [DOM Example](xml.dom.minidom.html#dom-example)
  + [minidom and the DOM standard](xml.dom.minidom.html#minidom-and-the-dom-standard)
* [`xml.dom.pulldom` — Support for building partial DOM trees](xml.dom.pulldom.html)
  + [DOMEventStream Objects](xml.dom.pulldom.html#domeventstream-objects)
* [`xml.sax` — Support for SAX2 parsers](xml.sax.html)
  + [SAXException Objects](xml.sax.html#saxexception-objects)
* [`xml.sax.handler` — Base classes for SAX handlers](xml.sax.handler.html)
  + [ContentHandler Objects](xml.sax.handler.html#contenthandler-objects)
  + [DTDHandler Objects](xml.sax.handler.html#dtdhandler-objects)
  + [EntityResolver Objects](xml.sax.handler.html#entityresolver-objects)
  + [ErrorHandler Objects](xml.sax.handler.html#errorhandler-objects)
  + [LexicalHandler Objects](xml.sax.handler.html#lexicalhandler-objects)
* [`xml.sax.saxutils` — SAX Utilities](xml.sax.utils.html)
* [`xml.sax.xmlreader` — Interface for XML parsers](xml.sax.reader.html)
  + [XMLReader Objects](xml.sax.reader.html#xmlreader-objects)
  + [IncrementalParser Objects](xml.sax.reader.html#incrementalparser-objects)
  + [Locator Objects](xml.sax.reader.html#locator-objects)
  + [InputSource Objects](xml.sax.reader.html#inputsource-objects)
  + [The `Attributes` Interface](xml.sax.reader.html#the-attributes-interface)
  + [The `AttributesNS` Interface](xml.sax.reader.html#the-attributesns-interface)
* [`xml.parsers.expat` — Fast XML parsing using Expat](pyexpat.html)
  + [XMLParser Objects](pyexpat.html#xmlparser-objects)
  + [ExpatError Exceptions](pyexpat.html#expaterror-exceptions)
  + [Example](pyexpat.html#example)
  + [Content Model Descriptions](pyexpat.html#module-xml.parsers.expat.model)
  + [Expat error constants](pyexpat.html#module-xml.parsers.expat.errors)

#### Previous topic

[`quopri` — Encode and decode MIME quoted-printable data](quopri.html "previous chapter")

#### Next topic

[`html` — HyperText Markup Language support](html.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/markup.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](html.html "html — HyperText Markup Language support") |
* [previous](quopri.html "quopri — Encode and decode MIME quoted-printable data") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Structured Markup Processing Tools
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