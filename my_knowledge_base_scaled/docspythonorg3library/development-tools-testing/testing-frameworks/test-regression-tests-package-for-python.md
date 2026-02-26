---
id: 0.0.14.2.4
title: "test— Regression tests package for Python¶"
nav_summary: "Internal Python regression tests: `test`, `test.support`, `test.regrtest` modules."
ref: https://docs.python.org/3/library/test.html
ref_type: url
---

# test— Regression tests package for Python¶

The `test` package is an internal Python module exclusively for regression testing within the standard library, intended solely for core developers. It includes the core regression test suite, along with supporting modules like `test.support` (for test utilities) and `test.regrtest` (the test runner). Modules prefixed with `test_` represent individual test suites for specific Python features. Tests should adhere to modern frameworks like `unittest` or `doctest`, though legacy tests may use deprecated `sys.stdout`-based comparisons. Key conventions include naming test modules with `test_<module>`, test methods with `test_<description>`, and avoiding docstrings (replaced by comments). The `unittest` boilerplate provides setup/teardown hooks and structured test classes for maintainability.

---

[Link to original](https://docs.python.org/3/library/test.html)
