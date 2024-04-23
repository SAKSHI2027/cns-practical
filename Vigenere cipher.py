def vigenere_cipher(text, key):
    encrypted_text = ""
    key_index = 0
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            shift = ord(key[key_index].upper()) - 65
            encrypted_text += chr(((ord(char) - 65 + shift) % 26) + 65)
            key_index = (key_index + 1) % len(key)
        # Check if the character is a lowercase letter
        elif char.islower():
            shift = ord(key[key_index].lower()) - 97
            encrypted_text += chr(((ord(char) - 97 + shift) % 26) + 97)
            key_index = (key_index + 1) % len(key)
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_text += char
    return encrypted_text

# Example usage:
plaintext = "Hello, World!"
key = "KEY"
cipher_text = vigenere_cipher(plaintext, key)
print("Encrypted text:", cipher_text)
