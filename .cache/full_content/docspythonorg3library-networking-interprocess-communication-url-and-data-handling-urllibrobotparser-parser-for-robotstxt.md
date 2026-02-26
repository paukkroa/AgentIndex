### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](http.html "http — HTTP modules") |
* [previous](urllib.error.html "urllib.error — Exception classes raised by urllib.request") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `urllib.robotparser` — Parser for robots.txt
* |
* Theme
  Auto
  Light
  Dark
   |

# `urllib.robotparser` — Parser for robots.txt[¶](#module-urllib.robotparser "Link to this heading")

**Source code:** [Lib/urllib/robotparser.py](https://github.com/python/cpython/tree/3.14/Lib/urllib/robotparser.py)

---

This module provides a single class, [`RobotFileParser`](#urllib.robotparser.RobotFileParser "urllib.robotparser.RobotFileParser"), which answers
questions about whether or not a particular user agent can fetch a URL on the
website that published the `robots.txt` file. For more details on the
structure of `robots.txt` files, see <http://www.robotstxt.org/orig.html>.

*class* urllib.robotparser.RobotFileParser(*url=''*)[¶](#urllib.robotparser.RobotFileParser "Link to this definition")
:   This class provides methods to read, parse and answer questions about the
    `robots.txt` file at *url*.

    set\_url(*url*)[¶](#urllib.robotparser.RobotFileParser.set_url "Link to this definition")
    :   Sets the URL referring to a `robots.txt` file.

    read()[¶](#urllib.robotparser.RobotFileParser.read "Link to this definition")
    :   Reads the `robots.txt` URL and feeds it to the parser.

    parse(*lines*)[¶](#urllib.robotparser.RobotFileParser.parse "Link to this definition")
    :   Parses the lines argument.

    can\_fetch(*useragent*, *url*)[¶](#urllib.robotparser.RobotFileParser.can_fetch "Link to this definition")
    :   Returns `True` if the *useragent* is allowed to fetch the *url*
        according to the rules contained in the parsed `robots.txt`
        file.

    mtime()[¶](#urllib.robotparser.RobotFileParser.mtime "Link to this definition")
    :   Returns the time the `robots.txt` file was last fetched. This is
        useful for long-running web spiders that need to check for new
        `robots.txt` files periodically.

    modified()[¶](#urllib.robotparser.RobotFileParser.modified "Link to this definition")
    :   Sets the time the `robots.txt` file was last fetched to the current
        time.

    crawl\_delay(*useragent*)[¶](#urllib.robotparser.RobotFileParser.crawl_delay "Link to this definition")
    :   Returns the value of the `Crawl-delay` parameter from `robots.txt`
        for the *useragent* in question. If there is no such parameter or it
        doesn’t apply to the *useragent* specified or the `robots.txt` entry
        for this parameter has invalid syntax, return `None`.

        Added in version 3.6.

    request\_rate(*useragent*)[¶](#urllib.robotparser.RobotFileParser.request_rate "Link to this definition")
    :   Returns the contents of the `Request-rate` parameter from
        `robots.txt` as a [named tuple](../glossary.html#term-named-tuple) `RequestRate(requests, seconds)`.
        If there is no such parameter or it doesn’t apply to the *useragent*
        specified or the `robots.txt` entry for this parameter has invalid
        syntax, return `None`.

        Added in version 3.6.

    site\_maps()[¶](#urllib.robotparser.RobotFileParser.site_maps "Link to this definition")
    :   Returns the contents of the `Sitemap` parameter from
        `robots.txt` in the form of a [`list()`](stdtypes.html#list "list"). If there is no such
        parameter or the `robots.txt` entry for this parameter has
        invalid syntax, return `None`.

        Added in version 3.8.

The following example demonstrates basic use of the [`RobotFileParser`](#urllib.robotparser.RobotFileParser "urllib.robotparser.RobotFileParser")
class:

```
>>> import urllib.robotparser
>>> rp = urllib.robotparser.RobotFileParser()
>>> rp.set_url("http://www.pythontest.net/robots.txt")
>>> rp.read()
>>> rrate = rp.request_rate("*")
>>> rrate.requests
1
>>> rrate.seconds
1
>>> rp.crawl_delay("*")
6
>>> rp.can_fetch("*", "http://www.pythontest.net/")
True
>>> rp.can_fetch("*", "http://www.pythontest.net/no-robots-here/")
False
```

#### Previous topic

[`urllib.error` — Exception classes raised by urllib.request](urllib.error.html "previous chapter")

#### Next topic

[`http` — HTTP modules](http.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/urllib.robotparser.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](http.html "http — HTTP modules") |
* [previous](urllib.error.html "urllib.error — Exception classes raised by urllib.request") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `urllib.robotparser` — Parser for robots.txt
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