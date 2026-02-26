### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](colorsys.html "colorsys — Conversions between color systems") |
* [previous](mm.html "Multimedia Services") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Multimedia Services](mm.html) »
* `wave` — Read and write WAV files
* |
* Theme
  Auto
  Light
  Dark
   |

# `wave` — Read and write WAV files[¶](#module-wave "Link to this heading")

**Source code:** [Lib/wave.py](https://github.com/python/cpython/tree/3.14/Lib/wave.py)

---

The `wave` module provides a convenient interface to the Waveform Audio
“WAVE” (or “WAV”) file format. Only uncompressed PCM encoded wave files are
supported.

Changed in version 3.12: Support for `WAVE_FORMAT_EXTENSIBLE` headers was added, provided that the
extended format is `KSDATAFORMAT_SUBTYPE_PCM`.

The `wave` module defines the following function and exception:

wave.open(*file*, *mode=None*)[¶](#wave.open "Link to this definition")
:   If *file* is a string, open the file by that name, otherwise treat it as a
    file-like object. *mode* can be:

    `'rb'`
    :   Read only mode.

    `'wb'`
    :   Write only mode.

    Note that it does not allow read/write WAV files.

    A *mode* of `'rb'` returns a [`Wave_read`](#wave.Wave_read "wave.Wave_read") object, while a *mode* of
    `'wb'` returns a [`Wave_write`](#wave.Wave_write "wave.Wave_write") object. If *mode* is omitted and a
    file-like object is passed as *file*, `file.mode` is used as the default
    value for *mode*.

    If you pass in a file-like object, the wave object will not close it when its
    `close()` method is called; it is the caller’s responsibility to close
    the file object.

    The [`open()`](#wave.open "wave.open") function may be used in a [`with`](../reference/compound_stmts.html#with) statement. When
    the `with` block completes, the [`Wave_read.close()`](#wave.Wave_read.close "wave.Wave_read.close") or
    [`Wave_write.close()`](#wave.Wave_write.close "wave.Wave_write.close") method is called.

    Changed in version 3.4: Added support for unseekable files.

*exception* wave.Error[¶](#wave.Error "Link to this definition")
:   An error raised when something is impossible because it violates the WAV
    specification or hits an implementation deficiency.

## Wave\_read Objects[¶](#wave-read-objects "Link to this heading")

*class* wave.Wave\_read[¶](#wave.Wave_read "Link to this definition")
:   Read a WAV file.

    Wave\_read objects, as returned by [`open()`](#wave.open "wave.open"), have the following methods:

    close()[¶](#wave.Wave_read.close "Link to this definition")
    :   Close the stream if it was opened by `wave`, and make the instance
        unusable. This is called automatically on object collection.

    getnchannels()[¶](#wave.Wave_read.getnchannels "Link to this definition")
    :   Returns number of audio channels (`1` for mono, `2` for stereo).

    getsampwidth()[¶](#wave.Wave_read.getsampwidth "Link to this definition")
    :   Returns sample width in bytes.

    getframerate()[¶](#wave.Wave_read.getframerate "Link to this definition")
    :   Returns sampling frequency.

    getnframes()[¶](#wave.Wave_read.getnframes "Link to this definition")
    :   Returns number of audio frames.

    getcomptype()[¶](#wave.Wave_read.getcomptype "Link to this definition")
    :   Returns compression type (`'NONE'` is the only supported type).

    getcompname()[¶](#wave.Wave_read.getcompname "Link to this definition")
    :   Human-readable version of [`getcomptype()`](#wave.Wave_read.getcomptype "wave.Wave_read.getcomptype"). Usually `'not compressed'`
        parallels `'NONE'`.

    getparams()[¶](#wave.Wave_read.getparams "Link to this definition")
    :   Returns a [`namedtuple()`](collections.html#collections.namedtuple "collections.namedtuple") `(nchannels, sampwidth,
        framerate, nframes, comptype, compname)`, equivalent to output of the
        `get*()` methods.

    readframes(*n*)[¶](#wave.Wave_read.readframes "Link to this definition")
    :   Reads and returns at most *n* frames of audio, as a [`bytes`](stdtypes.html#bytes "bytes") object.

    rewind()[¶](#wave.Wave_read.rewind "Link to this definition")
    :   Rewind the file pointer to the beginning of the audio stream.

    The following two methods are defined for compatibility with the old `aifc`
    module, and don’t do anything interesting.

    getmarkers()[¶](#wave.Wave_read.getmarkers "Link to this definition")
    :   Returns `None`.

        Deprecated since version 3.13, will be removed in version 3.15: The method only existed for compatibility with the `aifc` module
        which has been removed in Python 3.13.

    getmark(*id*)[¶](#wave.Wave_read.getmark "Link to this definition")
    :   Raise an error.

        Deprecated since version 3.13, will be removed in version 3.15: The method only existed for compatibility with the `aifc` module
        which has been removed in Python 3.13.

    The following two methods define a term “position” which is compatible between
    them, and is otherwise implementation dependent.

    setpos(*pos*)[¶](#wave.Wave_read.setpos "Link to this definition")
    :   Set the file pointer to the specified position.

    tell()[¶](#wave.Wave_read.tell "Link to this definition")
    :   Return current file pointer position.

## Wave\_write Objects[¶](#wave-write-objects "Link to this heading")

*class* wave.Wave\_write[¶](#wave.Wave_write "Link to this definition")
:   Write a WAV file.

    Wave\_write objects, as returned by [`open()`](#wave.open "wave.open").

    For seekable output streams, the `wave` header will automatically be updated
    to reflect the number of frames actually written. For unseekable streams, the
    *nframes* value must be accurate when the first frame data is written. An
    accurate *nframes* value can be achieved either by calling
    [`setnframes()`](#wave.Wave_write.setnframes "wave.Wave_write.setnframes") or [`setparams()`](#wave.Wave_write.setparams "wave.Wave_write.setparams") with the number
    of frames that will be written before [`close()`](#wave.Wave_write.close "wave.Wave_write.close") is called and
    then using [`writeframesraw()`](#wave.Wave_write.writeframesraw "wave.Wave_write.writeframesraw") to write the frame data, or by
    calling [`writeframes()`](#wave.Wave_write.writeframes "wave.Wave_write.writeframes") with all of the frame data to be
    written. In the latter case [`writeframes()`](#wave.Wave_write.writeframes "wave.Wave_write.writeframes") will calculate
    the number of frames in the data and set *nframes* accordingly before writing
    the frame data.

    Changed in version 3.4: Added support for unseekable files.

    Wave\_write objects have the following methods:

    close()[¶](#wave.Wave_write.close "Link to this definition")
    :   Make sure *nframes* is correct, and close the file if it was opened by
        `wave`. This method is called upon object collection. It will raise
        an exception if the output stream is not seekable and *nframes* does not
        match the number of frames actually written.

    setnchannels(*n*)[¶](#wave.Wave_write.setnchannels "Link to this definition")
    :   Set the number of channels.

    setsampwidth(*n*)[¶](#wave.Wave_write.setsampwidth "Link to this definition")
    :   Set the sample width to *n* bytes.

    setframerate(*n*)[¶](#wave.Wave_write.setframerate "Link to this definition")
    :   Set the frame rate to *n*.

        Changed in version 3.2: A non-integral input to this method is rounded to the nearest
        integer.

    setnframes(*n*)[¶](#wave.Wave_write.setnframes "Link to this definition")
    :   Set the number of frames to *n*. This will be changed later if the number
        of frames actually written is different (this update attempt will
        raise an error if the output stream is not seekable).

    setcomptype(*type*, *name*)[¶](#wave.Wave_write.setcomptype "Link to this definition")
    :   Set the compression type and description. At the moment, only compression type
        `NONE` is supported, meaning no compression.

    setparams(*tuple*)[¶](#wave.Wave_write.setparams "Link to this definition")
    :   The *tuple* should be `(nchannels, sampwidth, framerate, nframes, comptype,
        compname)`, with values valid for the `set*()` methods. Sets all
        parameters.

    tell()[¶](#wave.Wave_write.tell "Link to this definition")
    :   Return current position in the file, with the same disclaimer for the
        [`Wave_read.tell()`](#wave.Wave_read.tell "wave.Wave_read.tell") and [`Wave_read.setpos()`](#wave.Wave_read.setpos "wave.Wave_read.setpos") methods.

    writeframesraw(*data*)[¶](#wave.Wave_write.writeframesraw "Link to this definition")
    :   Write audio frames, without correcting *nframes*.

        Changed in version 3.4: Any [bytes-like object](../glossary.html#term-bytes-like-object) is now accepted.

    writeframes(*data*)[¶](#wave.Wave_write.writeframes "Link to this definition")
    :   Write audio frames and make sure *nframes* is correct. It will raise an
        error if the output stream is not seekable and the total number of frames
        that have been written after *data* has been written does not match the
        previously set value for *nframes*.

        Changed in version 3.4: Any [bytes-like object](../glossary.html#term-bytes-like-object) is now accepted.

        Note that it is invalid to set any parameters after calling [`writeframes()`](#wave.Wave_write.writeframes "wave.Wave_write.writeframes")
        or [`writeframesraw()`](#wave.Wave_write.writeframesraw "wave.Wave_write.writeframesraw"), and any attempt to do so will raise
        [`wave.Error`](#wave.Error "wave.Error").

### [Table of Contents](../contents.html)

* [`wave` — Read and write WAV files](#)
  + [Wave\_read Objects](#wave-read-objects)
  + [Wave\_write Objects](#wave-write-objects)

#### Previous topic

[Multimedia Services](mm.html "previous chapter")

#### Next topic

[`colorsys` — Conversions between color systems](colorsys.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/wave.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](colorsys.html "colorsys — Conversions between color systems") |
* [previous](mm.html "Multimedia Services") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Multimedia Services](mm.html) »
* `wave` — Read and write WAV files
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