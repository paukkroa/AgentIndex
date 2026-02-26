### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](mimetypes.html "mimetypes — Map filenames to MIME types") |
* [previous](json.html "json — JSON encoder and decoder") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `mailbox` — Manipulate mailboxes in various formats
* |
* Theme
  Auto
  Light
  Dark
   |

# `mailbox` — Manipulate mailboxes in various formats[¶](#module-mailbox "Link to this heading")

**Source code:** [Lib/mailbox.py](https://github.com/python/cpython/tree/3.14/Lib/mailbox.py)

---

This module defines two classes, [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") and [`Message`](#mailbox.Message "mailbox.Message"), for
accessing and manipulating on-disk mailboxes and the messages they contain.
`Mailbox` offers a dictionary-like mapping from keys to messages.
`Message` extends the [`email.message`](email.message.html#module-email.message "email.message: The base class representing email messages.") module’s
[`Message`](email.compat32-message.html#email.message.Message "email.message.Message") class with format-specific state and behavior.
Supported mailbox formats are Maildir, mbox, MH, Babyl, and MMDF.

See also

Module [`email`](email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
:   Represent and manipulate messages.

## `Mailbox` objects[¶](#mailbox-objects "Link to this heading")

*class* mailbox.Mailbox[¶](#mailbox.Mailbox "Link to this definition")
:   A mailbox, which may be inspected and modified.

    The `Mailbox` class defines an interface and is not intended to be
    instantiated. Instead, format-specific subclasses should inherit from
    `Mailbox` and your code should instantiate a particular subclass.

    The `Mailbox` interface is dictionary-like, with small keys
    corresponding to messages. Keys are issued by the `Mailbox` instance
    with which they will be used and are only meaningful to that `Mailbox`
    instance. A key continues to identify a message even if the corresponding
    message is modified, such as by replacing it with another message.

    Messages may be added to a `Mailbox` instance using the set-like
    method [`add()`](#mailbox.Mailbox.add "mailbox.Mailbox.add") and removed using a `del` statement or the set-like
    methods [`remove()`](#mailbox.Mailbox.remove "mailbox.Mailbox.remove") and [`discard()`](#mailbox.Mailbox.discard "mailbox.Mailbox.discard").

    `Mailbox` interface semantics differ from dictionary semantics in some
    noteworthy ways. Each time a message is requested, a new representation
    (typically a [`Message`](#mailbox.Message "mailbox.Message") instance) is generated based upon the current
    state of the mailbox. Similarly, when a message is added to a
    `Mailbox` instance, the provided message representation’s contents are
    copied. In neither case is a reference to the message representation kept by
    the `Mailbox` instance.

    The default `Mailbox` [iterator](../glossary.html#term-iterator) iterates over message
    representations, not keys as the default [`dictionary`](stdtypes.html#dict "dict")
    iterator does. Moreover, modification of a
    mailbox during iteration is safe and well-defined. Messages added to the
    mailbox after an iterator is created will not be seen by the
    iterator. Messages removed from the mailbox before the iterator yields them
    will be silently skipped, though using a key from an iterator may result in a
    [`KeyError`](exceptions.html#KeyError "KeyError") exception if the corresponding message is subsequently
    removed.

    Warning

    Be very cautious when modifying mailboxes that might be simultaneously
    changed by some other process. The safest mailbox format to use for such
    tasks is [`Maildir`](#mailbox.Maildir "mailbox.Maildir"); try to avoid using single-file formats such as
    [`mbox`](#mailbox.mbox "mailbox.mbox") for
    concurrent writing. If you’re modifying a mailbox, you *must* lock it by
    calling the [`lock()`](#mailbox.Mailbox.lock "mailbox.Mailbox.lock") and [`unlock()`](#mailbox.Mailbox.unlock "mailbox.Mailbox.unlock") methods *before* reading any
    messages in the file or making any changes by adding or deleting a
    message. Failing to lock the mailbox runs the risk of losing messages or
    corrupting the entire mailbox.

    `Mailbox` instances have the following methods:

    add(*message*)[¶](#mailbox.Mailbox.add "Link to this definition")
    :   Add *message* to the mailbox and return the key that has been assigned to
        it.

        Parameter *message* may be a [`Message`](#mailbox.Message "mailbox.Message") instance, an
        [`email.message.Message`](email.compat32-message.html#email.message.Message "email.message.Message") instance, a string, a byte string, or a
        file-like object (which should be open in binary mode). If *message* is
        an instance of the
        appropriate format-specific [`Message`](#mailbox.Message "mailbox.Message") subclass (e.g., if it’s an
        [`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") instance and this is an [`mbox`](#mailbox.mbox "mailbox.mbox") instance), its
        format-specific information is used. Otherwise, reasonable defaults for
        format-specific information are used.

        Changed in version 3.2: Support for binary input was added.

    remove(*key*)[¶](#mailbox.Mailbox.remove "Link to this definition")

    \_\_delitem\_\_(*key*)[¶](#mailbox.Mailbox.__delitem__ "Link to this definition")

    discard(*key*)[¶](#mailbox.Mailbox.discard "Link to this definition")
    :   Delete the message corresponding to *key* from the mailbox.

        If no such message exists, a [`KeyError`](exceptions.html#KeyError "KeyError") exception is raised if the
        method was called as [`remove()`](#mailbox.Mailbox.remove "mailbox.Mailbox.remove") or [`__delitem__()`](#mailbox.Mailbox.__delitem__ "mailbox.Mailbox.__delitem__") but no
        exception is raised if the method was called as [`discard()`](#mailbox.Mailbox.discard "mailbox.Mailbox.discard"). The
        behavior of [`discard()`](#mailbox.Mailbox.discard "mailbox.Mailbox.discard") may be preferred if the underlying mailbox
        format supports concurrent modification by other processes.

    \_\_setitem\_\_(*key*, *message*)[¶](#mailbox.Mailbox.__setitem__ "Link to this definition")
    :   Replace the message corresponding to *key* with *message*. Raise a
        [`KeyError`](exceptions.html#KeyError "KeyError") exception if no message already corresponds to *key*.

        As with [`add()`](#mailbox.Mailbox.add "mailbox.Mailbox.add"), parameter *message* may be a [`Message`](#mailbox.Message "mailbox.Message")
        instance, an [`email.message.Message`](email.compat32-message.html#email.message.Message "email.message.Message") instance, a string, a byte
        string, or a file-like object (which should be open in binary mode). If
        *message* is an
        instance of the appropriate format-specific [`Message`](#mailbox.Message "mailbox.Message") subclass
        (e.g., if it’s an [`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") instance and this is an
        [`mbox`](#mailbox.mbox "mailbox.mbox") instance), its format-specific information is
        used. Otherwise, the format-specific information of the message that
        currently corresponds to *key* is left unchanged.

    iterkeys()[¶](#mailbox.Mailbox.iterkeys "Link to this definition")
    :   Return an [iterator](../glossary.html#term-iterator) over all keys

    keys()[¶](#mailbox.Mailbox.keys "Link to this definition")
    :   The same as [`iterkeys()`](#mailbox.Mailbox.iterkeys "mailbox.Mailbox.iterkeys"), except that a [`list`](stdtypes.html#list "list") is returned
        rather than an [iterator](../glossary.html#term-iterator)

    itervalues()[¶](#mailbox.Mailbox.itervalues "Link to this definition")

    \_\_iter\_\_()[¶](#mailbox.Mailbox.__iter__ "Link to this definition")
    :   Return an [iterator](../glossary.html#term-iterator) over representations of all messages.
        The messages are represented
        as instances of the appropriate format-specific [`Message`](#mailbox.Message "mailbox.Message") subclass
        unless a custom message factory was specified when the `Mailbox`
        instance was initialized.

        Note

        The behavior of [`__iter__()`](#mailbox.Mailbox.__iter__ "mailbox.Mailbox.__iter__") is unlike that of dictionaries, which
        iterate over keys.

    values()[¶](#mailbox.Mailbox.values "Link to this definition")
    :   The same as [`itervalues()`](#mailbox.Mailbox.itervalues "mailbox.Mailbox.itervalues"), except that a [`list`](stdtypes.html#list "list") is returned
        rather than an [iterator](../glossary.html#term-iterator)

    iteritems()[¶](#mailbox.Mailbox.iteritems "Link to this definition")
    :   Return an [iterator](../glossary.html#term-iterator) over (*key*, *message*) pairs, where *key* is
        a key and *message* is a message representation. The messages are
        represented as instances of the appropriate format-specific
        [`Message`](#mailbox.Message "mailbox.Message") subclass unless a custom message factory was specified
        when the `Mailbox` instance was initialized.

    items()[¶](#mailbox.Mailbox.items "Link to this definition")
    :   The same as [`iteritems()`](#mailbox.Mailbox.iteritems "mailbox.Mailbox.iteritems"), except that a [`list`](stdtypes.html#list "list") of pairs is
        returned rather than an [iterator](../glossary.html#term-iterator) of pairs.

    get(*key*, *default=None*)[¶](#mailbox.Mailbox.get "Link to this definition")

    \_\_getitem\_\_(*key*)[¶](#mailbox.Mailbox.__getitem__ "Link to this definition")
    :   Return a representation of the message corresponding to *key*. If no such
        message exists, *default* is returned if the method was called as
        [`get()`](#mailbox.Mailbox.get "mailbox.Mailbox.get") and a [`KeyError`](exceptions.html#KeyError "KeyError") exception is raised if the method was
        called as `__getitem__()`. The message is represented as an instance
        of the appropriate format-specific [`Message`](#mailbox.Message "mailbox.Message") subclass unless a
        custom message factory was specified when the `Mailbox` instance
        was initialized.

    get\_message(*key*)[¶](#mailbox.Mailbox.get_message "Link to this definition")
    :   Return a representation of the message corresponding to *key* as an
        instance of the appropriate format-specific [`Message`](#mailbox.Message "mailbox.Message") subclass, or
        raise a [`KeyError`](exceptions.html#KeyError "KeyError") exception if no such message exists.

    get\_bytes(*key*)[¶](#mailbox.Mailbox.get_bytes "Link to this definition")
    :   Return a byte representation of the message corresponding to *key*, or
        raise a [`KeyError`](exceptions.html#KeyError "KeyError") exception if no such message exists.

        Added in version 3.2.

    get\_string(*key*)[¶](#mailbox.Mailbox.get_string "Link to this definition")
    :   Return a string representation of the message corresponding to *key*, or
        raise a [`KeyError`](exceptions.html#KeyError "KeyError") exception if no such message exists. The
        message is processed through [`email.message.Message`](email.compat32-message.html#email.message.Message "email.message.Message") to
        convert it to a 7bit clean representation.

    get\_file(*key*)[¶](#mailbox.Mailbox.get_file "Link to this definition")
    :   Return a [file-like](../glossary.html#term-file-like-object) representation of the
        message corresponding to *key*,
        or raise a [`KeyError`](exceptions.html#KeyError "KeyError") exception if no such message exists. The
        file-like object behaves as if open in binary mode. This file should be
        closed once it is no longer needed.

        Changed in version 3.2: The file object really is a [binary file](../glossary.html#term-binary-file); previously it was
        incorrectly returned in text mode. Also, the [file-like object](../glossary.html#term-file-like-object)
        now supports the [context manager](../glossary.html#term-context-manager) protocol: you can use a
        [`with`](../reference/compound_stmts.html#with) statement to automatically close it.

        Note

        Unlike other representations of messages,
        [file-like](../glossary.html#term-file-like-object) representations are not
        necessarily independent of the `Mailbox` instance that
        created them or of the underlying mailbox. More specific documentation
        is provided by each subclass.

    \_\_contains\_\_(*key*)[¶](#mailbox.Mailbox.__contains__ "Link to this definition")
    :   Return `True` if *key* corresponds to a message, `False` otherwise.

    \_\_len\_\_()[¶](#mailbox.Mailbox.__len__ "Link to this definition")
    :   Return a count of messages in the mailbox.

    clear()[¶](#mailbox.Mailbox.clear "Link to this definition")
    :   Delete all messages from the mailbox.

    pop(*key*, *default=None*)[¶](#mailbox.Mailbox.pop "Link to this definition")
    :   Return a representation of the message corresponding to *key* and delete
        the message. If no such message exists, return *default*. The message is
        represented as an instance of the appropriate format-specific
        [`Message`](#mailbox.Message "mailbox.Message") subclass unless a custom message factory was specified
        when the `Mailbox` instance was initialized.

    popitem()[¶](#mailbox.Mailbox.popitem "Link to this definition")
    :   Return an arbitrary (*key*, *message*) pair, where *key* is a key and
        *message* is a message representation, and delete the corresponding
        message. If the mailbox is empty, raise a [`KeyError`](exceptions.html#KeyError "KeyError") exception. The
        message is represented as an instance of the appropriate format-specific
        [`Message`](#mailbox.Message "mailbox.Message") subclass unless a custom message factory was specified
        when the `Mailbox` instance was initialized.

    update(*arg*)[¶](#mailbox.Mailbox.update "Link to this definition")
    :   Parameter *arg* should be a *key*-to-*message* mapping or an iterable of
        (*key*, *message*) pairs. Updates the mailbox so that, for each given
        *key* and *message*, the message corresponding to *key* is set to
        *message* as if by using [`__setitem__()`](#mailbox.Mailbox.__setitem__ "mailbox.Mailbox.__setitem__"). As with [`__setitem__()`](#mailbox.Mailbox.__setitem__ "mailbox.Mailbox.__setitem__"),
        each *key* must already correspond to a message in the mailbox or else a
        [`KeyError`](exceptions.html#KeyError "KeyError") exception will be raised, so in general it is incorrect
        for *arg* to be a `Mailbox` instance.

        Note

        Unlike with dictionaries, keyword arguments are not supported.

    flush()[¶](#mailbox.Mailbox.flush "Link to this definition")
    :   Write any pending changes to the filesystem. For some [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox")
        subclasses, changes are always written immediately and `flush()` does
        nothing, but you should still make a habit of calling this method.

    lock()[¶](#mailbox.Mailbox.lock "Link to this definition")
    :   Acquire an exclusive advisory lock on the mailbox so that other processes
        know not to modify it. An [`ExternalClashError`](#mailbox.ExternalClashError "mailbox.ExternalClashError") is raised if the lock
        is not available. The particular locking mechanisms used depend upon the
        mailbox format. You should *always* lock the mailbox before making any
        modifications to its contents.

    unlock()[¶](#mailbox.Mailbox.unlock "Link to this definition")
    :   Release the lock on the mailbox, if any.

    close()[¶](#mailbox.Mailbox.close "Link to this definition")
    :   Flush the mailbox, unlock it if necessary, and close any open files. For
        some `Mailbox` subclasses, this method does nothing.

### `Maildir` objects[¶](#maildir-objects "Link to this heading")

*class* mailbox.Maildir(*dirname*, *factory=None*, *create=True*)[¶](#mailbox.Maildir "Link to this definition")
:   A subclass of [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in Maildir format. Parameter
    *factory* is a callable object that accepts a file-like message representation
    (which behaves as if opened in binary mode) and returns a custom representation.
    If *factory* is `None`, [`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") is used as the default message
    representation. If *create* is `True`, the mailbox is created if it does not
    exist.

    If *create* is `True` and the *dirname* path exists, it will be treated as
    an existing maildir without attempting to verify its directory layout.

    It is for historical reasons that *dirname* is named as such rather than *path*.

    Maildir is a directory-based mailbox format invented for the qmail mail
    transfer agent and now widely supported by other programs. Messages in a
    Maildir mailbox are stored in separate files within a common directory
    structure. This design allows Maildir mailboxes to be accessed and modified
    by multiple unrelated programs without data corruption, so file locking is
    unnecessary.

    Maildir mailboxes contain three subdirectories, namely: `tmp`,
    `new`, and `cur`. Messages are created momentarily in the
    `tmp` subdirectory and then moved to the `new` subdirectory to
    finalize delivery. A mail user agent may subsequently move the message to the
    `cur` subdirectory and store information about the state of the message
    in a special “info” section appended to its file name.

    Folders of the style introduced by the Courier mail transfer agent are also
    supported. Any subdirectory of the main mailbox is considered a folder if
    `'.'` is the first character in its name. Folder names are represented by
    `Maildir` without the leading `'.'`. Each folder is itself a Maildir
    mailbox but should not contain other folders. Instead, a logical nesting is
    indicated using `'.'` to delimit levels, e.g., “Archived.2005.07”.

    colon[¶](#mailbox.Maildir.colon "Link to this definition")
    :   The Maildir specification requires the use of a colon (`':'`) in certain
        message file names. However, some operating systems do not permit this
        character in file names, If you wish to use a Maildir-like format on such
        an operating system, you should specify another character to use
        instead. The exclamation point (`'!'`) is a popular choice. For
        example:

        ```
        import mailbox
        mailbox.Maildir.colon = '!'
        ```

        The `colon` attribute may also be set on a per-instance basis.

    Changed in version 3.13: [`Maildir`](#mailbox.Maildir "mailbox.Maildir") now ignores files with a leading dot.

    `Maildir` instances have all of the methods of [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") in
    addition to the following:

    list\_folders()[¶](#mailbox.Maildir.list_folders "Link to this definition")
    :   Return a list of the names of all folders.

    get\_folder(*folder*)[¶](#mailbox.Maildir.get_folder "Link to this definition")
    :   Return a `Maildir` instance representing the folder whose name is
        *folder*. A [`NoSuchMailboxError`](#mailbox.NoSuchMailboxError "mailbox.NoSuchMailboxError") exception is raised if the folder
        does not exist.

    add\_folder(*folder*)[¶](#mailbox.Maildir.add_folder "Link to this definition")
    :   Create a folder whose name is *folder* and return a `Maildir`
        instance representing it.

    remove\_folder(*folder*)[¶](#mailbox.Maildir.remove_folder "Link to this definition")
    :   Delete the folder whose name is *folder*. If the folder contains any
        messages, a [`NotEmptyError`](#mailbox.NotEmptyError "mailbox.NotEmptyError") exception will be raised and the folder
        will not be deleted.

    clean()[¶](#mailbox.Maildir.clean "Link to this definition")
    :   Delete temporary files from the mailbox that have not been accessed in the
        last 36 hours. The Maildir specification says that mail-reading programs
        should do this occasionally.

    get\_flags(*key*)[¶](#mailbox.Maildir.get_flags "Link to this definition")
    :   Return as a string the flags that are set on the message
        corresponding to *key*.
        This is the same as `get_message(key).get_flags()` but much
        faster, because it does not open the message file.
        Use this method when iterating over the keys to determine which
        messages are interesting to get.

        If you do have a [`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") object, use
        its [`get_flags()`](#mailbox.MaildirMessage.get_flags "mailbox.MaildirMessage.get_flags") method instead, because
        changes made by the message’s [`set_flags()`](#mailbox.MaildirMessage.set_flags "mailbox.MaildirMessage.set_flags"),
        [`add_flag()`](#mailbox.MaildirMessage.add_flag "mailbox.MaildirMessage.add_flag") and [`remove_flag()`](#mailbox.MaildirMessage.remove_flag "mailbox.MaildirMessage.remove_flag")
        methods are not reflected here until the mailbox’s
        [`__setitem__()`](#mailbox.Maildir.__setitem__ "mailbox.Maildir.__setitem__") method is called.

        Added in version 3.13.

    set\_flags(*key*, *flags*)[¶](#mailbox.Maildir.set_flags "Link to this definition")
    :   On the message corresponding to *key*, set the flags specified
        by *flags* and unset all others.
        Calling `some_mailbox.set_flags(key, flags)` is similar to

        ```
        one_message = some_mailbox.get_message(key)
        one_message.set_flags(flags)
        some_mailbox[key] = one_message
        ```

        but faster, because it does not open the message file.

        If you do have a [`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") object, use
        its [`set_flags()`](#mailbox.MaildirMessage.set_flags "mailbox.MaildirMessage.set_flags") method instead, because
        changes made with this mailbox method will not be visible to the
        message object’s method, [`get_flags()`](#mailbox.MaildirMessage.get_flags "mailbox.MaildirMessage.get_flags").

        Added in version 3.13.

    add\_flag(*key*, *flag*)[¶](#mailbox.Maildir.add_flag "Link to this definition")
    :   On the message corresponding to *key*, set the flags specified
        by *flag* without changing other flags. To add more than one
        flag at a time, *flag* may be a string of more than one character.

        Considerations for using this method versus the message object’s
        [`add_flag()`](#mailbox.MaildirMessage.add_flag "mailbox.MaildirMessage.add_flag") method are similar to
        those for [`set_flags()`](#mailbox.Maildir.set_flags "mailbox.Maildir.set_flags"); see the discussion there.

        Added in version 3.13.

    remove\_flag(*key*, *flag*)[¶](#mailbox.Maildir.remove_flag "Link to this definition")
    :   On the message corresponding to *key*, unset the flags specified
        by *flag* without changing other flags. To remove more than one
        flag at a time, *flag* may be a string of more than one character.

        Considerations for using this method versus the message object’s
        [`remove_flag()`](#mailbox.MaildirMessage.remove_flag "mailbox.MaildirMessage.remove_flag") method are similar to
        those for [`set_flags()`](#mailbox.Maildir.set_flags "mailbox.Maildir.set_flags"); see the discussion there.

        Added in version 3.13.

    get\_info(*key*)[¶](#mailbox.Maildir.get_info "Link to this definition")
    :   Return a string containing the info for the message
        corresponding to *key*.
        This is the same as `get_message(key).get_info()` but much
        faster, because it does not open the message file.
        Use this method when iterating over the keys to determine which
        messages are interesting to get.

        If you do have a [`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") object, use
        its [`get_info()`](#mailbox.MaildirMessage.get_info "mailbox.MaildirMessage.get_info") method instead, because
        changes made by the message’s [`set_info()`](#mailbox.MaildirMessage.set_info "mailbox.MaildirMessage.set_info") method
        are not reflected here until the mailbox’s [`__setitem__()`](#mailbox.Maildir.__setitem__ "mailbox.Maildir.__setitem__") method
        is called.

        Added in version 3.13.

    set\_info(*key*, *info*)[¶](#mailbox.Maildir.set_info "Link to this definition")
    :   Set the info of the message corresponding to *key* to *info*.
        Calling `some_mailbox.set_info(key, flags)` is similar to

        ```
        one_message = some_mailbox.get_message(key)
        one_message.set_info(info)
        some_mailbox[key] = one_message
        ```

        but faster, because it does not open the message file.

        If you do have a [`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") object, use
        its [`set_info()`](#mailbox.MaildirMessage.set_info "mailbox.MaildirMessage.set_info") method instead, because
        changes made with this mailbox method will not be visible to the
        message object’s method, [`get_info()`](#mailbox.MaildirMessage.get_info "mailbox.MaildirMessage.get_info").

        Added in version 3.13.

    Some [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `Maildir` deserve special
    remarks:

    add(*message*)[¶](#mailbox.Maildir.add "Link to this definition")

    \_\_setitem\_\_(*key*, *message*)[¶](#mailbox.Maildir.__setitem__ "Link to this definition")

    update(*arg*)[¶](#mailbox.Maildir.update "Link to this definition")
    :   Warning

        These methods generate unique file names based upon the current process
        ID. When using multiple threads, undetected name clashes may occur and
        cause corruption of the mailbox unless threads are coordinated to avoid
        using these methods to manipulate the same mailbox simultaneously.

    flush()[¶](#mailbox.Maildir.flush "Link to this definition")
    :   All changes to Maildir mailboxes are immediately applied, so this method
        does nothing.

    lock()[¶](#mailbox.Maildir.lock "Link to this definition")

    unlock()[¶](#mailbox.Maildir.unlock "Link to this definition")
    :   Maildir mailboxes do not support (or require) locking, so these methods do
        nothing.

    close()[¶](#mailbox.Maildir.close "Link to this definition")
    :   `Maildir` instances do not keep any open files and the underlying
        mailboxes do not support locking, so this method does nothing.

    get\_file(*key*)[¶](#mailbox.Maildir.get_file "Link to this definition")
    :   Depending upon the host platform, it may not be possible to modify or
        remove the underlying message while the returned file remains open.

See also

[maildir man page from Courier](https://www.courier-mta.org/maildir.html)
:   A specification of the format. Describes a common extension for
    supporting folders.

[Using maildir format](https://cr.yp.to/proto/maildir.html)
:   Notes on Maildir by its inventor. Includes an updated name-creation scheme and
    details on “info” semantics.

### `mbox` objects[¶](#mbox-objects "Link to this heading")

*class* mailbox.mbox(*path*, *factory=None*, *create=True*)[¶](#mailbox.mbox "Link to this definition")
:   A subclass of [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in mbox format. Parameter *factory*
    is a callable object that accepts a file-like message representation (which
    behaves as if opened in binary mode) and returns a custom representation. If
    *factory* is `None`, [`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") is used as the default message
    representation. If *create* is `True`, the mailbox is created if it does not
    exist.

    The mbox format is the classic format for storing mail on Unix systems. All
    messages in an mbox mailbox are stored in a single file with the beginning of
    each message indicated by a line whose first five characters are “From “.

    Several variations of the mbox format exist to address perceived shortcomings in
    the original. In the interest of compatibility, `mbox` implements the
    original format, which is sometimes referred to as *mboxo*. This means that
    the *Content-Length* header, if present, is ignored and that any
    occurrences of “From “ at the beginning of a line in a message body are
    transformed to “>From “ when storing the message, although occurrences of “>From
    “ are not transformed to “From “ when reading the message.

    Some [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `mbox` deserve special
    remarks:

    get\_bytes(*key*, *from\_=False*)[¶](#mailbox.mbox.get_bytes "Link to this definition")
    :   Note: This method has an extra parameter (*from\_*) compared with other classes.
        The first line of an mbox file entry is the Unix “From “ line.
        If *from\_* is False, the first line of the file is dropped.

    get\_file(*key*, *from\_=False*)[¶](#mailbox.mbox.get_file "Link to this definition")
    :   Using the file after calling [`flush()`](#mailbox.Mailbox.flush "mailbox.Mailbox.flush") or
        [`close()`](#mailbox.Mailbox.close "mailbox.Mailbox.close") on the `mbox` instance may yield
        unpredictable results or raise an exception.

        Note: This method has an extra parameter (*from\_*) compared with other classes.
        The first line of an mbox file entry is the Unix “From “ line.
        If *from\_* is False, the first line of the file is dropped.

    get\_string(*key*, *from\_=False*)[¶](#mailbox.mbox.get_string "Link to this definition")
    :   Note: This method has an extra parameter (*from\_*) compared with other classes.
        The first line of an mbox file entry is the Unix “From “ line.
        If *from\_* is False, the first line of the file is dropped.

    lock()[¶](#mailbox.mbox.lock "Link to this definition")

    unlock()[¶](#mailbox.mbox.unlock "Link to this definition")
    :   Three locking mechanisms are used—dot locking and, if available, the
        `flock()` and `lockf()` system calls.

See also

[mbox man page from tin](http://www.tin.org/bin/man.cgi?section=5&topic=mbox)
:   A specification of the format, with details on locking.

[Configuring Netscape Mail on Unix: Why The Content-Length Format is Bad](https://www.jwz.org/doc/content-length.html)
:   An argument for using the original mbox format rather than a variation.

[“mbox” is a family of several mutually incompatible mailbox formats](https://www.loc.gov/preservation/digital/formats/fdd/fdd000383.shtml)
:   A history of mbox variations.

### `MH` objects[¶](#mh-objects "Link to this heading")

*class* mailbox.MH(*path*, *factory=None*, *create=True*)[¶](#mailbox.MH "Link to this definition")
:   A subclass of [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in MH format. Parameter *factory*
    is a callable object that accepts a file-like message representation (which
    behaves as if opened in binary mode) and returns a custom representation. If
    *factory* is `None`, [`MHMessage`](#mailbox.MHMessage "mailbox.MHMessage") is used as the default message
    representation. If *create* is `True`, the mailbox is created if it does not
    exist.

    MH is a directory-based mailbox format invented for the MH Message Handling
    System, a mail user agent. Each message in an MH mailbox resides in its own
    file. An MH mailbox may contain other MH mailboxes (called *folders*) in
    addition to messages. Folders may be nested indefinitely. MH mailboxes also
    support *sequences*, which are named lists used to logically group
    messages without moving them to sub-folders. Sequences are defined in a file
    called `.mh_sequences` in each folder.

    The `MH` class manipulates MH mailboxes, but it does not attempt to
    emulate all of **mh**’s behaviors. In particular, it does not modify
    and is not affected by the `context` or `.mh_profile` files that
    are used by **mh** to store its state and configuration.

    `MH` instances have all of the methods of [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") in addition
    to the following:

    Changed in version 3.13: Supported folders that don’t contain a `.mh_sequences` file.

    list\_folders()[¶](#mailbox.MH.list_folders "Link to this definition")
    :   Return a list of the names of all folders.

    get\_folder(*folder*)[¶](#mailbox.MH.get_folder "Link to this definition")
    :   Return an `MH` instance representing the folder whose name is
        *folder*. A [`NoSuchMailboxError`](#mailbox.NoSuchMailboxError "mailbox.NoSuchMailboxError") exception is raised if the folder
        does not exist.

    add\_folder(*folder*)[¶](#mailbox.MH.add_folder "Link to this definition")
    :   Create a folder whose name is *folder* and return an `MH` instance
        representing it.

    remove\_folder(*folder*)[¶](#mailbox.MH.remove_folder "Link to this definition")
    :   Delete the folder whose name is *folder*. If the folder contains any
        messages, a [`NotEmptyError`](#mailbox.NotEmptyError "mailbox.NotEmptyError") exception will be raised and the folder
        will not be deleted.

    get\_sequences()[¶](#mailbox.MH.get_sequences "Link to this definition")
    :   Return a dictionary of sequence names mapped to key lists. If there are no
        sequences, the empty dictionary is returned.

    set\_sequences(*sequences*)[¶](#mailbox.MH.set_sequences "Link to this definition")
    :   Re-define the sequences that exist in the mailbox based upon *sequences*,
        a dictionary of names mapped to key lists, like returned by
        [`get_sequences()`](#mailbox.MH.get_sequences "mailbox.MH.get_sequences").

    pack()[¶](#mailbox.MH.pack "Link to this definition")
    :   Rename messages in the mailbox as necessary to eliminate gaps in
        numbering. Entries in the sequences list are updated correspondingly.

        Note

        Already-issued keys are invalidated by this operation and should not be
        subsequently used.

    Some [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `MH` deserve special
    remarks:

    remove(*key*)[¶](#mailbox.MH.remove "Link to this definition")

    \_\_delitem\_\_(*key*)[¶](#mailbox.MH.__delitem__ "Link to this definition")

    discard(*key*)[¶](#mailbox.MH.discard "Link to this definition")
    :   These methods immediately delete the message. The MH convention of marking
        a message for deletion by prepending a comma to its name is not used.

    lock()[¶](#mailbox.MH.lock "Link to this definition")

    unlock()[¶](#mailbox.MH.unlock "Link to this definition")
    :   Three locking mechanisms are used—dot locking and, if available, the
        `flock()` and `lockf()` system calls. For MH mailboxes, locking
        the mailbox means locking the `.mh_sequences` file and, only for the
        duration of any operations that affect them, locking individual message
        files.

    get\_file(*key*)[¶](#mailbox.MH.get_file "Link to this definition")
    :   Depending upon the host platform, it may not be possible to remove the
        underlying message while the returned file remains open.

    flush()[¶](#mailbox.MH.flush "Link to this definition")
    :   All changes to MH mailboxes are immediately applied, so this method does
        nothing.

    close()[¶](#mailbox.MH.close "Link to this definition")
    :   `MH` instances do not keep any open files, so this method is
        equivalent to [`unlock()`](#mailbox.MH.unlock "mailbox.MH.unlock").

See also

[nmh - Message Handling System](https://www.nongnu.org/nmh/)
:   Home page of **nmh**, an updated version of the original **mh**.

[MH & nmh: Email for Users & Programmers](https://rand-mh.sourceforge.io/book/)
:   A GPL-licensed book on **mh** and **nmh**, with some information
    on the mailbox format.

### `Babyl` objects[¶](#babyl-objects "Link to this heading")

*class* mailbox.Babyl(*path*, *factory=None*, *create=True*)[¶](#mailbox.Babyl "Link to this definition")
:   A subclass of [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in Babyl format. Parameter
    *factory* is a callable object that accepts a file-like message representation
    (which behaves as if opened in binary mode) and returns a custom representation.
    If *factory* is `None`, [`BabylMessage`](#mailbox.BabylMessage "mailbox.BabylMessage") is used as the default message
    representation. If *create* is `True`, the mailbox is created if it does not
    exist.

    Babyl is a single-file mailbox format used by the Rmail mail user agent
    included with Emacs. The beginning of a message is indicated by a line
    containing the two characters Control-Underscore (`'\037'`) and Control-L
    (`'\014'`). The end of a message is indicated by the start of the next
    message or, in the case of the last message, a line containing a
    Control-Underscore (`'\037'`) character.

    Messages in a Babyl mailbox have two sets of headers, original headers and
    so-called visible headers. Visible headers are typically a subset of the
    original headers that have been reformatted or abridged to be more
    attractive. Each message in a Babyl mailbox also has an accompanying list of
    *labels*, or short strings that record extra information about the
    message, and a list of all user-defined labels found in the mailbox is kept
    in the Babyl options section.

    `Babyl` instances have all of the methods of [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") in
    addition to the following:

    get\_labels()[¶](#mailbox.Babyl.get_labels "Link to this definition")
    :   Return a list of the names of all user-defined labels used in the mailbox.

        Note

        The actual messages are inspected to determine which labels exist in
        the mailbox rather than consulting the list of labels in the Babyl
        options section, but the Babyl section is updated whenever the mailbox
        is modified.

    Some [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `Babyl` deserve special
    remarks:

    get\_file(*key*)[¶](#mailbox.Babyl.get_file "Link to this definition")
    :   In Babyl mailboxes, the headers of a message are not stored contiguously
        with the body of the message. To generate a file-like representation, the
        headers and body are copied together into an [`io.BytesIO`](io.html#io.BytesIO "io.BytesIO") instance,
        which has an API identical to that of a
        file. As a result, the file-like object is truly independent of the
        underlying mailbox but does not save memory compared to a string
        representation.

    lock()[¶](#mailbox.Babyl.lock "Link to this definition")

    unlock()[¶](#mailbox.Babyl.unlock "Link to this definition")
    :   Three locking mechanisms are used—dot locking and, if available, the
        `flock()` and `lockf()` system calls.

See also

[Format of Version 5 Babyl Files](https://quimby.gnus.org/notes/BABYL)
:   A specification of the Babyl format.

[Reading Mail with Rmail](https://www.gnu.org/software/emacs/manual/html_node/emacs/Rmail.html)
:   The Rmail manual, with some information on Babyl semantics.

### `MMDF` objects[¶](#mmdf-objects "Link to this heading")

*class* mailbox.MMDF(*path*, *factory=None*, *create=True*)[¶](#mailbox.MMDF "Link to this definition")
:   A subclass of [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in MMDF format. Parameter *factory*
    is a callable object that accepts a file-like message representation (which
    behaves as if opened in binary mode) and returns a custom representation. If
    *factory* is `None`, [`MMDFMessage`](#mailbox.MMDFMessage "mailbox.MMDFMessage") is used as the default message
    representation. If *create* is `True`, the mailbox is created if it does not
    exist.

    MMDF is a single-file mailbox format invented for the Multichannel Memorandum
    Distribution Facility, a mail transfer agent. Each message is in the same
    form as an mbox message but is bracketed before and after by lines containing
    four Control-A (`'\001'`) characters. As with the mbox format, the
    beginning of each message is indicated by a line whose first five characters
    are “From “, but additional occurrences of “From “ are not transformed to
    “>From “ when storing messages because the extra message separator lines
    prevent mistaking such occurrences for the starts of subsequent messages.

    Some [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `MMDF` deserve special
    remarks:

    get\_bytes(*key*, *from\_=False*)[¶](#mailbox.MMDF.get_bytes "Link to this definition")
    :   Note: This method has an extra parameter (*from\_*) compared with other classes.
        The first line of an mbox file entry is the Unix “From “ line.
        If *from\_* is False, the first line of the file is dropped.

    get\_file(*key*, *from\_=False*)[¶](#mailbox.MMDF.get_file "Link to this definition")
    :   Using the file after calling [`flush()`](#mailbox.Mailbox.flush "mailbox.Mailbox.flush") or
        [`close()`](#mailbox.Mailbox.close "mailbox.Mailbox.close") on the `MMDF` instance may yield
        unpredictable results or raise an exception.

        Note: This method has an extra parameter (*from\_*) compared with other classes.
        The first line of an mbox file entry is the Unix “From “ line.
        If *from\_* is False, the first line of the file is dropped.

    lock()[¶](#mailbox.MMDF.lock "Link to this definition")

    unlock()[¶](#mailbox.MMDF.unlock "Link to this definition")
    :   Three locking mechanisms are used—dot locking and, if available, the
        `flock()` and `lockf()` system calls.

See also

[mmdf man page from tin](http://www.tin.org/bin/man.cgi?section=5&topic=mmdf)
:   A specification of MMDF format from the documentation of tin, a newsreader.

[MMDF](https://en.wikipedia.org/wiki/MMDF)
:   A Wikipedia article describing the Multichannel Memorandum Distribution
    Facility.

## `Message` objects[¶](#message-objects "Link to this heading")

*class* mailbox.Message(*message=None*)[¶](#mailbox.Message "Link to this definition")
:   A subclass of the [`email.message`](email.message.html#module-email.message "email.message: The base class representing email messages.") module’s
    [`Message`](email.compat32-message.html#email.message.Message "email.message.Message"). Subclasses of `mailbox.Message` add
    mailbox-format-specific state and behavior.

    If *message* is omitted, the new instance is created in a default, empty state.
    If *message* is an [`email.message.Message`](email.compat32-message.html#email.message.Message "email.message.Message") instance, its contents are
    copied; furthermore, any format-specific information is converted insofar as
    possible if *message* is a `Message` instance. If *message* is a string,
    a byte string,
    or a file, it should contain an [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)-compliant message, which is read
    and parsed. Files should be open in binary mode, but text mode files
    are accepted for backward compatibility.

    The format-specific state and behaviors offered by subclasses vary, but in
    general it is only the properties that are not specific to a particular
    mailbox that are supported (although presumably the properties are specific
    to a particular mailbox format). For example, file offsets for single-file
    mailbox formats and file names for directory-based mailbox formats are not
    retained, because they are only applicable to the original mailbox. But state
    such as whether a message has been read by the user or marked as important is
    retained, because it applies to the message itself.

    There is no requirement that `Message` instances be used to represent
    messages retrieved using [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") instances. In some situations, the
    time and memory required to generate `Message` representations might
    not be acceptable. For such situations, `Mailbox` instances also
    offer string and file-like representations, and a custom message factory may
    be specified when a `Mailbox` instance is initialized.

### `MaildirMessage` objects[¶](#maildirmessage-objects "Link to this heading")

*class* mailbox.MaildirMessage(*message=None*)[¶](#mailbox.MaildirMessage "Link to this definition")
:   A message with Maildir-specific behaviors. Parameter *message* has the same
    meaning as with the [`Message`](#mailbox.Message "mailbox.Message") constructor.

    Typically, a mail user agent application moves all of the messages in the
    `new` subdirectory to the `cur` subdirectory after the first time
    the user opens and closes the mailbox, recording that the messages are old
    whether or not they’ve actually been read. Each message in `cur` has an
    “info” section added to its file name to store information about its state.
    (Some mail readers may also add an “info” section to messages in
    `new`.) The “info” section may take one of two forms: it may contain
    “2,” followed by a list of standardized flags (e.g., “2,FR”) or it may
    contain “1,” followed by so-called experimental information. Standard flags
    for Maildir messages are as follows:

    | Flag | Meaning | Explanation |
    | --- | --- | --- |
    | D | Draft | Under composition |
    | F | Flagged | Marked as important |
    | P | Passed | Forwarded, resent, or bounced |
    | R | Replied | Replied to |
    | S | Seen | Read |
    | T | Trashed | Marked for subsequent deletion |

    `MaildirMessage` instances offer the following methods:

    get\_subdir()[¶](#mailbox.MaildirMessage.get_subdir "Link to this definition")
    :   Return either “new” (if the message should be stored in the `new`
        subdirectory) or “cur” (if the message should be stored in the `cur`
        subdirectory).

        Note

        A message is typically moved from `new` to `cur` after its
        mailbox has been accessed, whether or not the message has been
        read. A message `msg` has been read if `"S" in msg.get_flags()` is
        `True`.

    set\_subdir(*subdir*)[¶](#mailbox.MaildirMessage.set_subdir "Link to this definition")
    :   Set the subdirectory the message should be stored in. Parameter *subdir*
        must be either “new” or “cur”.

    get\_flags()[¶](#mailbox.MaildirMessage.get_flags "Link to this definition")
    :   Return a string specifying the flags that are currently set. If the
        message complies with the standard Maildir format, the result is the
        concatenation in alphabetical order of zero or one occurrence of each of
        `'D'`, `'F'`, `'P'`, `'R'`, `'S'`, and `'T'`. The empty string
        is returned if no flags are set or if “info” contains experimental
        semantics.

    set\_flags(*flags*)[¶](#mailbox.MaildirMessage.set_flags "Link to this definition")
    :   Set the flags specified by *flags* and unset all others.

    add\_flag(*flag*)[¶](#mailbox.MaildirMessage.add_flag "Link to this definition")
    :   Set the flag(s) specified by *flag* without changing other flags. To add
        more than one flag at a time, *flag* may be a string of more than one
        character. The current “info” is overwritten whether or not it contains
        experimental information rather than flags.

    remove\_flag(*flag*)[¶](#mailbox.MaildirMessage.remove_flag "Link to this definition")
    :   Unset the flag(s) specified by *flag* without changing other flags. To
        remove more than one flag at a time, *flag* may be a string of more than
        one character. If “info” contains experimental information rather than
        flags, the current “info” is not modified.

    get\_date()[¶](#mailbox.MaildirMessage.get_date "Link to this definition")
    :   Return the delivery date of the message as a floating-point number
        representing seconds since the epoch.

    set\_date(*date*)[¶](#mailbox.MaildirMessage.set_date "Link to this definition")
    :   Set the delivery date of the message to *date*, a floating-point number
        representing seconds since the epoch.

    get\_info()[¶](#mailbox.MaildirMessage.get_info "Link to this definition")
    :   Return a string containing the “info” for a message. This is useful for
        accessing and modifying “info” that is experimental (i.e., not a list of
        flags).

    set\_info(*info*)[¶](#mailbox.MaildirMessage.set_info "Link to this definition")
    :   Set “info” to *info*, which should be a string.

When a `MaildirMessage` instance is created based upon an
[`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](#mailbox.MMDFMessage "mailbox.MMDFMessage") instance, the *Status*
and *X-Status* headers are omitted and the following conversions
take place:

| Resulting state | [`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](#mailbox.MMDFMessage "mailbox.MMDFMessage") state |
| --- | --- |
| “cur” subdirectory | O flag |
| F flag | F flag |
| R flag | A flag |
| S flag | R flag |
| T flag | D flag |

When a `MaildirMessage` instance is created based upon an
[`MHMessage`](#mailbox.MHMessage "mailbox.MHMessage") instance, the following conversions take place:

| Resulting state | [`MHMessage`](#mailbox.MHMessage "mailbox.MHMessage") state |
| --- | --- |
| “cur” subdirectory | “unseen” sequence |
| “cur” subdirectory and S flag | no “unseen” sequence |
| F flag | “flagged” sequence |
| R flag | “replied” sequence |

When a `MaildirMessage` instance is created based upon a
[`BabylMessage`](#mailbox.BabylMessage "mailbox.BabylMessage") instance, the following conversions take place:

| Resulting state | [`BabylMessage`](#mailbox.BabylMessage "mailbox.BabylMessage") state |
| --- | --- |
| “cur” subdirectory | “unseen” label |
| “cur” subdirectory and S flag | no “unseen” label |
| P flag | “forwarded” or “resent” label |
| R flag | “answered” label |
| T flag | “deleted” label |

### `mboxMessage` objects[¶](#mboxmessage-objects "Link to this heading")

*class* mailbox.mboxMessage(*message=None*)[¶](#mailbox.mboxMessage "Link to this definition")
:   A message with mbox-specific behaviors. Parameter *message* has the same meaning
    as with the [`Message`](#mailbox.Message "mailbox.Message") constructor.

    Messages in an mbox mailbox are stored together in a single file. The
    sender’s envelope address and the time of delivery are typically stored in a
    line beginning with “From “ that is used to indicate the start of a message,
    though there is considerable variation in the exact format of this data among
    mbox implementations. Flags that indicate the state of the message, such as
    whether it has been read or marked as important, are typically stored in
    *Status* and *X-Status* headers.

    Conventional flags for mbox messages are as follows:

    | Flag | Meaning | Explanation |
    | --- | --- | --- |
    | R | Read | Read |
    | O | Old | Previously detected by MUA |
    | D | Deleted | Marked for subsequent deletion |
    | F | Flagged | Marked as important |
    | A | Answered | Replied to |

    The “R” and “O” flags are stored in the *Status* header, and the
    “D”, “F”, and “A” flags are stored in the *X-Status* header. The
    flags and headers typically appear in the order mentioned.

    `mboxMessage` instances offer the following methods:

    get\_from()[¶](#mailbox.mboxMessage.get_from "Link to this definition")
    :   Return a string representing the “From “ line that marks the start of the
        message in an mbox mailbox. The leading “From “ and the trailing newline
        are excluded.

    set\_from(*from\_*, *time\_=None*)[¶](#mailbox.mboxMessage.set_from "Link to this definition")
    :   Set the “From “ line to *from\_*, which should be specified without a
        leading “From “ or trailing newline. For convenience, *time\_* may be
        specified and will be formatted appropriately and appended to *from\_*. If
        *time\_* is specified, it should be a [`time.struct_time`](time.html#time.struct_time "time.struct_time") instance, a
        tuple suitable for passing to [`time.strftime()`](time.html#time.strftime "time.strftime"), or `True` (to use
        [`time.gmtime()`](time.html#time.gmtime "time.gmtime")).

    get\_flags()[¶](#mailbox.mboxMessage.get_flags "Link to this definition")
    :   Return a string specifying the flags that are currently set. If the
        message complies with the conventional format, the result is the
        concatenation in the following order of zero or one occurrence of each of
        `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

    set\_flags(*flags*)[¶](#mailbox.mboxMessage.set_flags "Link to this definition")
    :   Set the flags specified by *flags* and unset all others. Parameter *flags*
        should be the concatenation in any order of zero or more occurrences of
        each of `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

    add\_flag(*flag*)[¶](#mailbox.mboxMessage.add_flag "Link to this definition")
    :   Set the flag(s) specified by *flag* without changing other flags. To add
        more than one flag at a time, *flag* may be a string of more than one
        character.

    remove\_flag(*flag*)[¶](#mailbox.mboxMessage.remove_flag "Link to this definition")
    :   Unset the flag(s) specified by *flag* without changing other flags. To
        remove more than one flag at a time, *flag* may be a string of more than
        one character.

When an `mboxMessage` instance is created based upon a
[`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") instance, a “From “ line is generated based upon the
[`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") instance’s delivery date, and the following conversions
take place:

| Resulting state | [`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") state |
| --- | --- |
| R flag | S flag |
| O flag | “cur” subdirectory |
| D flag | T flag |
| F flag | F flag |
| A flag | R flag |

When an `mboxMessage` instance is created based upon an
[`MHMessage`](#mailbox.MHMessage "mailbox.MHMessage") instance, the following conversions take place:

| Resulting state | [`MHMessage`](#mailbox.MHMessage "mailbox.MHMessage") state |
| --- | --- |
| R flag and O flag | no “unseen” sequence |
| O flag | “unseen” sequence |
| F flag | “flagged” sequence |
| A flag | “replied” sequence |

When an `mboxMessage` instance is created based upon a
[`BabylMessage`](#mailbox.BabylMessage "mailbox.BabylMessage") instance, the following conversions take place:

| Resulting state | [`BabylMessage`](#mailbox.BabylMessage "mailbox.BabylMessage") state |
| --- | --- |
| R flag and O flag | no “unseen” label |
| O flag | “unseen” label |
| D flag | “deleted” label |
| A flag | “answered” label |

When a `mboxMessage` instance is created based upon an
[`MMDFMessage`](#mailbox.MMDFMessage "mailbox.MMDFMessage")
instance, the “From “ line is copied and all flags directly correspond:

| Resulting state | [`MMDFMessage`](#mailbox.MMDFMessage "mailbox.MMDFMessage") state |
| --- | --- |
| R flag | R flag |
| O flag | O flag |
| D flag | D flag |
| F flag | F flag |
| A flag | A flag |

### `MHMessage` objects[¶](#mhmessage-objects "Link to this heading")

*class* mailbox.MHMessage(*message=None*)[¶](#mailbox.MHMessage "Link to this definition")
:   A message with MH-specific behaviors. Parameter *message* has the same meaning
    as with the [`Message`](#mailbox.Message "mailbox.Message") constructor.

    MH messages do not support marks or flags in the traditional sense, but they
    do support sequences, which are logical groupings of arbitrary messages. Some
    mail reading programs (although not the standard **mh** and
    **nmh**) use sequences in much the same way flags are used with other
    formats, as follows:

    | Sequence | Explanation |
    | --- | --- |
    | unseen | Not read, but previously detected by MUA |
    | replied | Replied to |
    | flagged | Marked as important |

    `MHMessage` instances offer the following methods:

    get\_sequences()[¶](#mailbox.MHMessage.get_sequences "Link to this definition")
    :   Return a list of the names of sequences that include this message.

    set\_sequences(*sequences*)[¶](#mailbox.MHMessage.set_sequences "Link to this definition")
    :   Set the list of sequences that include this message.

    add\_sequence(*sequence*)[¶](#mailbox.MHMessage.add_sequence "Link to this definition")
    :   Add *sequence* to the list of sequences that include this message.

    remove\_sequence(*sequence*)[¶](#mailbox.MHMessage.remove_sequence "Link to this definition")
    :   Remove *sequence* from the list of sequences that include this message.

When an `MHMessage` instance is created based upon a
[`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") instance, the following conversions take place:

| Resulting state | [`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") state |
| --- | --- |
| “unseen” sequence | no S flag |
| “replied” sequence | R flag |
| “flagged” sequence | F flag |

When an `MHMessage` instance is created based upon an
[`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](#mailbox.MMDFMessage "mailbox.MMDFMessage") instance, the *Status*
and *X-Status* headers are omitted and the following conversions
take place:

| Resulting state | [`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](#mailbox.MMDFMessage "mailbox.MMDFMessage") state |
| --- | --- |
| “unseen” sequence | no R flag |
| “replied” sequence | A flag |
| “flagged” sequence | F flag |

When an `MHMessage` instance is created based upon a
[`BabylMessage`](#mailbox.BabylMessage "mailbox.BabylMessage") instance, the following conversions take place:

| Resulting state | [`BabylMessage`](#mailbox.BabylMessage "mailbox.BabylMessage") state |
| --- | --- |
| “unseen” sequence | “unseen” label |
| “replied” sequence | “answered” label |

### `BabylMessage` objects[¶](#babylmessage-objects "Link to this heading")

*class* mailbox.BabylMessage(*message=None*)[¶](#mailbox.BabylMessage "Link to this definition")
:   A message with Babyl-specific behaviors. Parameter *message* has the same
    meaning as with the [`Message`](#mailbox.Message "mailbox.Message") constructor.

    Certain message labels, called *attributes*, are defined by convention
    to have special meanings. The attributes are as follows:

    | Label | Explanation |
    | --- | --- |
    | unseen | Not read, but previously detected by MUA |
    | deleted | Marked for subsequent deletion |
    | filed | Copied to another file or mailbox |
    | answered | Replied to |
    | forwarded | Forwarded |
    | edited | Modified by the user |
    | resent | Resent |

    By default, Rmail displays only visible headers. The `BabylMessage`
    class, though, uses the original headers because they are more
    complete. Visible headers may be accessed explicitly if desired.

    `BabylMessage` instances offer the following methods:

    get\_labels()[¶](#mailbox.BabylMessage.get_labels "Link to this definition")
    :   Return a list of labels on the message.

    set\_labels(*labels*)[¶](#mailbox.BabylMessage.set_labels "Link to this definition")
    :   Set the list of labels on the message to *labels*.

    add\_label(*label*)[¶](#mailbox.BabylMessage.add_label "Link to this definition")
    :   Add *label* to the list of labels on the message.

    remove\_label(*label*)[¶](#mailbox.BabylMessage.remove_label "Link to this definition")
    :   Remove *label* from the list of labels on the message.

    get\_visible()[¶](#mailbox.BabylMessage.get_visible "Link to this definition")
    :   Return a [`Message`](#mailbox.Message "mailbox.Message") instance whose headers are the message’s
        visible headers and whose body is empty.

    set\_visible(*visible*)[¶](#mailbox.BabylMessage.set_visible "Link to this definition")
    :   Set the message’s visible headers to be the same as the headers in
        *message*. Parameter *visible* should be a [`Message`](#mailbox.Message "mailbox.Message") instance, an
        [`email.message.Message`](email.compat32-message.html#email.message.Message "email.message.Message") instance, a string, or a file-like object
        (which should be open in text mode).

    update\_visible()[¶](#mailbox.BabylMessage.update_visible "Link to this definition")
    :   When a `BabylMessage` instance’s original headers are modified, the
        visible headers are not automatically modified to correspond. This method
        updates the visible headers as follows: each visible header with a
        corresponding original header is set to the value of the original header,
        each visible header without a corresponding original header is removed,
        and any of *Date*, *From*, *Reply-To*,
        *To*, *CC*, and *Subject* that are
        present in the original headers but not the visible headers are added to
        the visible headers.

When a `BabylMessage` instance is created based upon a
[`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") instance, the following conversions take place:

| Resulting state | [`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") state |
| --- | --- |
| “unseen” label | no S flag |
| “deleted” label | T flag |
| “answered” label | R flag |
| “forwarded” label | P flag |

When a `BabylMessage` instance is created based upon an
[`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](#mailbox.MMDFMessage "mailbox.MMDFMessage") instance, the *Status*
and *X-Status* headers are omitted and the following conversions
take place:

| Resulting state | [`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](#mailbox.MMDFMessage "mailbox.MMDFMessage") state |
| --- | --- |
| “unseen” label | no R flag |
| “deleted” label | D flag |
| “answered” label | A flag |

When a `BabylMessage` instance is created based upon an
[`MHMessage`](#mailbox.MHMessage "mailbox.MHMessage") instance, the following conversions take place:

| Resulting state | [`MHMessage`](#mailbox.MHMessage "mailbox.MHMessage") state |
| --- | --- |
| “unseen” label | “unseen” sequence |
| “answered” label | “replied” sequence |

### `MMDFMessage` objects[¶](#mmdfmessage-objects "Link to this heading")

*class* mailbox.MMDFMessage(*message=None*)[¶](#mailbox.MMDFMessage "Link to this definition")
:   A message with MMDF-specific behaviors. Parameter *message* has the same meaning
    as with the [`Message`](#mailbox.Message "mailbox.Message") constructor.

    As with message in an mbox mailbox, MMDF messages are stored with the
    sender’s address and the delivery date in an initial line beginning with
    “From “. Likewise, flags that indicate the state of the message are
    typically stored in *Status* and *X-Status* headers.

    Conventional flags for MMDF messages are identical to those of mbox message
    and are as follows:

    | Flag | Meaning | Explanation |
    | --- | --- | --- |
    | R | Read | Read |
    | O | Old | Previously detected by MUA |
    | D | Deleted | Marked for subsequent deletion |
    | F | Flagged | Marked as important |
    | A | Answered | Replied to |

    The “R” and “O” flags are stored in the *Status* header, and the
    “D”, “F”, and “A” flags are stored in the *X-Status* header. The
    flags and headers typically appear in the order mentioned.

    `MMDFMessage` instances offer the following methods, which are
    identical to those offered by [`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage"):

    get\_from()[¶](#mailbox.MMDFMessage.get_from "Link to this definition")
    :   Return a string representing the “From “ line that marks the start of the
        message in an mbox mailbox. The leading “From “ and the trailing newline
        are excluded.

    set\_from(*from\_*, *time\_=None*)[¶](#mailbox.MMDFMessage.set_from "Link to this definition")
    :   Set the “From “ line to *from\_*, which should be specified without a
        leading “From “ or trailing newline. For convenience, *time\_* may be
        specified and will be formatted appropriately and appended to *from\_*. If
        *time\_* is specified, it should be a [`time.struct_time`](time.html#time.struct_time "time.struct_time") instance, a
        tuple suitable for passing to [`time.strftime()`](time.html#time.strftime "time.strftime"), or `True` (to use
        [`time.gmtime()`](time.html#time.gmtime "time.gmtime")).

    get\_flags()[¶](#mailbox.MMDFMessage.get_flags "Link to this definition")
    :   Return a string specifying the flags that are currently set. If the
        message complies with the conventional format, the result is the
        concatenation in the following order of zero or one occurrence of each of
        `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

    set\_flags(*flags*)[¶](#mailbox.MMDFMessage.set_flags "Link to this definition")
    :   Set the flags specified by *flags* and unset all others. Parameter *flags*
        should be the concatenation in any order of zero or more occurrences of
        each of `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

    add\_flag(*flag*)[¶](#mailbox.MMDFMessage.add_flag "Link to this definition")
    :   Set the flag(s) specified by *flag* without changing other flags. To add
        more than one flag at a time, *flag* may be a string of more than one
        character.

    remove\_flag(*flag*)[¶](#mailbox.MMDFMessage.remove_flag "Link to this definition")
    :   Unset the flag(s) specified by *flag* without changing other flags. To
        remove more than one flag at a time, *flag* may be a string of more than
        one character.

When an `MMDFMessage` instance is created based upon a
[`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") instance, a “From “ line is generated based upon the
[`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") instance’s delivery date, and the following conversions
take place:

| Resulting state | [`MaildirMessage`](#mailbox.MaildirMessage "mailbox.MaildirMessage") state |
| --- | --- |
| R flag | S flag |
| O flag | “cur” subdirectory |
| D flag | T flag |
| F flag | F flag |
| A flag | R flag |

When an `MMDFMessage` instance is created based upon an
[`MHMessage`](#mailbox.MHMessage "mailbox.MHMessage") instance, the following conversions take place:

| Resulting state | [`MHMessage`](#mailbox.MHMessage "mailbox.MHMessage") state |
| --- | --- |
| R flag and O flag | no “unseen” sequence |
| O flag | “unseen” sequence |
| F flag | “flagged” sequence |
| A flag | “replied” sequence |

When an `MMDFMessage` instance is created based upon a
[`BabylMessage`](#mailbox.BabylMessage "mailbox.BabylMessage") instance, the following conversions take place:

| Resulting state | [`BabylMessage`](#mailbox.BabylMessage "mailbox.BabylMessage") state |
| --- | --- |
| R flag and O flag | no “unseen” label |
| O flag | “unseen” label |
| D flag | “deleted” label |
| A flag | “answered” label |

When an `MMDFMessage` instance is created based upon an
[`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") instance, the “From “ line is copied and all flags directly
correspond:

| Resulting state | [`mboxMessage`](#mailbox.mboxMessage "mailbox.mboxMessage") state |
| --- | --- |
| R flag | R flag |
| O flag | O flag |
| D flag | D flag |
| F flag | F flag |
| A flag | A flag |

## Exceptions[¶](#exceptions "Link to this heading")

The following exception classes are defined in the `mailbox` module:

*exception* mailbox.Error[¶](#mailbox.Error "Link to this definition")
:   The base class for all other module-specific exceptions.

*exception* mailbox.NoSuchMailboxError[¶](#mailbox.NoSuchMailboxError "Link to this definition")
:   Raised when a mailbox is expected but is not found, such as when instantiating a
    [`Mailbox`](#mailbox.Mailbox "mailbox.Mailbox") subclass with a path that does not exist (and with the *create*
    parameter set to `False`), or when opening a folder that does not exist.

*exception* mailbox.NotEmptyError[¶](#mailbox.NotEmptyError "Link to this definition")
:   Raised when a mailbox is not empty but is expected to be, such as when deleting
    a folder that contains messages.

*exception* mailbox.ExternalClashError[¶](#mailbox.ExternalClashError "Link to this definition")
:   Raised when some mailbox-related condition beyond the control of the program
    causes it to be unable to proceed, such as when failing to acquire a lock that
    another program already holds, or when a uniquely generated file name
    already exists.

*exception* mailbox.FormatError[¶](#mailbox.FormatError "Link to this definition")
:   Raised when the data in a file cannot be parsed, such as when an [`MH`](#mailbox.MH "mailbox.MH")
    instance attempts to read a corrupted `.mh_sequences` file.

## Examples[¶](#examples "Link to this heading")

A simple example of printing the subjects of all messages in a mailbox that seem
interesting:

```
import mailbox
for message in mailbox.mbox('~/mbox'):
    subject = message['subject']       # Could possibly be None.
    if subject and 'python' in subject.lower():
        print(subject)
```

To copy all mail from a Babyl mailbox to an MH mailbox, converting all of the
format-specific information that can be converted:

```
import mailbox
destination = mailbox.MH('~/Mail')
destination.lock()
for message in mailbox.Babyl('~/RMAIL'):
    destination.add(mailbox.MHMessage(message))
destination.flush()
destination.unlock()
```

This example sorts mail from several mailing lists into different mailboxes,
being careful to avoid mail corruption due to concurrent modification by other
programs, mail loss due to interruption of the program, or premature termination
due to malformed messages in the mailbox:

```
import mailbox
import email.errors

list_names = ('python-list', 'python-dev', 'python-bugs')

boxes = {name: mailbox.mbox('~/email/%s' % name) for name in list_names}
inbox = mailbox.Maildir('~/Maildir', factory=None)

for key in inbox.iterkeys():
    try:
        message = inbox[key]
    except email.errors.MessageParseError:
        continue                # The message is malformed. Just leave it.

    for name in list_names:
        list_id = message['list-id']
        if list_id and name in list_id:
            # Get mailbox to use
            box = boxes[name]

            # Write copy to disk before removing original.
            # If there's a crash, you might duplicate a message, but
            # that's better than losing a message completely.
            box.lock()
            box.add(message)
            box.flush()
            box.unlock()

            # Remove original message
            inbox.lock()
            inbox.discard(key)
            inbox.flush()
            inbox.unlock()
            break               # Found destination, so stop looking.

for box in boxes.itervalues():
    box.close()
```

### [Table of Contents](../contents.html)

* [`mailbox` — Manipulate mailboxes in various formats](#)
  + [`Mailbox` objects](#mailbox-objects)
    - [`Maildir` objects](#maildir-objects)
    - [`mbox` objects](#mbox-objects)
    - [`MH` objects](#mh-objects)
    - [`Babyl` objects](#babyl-objects)
    - [`MMDF` objects](#mmdf-objects)
  + [`Message` objects](#message-objects)
    - [`MaildirMessage` objects](#maildirmessage-objects)
    - [`mboxMessage` objects](#mboxmessage-objects)
    - [`MHMessage` objects](#mhmessage-objects)
    - [`BabylMessage` objects](#babylmessage-objects)
    - [`MMDFMessage` objects](#mmdfmessage-objects)
  + [Exceptions](#exceptions)
  + [Examples](#examples)

#### Previous topic

[`json` — JSON encoder and decoder](json.html "previous chapter")

#### Next topic

[`mimetypes` — Map filenames to MIME types](mimetypes.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/mailbox.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](mimetypes.html "mimetypes — Map filenames to MIME types") |
* [previous](json.html "json — JSON encoder and decoder") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Data Handling](netdata.html) »
* `mailbox` — Manipulate mailboxes in various formats
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