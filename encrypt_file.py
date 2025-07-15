from cryptography.fernet import Fernet

# Load the key
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# File to encrypt (Change filename if needed)
file_to_encrypt = "my_secret.txt"

# Read the original data
with open(file_to_encrypt, "rb") as f:
    original = f.read()

# Encrypt the data
encrypted = fernet.encrypt(original)

# Write the encrypted data back to the file
with open(file_to_encrypt, "wb") as f:
    f.write(encrypted)

print(f" '{file_to_encrypt}' has been encrypted successfully.")
