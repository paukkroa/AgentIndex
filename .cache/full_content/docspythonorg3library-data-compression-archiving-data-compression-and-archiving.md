### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](compression.html "The compression package") |
* [previous](sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Data Compression and Archiving
* |
* Theme
  Auto
  Light
  Dark
   |

# Data Compression and Archiving[¶](#data-compression-and-archiving "Link to this heading")

The modules described in this chapter support data compression with the zlib,
gzip, bzip2, lzma, and zstd algorithms, and the creation of ZIP- and tar-format
archives. See also [Archiving operations](shutil.html#archiving-operations) provided by the [`shutil`](shutil.html#module-shutil "shutil: High-level file operations, including copying.")
module.

* [The `compression` package](compression.html)
* [`compression.zstd` — Compression compatible with the Zstandard format](compression.zstd.html)
  + [Exceptions](compression.zstd.html#exceptions)
  + [Reading and writing compressed files](compression.zstd.html#reading-and-writing-compressed-files)
  + [Compressing and decompressing data in memory](compression.zstd.html#compressing-and-decompressing-data-in-memory)
  + [Zstandard dictionaries](compression.zstd.html#zstandard-dictionaries)
  + [Advanced parameter control](compression.zstd.html#advanced-parameter-control)
  + [Miscellaneous](compression.zstd.html#miscellaneous)
  + [Examples](compression.zstd.html#examples)
* [`zlib` — Compression compatible with **gzip**](zlib.html)
* [`gzip` — Support for **gzip** files](gzip.html)
  + [Examples of usage](gzip.html#examples-of-usage)
  + [Command-line interface](gzip.html#command-line-interface)
    - [Command-line options](gzip.html#command-line-options)
* [`bz2` — Support for **bzip2** compression](bz2.html)
  + [(De)compression of files](bz2.html#de-compression-of-files)
  + [Incremental (de)compression](bz2.html#incremental-de-compression)
  + [One-shot (de)compression](bz2.html#one-shot-de-compression)
  + [Examples of usage](bz2.html#examples-of-usage)
* [`lzma` — Compression using the LZMA algorithm](lzma.html)
  + [Reading and writing compressed files](lzma.html#reading-and-writing-compressed-files)
  + [Compressing and decompressing data in memory](lzma.html#compressing-and-decompressing-data-in-memory)
  + [Miscellaneous](lzma.html#miscellaneous)
  + [Specifying custom filter chains](lzma.html#specifying-custom-filter-chains)
  + [Examples](lzma.html#examples)
* [`zipfile` — Work with ZIP archives](zipfile.html)
  + [ZipFile objects](zipfile.html#zipfile-objects)
  + [Path objects](zipfile.html#path-objects)
  + [PyZipFile objects](zipfile.html#pyzipfile-objects)
  + [ZipInfo objects](zipfile.html#zipinfo-objects)
  + [Command-line interface](zipfile.html#command-line-interface)
    - [Command-line options](zipfile.html#command-line-options)
  + [Decompression pitfalls](zipfile.html#decompression-pitfalls)
    - [From file itself](zipfile.html#from-file-itself)
    - [File system limitations](zipfile.html#file-system-limitations)
    - [Resources limitations](zipfile.html#resources-limitations)
    - [Interruption](zipfile.html#interruption)
    - [Default behaviors of extraction](zipfile.html#default-behaviors-of-extraction)
* [`tarfile` — Read and write tar archive files](tarfile.html)
  + [TarFile Objects](tarfile.html#tarfile-objects)
  + [TarInfo Objects](tarfile.html#tarinfo-objects)
  + [Extraction filters](tarfile.html#extraction-filters)
    - [Default named filters](tarfile.html#default-named-filters)
    - [Filter errors](tarfile.html#filter-errors)
    - [Hints for further verification](tarfile.html#hints-for-further-verification)
    - [Supporting older Python versions](tarfile.html#supporting-older-python-versions)
    - [Stateful extraction filter example](tarfile.html#stateful-extraction-filter-example)
  + [Command-Line Interface](tarfile.html#command-line-interface)
    - [Command-line options](tarfile.html#command-line-options)
  + [Examples](tarfile.html#examples)
    - [Reading examples](tarfile.html#reading-examples)
    - [Writing examples](tarfile.html#writing-examples)
  + [Supported tar formats](tarfile.html#supported-tar-formats)
  + [Unicode issues](tarfile.html#unicode-issues)

#### Previous topic

[`sqlite3` — DB-API 2.0 interface for SQLite databases](sqlite3.html "previous chapter")

#### Next topic

[The `compression` package](compression.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/archiving.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](compression.html "The compression package") |
* [previous](sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Data Compression and Archiving
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