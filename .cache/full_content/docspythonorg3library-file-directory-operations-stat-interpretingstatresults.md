### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](filecmp.html "filecmp — File and Directory Comparisons") |
* [previous](os.path.html "os.path — Common pathname manipulations") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File and Directory Access](filesys.html) »
* `stat` — Interpreting `stat()` results
* |
* Theme
  Auto
  Light
  Dark
   |

# `stat` — Interpreting [`stat()`](os.html#os.stat "os.stat") results[¶](#module-stat "Link to this heading")

**Source code:** [Lib/stat.py](https://github.com/python/cpython/tree/3.14/Lib/stat.py)

---

The `stat` module defines constants and functions for interpreting the
results of [`os.stat()`](os.html#os.stat "os.stat"), [`os.fstat()`](os.html#os.fstat "os.fstat") and [`os.lstat()`](os.html#os.lstat "os.lstat") (if they
exist). For complete details about the `stat()`, `fstat()` and
`lstat()` calls, consult the documentation for your system.

Changed in version 3.4: The stat module is backed by a C implementation.

The `stat` module defines the following functions to test for specific file
types:

stat.S\_ISDIR(*mode*)[¶](#stat.S_ISDIR "Link to this definition")
:   Return non-zero if the mode is from a directory.

stat.S\_ISCHR(*mode*)[¶](#stat.S_ISCHR "Link to this definition")
:   Return non-zero if the mode is from a character special device file.

stat.S\_ISBLK(*mode*)[¶](#stat.S_ISBLK "Link to this definition")
:   Return non-zero if the mode is from a block special device file.

stat.S\_ISREG(*mode*)[¶](#stat.S_ISREG "Link to this definition")
:   Return non-zero if the mode is from a regular file.

stat.S\_ISFIFO(*mode*)[¶](#stat.S_ISFIFO "Link to this definition")
:   Return non-zero if the mode is from a FIFO (named pipe).

stat.S\_ISLNK(*mode*)[¶](#stat.S_ISLNK "Link to this definition")
:   Return non-zero if the mode is from a symbolic link.

stat.S\_ISSOCK(*mode*)[¶](#stat.S_ISSOCK "Link to this definition")
:   Return non-zero if the mode is from a socket.

stat.S\_ISDOOR(*mode*)[¶](#stat.S_ISDOOR "Link to this definition")
:   Return non-zero if the mode is from a door.

    Added in version 3.4.

stat.S\_ISPORT(*mode*)[¶](#stat.S_ISPORT "Link to this definition")
:   Return non-zero if the mode is from an event port.

    Added in version 3.4.

stat.S\_ISWHT(*mode*)[¶](#stat.S_ISWHT "Link to this definition")
:   Return non-zero if the mode is from a whiteout.

    Added in version 3.4.

Two additional functions are defined for more general manipulation of the file’s
mode:

stat.S\_IMODE(*mode*)[¶](#stat.S_IMODE "Link to this definition")
:   Return the portion of the file’s mode that can be set by
    [`os.chmod()`](os.html#os.chmod "os.chmod")—that is, the file’s permission bits, plus the sticky
    bit, set-group-id, and set-user-id bits (on systems that support them).

stat.S\_IFMT(*mode*)[¶](#stat.S_IFMT "Link to this definition")
:   Return the portion of the file’s mode that describes the file type (used by the
    `S_IS*()` functions above).

Normally, you would use the `os.path.is*()` functions for testing the type
of a file; the functions here are useful when you are doing multiple tests of
the same file and wish to avoid the overhead of the `stat()` system call
for each test. These are also useful when checking for information about a file
that isn’t handled by [`os.path`](os.path.html#module-os.path "os.path: Operations on pathnames."), like the tests for block and character
devices.

Example:

```
import os, sys
from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.lstat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)

if __name__ == '__main__':
    walktree(sys.argv[1], visitfile)
```

An additional utility function is provided to convert a file’s mode in a human
readable string:

stat.filemode(*mode*)[¶](#stat.filemode "Link to this definition")
:   Convert a file’s mode to a string of the form ‘-rwxrwxrwx’.

    Added in version 3.3.

    Changed in version 3.4: The function supports [`S_IFDOOR`](#stat.S_IFDOOR "stat.S_IFDOOR"), [`S_IFPORT`](#stat.S_IFPORT "stat.S_IFPORT") and
    [`S_IFWHT`](#stat.S_IFWHT "stat.S_IFWHT").

All the variables below are simply symbolic indexes into the 10-tuple returned
by [`os.stat()`](os.html#os.stat "os.stat"), [`os.fstat()`](os.html#os.fstat "os.fstat") or [`os.lstat()`](os.html#os.lstat "os.lstat").

stat.ST\_MODE[¶](#stat.ST_MODE "Link to this definition")
:   Inode protection mode.

stat.ST\_INO[¶](#stat.ST_INO "Link to this definition")
:   Inode number.

stat.ST\_DEV[¶](#stat.ST_DEV "Link to this definition")
:   Device inode resides on.

stat.ST\_NLINK[¶](#stat.ST_NLINK "Link to this definition")
:   Number of links to the inode.

stat.ST\_UID[¶](#stat.ST_UID "Link to this definition")
:   User id of the owner.

stat.ST\_GID[¶](#stat.ST_GID "Link to this definition")
:   Group id of the owner.

stat.ST\_SIZE[¶](#stat.ST_SIZE "Link to this definition")
:   Size in bytes of a plain file; amount of data waiting on some special files.

stat.ST\_ATIME[¶](#stat.ST_ATIME "Link to this definition")
:   Time of last access.

stat.ST\_MTIME[¶](#stat.ST_MTIME "Link to this definition")
:   Time of last modification.

stat.ST\_CTIME[¶](#stat.ST_CTIME "Link to this definition")
:   The “ctime” as reported by the operating system. On some systems (like Unix) is
    the time of the last metadata change, and, on others (like Windows), is the
    creation time (see platform documentation for details).

The interpretation of “file size” changes according to the file type. For plain
files this is the size of the file in bytes. For FIFOs and sockets under most
flavors of Unix (including Linux in particular), the “size” is the number of
bytes waiting to be read at the time of the call to [`os.stat()`](os.html#os.stat "os.stat"),
[`os.fstat()`](os.html#os.fstat "os.fstat"), or [`os.lstat()`](os.html#os.lstat "os.lstat"); this can sometimes be useful, especially
for polling one of these special files after a non-blocking open. The meaning
of the size field for other character and block devices varies more, depending
on the implementation of the underlying system call.

The variables below define the flags used in the [`ST_MODE`](#stat.ST_MODE "stat.ST_MODE") field.

Use of the functions above is more portable than use of the first set of flags:

stat.S\_IFSOCK[¶](#stat.S_IFSOCK "Link to this definition")
:   Socket.

stat.S\_IFLNK[¶](#stat.S_IFLNK "Link to this definition")
:   Symbolic link.

stat.S\_IFREG[¶](#stat.S_IFREG "Link to this definition")
:   Regular file.

stat.S\_IFBLK[¶](#stat.S_IFBLK "Link to this definition")
:   Block device.

stat.S\_IFDIR[¶](#stat.S_IFDIR "Link to this definition")
:   Directory.

stat.S\_IFCHR[¶](#stat.S_IFCHR "Link to this definition")
:   Character device.

stat.S\_IFIFO[¶](#stat.S_IFIFO "Link to this definition")
:   FIFO.

stat.S\_IFDOOR[¶](#stat.S_IFDOOR "Link to this definition")
:   Door.

    Added in version 3.4.

stat.S\_IFPORT[¶](#stat.S_IFPORT "Link to this definition")
:   Event port.

    Added in version 3.4.

stat.S\_IFWHT[¶](#stat.S_IFWHT "Link to this definition")
:   Whiteout.

    Added in version 3.4.

Note

[`S_IFDOOR`](#stat.S_IFDOOR "stat.S_IFDOOR"), [`S_IFPORT`](#stat.S_IFPORT "stat.S_IFPORT") or [`S_IFWHT`](#stat.S_IFWHT "stat.S_IFWHT") are defined as
0 when the platform does not have support for the file types.

The following flags can also be used in the *mode* argument of [`os.chmod()`](os.html#os.chmod "os.chmod"):

stat.S\_ISUID[¶](#stat.S_ISUID "Link to this definition")
:   Set UID bit.

stat.S\_ISGID[¶](#stat.S_ISGID "Link to this definition")
:   Set-group-ID bit. This bit has several special uses. For a directory
    it indicates that BSD semantics is to be used for that directory:
    files created there inherit their group ID from the directory, not
    from the effective group ID of the creating process, and directories
    created there will also get the [`S_ISGID`](#stat.S_ISGID "stat.S_ISGID") bit set. For a
    file that does not have the group execution bit ([`S_IXGRP`](#stat.S_IXGRP "stat.S_IXGRP"))
    set, the set-group-ID bit indicates mandatory file/record locking
    (see also [`S_ENFMT`](#stat.S_ENFMT "stat.S_ENFMT")).

stat.S\_ISVTX[¶](#stat.S_ISVTX "Link to this definition")
:   Sticky bit. When this bit is set on a directory it means that a file
    in that directory can be renamed or deleted only by the owner of the
    file, by the owner of the directory, or by a privileged process.

stat.S\_IRWXU[¶](#stat.S_IRWXU "Link to this definition")
:   Mask for file owner permissions.

stat.S\_IRUSR[¶](#stat.S_IRUSR "Link to this definition")
:   Owner has read permission.

stat.S\_IWUSR[¶](#stat.S_IWUSR "Link to this definition")
:   Owner has write permission.

stat.S\_IXUSR[¶](#stat.S_IXUSR "Link to this definition")
:   Owner has execute permission.

stat.S\_IRWXG[¶](#stat.S_IRWXG "Link to this definition")
:   Mask for group permissions.

stat.S\_IRGRP[¶](#stat.S_IRGRP "Link to this definition")
:   Group has read permission.

stat.S\_IWGRP[¶](#stat.S_IWGRP "Link to this definition")
:   Group has write permission.

stat.S\_IXGRP[¶](#stat.S_IXGRP "Link to this definition")
:   Group has execute permission.

stat.S\_IRWXO[¶](#stat.S_IRWXO "Link to this definition")
:   Mask for permissions for others (not in group).

stat.S\_IROTH[¶](#stat.S_IROTH "Link to this definition")
:   Others have read permission.

stat.S\_IWOTH[¶](#stat.S_IWOTH "Link to this definition")
:   Others have write permission.

stat.S\_IXOTH[¶](#stat.S_IXOTH "Link to this definition")
:   Others have execute permission.

stat.S\_ENFMT[¶](#stat.S_ENFMT "Link to this definition")
:   System V file locking enforcement. This flag is shared with [`S_ISGID`](#stat.S_ISGID "stat.S_ISGID"):
    file/record locking is enforced on files that do not have the group
    execution bit ([`S_IXGRP`](#stat.S_IXGRP "stat.S_IXGRP")) set.

stat.S\_IREAD[¶](#stat.S_IREAD "Link to this definition")
:   Unix V7 synonym for [`S_IRUSR`](#stat.S_IRUSR "stat.S_IRUSR").

stat.S\_IWRITE[¶](#stat.S_IWRITE "Link to this definition")
:   Unix V7 synonym for [`S_IWUSR`](#stat.S_IWUSR "stat.S_IWUSR").

stat.S\_IEXEC[¶](#stat.S_IEXEC "Link to this definition")
:   Unix V7 synonym for [`S_IXUSR`](#stat.S_IXUSR "stat.S_IXUSR").

The following flags can be used in the *flags* argument of [`os.chflags()`](os.html#os.chflags "os.chflags"):

stat.UF\_SETTABLE[¶](#stat.UF_SETTABLE "Link to this definition")
:   All user settable flags.

    Added in version 3.13.

stat.UF\_NODUMP[¶](#stat.UF_NODUMP "Link to this definition")
:   Do not dump the file.

stat.UF\_IMMUTABLE[¶](#stat.UF_IMMUTABLE "Link to this definition")
:   The file may not be changed.

stat.UF\_APPEND[¶](#stat.UF_APPEND "Link to this definition")
:   The file may only be appended to.

stat.UF\_OPAQUE[¶](#stat.UF_OPAQUE "Link to this definition")
:   The directory is opaque when viewed through a union stack.

stat.UF\_NOUNLINK[¶](#stat.UF_NOUNLINK "Link to this definition")
:   The file may not be renamed or deleted.

stat.UF\_COMPRESSED[¶](#stat.UF_COMPRESSED "Link to this definition")
:   The file is stored compressed (macOS 10.6+).

stat.UF\_TRACKED[¶](#stat.UF_TRACKED "Link to this definition")
:   Used for handling document IDs (macOS)

    Added in version 3.13.

stat.UF\_DATAVAULT[¶](#stat.UF_DATAVAULT "Link to this definition")
:   The file needs an entitlement for reading or writing (macOS 10.13+)

    Added in version 3.13.

stat.UF\_HIDDEN[¶](#stat.UF_HIDDEN "Link to this definition")
:   The file should not be displayed in a GUI (macOS 10.5+).

stat.SF\_SETTABLE[¶](#stat.SF_SETTABLE "Link to this definition")
:   All super-user changeable flags

    Added in version 3.13.

stat.SF\_SUPPORTED[¶](#stat.SF_SUPPORTED "Link to this definition")
:   All super-user supported flags

    [Availability](intro.html#availability): macOS

    Added in version 3.13.

stat.SF\_SYNTHETIC[¶](#stat.SF_SYNTHETIC "Link to this definition")
:   All super-user read-only synthetic flags

    [Availability](intro.html#availability): macOS

    Added in version 3.13.

stat.SF\_ARCHIVED[¶](#stat.SF_ARCHIVED "Link to this definition")
:   The file may be archived.

stat.SF\_IMMUTABLE[¶](#stat.SF_IMMUTABLE "Link to this definition")
:   The file may not be changed.

stat.SF\_APPEND[¶](#stat.SF_APPEND "Link to this definition")
:   The file may only be appended to.

stat.SF\_RESTRICTED[¶](#stat.SF_RESTRICTED "Link to this definition")
:   The file needs an entitlement to write to (macOS 10.13+)

    Added in version 3.13.

stat.SF\_NOUNLINK[¶](#stat.SF_NOUNLINK "Link to this definition")
:   The file may not be renamed or deleted.

stat.SF\_SNAPSHOT[¶](#stat.SF_SNAPSHOT "Link to this definition")
:   The file is a snapshot file.

stat.SF\_FIRMLINK[¶](#stat.SF_FIRMLINK "Link to this definition")
:   The file is a firmlink (macOS 10.15+)

    Added in version 3.13.

stat.SF\_DATALESS[¶](#stat.SF_DATALESS "Link to this definition")
:   The file is a dataless object (macOS 10.15+)

    Added in version 3.13.

See the \*BSD or macOS systems man page *[chflags(2)](https://manpages.debian.org/chflags(2))* for more information.

On Windows, the following file attribute constants are available for use when
testing bits in the `st_file_attributes` member returned by [`os.stat()`](os.html#os.stat "os.stat").
See the [Windows API documentation](https://msdn.microsoft.com/en-us/library/windows/desktop/gg258117.aspx)
for more detail on the meaning of these constants.

stat.FILE\_ATTRIBUTE\_ARCHIVE[¶](#stat.FILE_ATTRIBUTE_ARCHIVE "Link to this definition")

stat.FILE\_ATTRIBUTE\_COMPRESSED[¶](#stat.FILE_ATTRIBUTE_COMPRESSED "Link to this definition")

stat.FILE\_ATTRIBUTE\_DEVICE[¶](#stat.FILE_ATTRIBUTE_DEVICE "Link to this definition")

stat.FILE\_ATTRIBUTE\_DIRECTORY[¶](#stat.FILE_ATTRIBUTE_DIRECTORY "Link to this definition")

stat.FILE\_ATTRIBUTE\_ENCRYPTED[¶](#stat.FILE_ATTRIBUTE_ENCRYPTED "Link to this definition")

stat.FILE\_ATTRIBUTE\_HIDDEN[¶](#stat.FILE_ATTRIBUTE_HIDDEN "Link to this definition")

stat.FILE\_ATTRIBUTE\_INTEGRITY\_STREAM[¶](#stat.FILE_ATTRIBUTE_INTEGRITY_STREAM "Link to this definition")

stat.FILE\_ATTRIBUTE\_NORMAL[¶](#stat.FILE_ATTRIBUTE_NORMAL "Link to this definition")

stat.FILE\_ATTRIBUTE\_NOT\_CONTENT\_INDEXED[¶](#stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED "Link to this definition")

stat.FILE\_ATTRIBUTE\_NO\_SCRUB\_DATA[¶](#stat.FILE_ATTRIBUTE_NO_SCRUB_DATA "Link to this definition")

stat.FILE\_ATTRIBUTE\_OFFLINE[¶](#stat.FILE_ATTRIBUTE_OFFLINE "Link to this definition")

stat.FILE\_ATTRIBUTE\_READONLY[¶](#stat.FILE_ATTRIBUTE_READONLY "Link to this definition")

stat.FILE\_ATTRIBUTE\_REPARSE\_POINT[¶](#stat.FILE_ATTRIBUTE_REPARSE_POINT "Link to this definition")

stat.FILE\_ATTRIBUTE\_SPARSE\_FILE[¶](#stat.FILE_ATTRIBUTE_SPARSE_FILE "Link to this definition")

stat.FILE\_ATTRIBUTE\_SYSTEM[¶](#stat.FILE_ATTRIBUTE_SYSTEM "Link to this definition")

stat.FILE\_ATTRIBUTE\_TEMPORARY[¶](#stat.FILE_ATTRIBUTE_TEMPORARY "Link to this definition")

stat.FILE\_ATTRIBUTE\_VIRTUAL[¶](#stat.FILE_ATTRIBUTE_VIRTUAL "Link to this definition")
:   Added in version 3.5.

On Windows, the following constants are available for comparing against the
`st_reparse_tag` member returned by [`os.lstat()`](os.html#os.lstat "os.lstat"). These are well-known
constants, but are not an exhaustive list.

stat.IO\_REPARSE\_TAG\_SYMLINK[¶](#stat.IO_REPARSE_TAG_SYMLINK "Link to this definition")

stat.IO\_REPARSE\_TAG\_MOUNT\_POINT[¶](#stat.IO_REPARSE_TAG_MOUNT_POINT "Link to this definition")

stat.IO\_REPARSE\_TAG\_APPEXECLINK[¶](#stat.IO_REPARSE_TAG_APPEXECLINK "Link to this definition")
:   Added in version 3.8.

#### Previous topic

[`os.path` — Common pathname manipulations](os.path.html "previous chapter")

#### Next topic

[`filecmp` — File and Directory Comparisons](filecmp.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/stat.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](filecmp.html "filecmp — File and Directory Comparisons") |
* [previous](os.path.html "os.path — Common pathname manipulations") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File and Directory Access](filesys.html) »
* `stat` — Interpreting `stat()` results
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