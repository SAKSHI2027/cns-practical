def prepare_text(text):
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "").upper()
    # Replace 'J' with 'I' (standard Playfair cipher rule)
    text = text.replace("J", "I")
    # Split text into pairs of characters
    pairs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            pairs.append(text[i] + 'X')
            i += 1
        else:
            pairs.append(text[i] + (text[i + 1] if i + 1 < len(text) else 'X'))
            i += 2
    return pairs

def generate_matrix(key):
    # Create the 5x5 matrix based on the keyword
    key = key.replace("J", "I")  # Replace 'J' with 'I'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Use 25-letter alphabet (exclude 'J')
    key = "".join(dict.fromkeys(key))  # Remove duplicates from key
    key = key + alphabet
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    return matrix

def find_position(matrix, char):
    # Find position of a character in the matrix
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))
    return None

def playfair_cipher(text, key):
    text_pairs = prepare_text(text)
    matrix = generate_matrix(key)
    encrypted_text = ""
    for pair in text_pairs:
        a, b = pair[0], pair[1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:  # Same row
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle rule
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return encrypted_text

# Example usage:
plaintext = "HELLO WORLD"
key = "KEYWORD"
cipher_text = playfair_cipher(plaintext, key)
print("Encrypted text:", cipher_text)
