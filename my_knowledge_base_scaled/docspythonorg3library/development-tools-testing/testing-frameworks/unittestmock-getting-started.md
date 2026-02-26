---
id: 0.0.14.2.3
title: "unittest.mock— getting started¶"
nav_summary: "`unittest.mock: mock objects for testing dependencies`"
ref: https://docs.python.org/3/library/unittest.mock-examples.html
ref_type: url
---

# unittest.mock— getting started¶

The `unittest.mock` module, introduced in Python 3.3, provides tools for creating **mock objects** to isolate units of code during testing. Key features include:
- **Mocking methods** to verify correct usage via `Mock`/`MagicMock` objects, enabling assertions like `assert_called_with()` or `assert_called_once_with()` to validate arguments.
- **Patching objects** by replacing methods (e.g., `real.method = MagicMock()`) or entire classes to simulate dependencies.
- **Recording method calls** on objects passed to functions, allowing inspection of interactions (e.g., `mock.close.assert_called_with()`).
- **Lazy attribute creation**—mock methods/attributes are dynamically generated when accessed, ensuring flexibility.
- **Class mocking**—replace entire classes (e.g., via `patch`) to simulate external dependencies, with instances created via the mock class.

Use cases range from verifying method calls to testing object interactions or replacing external dependencies entirely.

---

[Link to original](https://docs.python.org/3/library/unittest.mock-examples.html)
