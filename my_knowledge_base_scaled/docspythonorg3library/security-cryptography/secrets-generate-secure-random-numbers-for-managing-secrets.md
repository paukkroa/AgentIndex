---
id: 0.0.7.3
title: "secrets— Generate secure random numbers for managing secrets¶"
nav_summary: "`secrets` module: cryptographically secure random tokens & numbers."
ref: https://docs.python.org/3/library/secrets.html
ref_type: url
---

# secrets— Generate secure random numbers for managing secrets¶

The `secrets` module in Python (introduced in **v3.6**) provides cryptographically secure random number generation, essential for managing sensitive data like passwords, tokens, and authentication keys. Unlike the `random` module—designed for simulations—`secrets` leverages the OS’s highest-quality randomness sources via `SystemRandom`, ensuring resistance to predictability attacks. Key features include:
- **Core Functions**: `choice()` (selects from sequences), `randbelow()` (generates bounded integers), and `randbits()` (produces bit-length integers).
- **Token Generation**: Secure byte strings (`token_bytes`), hex-encoded strings (`token_hex`), and URL-safe Base64 strings (`token_urlsafe`), with configurable entropy (default: `DEFAULT_ENTROPY`). Tokens must balance length (e.g., 16+ bytes) and entropy to thwart brute-force attacks. See [PEP 506](https://peps.python.org/pep-0506/) for design rationale.

---

[Link to original](https://docs.python.org/3/library/secrets.html)
