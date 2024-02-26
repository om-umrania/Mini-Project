import pyDes
from time import time
import timeit

def main():
    # Prompt the user for plaintext input
    data = input("Please enter plain text for encryption: ").encode('utf-8')

    # Prompt the user for a key
    keystring = input("Enter a 16 or 24 byte string for key generation: ").encode('utf-8')

    # Validate key length
    if len(keystring) not in [16, 24]:
        print("Key must be either 16 or 24 bytes long.")
        return

    # Initialize Triple DES cipher
    try:
        k = pyDes.triple_des(keystring, pyDes.CBC, IV=None, pad=None, padmode=pyDes.PAD_PKCS5)
    except ValueError as e:
        print(f"Error initializing triple DES: {e}")
        return

    # Encrypt the data
    encrypted_data = k.encrypt(data)
    print(f"Cipher text: {repr(encrypted_data)}")

    # Decrypt the data
    decrypted_data = k.decrypt(encrypted_data)
    print(f"Plain text: {repr(decrypted_data)}")

    # Measure encryption time for 1,000 iterations
    start_time = timeit.default_timer()
    for _ in range(1000):
        _ = k.encrypt(data)
    end_time = timeit.default_timer()

    print(f"Elapsed time for 1,000 encryptions: {end_time - start_time:.3f}s")

if __name__ == "__main__":
    main()
