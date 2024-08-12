def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = ord(char) + shift_amount
            if char.islower():
                if shifted_char > ord('z'):
                    shifted_char -= 26
            elif char.isupper():
                if shifted_char > ord('Z'):
                    shifted_char -= 26
            encrypted_text += chr(shifted_char)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = ord(char) - shift_amount
            if char.islower():
                if shifted_char < ord('a'):
                    shifted_char += 26
            elif char.isupper():
                if shifted_char < ord('A'):
                    shifted_char += 26
            decrypted_text += chr(shifted_char)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")

        another = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
