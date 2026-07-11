# ⚛️ Quantum Random Number Generation (QRNG)

> **Hackathon Project**  
> Generate **True Random Numbers** using Quantum Computing, validate them using statistical tests, and demonstrate their use in cryptography with a One-Time Pad.

---

# 🏆 Problem Statement

Develop a **Quantum Random Number Generation (QRNG)** system that:

- Generates **true random numbers** using quantum mechanics.
- Validates randomness using statistical tests.
- Demonstrates a real-world security application requiring high-quality randomness.

---

# 🚀 Elevator Pitch

Classical computers cannot generate **true randomness**.

Instead, they use **Pseudo Random Number Generators (PRNGs)**, which are deterministic algorithms and can potentially be predicted if enough internal state is known.

Our project leverages **Quantum Mechanics**, where measurement outcomes are fundamentally unpredictable.

By placing qubits into **superposition** and measuring their collapse, we generate **True Random Numbers (TRNG)** suitable for high-security applications like cryptography.

---

# 🧠 Project Architecture

```
                 +----------------------+
                 | Quantum Circuit      |
                 | (Qiskit)             |
                 +----------+-----------+
                            |
                            v
               Quantum Random Bitstream
                            |
          +-----------------+----------------+
          |                                  |
          v                                  v
 Validation Engine                    OTP Encryption
 (NIST Tests)                     (One-Time Pad Demo)
```

---

# 📂 Project Structure

```
qrng-hackathon/
│
├── src/
│   ├── qrng_generator.py
│   ├── generate_classical_rng.py
│   ├── validate_rng.py
│   └── qrng_otp_app.py
│
├── docs/
│   ├── theory.md
│   ├── statistical_report.md
│   └── otp_explained.md
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Components

## 1️⃣ Quantum Engine

**File**

```text
src/qrng_generator.py
```

### Responsibilities

- Creates a **16-qubit quantum circuit**
- Applies **Hadamard Gates**
- Places every qubit into superposition
- Measures each qubit
- Produces quantum random bits

### Workflow

```
Initialize Qubits
        │
        ▼
Apply Hadamard Gates
        │
        ▼
Create Superposition
        │
        ▼
Quantum Measurement
        │
        ▼
Random Binary Output
```

---

## 2️⃣ Validation Framework

**File**

```text
src/validate_rng.py
```

### Responsibilities

- Load Quantum Random Numbers
- Load Classical PRNG Numbers
- Compare both datasets
- Run statistical randomness tests

### Statistical Tests

- Frequency Test
- Runs Test
- Entropy Analysis
- Bit Distribution
- Additional NIST SP 800-22 tests (if available)

---

## 3️⃣ One-Time Pad Application

**File**

```text
src/qrng_otp_app.py
```

Demonstrates secure communication using a **One-Time Pad (OTP)**.

### Why OTP?

The One-Time Pad is **mathematically unbreakable** when:

- the key is truly random,
- the key is never reused,
- the key length equals the message length.

Our QRNG provides the required truly random key.

---

# 🔐 Encryption Flow

```
Message
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

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/qrng-hackathon.git
```

Move into the project folder:

```bash
cd qrng-hackathon
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Step 1 — Generate Quantum Random Numbers

```bash
python src/qrng_generator.py
```

---

## Step 2 — Generate Classical Random Numbers

```bash
python src/generate_classical_rng.py
```

---

## Step 3 — Validate Randomness

```bash
python src/validate_rng.py
```

This compares:

- Quantum RNG
- Classical PRNG

using statistical randomness tests.

---

## Step 4 — Run One-Time Pad Demo

```bash
python src/qrng_otp_app.py
```

Expected Output

```
Original Message:
HELLO

Quantum Key:
011001001010...

Encrypted:
ÆØ§...

Decrypted:
HELLO
```

---

# 📊 Validation

The generated quantum random numbers are evaluated using statistical randomness tests inspired by the **NIST SP 800-22 Statistical Test Suite**.

The validation process checks:

- Uniform distribution
- Frequency balance
- Run lengths
- Entropy
- Randomness quality

---

# 📚 Documentation

Detailed explanations are available in the `docs/` directory.

| File | Description |
|------|-------------|
| `theory.md` | Quantum physics behind QRNG |
| `statistical_report.md` | Randomness validation results |
| `otp_explained.md` | One-Time Pad cryptography |

---

# 🛠️ Technologies Used

- Python
- Qiskit
- NumPy
- Matplotlib
- NIST Statistical Tests
- IBM Quantum Principles

---

# 🌟 Future Improvements

- IBM Quantum Cloud Integration
- Quantum Hardware Execution
- Live Randomness Dashboard
- QRNG REST API
- AES Key Generation using QRNG
- Quantum Key Distribution (QKD)

---

# 👥 Team

Hackathon Project

**Quantum Random Number Generation (QRNG)**

Built for secure cryptographic applications using quantum mechanics.

---

# 📄 License

This project is released under the MIT License.