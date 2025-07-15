# 🔐 Simple File Locker using Python

This is a beginner-friendly project that demonstrates how to encrypt and decrypt files using symmetric encryption with the `cryptography` module in Python. It helps you understand the basics of how file encryption works in real-world security systems.


## 🛠 Requirements

* Python 3.x
* cryptography module
  Install via pip:

  ```bash
  pip install cryptography
  ```

  
## ⚙️ How It Works

### 1. 🔑 **Key Generation**

The `key_generator.py` script generates a secure encryption key using the `Fernet` class from the `cryptography` module. This key is saved in a file named `key.key`.

```bash
python key_generator.py
```

> Output:

```
🔐 Encryption key generated and saved as 'key.key'
```

---

### 2. 🔒 **Encrypt a File**

The `encrypt_file.py` script reads the original file, encrypts its contents, and overwrites it with encrypted data.

```bash
python encrypt_file.py
```

> Output:

```
File 'my_secret.txt' has been encrypted successfully.
```

---

### 3. 🔓 **Decrypt a File**

The `decrypt_file.py` script decrypts the encrypted file using the stored key and creates a new decrypted copy.

```bash
python decrypt_file.py
```

> Output:

```
File decrypted successfully as 'my_secret_decrypted.txt'
```


## Output


### Before encryption:
<img width="288" height="133" alt="Screenshot 2025-07-15 084526" src="https://github.com/user-attachments/assets/caaaabbd-64af-4c20-b46c-c90113449c6a" />




### After encryption:
<img width="1467" height="129" alt="Screenshot 2025-07-15 084424" src="https://github.com/user-attachments/assets/366251aa-ccd0-41ac-a6e9-b9162321c6c2" />




### After decryption:
<img width="288" height="133" alt="Screenshot 2025-07-15 084526" src="https://github.com/user-attachments/assets/a5829230-1398-49be-8d9e-7f5b08e84018" />




## 📚 Learning Outcomes

* Understand symmetric encryption (Fernet).
* Learn how to securely store and retrieve encryption keys.
* Practice file handling in Python.
* Build real-world inspired security applications.



## 🚀 Future Improvements

* Add a password prompt for access control
* Support for encrypting/decrypting entire folders
* Add GUI using Tkinter or PyQt


