import random
import time
import os


def generate_classical_random_bits(total_bits_needed, output_filename):
    """Generates pseudo-random bits using Python's standard PRNG."""

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    print(f"Starting Classical Pseudo-Random Number Generation (PRNG)...")
    print(f"Target: {total_bits_needed} bits")
    print(f"Output File: {output_filename}\n")

    start_time = time.time()

    random_int = random.getrandbits(total_bits_needed)
    binary_string = bin(random_int)[2:].zfill(total_bits_needed)
    binary_string = binary_string[:total_bits_needed]

    with open(output_filename, 'w') as f:
        f.write(binary_string)

    end_time = time.time()

    print(f"\n--- Generation Complete ---")
    print(f"Total Bits Generated: {len(binary_string)}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Saved to: {output_filename}")


if __name__ == "__main__":
    TARGET_BITS = 1_000_000

    # Dynamically resolve the path to ensure 'data' is created at the project root
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
    FILENAME = os.path.join(PROJECT_ROOT, "data", "classical_random_data.txt")

    generate_classical_random_bits(TARGET_BITS, FILENAME)