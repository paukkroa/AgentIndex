---
id: 0.0.19.2
title: "random— Generate pseudo-random numbers¶"
nav_summary: "`random` module: Pseudo-random number generation (Mersenne Twister, distributions)."
ref: https://docs.python.org/3/library/random.html
ref_type: url
---

# random— Generate pseudo-random numbers¶

The `random` module in Python provides pseudo-random number generation for various statistical distributions, leveraging the **Mersenne Twister algorithm** (a 53-bit precision generator with a period of **2¹⁹⁹³⁷–1**) as its core. Key features include uniform integer selection, permutations, sampling without replacement, and distributions like **uniform, normal (Gaussian), lognormal, exponential, gamma, beta, and von Mises**. The module exposes a hidden `Random` class (instantiable for isolated generators) and `SystemRandom` (using OS-level entropy via `os.urandom`). While thread-safe, concurrent calls may degrade performance; separate instances per thread are recommended. **Security warnings**: Avoid for cryptographic use; prefer the `secrets` module instead.

---

[Link to original](https://docs.python.org/3/library/random.html)
