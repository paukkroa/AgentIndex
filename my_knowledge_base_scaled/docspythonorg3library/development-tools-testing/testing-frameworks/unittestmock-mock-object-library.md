---
id: 0.0.14.2.2
title: "unittest.mock— mock object library¶"
nav_summary: "The `unittest"
ref: https://docs.python.org/3/library/unittest.mock.html
ref_type: url
---

# unittest.mock— mock object library¶

The `unittest.mock` library is a powerful Python module (introduced in Python 3.3) designed for unit testing by replacing real system components with **mock objects**. It eliminates the need for manual stub creation by providing the core [`Mock`](#unittest.mock.Mock) class, which dynamically creates attributes/methods on-demand while tracking usage. Key features include:
- **Dynamic mocking**: Attributes/methods appear only when accessed, with configurable return values (e.g., `return_value`, `side_effect`).
- **Side effects**: Simulate exceptions, return dynamic values (e.g., dictionaries, lists), or execute arbitrary logic during calls.
- **Assertions**: Verify method calls (e.g., `assert_called_with`) and arguments.
- **Spec-based mocks**: Restrict mock behavior to match a real object’s interface (via `spec` argument), raising `AttributeError` for invalid accesses.
- **`patch()` decorator/context manager**: Temporarily replaces modules/classes with mocks during tests, scoped to test functions or blocks.
- **`MagicMock`**: A subclass of `Mock` with enhanced features (e.g., auto-creation of nested attributes).
- **`sentinel`

[Link to original](https://docs.python.org/3/library/unittest.mock.html)
