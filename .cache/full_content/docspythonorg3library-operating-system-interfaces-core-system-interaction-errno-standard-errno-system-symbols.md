### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](ctypes.html "ctypes — A foreign function library for Python") |
* [previous](platform.html "platform — Access to underlying platform’s identifying data") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Generic Operating System Services](allos.html) »
* `errno` — Standard errno system symbols
* |
* Theme
  Auto
  Light
  Dark
   |

# `errno` — Standard errno system symbols[¶](#module-errno "Link to this heading")

---

This module makes available standard `errno` system symbols. The value of each
symbol is the corresponding integer value. The names and descriptions are
borrowed from `linux/include/errno.h`, which should be
all-inclusive.

errno.errorcode[¶](#errno.errorcode "Link to this definition")
:   Dictionary providing a mapping from the errno value to the string name in the
    underlying system. For instance, `errno.errorcode[errno.EPERM]` maps to
    `'EPERM'`.

To translate a numeric error code to an error message, use [`os.strerror()`](os.html#os.strerror "os.strerror").

Of the following list, symbols that are not used on the current platform are not
defined by the module. The specific list of defined symbols is available as
`errno.errorcode.keys()`. Symbols available can include:

errno.EPERM[¶](#errno.EPERM "Link to this definition")
:   Operation not permitted. This error is mapped to the exception
    [`PermissionError`](exceptions.html#PermissionError "PermissionError").

errno.ENOENT[¶](#errno.ENOENT "Link to this definition")
:   No such file or directory. This error is mapped to the exception
    [`FileNotFoundError`](exceptions.html#FileNotFoundError "FileNotFoundError").

errno.ESRCH[¶](#errno.ESRCH "Link to this definition")
:   No such process. This error is mapped to the exception
    [`ProcessLookupError`](exceptions.html#ProcessLookupError "ProcessLookupError").

errno.EINTR[¶](#errno.EINTR "Link to this definition")
:   Interrupted system call. This error is mapped to the exception
    [`InterruptedError`](exceptions.html#InterruptedError "InterruptedError").

errno.EIO[¶](#errno.EIO "Link to this definition")
:   I/O error

errno.ENXIO[¶](#errno.ENXIO "Link to this definition")
:   No such device or address

errno.E2BIG[¶](#errno.E2BIG "Link to this definition")
:   Arg list too long

errno.ENOEXEC[¶](#errno.ENOEXEC "Link to this definition")
:   Exec format error

errno.EBADF[¶](#errno.EBADF "Link to this definition")
:   Bad file number

errno.ECHILD[¶](#errno.ECHILD "Link to this definition")
:   No child processes. This error is mapped to the exception
    [`ChildProcessError`](exceptions.html#ChildProcessError "ChildProcessError").

errno.EAGAIN[¶](#errno.EAGAIN "Link to this definition")
:   Try again. This error is mapped to the exception [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError").

errno.ENOMEM[¶](#errno.ENOMEM "Link to this definition")
:   Out of memory

errno.EACCES[¶](#errno.EACCES "Link to this definition")
:   Permission denied. This error is mapped to the exception
    [`PermissionError`](exceptions.html#PermissionError "PermissionError").

errno.EFAULT[¶](#errno.EFAULT "Link to this definition")
:   Bad address

errno.ENOTBLK[¶](#errno.ENOTBLK "Link to this definition")
:   Block device required

errno.EBUSY[¶](#errno.EBUSY "Link to this definition")
:   Device or resource busy

errno.EEXIST[¶](#errno.EEXIST "Link to this definition")
:   File exists. This error is mapped to the exception
    [`FileExistsError`](exceptions.html#FileExistsError "FileExistsError").

errno.EXDEV[¶](#errno.EXDEV "Link to this definition")
:   Cross-device link

errno.ENODEV[¶](#errno.ENODEV "Link to this definition")
:   No such device

errno.ENOTDIR[¶](#errno.ENOTDIR "Link to this definition")
:   Not a directory. This error is mapped to the exception
    [`NotADirectoryError`](exceptions.html#NotADirectoryError "NotADirectoryError").

errno.EISDIR[¶](#errno.EISDIR "Link to this definition")
:   Is a directory. This error is mapped to the exception
    [`IsADirectoryError`](exceptions.html#IsADirectoryError "IsADirectoryError").

errno.EINVAL[¶](#errno.EINVAL "Link to this definition")
:   Invalid argument

errno.ENFILE[¶](#errno.ENFILE "Link to this definition")
:   File table overflow

errno.EMFILE[¶](#errno.EMFILE "Link to this definition")
:   Too many open files

errno.ENOTTY[¶](#errno.ENOTTY "Link to this definition")
:   Not a typewriter

errno.ETXTBSY[¶](#errno.ETXTBSY "Link to this definition")
:   Text file busy

errno.EFBIG[¶](#errno.EFBIG "Link to this definition")
:   File too large

errno.ENOSPC[¶](#errno.ENOSPC "Link to this definition")
:   No space left on device

errno.ESPIPE[¶](#errno.ESPIPE "Link to this definition")
:   Illegal seek

errno.EROFS[¶](#errno.EROFS "Link to this definition")
:   Read-only file system

errno.EMLINK[¶](#errno.EMLINK "Link to this definition")
:   Too many links

errno.EPIPE[¶](#errno.EPIPE "Link to this definition")
:   Broken pipe. This error is mapped to the exception
    [`BrokenPipeError`](exceptions.html#BrokenPipeError "BrokenPipeError").

errno.EDOM[¶](#errno.EDOM "Link to this definition")
:   Math argument out of domain of func

errno.ERANGE[¶](#errno.ERANGE "Link to this definition")
:   Math result not representable

errno.EDEADLK[¶](#errno.EDEADLK "Link to this definition")
:   Resource deadlock would occur

errno.ENAMETOOLONG[¶](#errno.ENAMETOOLONG "Link to this definition")
:   File name too long

errno.ENOLCK[¶](#errno.ENOLCK "Link to this definition")
:   No record locks available

errno.ENOSYS[¶](#errno.ENOSYS "Link to this definition")
:   Function not implemented

errno.ENOTEMPTY[¶](#errno.ENOTEMPTY "Link to this definition")
:   Directory not empty

errno.ELOOP[¶](#errno.ELOOP "Link to this definition")
:   Too many symbolic links encountered

errno.EWOULDBLOCK[¶](#errno.EWOULDBLOCK "Link to this definition")
:   Operation would block. This error is mapped to the exception
    [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError").

errno.ENOMSG[¶](#errno.ENOMSG "Link to this definition")
:   No message of desired type

errno.EIDRM[¶](#errno.EIDRM "Link to this definition")
:   Identifier removed

errno.ECHRNG[¶](#errno.ECHRNG "Link to this definition")
:   Channel number out of range

errno.EL2NSYNC[¶](#errno.EL2NSYNC "Link to this definition")
:   Level 2 not synchronized

errno.EL3HLT[¶](#errno.EL3HLT "Link to this definition")
:   Level 3 halted

errno.EL3RST[¶](#errno.EL3RST "Link to this definition")
:   Level 3 reset

errno.ELNRNG[¶](#errno.ELNRNG "Link to this definition")
:   Link number out of range

errno.EUNATCH[¶](#errno.EUNATCH "Link to this definition")
:   Protocol driver not attached

errno.ENOCSI[¶](#errno.ENOCSI "Link to this definition")
:   No CSI structure available

errno.EL2HLT[¶](#errno.EL2HLT "Link to this definition")
:   Level 2 halted

errno.EBADE[¶](#errno.EBADE "Link to this definition")
:   Invalid exchange

errno.EBADR[¶](#errno.EBADR "Link to this definition")
:   Invalid request descriptor

errno.EXFULL[¶](#errno.EXFULL "Link to this definition")
:   Exchange full

errno.ENOANO[¶](#errno.ENOANO "Link to this definition")
:   No anode

errno.EBADRQC[¶](#errno.EBADRQC "Link to this definition")
:   Invalid request code

errno.EBADSLT[¶](#errno.EBADSLT "Link to this definition")
:   Invalid slot

errno.EDEADLOCK[¶](#errno.EDEADLOCK "Link to this definition")
:   File locking deadlock error

errno.EBFONT[¶](#errno.EBFONT "Link to this definition")
:   Bad font file format

errno.ENOSTR[¶](#errno.ENOSTR "Link to this definition")
:   Device not a stream

errno.ENODATA[¶](#errno.ENODATA "Link to this definition")
:   No data available

errno.ETIME[¶](#errno.ETIME "Link to this definition")
:   Timer expired

errno.ENOSR[¶](#errno.ENOSR "Link to this definition")
:   Out of streams resources

errno.ENONET[¶](#errno.ENONET "Link to this definition")
:   Machine is not on the network

errno.ENOPKG[¶](#errno.ENOPKG "Link to this definition")
:   Package not installed

errno.EREMOTE[¶](#errno.EREMOTE "Link to this definition")
:   Object is remote

errno.ENOLINK[¶](#errno.ENOLINK "Link to this definition")
:   Link has been severed

errno.EADV[¶](#errno.EADV "Link to this definition")
:   Advertise error

errno.ESRMNT[¶](#errno.ESRMNT "Link to this definition")
:   Srmount error

errno.ECOMM[¶](#errno.ECOMM "Link to this definition")
:   Communication error on send

errno.EPROTO[¶](#errno.EPROTO "Link to this definition")
:   Protocol error

errno.EMULTIHOP[¶](#errno.EMULTIHOP "Link to this definition")
:   Multihop attempted

errno.EDOTDOT[¶](#errno.EDOTDOT "Link to this definition")
:   RFS specific error

errno.EBADMSG[¶](#errno.EBADMSG "Link to this definition")
:   Not a data message

errno.EOVERFLOW[¶](#errno.EOVERFLOW "Link to this definition")
:   Value too large for defined data type

errno.ENOTUNIQ[¶](#errno.ENOTUNIQ "Link to this definition")
:   Name not unique on network

errno.EBADFD[¶](#errno.EBADFD "Link to this definition")
:   File descriptor in bad state

errno.EREMCHG[¶](#errno.EREMCHG "Link to this definition")
:   Remote address changed

errno.ELIBACC[¶](#errno.ELIBACC "Link to this definition")
:   Can not access a needed shared library

errno.ELIBBAD[¶](#errno.ELIBBAD "Link to this definition")
:   Accessing a corrupted shared library

errno.ELIBSCN[¶](#errno.ELIBSCN "Link to this definition")
:   .lib section in a.out corrupted

errno.ELIBMAX[¶](#errno.ELIBMAX "Link to this definition")
:   Attempting to link in too many shared libraries

errno.ELIBEXEC[¶](#errno.ELIBEXEC "Link to this definition")
:   Cannot exec a shared library directly

errno.EILSEQ[¶](#errno.EILSEQ "Link to this definition")
:   Illegal byte sequence

errno.ERESTART[¶](#errno.ERESTART "Link to this definition")
:   Interrupted system call should be restarted

errno.ESTRPIPE[¶](#errno.ESTRPIPE "Link to this definition")
:   Streams pipe error

errno.EUSERS[¶](#errno.EUSERS "Link to this definition")
:   Too many users

errno.ENOTSOCK[¶](#errno.ENOTSOCK "Link to this definition")
:   Socket operation on non-socket

errno.EDESTADDRREQ[¶](#errno.EDESTADDRREQ "Link to this definition")
:   Destination address required

errno.EMSGSIZE[¶](#errno.EMSGSIZE "Link to this definition")
:   Message too long

errno.EPROTOTYPE[¶](#errno.EPROTOTYPE "Link to this definition")
:   Protocol wrong type for socket

errno.ENOPROTOOPT[¶](#errno.ENOPROTOOPT "Link to this definition")
:   Protocol not available

errno.EPROTONOSUPPORT[¶](#errno.EPROTONOSUPPORT "Link to this definition")
:   Protocol not supported

errno.ESOCKTNOSUPPORT[¶](#errno.ESOCKTNOSUPPORT "Link to this definition")
:   Socket type not supported

errno.EOPNOTSUPP[¶](#errno.EOPNOTSUPP "Link to this definition")
:   Operation not supported on transport endpoint

errno.ENOTSUP[¶](#errno.ENOTSUP "Link to this definition")
:   Operation not supported

    Added in version 3.2.

errno.EPFNOSUPPORT[¶](#errno.EPFNOSUPPORT "Link to this definition")
:   Protocol family not supported

errno.EAFNOSUPPORT[¶](#errno.EAFNOSUPPORT "Link to this definition")
:   Address family not supported by protocol

errno.EADDRINUSE[¶](#errno.EADDRINUSE "Link to this definition")
:   Address already in use

errno.EADDRNOTAVAIL[¶](#errno.EADDRNOTAVAIL "Link to this definition")
:   Cannot assign requested address

errno.ENETDOWN[¶](#errno.ENETDOWN "Link to this definition")
:   Network is down

errno.ENETUNREACH[¶](#errno.ENETUNREACH "Link to this definition")
:   Network is unreachable

errno.ENETRESET[¶](#errno.ENETRESET "Link to this definition")
:   Network dropped connection because of reset

errno.ECONNABORTED[¶](#errno.ECONNABORTED "Link to this definition")
:   Software caused connection abort. This error is mapped to the
    exception [`ConnectionAbortedError`](exceptions.html#ConnectionAbortedError "ConnectionAbortedError").

errno.ECONNRESET[¶](#errno.ECONNRESET "Link to this definition")
:   Connection reset by peer. This error is mapped to the exception
    [`ConnectionResetError`](exceptions.html#ConnectionResetError "ConnectionResetError").

errno.ENOBUFS[¶](#errno.ENOBUFS "Link to this definition")
:   No buffer space available

errno.EISCONN[¶](#errno.EISCONN "Link to this definition")
:   Transport endpoint is already connected

errno.ENOTCONN[¶](#errno.ENOTCONN "Link to this definition")
:   Transport endpoint is not connected

errno.ESHUTDOWN[¶](#errno.ESHUTDOWN "Link to this definition")
:   Cannot send after transport endpoint shutdown. This error is mapped
    to the exception [`BrokenPipeError`](exceptions.html#BrokenPipeError "BrokenPipeError").

errno.ETOOMANYREFS[¶](#errno.ETOOMANYREFS "Link to this definition")
:   Too many references: cannot splice

errno.ETIMEDOUT[¶](#errno.ETIMEDOUT "Link to this definition")
:   Connection timed out. This error is mapped to the exception
    [`TimeoutError`](exceptions.html#TimeoutError "TimeoutError").

errno.ECONNREFUSED[¶](#errno.ECONNREFUSED "Link to this definition")
:   Connection refused. This error is mapped to the exception
    [`ConnectionRefusedError`](exceptions.html#ConnectionRefusedError "ConnectionRefusedError").

errno.EHOSTDOWN[¶](#errno.EHOSTDOWN "Link to this definition")
:   Host is down

errno.EHOSTUNREACH[¶](#errno.EHOSTUNREACH "Link to this definition")
:   No route to host

errno.EHWPOISON[¶](#errno.EHWPOISON "Link to this definition")
:   Memory page has hardware error.

    Added in version 3.14.

errno.EALREADY[¶](#errno.EALREADY "Link to this definition")
:   Operation already in progress. This error is mapped to the
    exception [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError").

errno.EINPROGRESS[¶](#errno.EINPROGRESS "Link to this definition")
:   Operation now in progress. This error is mapped to the exception
    [`BlockingIOError`](exceptions.html#BlockingIOError "BlockingIOError").

errno.ESTALE[¶](#errno.ESTALE "Link to this definition")
:   Stale NFS file handle

errno.EUCLEAN[¶](#errno.EUCLEAN "Link to this definition")
:   Structure needs cleaning

errno.ENOTNAM[¶](#errno.ENOTNAM "Link to this definition")
:   Not a XENIX named type file

errno.ENAVAIL[¶](#errno.ENAVAIL "Link to this definition")
:   No XENIX semaphores available

errno.EISNAM[¶](#errno.EISNAM "Link to this definition")
:   Is a named type file

errno.EREMOTEIO[¶](#errno.EREMOTEIO "Link to this definition")
:   Remote I/O error

errno.EDQUOT[¶](#errno.EDQUOT "Link to this definition")
:   Quota exceeded

errno.EQFULL[¶](#errno.EQFULL "Link to this definition")
:   Interface output queue is full

    Added in version 3.11.

errno.ENOMEDIUM[¶](#errno.ENOMEDIUM "Link to this definition")
:   No medium found

errno.EMEDIUMTYPE[¶](#errno.EMEDIUMTYPE "Link to this definition")
:   Wrong medium type

errno.ENOKEY[¶](#errno.ENOKEY "Link to this definition")
:   Required key not available

errno.EKEYEXPIRED[¶](#errno.EKEYEXPIRED "Link to this definition")
:   Key has expired

errno.EKEYREVOKED[¶](#errno.EKEYREVOKED "Link to this definition")
:   Key has been revoked

errno.EKEYREJECTED[¶](#errno.EKEYREJECTED "Link to this definition")
:   Key was rejected by service

errno.ERFKILL[¶](#errno.ERFKILL "Link to this definition")
:   Operation not possible due to RF-kill

errno.ELOCKUNMAPPED[¶](#errno.ELOCKUNMAPPED "Link to this definition")
:   Locked lock was unmapped

errno.ENOTACTIVE[¶](#errno.ENOTACTIVE "Link to this definition")
:   Facility is not active

errno.EAUTH[¶](#errno.EAUTH "Link to this definition")
:   Authentication error

    Added in version 3.2.

errno.EBADARCH[¶](#errno.EBADARCH "Link to this definition")
:   Bad CPU type in executable

    Added in version 3.2.

errno.EBADEXEC[¶](#errno.EBADEXEC "Link to this definition")
:   Bad executable (or shared library)

    Added in version 3.2.

errno.EBADMACHO[¶](#errno.EBADMACHO "Link to this definition")
:   Malformed Mach-o file

    Added in version 3.2.

errno.EDEVERR[¶](#errno.EDEVERR "Link to this definition")
:   Device error

    Added in version 3.2.

errno.EFTYPE[¶](#errno.EFTYPE "Link to this definition")
:   Inappropriate file type or format

    Added in version 3.2.

errno.ENEEDAUTH[¶](#errno.ENEEDAUTH "Link to this definition")
:   Need authenticator

    Added in version 3.2.

errno.ENOATTR[¶](#errno.ENOATTR "Link to this definition")
:   Attribute not found

    Added in version 3.2.

errno.ENOPOLICY[¶](#errno.ENOPOLICY "Link to this definition")
:   Policy not found

    Added in version 3.2.

errno.EPROCLIM[¶](#errno.EPROCLIM "Link to this definition")
:   Too many processes

    Added in version 3.2.

errno.EPROCUNAVAIL[¶](#errno.EPROCUNAVAIL "Link to this definition")
:   Bad procedure for program

    Added in version 3.2.

errno.EPROGMISMATCH[¶](#errno.EPROGMISMATCH "Link to this definition")
:   Program version wrong

    Added in version 3.2.

errno.EPROGUNAVAIL[¶](#errno.EPROGUNAVAIL "Link to this definition")
:   RPC prog. not avail

    Added in version 3.2.

errno.EPWROFF[¶](#errno.EPWROFF "Link to this definition")
:   Device power is off

    Added in version 3.2.

errno.EBADRPC[¶](#errno.EBADRPC "Link to this definition")
:   RPC struct is bad

    Added in version 3.2.

errno.ERPCMISMATCH[¶](#errno.ERPCMISMATCH "Link to this definition")
:   RPC version wrong

    Added in version 3.2.

errno.ESHLIBVERS[¶](#errno.ESHLIBVERS "Link to this definition")
:   Shared library version mismatch

    Added in version 3.2.

errno.ENOTCAPABLE[¶](#errno.ENOTCAPABLE "Link to this definition")
:   Capabilities insufficient. This error is mapped to the exception
    [`PermissionError`](exceptions.html#PermissionError "PermissionError").

    [Availability](intro.html#availability): WASI, FreeBSD

    Added in version 3.11.1.

errno.ECANCELED[¶](#errno.ECANCELED "Link to this definition")
:   Operation canceled

    Added in version 3.2.

errno.EOWNERDEAD[¶](#errno.EOWNERDEAD "Link to this definition")
:   Owner died

    Added in version 3.2.

errno.ENOTRECOVERABLE[¶](#errno.ENOTRECOVERABLE "Link to this definition")
:   State not recoverable

    Added in version 3.2.

#### Previous topic

[`platform` — Access to underlying platform’s identifying data](platform.html "previous chapter")

#### Next topic

[`ctypes` — A foreign function library for Python](ctypes.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/errno.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](ctypes.html "ctypes — A foreign function library for Python") |
* [previous](platform.html "platform — Access to underlying platform’s identifying data") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Generic Operating System Services](allos.html) »
* `errno` — Standard errno system symbols
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