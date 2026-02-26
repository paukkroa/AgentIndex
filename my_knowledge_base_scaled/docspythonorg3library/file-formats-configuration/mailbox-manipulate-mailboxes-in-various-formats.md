---
id: 0.0.6.6
title: "mailbox— Manipulate mailboxes in various formats¶"
nav_summary: "`mailbox` module: Access/manipulate mailboxes (Maildir, mbox, MH, etc.)."
ref: https://docs.python.org/3/library/mailbox.html
ref_type: url
---

# mailbox— Manipulate mailboxes in various formats¶

The `mailbox` module in Python’s standard library provides classes for accessing and manipulating mailboxes in multiple formats (Maildir, mbox, MH, Babyl, and MMDF) via the abstract `Mailbox` class and its format-specific subclasses. The `Mailbox` class offers a dictionary-like interface for managing messages, where keys uniquely identify messages within the mailbox (not across instances). Messages are dynamically recreated on access, ensuring no persistent references are maintained. Key operations include adding (`add()`), removing (`remove()`, `discard()`), and iterating over messages, with thread-safety considerations—particularly for `Maildir`, which is the safest format for concurrent access. The `Message` class extends `email.message.Message`, embedding format-specific behavior. The module integrates with the broader `email` package for message parsing and manipulation.

---

[Link to original](https://docs.python.org/3/library/mailbox.html)
