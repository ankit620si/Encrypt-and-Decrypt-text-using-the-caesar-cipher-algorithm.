def caesar_cipher_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            # Preserve case
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Non-alphabet characters remain unchanged
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Encryption/Decryption ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").strip().upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select E or D.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'E':
        result = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {result}")
    else:
        result = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
