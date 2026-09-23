def encrypt_text(text, shift):
    encrypted_text = ""

    for character in text:

        if character.isupper():
            encrypted_character = chr(
                (ord(character) - ord('A') + shift) % 26 + ord('A')
            )
            encrypted_text += encrypted_character

        elif character.islower():
            encrypted_character = chr(
                (ord(character) - ord('a') + shift) % 26 + ord('a')
            )
            encrypted_text += encrypted_character

        else:
            encrypted_text += character

    return encrypted_text


def decrypt_text(text, shift):
    return encrypt_text(text, -shift)


def encrypt_file():
    print("\n---------- FILE ENCRYPTION ----------")

    input_file = input("Enter the file name to encrypt: ").strip()

    try:
        shift = int(input("Enter encryption shift (1-25): "))

        if shift < 1 or shift > 25:
            print("Shift must be between 1 and 25.")
            return

        with open(input_file, "r", encoding="utf-8") as file:
            original_text = file.read()

        encrypted_text = encrypt_text(original_text, shift)

        output_file = input(
            "Enter the name for the encrypted file: "
        ).strip()

        if output_file == "":
            output_file = "encrypted_file.txt"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(encrypted_text)

        print("\nFile encrypted successfully!")
        print("Encrypted file:", output_file)

    except FileNotFoundError:
        print("Error: The specified file was not found.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except ValueError:
        print("Error: Shift must be a number.")


def decrypt_file():
    print("\n---------- FILE DECRYPTION ----------")

    input_file = input("Enter the encrypted file name: ").strip()

    try:
        shift = int(input("Enter the decryption shift (1-25): "))

        if shift < 1 or shift > 25:
            print("Shift must be between 1 and 25.")
            return

        with open(input_file, "r", encoding="utf-8") as file:
            encrypted_text = file.read()

        decrypted_text = decrypt_text(encrypted_text, shift)

        output_file = input(
            "Enter the name for the decrypted file: "
        ).strip()

        if output_file == "":
            output_file = "decrypted_file.txt"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(decrypted_text)

        print("\nFile decrypted successfully!")
        print("Decrypted file:", output_file)

    except FileNotFoundError:
        print("Error: The specified file was not found.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except ValueError:
        print("Error: Shift must be a number.")


def main():

    while True:

        print()
        print("\n FILE ENCRYPTION / DECRYPTION TOOL ")
        
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        print("____________________________________")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            encrypt_file()

        elif choice == "2":
            decrypt_file()

        elif choice == "3":
            print("\nThank you for using the File Encryption Tool.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
