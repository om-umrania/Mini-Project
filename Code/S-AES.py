from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def get_padded_key(key):
    # Ensure the key is properly padded to 16, 24, or 32 bytes
    return pad(key.encode(), AES.block_size)

def encrypt(plain_text, key):
    # Pad the key and plaintext
    padded_key = get_padded_key(key)
    padded_text = pad(plain_text.encode(), AES.block_size)
    
    # Generate a random IV
    iv = get_random_bytes(AES.block_size)
    
    # Create cipher object and encrypt
    cipher = AES.new(padded_key, AES.MODE_CBC, iv)
    encrypted_text = cipher.encrypt(padded_text)
    
    # Return IV + encrypted_text to ensure IV is available for decryption
    return iv + encrypted_text

def decrypt(encrypted_message, key):
    # Separate the IV from the rest of the encrypted message
    iv = encrypted_message[:AES.block_size]
    encrypted_text = encrypted_message[AES.block_size:]
    
    # Pad the key
    padded_key = get_padded_key(key)
    
    # Decrypt
    cipher = AES.new(padded_key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text), AES.block_size)
    
    return decrypted_text.decode()

# Get user input
plain_input = input("Enter the text to be encrypted: ")
key_input = input("Enter in a key (will be padded if not 16, 24, or 32 characters): ")

# Check key length (not strictly necessary with padding but good for demonstration)
if not (16 <= len(key_input) <= 32):
    print("Key must be between 16 and 32 characters for raw AES keys without padding!")
else:
    # Encrypt
    encrypted_message = encrypt(plain_input, key_input)
    print("Encrypted:", encrypted_message)
    
    # Decrypt
    decrypted_message = decrypt(encrypted_message, key_input)
    print("Decrypted:", decrypted_message)
