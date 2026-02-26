### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](os.html "os — Miscellaneous operating system interfaces") |
* [previous](secrets.html "secrets — Generate secure random numbers for managing secrets") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Generic Operating System Services
* |
* Theme
  Auto
  Light
  Dark
   |

# Generic Operating System Services[¶](#generic-operating-system-services "Link to this heading")

The modules described in this chapter provide interfaces to operating system
features that are available on (almost) all operating systems, such as files and
a clock. The interfaces are generally modeled after the Unix or C interfaces,
but they are available on most other systems as well. Here’s an overview:

* [`os` — Miscellaneous operating system interfaces](os.html)
  + [File Names, Command Line Arguments, and Environment Variables](os.html#file-names-command-line-arguments-and-environment-variables)
  + [Python UTF-8 Mode](os.html#python-utf-8-mode)
  + [Process Parameters](os.html#process-parameters)
  + [File Object Creation](os.html#file-object-creation)
  + [File Descriptor Operations](os.html#file-descriptor-operations)
    - [Querying the size of a terminal](os.html#querying-the-size-of-a-terminal)
    - [Inheritance of File Descriptors](os.html#inheritance-of-file-descriptors)
  + [Files and Directories](os.html#files-and-directories)
    - [Timer File Descriptors](os.html#timer-file-descriptors)
    - [Linux extended attributes](os.html#linux-extended-attributes)
  + [Process Management](os.html#process-management)
  + [Interface to the scheduler](os.html#interface-to-the-scheduler)
  + [Miscellaneous System Information](os.html#miscellaneous-system-information)
  + [Random numbers](os.html#random-numbers)
* [`io` — Core tools for working with streams](io.html)
  + [Overview](io.html#overview)
    - [Text I/O](io.html#text-i-o)
    - [Binary I/O](io.html#binary-i-o)
    - [Raw I/O](io.html#raw-i-o)
  + [Text Encoding](io.html#text-encoding)
    - [Opt-in EncodingWarning](io.html#opt-in-encodingwarning)
  + [High-level Module Interface](io.html#high-level-module-interface)
  + [Class hierarchy](io.html#class-hierarchy)
    - [I/O Base Classes](io.html#i-o-base-classes)
    - [Raw File I/O](io.html#raw-file-i-o)
    - [Buffered Streams](io.html#buffered-streams)
    - [Text I/O](io.html#id1)
  + [Static Typing](io.html#static-typing)
  + [Performance](io.html#performance)
    - [Binary I/O](io.html#id2)
    - [Text I/O](io.html#id3)
    - [Multi-threading](io.html#multi-threading)
    - [Reentrancy](io.html#reentrancy)
* [`time` — Time access and conversions](time.html)
  + [Functions](time.html#functions)
  + [Clock ID Constants](time.html#clock-id-constants)
  + [Timezone Constants](time.html#timezone-constants)
* [`logging` — Logging facility for Python](logging.html)
  + [Logger Objects](logging.html#logger-objects)
  + [Logging Levels](logging.html#logging-levels)
  + [Handler Objects](logging.html#handler-objects)
  + [Formatter Objects](logging.html#formatter-objects)
  + [Filter Objects](logging.html#filter-objects)
  + [LogRecord Objects](logging.html#logrecord-objects)
  + [LogRecord attributes](logging.html#logrecord-attributes)
  + [LoggerAdapter Objects](logging.html#loggeradapter-objects)
  + [Thread Safety](logging.html#thread-safety)
  + [Module-Level Functions](logging.html#module-level-functions)
  + [Module-Level Attributes](logging.html#module-level-attributes)
  + [Integration with the warnings module](logging.html#integration-with-the-warnings-module)
* [`logging.config` — Logging configuration](logging.config.html)
  + [Configuration functions](logging.config.html#configuration-functions)
  + [Security considerations](logging.config.html#security-considerations)
  + [Configuration dictionary schema](logging.config.html#configuration-dictionary-schema)
    - [Dictionary Schema Details](logging.config.html#dictionary-schema-details)
    - [Incremental Configuration](logging.config.html#incremental-configuration)
    - [Object connections](logging.config.html#object-connections)
    - [User-defined objects](logging.config.html#user-defined-objects)
    - [Handler configuration order](logging.config.html#handler-configuration-order)
    - [Access to external objects](logging.config.html#access-to-external-objects)
    - [Access to internal objects](logging.config.html#access-to-internal-objects)
    - [Import resolution and custom importers](logging.config.html#import-resolution-and-custom-importers)
    - [Configuring QueueHandler and QueueListener](logging.config.html#configuring-queuehandler-and-queuelistener)
  + [Configuration file format](logging.config.html#configuration-file-format)
* [`logging.handlers` — Logging handlers](logging.handlers.html)
  + [StreamHandler](logging.handlers.html#streamhandler)
  + [FileHandler](logging.handlers.html#filehandler)
  + [NullHandler](logging.handlers.html#nullhandler)
  + [WatchedFileHandler](logging.handlers.html#watchedfilehandler)
  + [BaseRotatingHandler](logging.handlers.html#baserotatinghandler)
  + [RotatingFileHandler](logging.handlers.html#rotatingfilehandler)
  + [TimedRotatingFileHandler](logging.handlers.html#timedrotatingfilehandler)
  + [SocketHandler](logging.handlers.html#sockethandler)
  + [DatagramHandler](logging.handlers.html#datagramhandler)
  + [SysLogHandler](logging.handlers.html#sysloghandler)
  + [NTEventLogHandler](logging.handlers.html#nteventloghandler)
  + [SMTPHandler](logging.handlers.html#smtphandler)
  + [MemoryHandler](logging.handlers.html#memoryhandler)
  + [HTTPHandler](logging.handlers.html#httphandler)
  + [QueueHandler](logging.handlers.html#queuehandler)
  + [QueueListener](logging.handlers.html#queuelistener)
* [`platform` — Access to underlying platform’s identifying data](platform.html)
  + [Cross platform](platform.html#cross-platform)
  + [Java platform](platform.html#java-platform)
  + [Windows platform](platform.html#windows-platform)
  + [macOS platform](platform.html#macos-platform)
  + [iOS platform](platform.html#ios-platform)
  + [Unix platforms](platform.html#unix-platforms)
  + [Linux platforms](platform.html#linux-platforms)
  + [Android platform](platform.html#android-platform)
  + [Command-line usage](platform.html#command-line-usage)
* [`errno` — Standard errno system symbols](errno.html)
* [`ctypes` — A foreign function library for Python](ctypes.html)
  + [ctypes tutorial](ctypes.html#ctypes-tutorial)
    - [Loading dynamic link libraries](ctypes.html#loading-dynamic-link-libraries)
    - [Accessing functions from loaded dlls](ctypes.html#accessing-functions-from-loaded-dlls)
    - [Calling functions](ctypes.html#calling-functions)
    - [Fundamental data types](ctypes.html#fundamental-data-types)
    - [Calling functions, continued](ctypes.html#calling-functions-continued)
    - [Calling variadic functions](ctypes.html#calling-variadic-functions)
    - [Calling functions with your own custom data types](ctypes.html#calling-functions-with-your-own-custom-data-types)
    - [Specifying the required argument types (function prototypes)](ctypes.html#specifying-the-required-argument-types-function-prototypes)
    - [Return types](ctypes.html#return-types)
    - [Passing pointers (or: passing parameters by reference)](ctypes.html#passing-pointers-or-passing-parameters-by-reference)
    - [Structures and unions](ctypes.html#structures-and-unions)
    - [Structure/union layout, alignment and byte order](ctypes.html#structure-union-layout-alignment-and-byte-order)
    - [Bit fields in structures and unions](ctypes.html#bit-fields-in-structures-and-unions)
    - [Arrays](ctypes.html#arrays)
    - [Pointers](ctypes.html#pointers)
    - [Thread safety without the GIL](ctypes.html#thread-safety-without-the-gil)
    - [Type conversions](ctypes.html#type-conversions)
    - [Incomplete Types](ctypes.html#incomplete-types)
    - [Callback functions](ctypes.html#callback-functions)
    - [Accessing values exported from dlls](ctypes.html#accessing-values-exported-from-dlls)
    - [Surprises](ctypes.html#surprises)
    - [Variable-sized data types](ctypes.html#variable-sized-data-types)
  + [ctypes reference](ctypes.html#ctypes-reference)
    - [Finding shared libraries](ctypes.html#finding-shared-libraries)
    - [Listing loaded shared libraries](ctypes.html#listing-loaded-shared-libraries)
    - [Loading shared libraries](ctypes.html#loading-shared-libraries)
    - [Foreign functions](ctypes.html#foreign-functions)
    - [Function prototypes](ctypes.html#function-prototypes)
    - [Utility functions](ctypes.html#utility-functions)
    - [Data types](ctypes.html#data-types)
    - [Fundamental data types](ctypes.html#ctypes-fundamental-data-types-2)
    - [Structured data types](ctypes.html#structured-data-types)
    - [Arrays and pointers](ctypes.html#arrays-and-pointers)
    - [Exceptions](ctypes.html#exceptions)

#### Previous topic

[`secrets` — Generate secure random numbers for managing secrets](secrets.html "previous chapter")

#### Next topic

[`os` — Miscellaneous operating system interfaces](os.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/allos.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](os.html "os — Miscellaneous operating system interfaces") |
* [previous](secrets.html "secrets — Generate secure random numbers for managing secrets") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Generic Operating System Services
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