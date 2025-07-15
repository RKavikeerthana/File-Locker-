from cryptography.fernet import Fernet
import os

# Load the key from file
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found. Please generate it using key_generator.py.")
        return None

# Encrypt a file
def encrypt_file():
    key = load_key()
    if not key:
        return

    file_path = input("Enter the name of the file to encrypt (e.g., my_secret.txt): ")

    if not os.path.exists(file_path):
        print("File not found.")
        return

    with open(file_path, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file_path, "wb") as f:
        f.write(encrypted)

    print(f"{file_path} has been encrypted successfully.")

# Decrypt a file
def decrypt_file():
    key = load_key()
    if not key:
        return

    file_path = input("Enter the name of the file to decrypt: ")

    if not os.path.exists(file_path):
        print("File not found.")
        return

    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted_data)
    except Exception:
        print("Decryption failed. Make sure the file was encrypted with the correct key.")
        return

    decrypted_name = input("Enter the name to save the decrypted file as (e.g., decrypted.txt): ")
    with open(decrypted_name, "wb") as f:
        f.write(decrypted)

    print(f"File decrypted successfully as {decrypted_name}.")

# Menu interface
def main():
    while True:
        print("\nFile Locker Menu")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            encrypt_file()
        elif choice == "2":
            decrypt_file()
        elif choice == "3":
            print("Exiting File Locker.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the tool
main()
