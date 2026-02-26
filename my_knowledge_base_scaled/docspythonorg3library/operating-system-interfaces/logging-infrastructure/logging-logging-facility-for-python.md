---
id: 0.0.8.3.0
title: "logging— Logging facility for Python¶"
nav_summary: "Python’s hierarchical logging module with loggers, handlers, filters, formatters."
ref: https://docs.python.org/3/library/logging.html
ref_type: url
---

# logging— Logging facility for Python¶

The **`logging`** module in Python provides a flexible, hierarchical event logging system designed for applications and libraries. It enables standardized logging across modules, allowing integration of application logs with third-party modules. Core components include **loggers** (interface for application code), **handlers** (direct log records to destinations like files or consoles), **filters** (fine-tune log output based on criteria), and **formatters** (define log record layouts). Loggers are created via `logging.getLogger(__name__)` and follow a hierarchical structure, forwarding messages upward to parent loggers (e.g., the root logger). Configuration is essential—methods like `basicConfig()` simplify root logger setup for common use cases, while deeper customization requires configuring log levels, handlers, and formatters. The module supports advanced features like log rotation, asynchronous logging, and custom destinations, making it extensible for diverse applications.

---

[Link to original](https://docs.python.org/3/library/logging.html)
