def multiplicative_cipher(text, key):
    encrypted_text = ""
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character by the key value
            encrypted_text += chr(((ord(char) - 65) * key) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character by the key value
            encrypted_text += chr(((ord(char) - 97) * key) % 26 + 97)
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_text += char
    return encrypted_text

# Example usage:
plaintext = "Hello, World!"
key = 5
cipher_text = multiplicative_cipher(plaintext, key)
print("Encrypted text:", cipher_text)
