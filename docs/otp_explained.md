# 🔐 Application: Quantum One-Time Pad (OTP)

> **Objective:** Demonstrate a practical application of the Quantum Random Number Generator (QRNG) by using quantum-generated random bits as the encryption key in a **One-Time Pad (OTP)** cryptographic system.

---

# Table of Contents

- [Introduction](#introduction)
- [What is a One-Time Pad?](#what-is-a-one-time-pad)
- [How OTP Works](#how-otp-works)
- [The XOR Operation](#the-xor-operation)
- [Encryption Workflow](#encryption-workflow)
- [Why QRNG Matters](#why-qrng-matters)
- [Project Demonstration](#project-demonstration)
- [Advantages](#advantages)
- [Conclusion](#conclusion)

---

# Introduction

To demonstrate the practical value of our **Quantum Random Number Generator (QRNG)**, we integrated it into a secure communication system based on the **One-Time Pad (OTP)** encryption algorithm.

The One-Time Pad is widely recognized as the **only encryption method that is mathematically proven to achieve perfect secrecy**, provided that its security requirements are fully satisfied.

Our implementation uses **quantum-generated random bits** as the encryption key, ensuring that the key originates from a fundamentally unpredictable physical process rather than a deterministic algorithm.

---

# What is a One-Time Pad?

A **One-Time Pad (OTP)** is a symmetric encryption technique in which:

- the encryption key is exactly the same length as the message,
- each key is used only once,
- the key is completely random,
- the key remains secret.

When these conditions are met, the encrypted message provides **perfect secrecy**, meaning that the ciphertext reveals no information about the original plaintext.

Unlike conventional encryption algorithms, the security of OTP does not depend on computational complexity or the attacker's available computing power.

> **Important:** A correctly implemented One-Time Pad remains theoretically secure even against future quantum computers.

---

# How OTP Works

The encryption process combines the plaintext with the secret key using the **Exclusive-OR (XOR)** operation.

```text
Plaintext
     │
     ▼
Quantum Random Key
     │
     ▼
 XOR Operation
     │
     ▼
Ciphertext
```

The receiver decrypts the message by performing the **same XOR operation** using the identical secret key.

```text
Ciphertext
     │
     ▼
Quantum Random Key
     │
     ▼
 XOR Operation
     │
     ▼
Original Message
```

---

# The XOR Operation

The XOR (Exclusive OR) operator compares two binary values.

| Bit A | Bit B | XOR Result |
|:----:|:----:|:----------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

The rule is simple:

- Equal bits produce **0**
- Different bits produce **1**

Mathematically,

$$
Ciphertext = Plaintext \oplus Key
$$

and

$$
Plaintext = Ciphertext \oplus Key
$$

where

- $\oplus$ denotes the XOR operation.

---

# Example

Suppose we wish to encrypt the binary message

```text
Message

10110110
```

Our Quantum Random Number Generator produces

```text
Quantum Key

01101001
```

Applying XOR gives

```text
Ciphertext

11011111
```

To decrypt,

```text
11011111

XOR

01101001

=

10110110
```

The original message is recovered exactly.

---

# Why QRNG Matters

The security of a One-Time Pad depends entirely on the quality of the encryption key.

A secure OTP requires that the key must satisfy four conditions.

| Requirement | Importance |
|-------------|------------|
| Key length equals message length | Prevents information leakage |
| Key used only once | Prevents reuse attacks |
| Key remains secret | Prevents unauthorized decryption |
| Key is truly random | Ensures perfect secrecy |

Among these, **true randomness** is the most difficult requirement to achieve using conventional computers.

---

# Why Classical PRNGs Are Not Enough

Traditional computers generate keys using **Pseudo-Random Number Generators (PRNGs)**.

Although these generators produce sequences that appear random, they are fundamentally deterministic because they rely on mathematical algorithms and an initial seed.

```text
Seed
 │
 ▼
Mathematical Algorithm
 │
 ▼
Pseudo-Random Key
```

If an attacker discovers the algorithm and seed, the entire key sequence can be reproduced.

This compromises the security of the encrypted communication.

---

# Why Quantum Randomness Is Better

Our QRNG generates keys through **quantum measurement**.

Each bit is produced by measuring a qubit prepared in quantum superposition.

```text
|0>

   │

Hadamard Gate

   │

Superposition

   │

Measurement

   │

Random Bit
```

Because the measurement outcome cannot be predicted before observation, every generated bit is fundamentally random.

This satisfies the most critical requirement of the One-Time Pad.

---

# Project Demonstration

The demonstration follows these steps:

1. Generate quantum random bits.
2. Convert the plaintext into binary.
3. Generate a quantum key of equal length.
4. Encrypt the message using XOR.
5. Produce the ciphertext.
6. Decrypt using the same quantum key.
7. Recover the original message.

```text
Generate QRNG Key
        │
        ▼
Convert Message to Binary
        │
        ▼
Encrypt Using XOR
        │
        ▼
Ciphertext
        │
        ▼
Decrypt with Same Key
        │
        ▼
Original Message
```

---

# Security Comparison

| Property | Classical PRNG Key | Quantum QRNG Key |
|-----------|-------------------|------------------|
| Randomness Source | Mathematical algorithm | Quantum mechanics |
| Requires Seed | Yes | No |
| Predictable | Potentially | Fundamentally unpredictable |
| Suitable for OTP | Limited | Ideal |
| Cryptographic Strength | High (algorithm-dependent) | Extremely high (physics-based) |

---

# Advantages of Quantum OTP

- True randomness generated from quantum mechanics
- No deterministic algorithm behind key generation
- Resistant to prediction and replay
- Supports perfect secrecy when OTP conditions are met
- Suitable for high-security cryptographic applications

---

# Conclusion

This project demonstrates how **Quantum Random Number Generation (QRNG)** can be directly integrated into a **One-Time Pad (OTP)** encryption system.

By replacing deterministic pseudo-random keys with quantum-generated random keys, the implementation satisfies the most challenging requirement of the One-Time Pad: **true randomness**.

The demonstration illustrates how principles of quantum mechanics can strengthen modern cryptographic systems, providing a practical example of quantum technology applied to secure digital communication.

---

# References

1. Claude E. Shannon, *Communication Theory of Secrecy Systems* (1949)
2. NIST SP 800-22 Revision 1a
3. IBM Quantum Documentation
4. Qiskit Documentation
5. Quantum Computation and Quantum Information — Michael A. Nielsen & Isaac L. Chuang