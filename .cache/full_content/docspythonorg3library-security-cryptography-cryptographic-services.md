### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](hashlib.html "hashlib — Secure hashes and message digests") |
* [previous](plistlib.html "plistlib — Generate and parse Apple .plist files") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Cryptographic Services
* |
* Theme
  Auto
  Light
  Dark
   |

# Cryptographic Services[¶](#cryptographic-services "Link to this heading")

The modules described in this chapter implement various algorithms of a
cryptographic nature. They are available at the discretion of the installation.
Here’s an overview:

* [`hashlib` — Secure hashes and message digests](hashlib.html)
  + [Hash algorithms](hashlib.html#hash-algorithms)
  + [Usage](hashlib.html#usage)
  + [Constructors](hashlib.html#constructors)
  + [Attributes](hashlib.html#attributes)
  + [Hash Objects](hashlib.html#hash-objects)
  + [SHAKE variable length digests](hashlib.html#shake-variable-length-digests)
  + [File hashing](hashlib.html#file-hashing)
  + [Key derivation](hashlib.html#key-derivation)
  + [BLAKE2](hashlib.html#blake2)
    - [Creating hash objects](hashlib.html#creating-hash-objects)
    - [Constants](hashlib.html#constants)
    - [Examples](hashlib.html#examples)
      * [Simple hashing](hashlib.html#simple-hashing)
      * [Using different digest sizes](hashlib.html#using-different-digest-sizes)
      * [Keyed hashing](hashlib.html#keyed-hashing)
      * [Randomized hashing](hashlib.html#randomized-hashing)
      * [Personalization](hashlib.html#personalization)
      * [Tree mode](hashlib.html#tree-mode)
    - [Credits](hashlib.html#credits)
* [`hmac` — Keyed-Hashing for Message Authentication](hmac.html)
* [`secrets` — Generate secure random numbers for managing secrets](secrets.html)
  + [Random numbers](secrets.html#random-numbers)
  + [Generating tokens](secrets.html#generating-tokens)
    - [How many bytes should tokens use?](secrets.html#how-many-bytes-should-tokens-use)
  + [Other functions](secrets.html#other-functions)
  + [Recipes and best practices](secrets.html#recipes-and-best-practices)

#### Previous topic

[`plistlib` — Generate and parse Apple `.plist` files](plistlib.html "previous chapter")

#### Next topic

[`hashlib` — Secure hashes and message digests](hashlib.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/crypto.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](hashlib.html "hashlib — Secure hashes and message digests") |
* [previous](plistlib.html "plistlib — Generate and parse Apple .plist files") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Cryptographic Services
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