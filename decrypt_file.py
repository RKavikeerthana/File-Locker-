from cryptography.fernet import Fernet

# Load the key
with open("key.key", "rb") as key_file:
    key = key_file.read()

# Create Fernet object
fernet = Fernet(key)

# File to decrypt (make sure this is the encrypted one)
file_to_decrypt = "my_secret.txt"

# Read encrypted content
with open(file_to_decrypt, "rb") as f:
    encrypted_data = f.read()

# Decrypt data
decrypted_data = fernet.decrypt(encrypted_data)

# Save decrypted data to a new file
with open("my_secret_decrypted.txt", "wb") as f:
    f.write(decrypted_data)

print(" File decrypted successfully as 'my_secret_decrypted.txt'")
