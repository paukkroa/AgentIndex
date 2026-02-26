### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](_thread.html "_thread — Low-level threading API") |
* [previous](queue.html "queue — A synchronized queue class") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `contextvars` — Context Variables
* |
* Theme
  Auto
  Light
  Dark
   |

# `contextvars` — Context Variables[¶](#module-contextvars "Link to this heading")

---

This module provides APIs to manage, store, and access context-local
state. The [`ContextVar`](#contextvars.ContextVar "contextvars.ContextVar") class is used to declare
and work with *Context Variables*. The [`copy_context()`](#contextvars.copy_context "contextvars.copy_context")
function and the [`Context`](#contextvars.Context "contextvars.Context") class should be used to
manage the current context in asynchronous frameworks.

Context managers that have state should use Context Variables
instead of [`threading.local()`](threading.html#threading.local "threading.local") to prevent their state from
bleeding to other code unexpectedly, when used in concurrent code.

See also [**PEP 567**](https://peps.python.org/pep-0567/) for additional details.

Added in version 3.7.

## Context Variables[¶](#context-variables "Link to this heading")

*class* contextvars.ContextVar(*name*[, *\**, *default*])[¶](#contextvars.ContextVar "Link to this definition")
:   This class is used to declare a new Context Variable, e.g.:

    ```
    var: ContextVar[int] = ContextVar('var', default=42)
    ```

    The required *name* parameter is used for introspection and debug
    purposes.

    The optional keyword-only *default* parameter is returned by
    [`ContextVar.get()`](#contextvars.ContextVar.get "contextvars.ContextVar.get") when no value for the variable is found
    in the current context.

    **Important:** Context Variables should be created at the top module
    level and never in closures. [`Context`](#contextvars.Context "contextvars.Context") objects hold strong
    references to context variables which prevents context variables
    from being properly garbage collected.

    name[¶](#contextvars.ContextVar.name "Link to this definition")
    :   The name of the variable. This is a read-only property.

        Added in version 3.7.1.

    get([*default*])[¶](#contextvars.ContextVar.get "Link to this definition")
    :   Return a value for the context variable for the current context.

        If there is no value for the variable in the current context,
        the method will:

        * return the value of the *default* argument of the method,
          if provided; or
        * return the default value for the context variable,
          if it was created with one; or
        * raise a [`LookupError`](exceptions.html#LookupError "LookupError").

    set(*value*)[¶](#contextvars.ContextVar.set "Link to this definition")
    :   Call to set a new value for the context variable in the current
        context.

        The required *value* argument is the new value for the context
        variable.

        Returns a [`Token`](#contextvars.Token "contextvars.Token") object that can be used
        to restore the variable to its previous value via the
        [`ContextVar.reset()`](#contextvars.ContextVar.reset "contextvars.ContextVar.reset") method.

        For convenience, the token object can be used as a context manager
        to avoid calling [`ContextVar.reset()`](#contextvars.ContextVar.reset "contextvars.ContextVar.reset") manually:

        ```
        var = ContextVar('var', default='default value')

        with var.set('new value'):
            assert var.get() == 'new value'

        assert var.get() == 'default value'
        ```

        It is a shorthand for:

        ```
        var = ContextVar('var', default='default value')

        token = var.set('new value')
        try:
            assert var.get() == 'new value'
        finally:
            var.reset(token)

        assert var.get() == 'default value'
        ```

        Added in version 3.14: Added support for using tokens as context managers.

    reset(*token*)[¶](#contextvars.ContextVar.reset "Link to this definition")
    :   Reset the context variable to the value it had before the
        [`ContextVar.set()`](#contextvars.ContextVar.set "contextvars.ContextVar.set") that created the *token* was used.

        For example:

        ```
        var = ContextVar('var')

        token = var.set('new value')
        # code that uses 'var'; var.get() returns 'new value'.
        var.reset(token)

        # After the reset call the var has no value again, so
        # var.get() would raise a LookupError.
        ```

        The same *token* cannot be used twice.

*class* contextvars.Token[¶](#contextvars.Token "Link to this definition")
:   *Token* objects are returned by the [`ContextVar.set()`](#contextvars.ContextVar.set "contextvars.ContextVar.set") method.
    They can be passed to the [`ContextVar.reset()`](#contextvars.ContextVar.reset "contextvars.ContextVar.reset") method to revert
    the value of the variable to what it was before the corresponding
    *set*. A single token cannot reset a context variable more than once.

    Tokens support the [context manager protocol](../reference/datamodel.html#context-managers)
    to automatically reset context variables. See [`ContextVar.set()`](#contextvars.ContextVar.set "contextvars.ContextVar.set").

    Added in version 3.14: Added support for usage as a context manager.

    var[¶](#contextvars.Token.var "Link to this definition")
    :   A read-only property. Points to the [`ContextVar`](#contextvars.ContextVar "contextvars.ContextVar") object
        that created the token.

    old\_value[¶](#contextvars.Token.old_value "Link to this definition")
    :   A read-only property. Set to the value the variable had before
        the [`ContextVar.set()`](#contextvars.ContextVar.set "contextvars.ContextVar.set") method call that created the token.
        It points to [`Token.MISSING`](#contextvars.Token.MISSING "contextvars.Token.MISSING") if the variable was not set
        before the call.

    MISSING[¶](#contextvars.Token.MISSING "Link to this definition")
    :   A marker object used by [`Token.old_value`](#contextvars.Token.old_value "contextvars.Token.old_value").

## Manual Context Management[¶](#manual-context-management "Link to this heading")

contextvars.copy\_context()[¶](#contextvars.copy_context "Link to this definition")
:   Returns a copy of the current [`Context`](#contextvars.Context "contextvars.Context") object.

    The following snippet gets a copy of the current context and prints
    all variables and their values that are set in it:

    ```
    ctx: Context = copy_context()
    print(list(ctx.items()))
    ```

    The function has an *O*(1) complexity, i.e. works equally fast for
    contexts with a few context variables and for contexts that have
    a lot of them.

*class* contextvars.Context[¶](#contextvars.Context "Link to this definition")
:   A mapping of [`ContextVars`](#contextvars.ContextVar "contextvars.ContextVar") to their values.

    `Context()` creates an empty context with no values in it.
    To get a copy of the current context use the
    [`copy_context()`](#contextvars.copy_context "contextvars.copy_context") function.

    Each thread has its own effective stack of `Context` objects. The
    [current context](../glossary.html#term-current-context) is the `Context` object at the top of the
    current thread’s stack. All `Context` objects in the stacks are
    considered to be *entered*.

    *Entering* a context, which can be done by calling its [`run()`](#contextvars.Context.run "contextvars.Context.run")
    method, makes the context the current context by pushing it onto the top of
    the current thread’s context stack.

    *Exiting* from the current context, which can be done by returning from the
    callback passed to the [`run()`](#contextvars.Context.run "contextvars.Context.run") method, restores the current
    context to what it was before the context was entered by popping the context
    off the top of the context stack.

    Since each thread has its own context stack, [`ContextVar`](#contextvars.ContextVar "contextvars.ContextVar") objects
    behave in a similar fashion to [`threading.local()`](threading.html#threading.local "threading.local") when values are
    assigned in different threads.

    Attempting to enter an already entered context, including contexts entered in
    other threads, raises a [`RuntimeError`](exceptions.html#RuntimeError "RuntimeError").

    After exiting a context, it can later be re-entered (from any thread).

    Any changes to [`ContextVar`](#contextvars.ContextVar "contextvars.ContextVar") values via the [`ContextVar.set()`](#contextvars.ContextVar.set "contextvars.ContextVar.set")
    method are recorded in the current context. The [`ContextVar.get()`](#contextvars.ContextVar.get "contextvars.ContextVar.get")
    method returns the value associated with the current context. Exiting a
    context effectively reverts any changes made to context variables while the
    context was entered (if needed, the values can be restored by re-entering the
    context).

    Context implements the [`collections.abc.Mapping`](collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") interface.

    run(*callable*, *\*args*, *\*\*kwargs*)[¶](#contextvars.Context.run "Link to this definition")
    :   Enters the Context, executes `callable(*args, **kwargs)`, then exits the
        Context. Returns *callable*’s return value, or propagates an exception if
        one occurred.

        Example:

        ```
        import contextvars

        var = contextvars.ContextVar('var')
        var.set('spam')
        print(var.get())  # 'spam'

        ctx = contextvars.copy_context()

        def main():
            # 'var' was set to 'spam' before
            # calling 'copy_context()' and 'ctx.run(main)', so:
            print(var.get())  # 'spam'
            print(ctx[var])  # 'spam'

            var.set('ham')

            # Now, after setting 'var' to 'ham':
            print(var.get())  # 'ham'
            print(ctx[var])  # 'ham'

        # Any changes that the 'main' function makes to 'var'
        # will be contained in 'ctx'.
        ctx.run(main)

        # The 'main()' function was run in the 'ctx' context,
        # so changes to 'var' are contained in it:
        print(ctx[var])  # 'ham'

        # However, outside of 'ctx', 'var' is still set to 'spam':
        print(var.get())  # 'spam'
        ```

    copy()[¶](#contextvars.Context.copy "Link to this definition")
    :   Return a shallow copy of the context object.

    var in context
    :   Return `True` if the *context* has a value for *var* set;
        return `False` otherwise.

    context[var]
    :   Return the value of the *var* [`ContextVar`](#contextvars.ContextVar "contextvars.ContextVar") variable.
        If the variable is not set in the context object, a
        [`KeyError`](exceptions.html#KeyError "KeyError") is raised.

    get(*var*[, *default*])[¶](#contextvars.Context.get "Link to this definition")
    :   Return the value for *var* if *var* has the value in the context
        object. Return *default* otherwise. If *default* is not given,
        return `None`.

    iter(context)
    :   Return an iterator over the variables stored in the context
        object.

    len(proxy)
    :   Return the number of variables set in the context object.

    keys()[¶](#contextvars.Context.keys "Link to this definition")
    :   Return a list of all variables in the context object.

    values()[¶](#contextvars.Context.values "Link to this definition")
    :   Return a list of all variables’ values in the context object.

    items()[¶](#contextvars.Context.items "Link to this definition")
    :   Return a list of 2-tuples containing all variables and their
        values in the context object.

## asyncio support[¶](#asyncio-support "Link to this heading")

Context variables are natively supported in [`asyncio`](asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") and are
ready to be used without any extra configuration. For example, here
is a simple echo server, that uses a context variable to make the
address of a remote client available in the Task that handles that
client:

```
import asyncio
import contextvars

client_addr_var = contextvars.ContextVar('client_addr')

def render_goodbye():
    # The address of the currently handled client can be accessed
    # without passing it explicitly to this function.

    client_addr = client_addr_var.get()
    return f'Good bye, client @ {client_addr}\r\n'.encode()

async def handle_request(reader, writer):
    addr = writer.transport.get_extra_info('socket').getpeername()
    client_addr_var.set(addr)

    # In any code that we call is now possible to get
    # client's address by calling 'client_addr_var.get()'.

    while True:
        line = await reader.readline()
        print(line)
        if not line.strip():
            break

    writer.write(b'HTTP/1.1 200 OK\r\n')  # status line
    writer.write(b'\r\n')  # headers
    writer.write(render_goodbye())  # body
    writer.close()

async def main():
    srv = await asyncio.start_server(
        handle_request, '127.0.0.1', 8081)

    async with srv:
        await srv.serve_forever()

asyncio.run(main())

# To test it you can use telnet or curl:
#     telnet 127.0.0.1 8081
#     curl 127.0.0.1:8081
```

### [Table of Contents](../contents.html)

* [`contextvars` — Context Variables](#)
  + [Context Variables](#context-variables)
  + [Manual Context Management](#manual-context-management)
  + [asyncio support](#asyncio-support)

#### Previous topic

[`queue` — A synchronized queue class](queue.html "previous chapter")

#### Next topic

[`_thread` — Low-level threading API](_thread.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/contextvars.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](_thread.html "_thread — Low-level threading API") |
* [previous](queue.html "queue — A synchronized queue class") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `contextvars` — Context Variables
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