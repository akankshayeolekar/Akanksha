def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Example usage:
message = "Hello World"
shift = 3
encrypted = caesar_cipher(message, shift, mode='encrypt')
decrypted = caesar_cipher(encrypted, shift, mode='decrypt')

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)