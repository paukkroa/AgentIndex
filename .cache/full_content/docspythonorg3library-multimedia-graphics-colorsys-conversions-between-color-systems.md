### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](i18n.html "Internationalization") |
* [previous](wave.html "wave — Read and write WAV files") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Multimedia Services](mm.html) »
* `colorsys` — Conversions between color systems
* |
* Theme
  Auto
  Light
  Dark
   |

# `colorsys` — Conversions between color systems[¶](#module-colorsys "Link to this heading")

**Source code:** [Lib/colorsys.py](https://github.com/python/cpython/tree/3.14/Lib/colorsys.py)

---

The `colorsys` module defines bidirectional conversions of color values
between colors expressed in the RGB (Red Green Blue) color space used in
computer monitors and three other coordinate systems: YIQ, HLS (Hue Lightness
Saturation) and HSV (Hue Saturation Value). Coordinates in all of these color
spaces are floating-point values. In the YIQ space, the Y coordinate is between
0 and 1, but the I and Q coordinates can be positive or negative. In all other
spaces, the coordinates are all between 0 and 1.

See also

More information about color spaces can be found at
<https://poynton.ca/ColorFAQ.html> and
<https://www.cambridgeincolour.com/tutorials/color-spaces.htm>.

The `colorsys` module defines the following functions:

colorsys.rgb\_to\_yiq(*r*, *g*, *b*)[¶](#colorsys.rgb_to_yiq "Link to this definition")
:   Convert the color from RGB coordinates to YIQ coordinates.

colorsys.yiq\_to\_rgb(*y*, *i*, *q*)[¶](#colorsys.yiq_to_rgb "Link to this definition")
:   Convert the color from YIQ coordinates to RGB coordinates.

colorsys.rgb\_to\_hls(*r*, *g*, *b*)[¶](#colorsys.rgb_to_hls "Link to this definition")
:   Convert the color from RGB coordinates to HLS coordinates.

colorsys.hls\_to\_rgb(*h*, *l*, *s*)[¶](#colorsys.hls_to_rgb "Link to this definition")
:   Convert the color from HLS coordinates to RGB coordinates.

colorsys.rgb\_to\_hsv(*r*, *g*, *b*)[¶](#colorsys.rgb_to_hsv "Link to this definition")
:   Convert the color from RGB coordinates to HSV coordinates.

colorsys.hsv\_to\_rgb(*h*, *s*, *v*)[¶](#colorsys.hsv_to_rgb "Link to this definition")
:   Convert the color from HSV coordinates to RGB coordinates.

Example:

```
>>> import colorsys
>>> colorsys.rgb_to_hsv(0.2, 0.4, 0.4)
(0.5, 0.5, 0.4)
>>> colorsys.hsv_to_rgb(0.5, 0.5, 0.4)
(0.2, 0.4, 0.4)
```

#### Previous topic

[`wave` — Read and write WAV files](wave.html "previous chapter")

#### Next topic

[Internationalization](i18n.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/colorsys.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](i18n.html "Internationalization") |
* [previous](wave.html "wave — Read and write WAV files") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Multimedia Services](mm.html) »
* `colorsys` — Conversions between color systems
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