import time
import os
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def generate_quantum_random_bits(total_bits_needed, output_filename, use_hardware=False):
    """Generates a specified number of true random bits using a quantum circuit."""

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    print(f"Starting Quantum Random Number Generation...")
    print(f"Target: {total_bits_needed} bits")
    print(f"Output File: {output_filename}\n")

    num_qubits = 16
    shots_per_job = 10000
    bits_per_job = num_qubits * shots_per_job
    total_batches = (total_bits_needed // bits_per_job) + 1

    if use_hardware:
        print("Hardware execution requested, but defaulting to simulator for this script.")
        backend = AerSimulator()
    else:
        backend = AerSimulator()
        print("Using Local Simulator: AerSimulator")

    qc = QuantumCircuit(num_qubits, num_qubits)

    for i in range(num_qubits):
        qc.h(i)

    qc.measure(range(num_qubits), range(num_qubits))

    print("\nCircuit Architecture:")
    print(qc.draw(output='text'))

    bits_generated = 0
    start_time = time.time()

    with open(output_filename, 'w') as f:
        f.write("")

    for batch in range(total_batches):
        if bits_generated >= total_bits_needed:
            break

        job = backend.run(qc, shots=shots_per_job, memory=True)
        result = job.result()
        raw_memory = result.get_memory(qc)
        batch_bitstring = "".join(raw_memory)

        with open(output_filename, 'a') as f:
            f.write(batch_bitstring)

        bits_generated += len(batch_bitstring)
        print(f"Batch {batch + 1}/{total_batches} complete. Generated {bits_generated} bits so far...")

    if bits_generated > total_bits_needed:
        with open(output_filename, 'r') as f:
            data = f.read()
        with open(output_filename, 'w') as f:
            f.write(data[:total_bits_needed])
        print(f"\nTrimmed excess bits. Final count exact.")

    end_time = time.time()
    print(f"\n--- Generation Complete ---")
    print(f"Total Bits: {total_bits_needed}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Saved to: {output_filename}")


if __name__ == "__main__":
    TARGET_BITS = 1_000_000

    # Dynamically resolve the path to ensure 'data' is created at the project root
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
    FILENAME = os.path.join(PROJECT_ROOT, "data", "quantum_random_data.txt")

    generate_quantum_random_bits(TARGET_BITS, FILENAME)