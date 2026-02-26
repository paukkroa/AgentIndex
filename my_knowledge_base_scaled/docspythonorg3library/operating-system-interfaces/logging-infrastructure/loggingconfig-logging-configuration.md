---
id: 0.0.8.3.1
title: "logging.config— Logging configuration¶"
nav_summary: "`logging.config` – Programmatic logging configuration via dictionaries."
ref: https://docs.python.org/3/library/logging.config.html
ref_type: url
---

# logging.config— Logging configuration¶

The `logging.config` module in Python provides an API for programmatically configuring the logging system via structured dictionaries or files. Its primary function, `dictConfig()`, parses a configuration dictionary (defined by a schema including keys like `version`, `formatters`, `handlers`, `filters`, `loggers`, and `root`) to dynamically set up loggers, handlers, filters, and formatters. Errors (e.g., invalid levels, missing IDs, or unresolved objects) raise exceptions (`ValueError`, `TypeError`, etc.). The `DictConfigurator` class handles parsing and configuration, allowing customization via the `dictConfigClass` attribute. This approach enables flexible, centralized logging setup, especially useful for complex applications or external configuration files (e.g., JSON/YAML). For tutorials, refer to the [Logging How-To Guides](https://docs.python.org/3/howto/logging.html).

---

[Link to original](https://docs.python.org/3/library/logging.config.html)
