### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](typing.html "typing — Support for type hints") |
* [previous](turtle.html "turtle — Turtle graphics") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Development Tools
* |
* Theme
  Auto
  Light
  Dark
   |

# Development Tools[¶](#development-tools "Link to this heading")

The modules described in this chapter help you write software. For example, the
[`pydoc`](pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.") module takes a module and generates documentation based on the
module’s contents. The [`doctest`](doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") and [`unittest`](unittest.html#module-unittest "unittest: Unit testing framework for Python.") modules contains
frameworks for writing unit tests that automatically exercise code and verify
that the expected output is produced.

The list of modules described in this chapter is:

* [`typing` — Support for type hints](typing.html)
  + [Specification for the Python Type System](typing.html#specification-for-the-python-type-system)
  + [Type aliases](typing.html#type-aliases)
  + [NewType](typing.html#newtype)
  + [Annotating callable objects](typing.html#annotating-callable-objects)
  + [Generics](typing.html#generics)
  + [Annotating tuples](typing.html#annotating-tuples)
  + [The type of class objects](typing.html#the-type-of-class-objects)
  + [Annotating generators and coroutines](typing.html#annotating-generators-and-coroutines)
  + [User-defined generic types](typing.html#user-defined-generic-types)
  + [The `Any` type](typing.html#the-any-type)
  + [Nominal vs structural subtyping](typing.html#nominal-vs-structural-subtyping)
  + [Module contents](typing.html#module-contents)
    - [Special typing primitives](typing.html#special-typing-primitives)
      * [Special types](typing.html#special-types)
      * [Special forms](typing.html#special-forms)
      * [Building generic types and type aliases](typing.html#building-generic-types-and-type-aliases)
      * [Other special directives](typing.html#other-special-directives)
    - [Protocols](typing.html#protocols)
    - [ABCs and Protocols for working with I/O](typing.html#abcs-and-protocols-for-working-with-i-o)
    - [Functions and decorators](typing.html#functions-and-decorators)
    - [Introspection helpers](typing.html#introspection-helpers)
    - [Constant](typing.html#constant)
    - [Deprecated aliases](typing.html#deprecated-aliases)
      * [Aliases to built-in types](typing.html#aliases-to-built-in-types)
      * [Aliases to types in `collections`](typing.html#aliases-to-types-in-collections)
      * [Aliases to other concrete types](typing.html#aliases-to-other-concrete-types)
      * [Aliases to container ABCs in `collections.abc`](typing.html#aliases-to-container-abcs-in-collections-abc)
      * [Aliases to asynchronous ABCs in `collections.abc`](typing.html#aliases-to-asynchronous-abcs-in-collections-abc)
      * [Aliases to other ABCs in `collections.abc`](typing.html#aliases-to-other-abcs-in-collections-abc)
      * [Aliases to `contextlib` ABCs](typing.html#aliases-to-contextlib-abcs)
  + [Deprecation Timeline of Major Features](typing.html#deprecation-timeline-of-major-features)
* [`pydoc` — Documentation generator and online help system](pydoc.html)
* [Python Development Mode](devmode.html)
  + [Effects of the Python Development Mode](devmode.html#effects-of-the-python-development-mode)
  + [ResourceWarning Example](devmode.html#resourcewarning-example)
  + [Bad file descriptor error example](devmode.html#bad-file-descriptor-error-example)
* [`doctest` — Test interactive Python examples](doctest.html)
  + [Simple Usage: Checking Examples in Docstrings](doctest.html#simple-usage-checking-examples-in-docstrings)
  + [Simple Usage: Checking Examples in a Text File](doctest.html#simple-usage-checking-examples-in-a-text-file)
  + [Command-line Usage](doctest.html#command-line-usage)
  + [How It Works](doctest.html#how-it-works)
    - [Which Docstrings Are Examined?](doctest.html#which-docstrings-are-examined)
    - [How are Docstring Examples Recognized?](doctest.html#how-are-docstring-examples-recognized)
    - [What’s the Execution Context?](doctest.html#what-s-the-execution-context)
    - [What About Exceptions?](doctest.html#what-about-exceptions)
    - [Option Flags](doctest.html#option-flags)
    - [Directives](doctest.html#directives)
    - [Warnings](doctest.html#warnings)
  + [Basic API](doctest.html#basic-api)
  + [Unittest API](doctest.html#unittest-api)
  + [Advanced API](doctest.html#advanced-api)
    - [DocTest Objects](doctest.html#doctest-objects)
    - [Example Objects](doctest.html#example-objects)
    - [DocTestFinder objects](doctest.html#doctestfinder-objects)
    - [DocTestParser objects](doctest.html#doctestparser-objects)
    - [TestResults objects](doctest.html#testresults-objects)
    - [DocTestRunner objects](doctest.html#doctestrunner-objects)
    - [OutputChecker objects](doctest.html#outputchecker-objects)
  + [Debugging](doctest.html#debugging)
  + [Soapbox](doctest.html#soapbox)
* [`unittest` — Unit testing framework](unittest.html)
  + [Basic example](unittest.html#basic-example)
  + [Command-Line Interface](unittest.html#command-line-interface)
    - [Command-line options](unittest.html#command-line-options)
  + [Test Discovery](unittest.html#test-discovery)
  + [Organizing test code](unittest.html#organizing-test-code)
  + [Re-using old test code](unittest.html#re-using-old-test-code)
  + [Skipping tests and expected failures](unittest.html#skipping-tests-and-expected-failures)
  + [Distinguishing test iterations using subtests](unittest.html#distinguishing-test-iterations-using-subtests)
  + [Classes and functions](unittest.html#classes-and-functions)
    - [Test cases](unittest.html#test-cases)
    - [Grouping tests](unittest.html#grouping-tests)
    - [Loading and running tests](unittest.html#loading-and-running-tests)
      * [load\_tests Protocol](unittest.html#load-tests-protocol)
  + [Class and Module Fixtures](unittest.html#class-and-module-fixtures)
    - [setUpClass and tearDownClass](unittest.html#setupclass-and-teardownclass)
    - [setUpModule and tearDownModule](unittest.html#setupmodule-and-teardownmodule)
  + [Signal Handling](unittest.html#signal-handling)
* [`unittest.mock` — mock object library](unittest.mock.html)
  + [Quick Guide](unittest.mock.html#quick-guide)
  + [The Mock Class](unittest.mock.html#the-mock-class)
    - [Calling](unittest.mock.html#calling)
    - [Deleting Attributes](unittest.mock.html#deleting-attributes)
    - [Mock names and the name attribute](unittest.mock.html#mock-names-and-the-name-attribute)
    - [Attaching Mocks as Attributes](unittest.mock.html#attaching-mocks-as-attributes)
  + [The patchers](unittest.mock.html#the-patchers)
    - [patch](unittest.mock.html#patch)
    - [patch.object](unittest.mock.html#patch-object)
    - [patch.dict](unittest.mock.html#patch-dict)
    - [patch.multiple](unittest.mock.html#patch-multiple)
    - [patch methods: start and stop](unittest.mock.html#patch-methods-start-and-stop)
    - [patch builtins](unittest.mock.html#patch-builtins)
    - [TEST\_PREFIX](unittest.mock.html#test-prefix)
    - [Nesting Patch Decorators](unittest.mock.html#nesting-patch-decorators)
    - [Where to patch](unittest.mock.html#where-to-patch)
    - [Patching Descriptors and Proxy Objects](unittest.mock.html#patching-descriptors-and-proxy-objects)
  + [MagicMock and magic method support](unittest.mock.html#magicmock-and-magic-method-support)
    - [Mocking Magic Methods](unittest.mock.html#mocking-magic-methods)
    - [Magic Mock](unittest.mock.html#magic-mock)
  + [Helpers](unittest.mock.html#helpers)
    - [sentinel](unittest.mock.html#sentinel)
    - [DEFAULT](unittest.mock.html#default)
    - [call](unittest.mock.html#call)
    - [create\_autospec](unittest.mock.html#create-autospec)
    - [ANY](unittest.mock.html#any)
    - [FILTER\_DIR](unittest.mock.html#filter-dir)
    - [mock\_open](unittest.mock.html#mock-open)
    - [Autospeccing](unittest.mock.html#autospeccing)
    - [Sealing mocks](unittest.mock.html#sealing-mocks)
  + [Order of precedence of `side_effect`, `return_value` and *wraps*](unittest.mock.html#order-of-precedence-of-side-effect-return-value-and-wraps)
* [`unittest.mock` — getting started](unittest.mock-examples.html)
  + [Using Mock](unittest.mock-examples.html#using-mock)
    - [Mock Patching Methods](unittest.mock-examples.html#mock-patching-methods)
    - [Mock for Method Calls on an Object](unittest.mock-examples.html#mock-for-method-calls-on-an-object)
    - [Mocking Classes](unittest.mock-examples.html#mocking-classes)
    - [Naming your mocks](unittest.mock-examples.html#naming-your-mocks)
    - [Tracking all Calls](unittest.mock-examples.html#tracking-all-calls)
    - [Setting Return Values and Attributes](unittest.mock-examples.html#setting-return-values-and-attributes)
    - [Raising exceptions with mocks](unittest.mock-examples.html#raising-exceptions-with-mocks)
    - [Side effect functions and iterables](unittest.mock-examples.html#side-effect-functions-and-iterables)
    - [Mocking asynchronous iterators](unittest.mock-examples.html#mocking-asynchronous-iterators)
    - [Mocking asynchronous context manager](unittest.mock-examples.html#mocking-asynchronous-context-manager)
    - [Creating a Mock from an Existing Object](unittest.mock-examples.html#creating-a-mock-from-an-existing-object)
    - [Using side\_effect to return per file content](unittest.mock-examples.html#using-side-effect-to-return-per-file-content)
  + [Patch Decorators](unittest.mock-examples.html#patch-decorators)
  + [Further Examples](unittest.mock-examples.html#further-examples)
    - [Mocking chained calls](unittest.mock-examples.html#mocking-chained-calls)
    - [Partial mocking](unittest.mock-examples.html#partial-mocking)
    - [Mocking a Generator Method](unittest.mock-examples.html#mocking-a-generator-method)
    - [Applying the same patch to every test method](unittest.mock-examples.html#applying-the-same-patch-to-every-test-method)
    - [Mocking Unbound Methods](unittest.mock-examples.html#mocking-unbound-methods)
    - [Checking multiple calls with mock](unittest.mock-examples.html#checking-multiple-calls-with-mock)
    - [Coping with mutable arguments](unittest.mock-examples.html#coping-with-mutable-arguments)
    - [Nesting Patches](unittest.mock-examples.html#nesting-patches)
    - [Mocking a dictionary with MagicMock](unittest.mock-examples.html#mocking-a-dictionary-with-magicmock)
    - [Mock subclasses and their attributes](unittest.mock-examples.html#mock-subclasses-and-their-attributes)
    - [Mocking imports with patch.dict](unittest.mock-examples.html#mocking-imports-with-patch-dict)
    - [Tracking order of calls and less verbose call assertions](unittest.mock-examples.html#tracking-order-of-calls-and-less-verbose-call-assertions)
    - [More complex argument matching](unittest.mock-examples.html#more-complex-argument-matching)
* [`test` — Regression tests package for Python](test.html)
  + [Writing Unit Tests for the `test` package](test.html#writing-unit-tests-for-the-test-package)
  + [Running tests using the command-line interface](test.html#module-test.regrtest)
* [`test.support` — Utilities for the Python test suite](test.html#module-test.support)
* [`test.support.socket_helper` — Utilities for socket tests](test.html#module-test.support.socket_helper)
* [`test.support.script_helper` — Utilities for the Python execution tests](test.html#module-test.support.script_helper)
* [`test.support.bytecode_helper` — Support tools for testing correct bytecode generation](test.html#module-test.support.bytecode_helper)
* [`test.support.threading_helper` — Utilities for threading tests](test.html#module-test.support.threading_helper)
* [`test.support.os_helper` — Utilities for os tests](test.html#module-test.support.os_helper)
* [`test.support.import_helper` — Utilities for import tests](test.html#module-test.support.import_helper)
* [`test.support.warnings_helper` — Utilities for warnings tests](test.html#module-test.support.warnings_helper)

#### Previous topic

[`turtle` — Turtle graphics](turtle.html "previous chapter")

#### Next topic

[`typing` — Support for type hints](typing.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/development.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](typing.html "typing — Support for type hints") |
* [previous](turtle.html "turtle — Turtle graphics") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Development Tools
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