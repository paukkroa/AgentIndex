---
id: 0.0.0.0.1
title: "Built-in Exceptions¶"
nav_summary: "The **Built-in Exceptions** page in Python’s standard library documents the core exception classes derived from [`BaseException`](https://docs"
ref: https://docs.python.org/3/library/exceptions.html
ref_type: url
---

# Built-in Exceptions¶

The **Built-in Exceptions** page in Python’s standard library documents the core exception classes derived from [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException), which serve as error-handling mechanisms in `try-except` blocks. Key concepts include:
1. **Exception Hierarchy**: Exceptions are class-based; catching a parent class (e.g., `Exception`) handles all derived subclasses, but unrelated exceptions remain distinct. Built-in exceptions are raised by the interpreter or built-in functions and often include an "associated value" (e.g., error strings or tuples) passed to their constructors.
2. **Exception Context**: Exception objects feature attributes like `__context__`, `__cause__`, and `__suppress_context__` to track nested error chains. The `raise new_exc from original_exc` syntax explicitly links exceptions, while `__cause__` overrides implicit context for debugging clarity.
3. **Customization**: Users can subclass built-in exceptions (preferably from `Exception`, not `BaseException`) to define new errors. The page also references [User-defined Exceptions](https://docs.python.org/3/tutorial/errors.html#tut-userexceptions) for further guidance.

---

**

[Link to original](https://docs.python.org/3/library/exceptions.html)
