### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](contextvars.html "contextvars — Context Variables") |
* [previous](sched.html "sched — Event scheduler") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `queue` — A synchronized queue class
* |
* Theme
  Auto
  Light
  Dark
   |

# `queue` — A synchronized queue class[¶](#module-queue "Link to this heading")

**Source code:** [Lib/queue.py](https://github.com/python/cpython/tree/3.14/Lib/queue.py)

---

The `queue` module implements multi-producer, multi-consumer queues.
It is especially useful in threaded programming when information must be
exchanged safely between multiple threads. The [`Queue`](#queue.Queue "queue.Queue") class in this
module implements all the required locking semantics.

The module implements three types of queue, which differ only in the order in
which the entries are retrieved. In a FIFO
queue, the first tasks added are the first retrieved. In a
LIFO queue, the most recently added entry is
the first retrieved (operating like a stack). With a priority queue,
the entries are kept sorted (using the [`heapq`](heapq.html#module-heapq "heapq: Heap queue algorithm (a.k.a. priority queue).") module) and the
lowest valued entry is retrieved first.

Internally, those three types of queues use locks to temporarily block
competing threads; however, they are not designed to handle reentrancy
within a thread.

In addition, the module implements a “simple”
FIFO queue type, [`SimpleQueue`](#queue.SimpleQueue "queue.SimpleQueue"), whose
specific implementation provides additional guarantees
in exchange for the smaller functionality.

The `queue` module defines the following classes and exceptions:

*class* queue.Queue(*maxsize=0*)[¶](#queue.Queue "Link to this definition")
:   Constructor for a FIFO queue. *maxsize* is
    an integer that sets the upperbound
    limit on the number of items that can be placed in the queue. Insertion will
    block once this size has been reached, until queue items are consumed. If
    *maxsize* is less than or equal to zero, the queue size is infinite.

*class* queue.LifoQueue(*maxsize=0*)[¶](#queue.LifoQueue "Link to this definition")
:   Constructor for a LIFO queue. *maxsize* is
    an integer that sets the upperbound
    limit on the number of items that can be placed in the queue. Insertion will
    block once this size has been reached, until queue items are consumed. If
    *maxsize* is less than or equal to zero, the queue size is infinite.

*class* queue.PriorityQueue(*maxsize=0*)[¶](#queue.PriorityQueue "Link to this definition")
:   Constructor for a priority queue. *maxsize* is an integer that sets the upperbound
    limit on the number of items that can be placed in the queue. Insertion will
    block once this size has been reached, until queue items are consumed. If
    *maxsize* is less than or equal to zero, the queue size is infinite.

    The lowest valued entries are retrieved first (the lowest valued entry is the
    one that would be returned by `min(entries)`). A typical pattern for
    entries is a tuple in the form: `(priority_number, data)`.

    If the *data* elements are not comparable, the data can be wrapped in a class
    that ignores the data item and only compares the priority number:

    ```
    from dataclasses import dataclass, field
    from typing import Any

    @dataclass(order=True)
    class PrioritizedItem:
        priority: int
        item: Any=field(compare=False)
    ```

*class* queue.SimpleQueue[¶](#queue.SimpleQueue "Link to this definition")
:   Constructor for an unbounded FIFO queue.
    Simple queues lack advanced functionality such as task tracking.

    Added in version 3.7.

*exception* queue.Empty[¶](#queue.Empty "Link to this definition")
:   Exception raised when non-blocking [`get()`](#queue.Queue.get "queue.Queue.get") (or
    [`get_nowait()`](#queue.Queue.get_nowait "queue.Queue.get_nowait")) is called
    on a [`Queue`](#queue.Queue "queue.Queue") object which is empty.

*exception* queue.Full[¶](#queue.Full "Link to this definition")
:   Exception raised when non-blocking [`put()`](#queue.Queue.put "queue.Queue.put") (or
    [`put_nowait()`](#queue.Queue.put_nowait "queue.Queue.put_nowait")) is called
    on a [`Queue`](#queue.Queue "queue.Queue") object which is full.

*exception* queue.ShutDown[¶](#queue.ShutDown "Link to this definition")
:   Exception raised when [`put()`](#queue.Queue.put "queue.Queue.put") or [`get()`](#queue.Queue.get "queue.Queue.get") is called on
    a [`Queue`](#queue.Queue "queue.Queue") object which has been shut down.

    Added in version 3.13.

## Queue Objects[¶](#queue-objects "Link to this heading")

Queue objects ([`Queue`](#queue.Queue "queue.Queue"), [`LifoQueue`](#queue.LifoQueue "queue.LifoQueue"), or [`PriorityQueue`](#queue.PriorityQueue "queue.PriorityQueue"))
provide the public methods described below.

Queue.qsize()[¶](#queue.Queue.qsize "Link to this definition")
:   Return the approximate size of the queue. Note, qsize() > 0 doesn’t
    guarantee that a subsequent get() will not block, nor will qsize() < maxsize
    guarantee that put() will not block.

Queue.empty()[¶](#queue.Queue.empty "Link to this definition")
:   Return `True` if the queue is empty, `False` otherwise. If empty()
    returns `True` it doesn’t guarantee that a subsequent call to put()
    will not block. Similarly, if empty() returns `False` it doesn’t
    guarantee that a subsequent call to get() will not block.

Queue.full()[¶](#queue.Queue.full "Link to this definition")
:   Return `True` if the queue is full, `False` otherwise. If full()
    returns `True` it doesn’t guarantee that a subsequent call to get()
    will not block. Similarly, if full() returns `False` it doesn’t
    guarantee that a subsequent call to put() will not block.

Queue.put(*item*, *block=True*, *timeout=None*)[¶](#queue.Queue.put "Link to this definition")
:   Put *item* into the queue. If optional args *block* is true and *timeout* is
    `None` (the default), block if necessary until a free slot is available. If
    *timeout* is a positive number, it blocks at most *timeout* seconds and raises
    the [`Full`](#queue.Full "queue.Full") exception if no free slot was available within that time.
    Otherwise (*block* is false), put an item on the queue if a free slot is
    immediately available, else raise the [`Full`](#queue.Full "queue.Full") exception (*timeout* is
    ignored in that case).

    Raises [`ShutDown`](#queue.ShutDown "queue.ShutDown") if the queue has been shut down.

Queue.put\_nowait(*item*)[¶](#queue.Queue.put_nowait "Link to this definition")
:   Equivalent to `put(item, block=False)`.

Queue.get(*block=True*, *timeout=None*)[¶](#queue.Queue.get "Link to this definition")
:   Remove and return an item from the queue. If optional args *block* is true and
    *timeout* is `None` (the default), block if necessary until an item is available.
    If *timeout* is a positive number, it blocks at most *timeout* seconds and
    raises the [`Empty`](#queue.Empty "queue.Empty") exception if no item was available within that time.
    Otherwise (*block* is false), return an item if one is immediately available,
    else raise the [`Empty`](#queue.Empty "queue.Empty") exception (*timeout* is ignored in that case).

    Prior to 3.0 on POSIX systems, and for all versions on Windows, if
    *block* is true and *timeout* is `None`, this operation goes into
    an uninterruptible wait on an underlying lock. This means that no exceptions
    can occur, and in particular a SIGINT will not trigger a [`KeyboardInterrupt`](exceptions.html#KeyboardInterrupt "KeyboardInterrupt").

    Raises [`ShutDown`](#queue.ShutDown "queue.ShutDown") if the queue has been shut down and is empty, or if
    the queue has been shut down immediately.

Queue.get\_nowait()[¶](#queue.Queue.get_nowait "Link to this definition")
:   Equivalent to `get(False)`.

Two methods are offered to support tracking whether enqueued tasks have been
fully processed by daemon consumer threads.

Queue.task\_done()[¶](#queue.Queue.task_done "Link to this definition")
:   Indicate that a formerly enqueued task is complete. Used by queue consumer
    threads. For each [`get()`](#queue.Queue.get "queue.Queue.get") used to fetch a task, a subsequent call to
    [`task_done()`](#queue.Queue.task_done "queue.Queue.task_done") tells the queue that the processing on the task is complete.

    If a [`join()`](#queue.Queue.join "queue.Queue.join") is currently blocking, it will resume when all items have been
    processed (meaning that a [`task_done()`](#queue.Queue.task_done "queue.Queue.task_done") call was received for every item
    that had been [`put()`](#queue.Queue.put "queue.Queue.put") into the queue).

    Raises a [`ValueError`](exceptions.html#ValueError "ValueError") if called more times than there were items placed in
    the queue.

Queue.join()[¶](#queue.Queue.join "Link to this definition")
:   Blocks until all items in the queue have been gotten and processed.

    The count of unfinished tasks goes up whenever an item is added to the queue.
    The count goes down whenever a consumer thread calls [`task_done()`](#queue.Queue.task_done "queue.Queue.task_done") to
    indicate that the item was retrieved and all work on it is complete. When the
    count of unfinished tasks drops to zero, [`join()`](#queue.Queue.join "queue.Queue.join") unblocks.

### Waiting for task completion[¶](#waiting-for-task-completion "Link to this heading")

Example of how to wait for enqueued tasks to be completed:

```
import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')
```

### Terminating queues[¶](#terminating-queues "Link to this heading")

When no longer needed, [`Queue`](#queue.Queue "queue.Queue") objects can be wound down
until empty or terminated immediately with a hard shutdown.

Queue.shutdown(*immediate=False*)[¶](#queue.Queue.shutdown "Link to this definition")
:   Put a [`Queue`](#queue.Queue "queue.Queue") instance into a shutdown mode.

    The queue can no longer grow.
    Future calls to [`put()`](#queue.Queue.put "queue.Queue.put") raise [`ShutDown`](#queue.ShutDown "queue.ShutDown").
    Currently blocked callers of [`put()`](#queue.Queue.put "queue.Queue.put") will be unblocked
    and will raise [`ShutDown`](#queue.ShutDown "queue.ShutDown") in the formerly blocked thread.

    If *immediate* is false (the default), the queue can be wound
    down normally with [`get()`](#queue.Queue.get "queue.Queue.get") calls to extract tasks
    that have already been loaded.

    And if [`task_done()`](#queue.Queue.task_done "queue.Queue.task_done") is called for each remaining task, a
    pending [`join()`](#queue.Queue.join "queue.Queue.join") will be unblocked normally.

    Once the queue is empty, future calls to [`get()`](#queue.Queue.get "queue.Queue.get") will
    raise [`ShutDown`](#queue.ShutDown "queue.ShutDown").

    If *immediate* is true, the queue is terminated immediately.
    The queue is drained to be completely empty and the count
    of unfinished tasks is reduced by the number of tasks drained.
    If unfinished tasks is zero, callers of [`join()`](#queue.Queue.join "queue.Queue.join")
    are unblocked. Also, blocked callers of [`get()`](#queue.Queue.get "queue.Queue.get")
    are unblocked and will raise [`ShutDown`](#queue.ShutDown "queue.ShutDown") because the
    queue is empty.

    Use caution when using [`join()`](#queue.Queue.join "queue.Queue.join") with *immediate* set
    to true. This unblocks the join even when no work has been done
    on the tasks, violating the usual invariant for joining a queue.

    Added in version 3.13.

## SimpleQueue Objects[¶](#simplequeue-objects "Link to this heading")

[`SimpleQueue`](#queue.SimpleQueue "queue.SimpleQueue") objects provide the public methods described below.

SimpleQueue.qsize()[¶](#queue.SimpleQueue.qsize "Link to this definition")
:   Return the approximate size of the queue. Note, qsize() > 0 doesn’t
    guarantee that a subsequent get() will not block.

SimpleQueue.empty()[¶](#queue.SimpleQueue.empty "Link to this definition")
:   Return `True` if the queue is empty, `False` otherwise. If empty()
    returns `False` it doesn’t guarantee that a subsequent call to get()
    will not block.

SimpleQueue.put(*item*, *block=True*, *timeout=None*)[¶](#queue.SimpleQueue.put "Link to this definition")
:   Put *item* into the queue. The method never blocks and always succeeds
    (except for potential low-level errors such as failure to allocate memory).
    The optional args *block* and *timeout* are ignored and only provided
    for compatibility with [`Queue.put()`](#queue.Queue.put "queue.Queue.put").

    **CPython implementation detail:** This method has a C implementation which is reentrant. That is, a
    `put()` or `get()` call can be interrupted by another `put()`
    call in the same thread without deadlocking or corrupting internal
    state inside the queue. This makes it appropriate for use in
    destructors such as `__del__` methods or [`weakref`](weakref.html#module-weakref "weakref: Support for weak references and weak dictionaries.") callbacks.

SimpleQueue.put\_nowait(*item*)[¶](#queue.SimpleQueue.put_nowait "Link to this definition")
:   Equivalent to `put(item, block=False)`, provided for compatibility with
    [`Queue.put_nowait()`](#queue.Queue.put_nowait "queue.Queue.put_nowait").

SimpleQueue.get(*block=True*, *timeout=None*)[¶](#queue.SimpleQueue.get "Link to this definition")
:   Remove and return an item from the queue. If optional args *block* is true and
    *timeout* is `None` (the default), block if necessary until an item is available.
    If *timeout* is a positive number, it blocks at most *timeout* seconds and
    raises the [`Empty`](#queue.Empty "queue.Empty") exception if no item was available within that time.
    Otherwise (*block* is false), return an item if one is immediately available,
    else raise the [`Empty`](#queue.Empty "queue.Empty") exception (*timeout* is ignored in that case).

SimpleQueue.get\_nowait()[¶](#queue.SimpleQueue.get_nowait "Link to this definition")
:   Equivalent to `get(False)`.

See also

Class [`multiprocessing.Queue`](multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue")
:   A queue class for use in a multi-processing (rather than multi-threading)
    context.

[`collections.deque`](collections.html#collections.deque "collections.deque") is an alternative implementation of unbounded
queues with fast atomic [`append()`](collections.html#collections.deque.append "collections.deque.append") and
[`popleft()`](collections.html#collections.deque.popleft "collections.deque.popleft") operations that do not require locking
and also support indexing.

### [Table of Contents](../contents.html)

* [`queue` — A synchronized queue class](#)
  + [Queue Objects](#queue-objects)
    - [Waiting for task completion](#waiting-for-task-completion)
    - [Terminating queues](#terminating-queues)
  + [SimpleQueue Objects](#simplequeue-objects)

#### Previous topic

[`sched` — Event scheduler](sched.html "previous chapter")

#### Next topic

[`contextvars` — Context Variables](contextvars.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/queue.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](contextvars.html "contextvars — Context Variables") |
* [previous](sched.html "sched — Event scheduler") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `queue` — A synchronized queue class
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