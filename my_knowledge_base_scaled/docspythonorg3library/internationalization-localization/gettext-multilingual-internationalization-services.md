---
id: 0.0.12.1
title: "gettext— Multilingual internationalization services¶"
nav_summary: "The `gettext` module in Python provides robust **multilingual internationalization (I18N)** and **localization (L10N)** services, enabling application"
ref: https://docs.python.org/3/library/gettext.html
ref_type: url
---

# gettext— Multilingual internationalization services¶

The `gettext` module in Python provides robust **multilingual internationalization (I18N)** and **localization (L10N)** services, enabling applications to dynamically switch languages based on user preferences or system settings. It supports two APIs: the **GNU `gettext` API** (for global application-wide translations) and a **class-based API** (ideal for modular or dynamic language switching). Key functions include:
- **`bindtextdomain(domain, localedir)`**: Binds a translation domain to a directory containing `.mo` binary catalogs (e.g., `localedir/language/LC_MESSAGES/domain.mo`), with fallback to environment variables (`LANGUAGE`, `LC_ALL`, etc.).
- **`textdomain(domain)`**: Sets/gets the global translation domain.
- **`gettext(message)`**: Retrieves localized translations (often aliased as `_()` for convenience).
- **`dgettext(domain, message)`**: Domain-specific translation lookup.
- **`ngettext(singular, plural, n)`**: Handles plural forms via language-specific formulas (e.g., for Spanish or Russian).
- **`dngettext(domain, singular, plural,

[Link to original](https://docs.python.org/3/library/gettext.html)
