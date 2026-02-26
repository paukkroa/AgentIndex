### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](gettext.html "gettext — Multilingual internationalization services") |
* [previous](colorsys.html "colorsys — Conversions between color systems") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Internationalization
* |
* Theme
  Auto
  Light
  Dark
   |

# Internationalization[¶](#internationalization "Link to this heading")

The modules described in this chapter help you write software that is
independent of language and locale by providing mechanisms for selecting a
language to be used in program messages or by tailoring output to match local
conventions.

The list of modules described in this chapter is:

* [`gettext` — Multilingual internationalization services](gettext.html)
  + [GNU **gettext** API](gettext.html#gnu-gettext-api)
  + [Class-based API](gettext.html#class-based-api)
    - [The `NullTranslations` class](gettext.html#the-nulltranslations-class)
    - [The `GNUTranslations` class](gettext.html#the-gnutranslations-class)
    - [Solaris message catalog support](gettext.html#solaris-message-catalog-support)
    - [The Catalog constructor](gettext.html#the-catalog-constructor)
  + [Internationalizing your programs and modules](gettext.html#internationalizing-your-programs-and-modules)
    - [Localizing your module](gettext.html#localizing-your-module)
    - [Localizing your application](gettext.html#localizing-your-application)
    - [Changing languages on the fly](gettext.html#changing-languages-on-the-fly)
    - [Deferred translations](gettext.html#deferred-translations)
  + [Acknowledgements](gettext.html#acknowledgements)
* [`locale` — Internationalization services](locale.html)
  + [Background, details, hints, tips and caveats](locale.html#background-details-hints-tips-and-caveats)
  + [Locale names](locale.html#locale-names)
  + [For extension writers and programs that embed Python](locale.html#for-extension-writers-and-programs-that-embed-python)
  + [Access to message catalogs](locale.html#access-to-message-catalogs)

#### Previous topic

[`colorsys` — Conversions between color systems](colorsys.html "previous chapter")

#### Next topic

[`gettext` — Multilingual internationalization services](gettext.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/i18n.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](gettext.html "gettext — Multilingual internationalization services") |
* [previous](colorsys.html "colorsys — Conversions between color systems") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Internationalization
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