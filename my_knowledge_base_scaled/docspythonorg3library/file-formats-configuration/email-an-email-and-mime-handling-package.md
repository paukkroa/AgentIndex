---
id: 0.0.6.5
title: "email— An email and MIME handling package¶"
nav_summary: "The `email` package is a Python standard library module designed for parsing, constructing, and manipulating email messages and MIME (Multipurpose Int"
ref: https://docs.python.org/3/library/email.html
ref_type: url
---

# email— An email and MIME handling package¶

The `email` package is a Python standard library module designed for parsing, constructing, and manipulating email messages and MIME (Multipurpose Internet Mail Extensions) data while adhering to RFC standards. It does **not** handle email transmission (e.g., SMTP) but focuses on message representation and serialization. The package comprises four core components:
1. **Object Model** (`email.message`): A hierarchical tree of `EmailMessage` objects representing email structure (headers, body, attachments) via a unified API.
2. **Parser** (`email.parser`): Converts raw email byte streams (or text) into structured `EmailMessage` objects, supporting RFC 5322 and MIME standards.
3. **Generator** (`email.generator`): Serializes `EmailMessage` objects back into RFC-compliant byte streams for transmission or storage.
4. **Policy Module** (`email.policy`): Configures parsing/generation behavior (e.g., header decoding, charset handling) to ensure compliance with RFCs like 2045–2047 and 2231.

Key features include RFC-compliance (RFC 5322, 6532, MIME

[Link to original](https://docs.python.org/3/library/email.html)
