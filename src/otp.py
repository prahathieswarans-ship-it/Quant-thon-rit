import os
import sys


def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)


def binary_to_text(binary_str):
    chars = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if len(char) == 8)


def xor_binary_strings(bin1, bin2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bin1, bin2))


def encrypt_message(message, random_file):
    message_bin = text_to_binary(message)
    bits_needed = len(message_bin)

    if not os.path.exists(random_file):
        print(f"\n[ERROR] Key file '{random_file}' not found. Generate it first!")
        return None, None

    file_size = os.path.getsize(random_file)
    if file_size < bits_needed:
        print(f"\n[ERROR] Not enough random bits! Need {bits_needed}, but file has {file_size}.")
        return None, None

    with open(random_file, 'r') as f:
        key_bin = f.read(bits_needed)

    ciphertext_bin = xor_binary_strings(message_bin, key_bin)
    return ciphertext_bin, key_bin


def decrypt_message(ciphertext_bin, key_bin):
    decrypted_bin = xor_binary_strings(ciphertext_bin, key_bin)
    return binary_to_text(decrypted_bin)


def main():
    print("=" * 65)
    print("   QUANTUM RANDOM NUMBER GENERATOR (QRNG) - SECURITY DEMO")
    print("           Unbreakable One-Time Pad (OTP) Encryption")
    print("=" * 65)

    # Dynamically find the data folder at the project root
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
    QUANTUM_FILE = os.path.join(PROJECT_ROOT, "data", "quantum_random_data.txt")

    while True:
        print("\nMain Menu:")
        print("1. Encrypt a Secret Message")
        print("2. Exit")

        choice = input("Select an option (1-2): ")

        if choice == '1':
            message = input("\nEnter the secret message to encrypt: ")
            print(f"\n[SYSTEM] Connecting to Quantum Key Database ({QUANTUM_FILE})...")

            ciphertext_bin, key_bin = encrypt_message(message, QUANTUM_FILE)

            if ciphertext_bin:
                print("\n" + "-" * 40)
                print("🔒 ENCRYPTION SUCCESSFUL")
                print("-" * 40)

                message_bin = text_to_binary(message)
                print(f"Message Binary : {message_bin[:64]}... (truncated)")
                print(f"Quantum Key    : {key_bin[:64]}... (truncated)")
                print(f"Ciphertext (XOR): {ciphertext_bin[:64]}... (truncated)")

                hex_cipher = hex(int(ciphertext_bin, 2))[2:].upper()
                print(f"\nEncrypted Hex Payload:\n{hex_cipher}")

                print("\n[SYSTEM] To decrypt, the receiver needs the EXACT Quantum Key.")
                input("\nPress ENTER to simulate sending over the network and decrypting...")

                print("\n" + "-" * 40)
                print("🔓 DECRYPTION PROCESS")
                print("-" * 40)
                decrypted_message = decrypt_message(ciphertext_bin, key_bin)
                print(f"Applying Quantum Key...")
                print(f"Recovered Message: >> {decrypted_message} <<")

        elif choice == '2':
            print("\nExiting QRNG Secure System. Goodbye!")
            sys.exit(0)
        else:
            print("\n[ERROR] Invalid choice. Try again.")


if __name__ == "__main__":
    main()