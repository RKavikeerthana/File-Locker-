from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Save the key into a file
with open("key.key", "wb") as key_file:
    key_file.write(key)

print("Encryption key generated and saved as 'key.key'")
