from pyDes import des, PAD_PKCS5, ECB

def des_encrypt(plaintext, key):
    # Initialize DES cipher object
    cipher = des(key, ECB, padmode=PAD_PKCS5)
    # Encrypt the plaintext
    encrypted_text = cipher.encrypt(plaintext)
    return encrypted_text

# Example usage:
plaintext = b"Hello, World!"  # Note: Input should be bytes
key = b"12345678"  # 64-bit key (8 bytes)
cipher_text = des_encrypt(plaintext, key)
print("Encrypted text:", cipher_text)
