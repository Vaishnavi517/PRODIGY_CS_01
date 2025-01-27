def caesar_cipher(message, shift, mode):
    """
    Encrypts or decrypts a message using the Caesar cipher algorithm.

    Args:
        message (str): The message to be encrypted or decrypted.
        shift (int): The shift value for the Caesar cipher.
        mode (str): 'e' for encryption or 'd' for decryption.

    Returns:
        str: The encrypted or decrypted message.
    """

    result = ""

    for char in message:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            shift_amount = shift if mode == 'e' else -shift
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char

    return result

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            message = input("Enter the message to be encrypted: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift, 'e')
            print(f"Encrypted message: {encrypted_message}")

        elif choice == '2':
            message = input("Enter the message to be decrypted: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift, 'd')
            print(f"Decrypted message: {decrypted_message}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()