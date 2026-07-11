import numpy as np
from nistrng import *


def validate_randomness(filename):
    print(f"Loading data from {filename}...")

    try:
        with open(filename, 'r') as f:
            binary_string = f.read()
    except FileNotFoundError:
        print(f"[ERROR] Could not find {filename}. Run the generator scripts first!")
        return

    print(f"Total bits loaded: {len(binary_string)}")

    # CRITICAL FIX applied here: Convert directly to int8 array
    binary_sequence = np.array([int(bit) for bit in binary_string], dtype=np.int8)

    eligible_battery = check_eligibility_all_battery(binary_sequence, SP800_22R1A_BATTERY)

    print("\nStarting NIST SP 800-22 Tests. This may take several minutes...")

    results = run_all_battery(binary_sequence, eligible_battery, False)

    print("\n--- NIST SP 800-22 TEST RESULTS ---")
    print(f"{'Test Name':<35} | {'P-Value':<20} | {'Status'}")
    print("-" * 65)

    passed_tests = 0
    for result, elapsed_time in results:
        status = "PASS" if result.passed else "FAIL"
        if result.passed:
            passed_tests += 1

        print(f"{result.name:<35} | {result.score:<20.6f} | {status}")

    print("-" * 65)
    print(f"Total Passed: {passed_tests} / {len(results)}")

    if passed_tests == len(results):
        print("CONCLUSION: The sequence is CRYPTOGRAPHICALLY RANDOM.")
    else:
        print("CONCLUSION: The sequence shows non-random patterns.")


if __name__ == "__main__":
    import os

    # Dynamically find the data folder at the project root
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

    quantum_file = os.path.join(PROJECT_ROOT, "data", "quantum_random_data.txt")

    print("Testing Quantum Data...")
    validate_randomness(quantum_file)

    # Uncomment the lines below to run the classical comparison test
    # classical_file = os.path.join(PROJECT_ROOT, "data", "classical_random_data.txt")
    # print("\nTesting Classical Data...")
    # validate_randomness(classical_file)