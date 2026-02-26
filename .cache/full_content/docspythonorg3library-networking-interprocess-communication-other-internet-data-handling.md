### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](email.html "email — An email and MIME handling package") |
* [previous](mmap.html "mmap — Memory-mapped file support") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Internet Data Handling
* |
* Theme
  Auto
  Light
  Dark
   |

# Internet Data Handling[¶](#internet-data-handling "Link to this heading")

This chapter describes modules which support handling data formats commonly used
on the internet.

* [`email` — An email and MIME handling package](email.html)
  + [`email.message`: Representing an email message](email.message.html)
  + [`email.parser`: Parsing email messages](email.parser.html)
    - [FeedParser API](email.parser.html#feedparser-api)
    - [Parser API](email.parser.html#parser-api)
    - [Additional notes](email.parser.html#additional-notes)
  + [`email.generator`: Generating MIME documents](email.generator.html)
  + [`email.policy`: Policy Objects](email.policy.html)
  + [`email.errors`: Exception and Defect classes](email.errors.html)
  + [`email.headerregistry`: Custom Header Objects](email.headerregistry.html)
  + [`email.contentmanager`: Managing MIME Content](email.contentmanager.html)
    - [Content Manager Instances](email.contentmanager.html#content-manager-instances)
  + [`email`: Examples](email.examples.html)
  + [`email.message.Message`: Representing an email message using the `compat32` API](email.compat32-message.html)
  + [`email.mime`: Creating email and MIME objects from scratch](email.mime.html)
  + [`email.header`: Internationalized headers](email.header.html)
  + [`email.charset`: Representing character sets](email.charset.html)
  + [`email.encoders`: Encoders](email.encoders.html)
  + [`email.utils`: Miscellaneous utilities](email.utils.html)
  + [`email.iterators`: Iterators](email.iterators.html)
* [`json` — JSON encoder and decoder](json.html)
  + [Basic Usage](json.html#basic-usage)
  + [Encoders and Decoders](json.html#encoders-and-decoders)
  + [Exceptions](json.html#exceptions)
  + [Standard Compliance and Interoperability](json.html#standard-compliance-and-interoperability)
    - [Character Encodings](json.html#character-encodings)
    - [Infinite and NaN Number Values](json.html#infinite-and-nan-number-values)
    - [Repeated Names Within an Object](json.html#repeated-names-within-an-object)
    - [Top-level Non-Object, Non-Array Values](json.html#top-level-non-object-non-array-values)
    - [Implementation Limitations](json.html#implementation-limitations)
  + [Command-line interface](json.html#module-json.tool)
    - [Command-line options](json.html#command-line-options)
* [`mailbox` — Manipulate mailboxes in various formats](mailbox.html)
  + [`Mailbox` objects](mailbox.html#mailbox-objects)
    - [`Maildir` objects](mailbox.html#maildir-objects)
    - [`mbox` objects](mailbox.html#mbox-objects)
    - [`MH` objects](mailbox.html#mh-objects)
    - [`Babyl` objects](mailbox.html#babyl-objects)
    - [`MMDF` objects](mailbox.html#mmdf-objects)
  + [`Message` objects](mailbox.html#message-objects)
    - [`MaildirMessage` objects](mailbox.html#maildirmessage-objects)
    - [`mboxMessage` objects](mailbox.html#mboxmessage-objects)
    - [`MHMessage` objects](mailbox.html#mhmessage-objects)
    - [`BabylMessage` objects](mailbox.html#babylmessage-objects)
    - [`MMDFMessage` objects](mailbox.html#mmdfmessage-objects)
  + [Exceptions](mailbox.html#exceptions)
  + [Examples](mailbox.html#examples)
* [`mimetypes` — Map filenames to MIME types](mimetypes.html)
  + [MimeTypes objects](mimetypes.html#mimetypes-objects)
  + [Command-line usage](mimetypes.html#command-line-usage)
  + [Command-line example](mimetypes.html#command-line-example)
* [`base64` — Base16, Base32, Base64, Base85 Data Encodings](base64.html)
  + [RFC 4648 Encodings](base64.html#rfc-4648-encodings)
  + [Base85 Encodings](base64.html#base85-encodings)
  + [Legacy Interface](base64.html#legacy-interface)
  + [Security Considerations](base64.html#security-considerations)
* [`binascii` — Convert between binary and ASCII](binascii.html)
* [`quopri` — Encode and decode MIME quoted-printable data](quopri.html)

#### Previous topic

[`mmap` — Memory-mapped file support](mmap.html "previous chapter")

#### Next topic

[`email` — An email and MIME handling package](email.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/netdata.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](email.html "email — An email and MIME handling package") |
* [previous](mmap.html "mmap — Memory-mapped file support") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Internet Data Handling
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