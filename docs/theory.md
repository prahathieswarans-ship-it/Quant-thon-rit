# ⚛️ Quantum Theory and Methodology

> **Objective:** Explain the scientific principles behind the Quantum Random Number Generator (QRNG) and describe how they are implemented in this project.

---

# Table of Contents

- [Introduction](#introduction)
- [The Problem with Classical Randomness](#the-problem-with-classical-randomness)
- [The Quantum Solution](#the-quantum-solution)
- [Methodology](#methodology)
  - [Step 1 — Initialization](#step-1--initialization)
  - [Step 2 — Superposition](#step-2--superposition)
  - [Step 3 — Measurement](#step-3--measurement)
- [Implementation Details](#implementation-details)
- [Quantum Circuit Workflow](#quantum-circuit-workflow)
- [Why Quantum Randomness Matters](#why-quantum-randomness-matters)
- [Conclusion](#conclusion)

---

# Introduction

Random numbers are fundamental to modern computing. They power applications including:

- Cryptography
- Secure communications
- Scientific simulations
- Online banking
- Digital signatures
- Authentication protocols

The quality of randomness directly impacts the security of these systems.

Unlike conventional computers, **Quantum Random Number Generators (QRNGs)** derive randomness from the laws of quantum mechanics, making the generated bits fundamentally unpredictable.

---

# The Problem with Classical Randomness

Most computers generate random numbers using **Pseudo-Random Number Generators (PRNGs)**.

Popular algorithms include:

- Mersenne Twister
- Linear Congruential Generator (LCG)
- Xorshift
- PCG

Although these algorithms produce sequences that appear random, they are actually **deterministic**.

Their output depends entirely on an initial value known as the **seed**.

```
Seed
  │
  ▼
Deterministic Algorithm
  │
  ▼
Pseudo-Random Numbers
```

## Security Limitation

If an attacker knows:

- the algorithm
- the initial seed

they can reproduce the entire sequence of generated numbers.

> **Key Insight:** PRNGs simulate randomness—they do not create true randomness.

---

# The Quantum Solution

Our project generates random numbers using **Quantum Mechanics**, where uncertainty is a fundamental property of nature.

The QRNG follows the **Copenhagen Interpretation**, which states that a quantum system does not possess a definite state until it is measured.

Instead, quantum particles exist in a **superposition** of multiple possible states.

Only when a measurement occurs does the wave function collapse into one observable outcome.

---

# Methodology

The QRNG consists of three major stages.

---

# Step 1 — Initialization

Each qubit begins in the ground state.

$$
|0\rangle
$$

This represents a binary value of **0**.

Initially, every qubit is prepared identically before quantum operations begin.

---

# Step 2 — Superposition

A **Hadamard Gate (H)** is applied to every qubit.

The Hadamard transformation is

$$
H|0\rangle=
\frac{1}{\sqrt{2}}
\left(
|0\rangle+|1\rangle
\right)
$$

After this operation, the qubit exists in a perfect superposition.

Instead of representing **0** or **1**, it simultaneously represents both states with equal probability.

```
Before Hadamard

|0>

      │

      ▼

After Hadamard

      50%

|0> ---------

              \
               \
                \
                 \
                  \
                   \
                    \
                     -------- |1>

                      50%
```

---

# Step 3 — Measurement

The quantum state is measured.

Measurement forces the wave function to collapse into one classical state.

According to the **Born Rule**,

$$
P(|0\rangle)=\frac{1}{2}
$$

$$
P(|1\rangle)=\frac{1}{2}
$$

Each measurement produces either

- **0**
- **1**

with equal probability.

Unlike classical algorithms, there is **no hidden deterministic process** deciding the outcome.

The result is **fundamentally unpredictable**.

---

# Quantum Circuit Workflow

```
          Initialize Qubits

                |0>

                  │

                  ▼

        Apply Hadamard Gates

                  │

                  ▼

       Quantum Superposition

                  │

                  ▼

        Perform Measurement

                  │

                  ▼

      True Random Binary Bits
```

---

# Implementation Details

The theoretical model is implemented using **Qiskit**.

## Circuit Configuration

| Parameter | Value |
|-----------|------:|
| Framework | Qiskit |
| Simulator | AerSimulator |
| Number of Qubits | 16 |
| Shots per Batch | 10,000 |
| Total Random Bits | 1,000,000 |

---

## Generation Process

1. Create a 16-qubit quantum circuit.
2. Apply a Hadamard gate to every qubit.
3. Measure all qubits.
4. Execute the circuit using AerSimulator.
5. Repeat multiple batches.
6. Combine all measurement results.
7. Produce approximately **1,000,000** random bits.

---

# Why Quantum Randomness Matters

Quantum randomness offers several advantages over classical methods.

| Classical PRNG | Quantum RNG |
|---------------|------------|
| Deterministic | Truly Random |
| Seed Required | No Seed |
| Predictable | Fundamentally Unpredictable |
| Mathematical Algorithm | Physical Quantum Process |
| Suitable for General Applications | Suitable for High-Security Cryptography |

---

# Applications

The generated quantum random numbers can be used in:

- One-Time Pad Encryption
- AES Key Generation
- Secure Password Generation
- Digital Signatures
- Blockchain Security
- Monte Carlo Simulations
- Scientific Research
- Quantum Cryptography

---

# Conclusion

This project demonstrates how the principles of quantum mechanics can be used to generate **true random numbers**.

By exploiting quantum superposition and wave function collapse, the QRNG produces randomness that cannot be reproduced through deterministic computation.

These quantum-generated random numbers provide a strong foundation for cryptographic systems, particularly applications such as **One-Time Pad (OTP)** encryption, where the quality of randomness directly determines the security of the communication.