#!/usr/bin/env python3

# Script name Challenge: 401 Class 6
# Author Name Christen Reinhart
# Date of Latest Revision 01/17/2024
# Sources
# Purpose In Python, Create a Script 

# Prompt the user to select a mode
# Encrypt a file
# Decrypt a file 
# Encrypt a message
# Decrypt a message

# pip install cryptography 

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
        length=32,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)

    with open(file_path, 'rb') as file:
        plaintext = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as file:
        file.write(salt + ciphertext)

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        data = file.read()

    salt = data[:16]
    ciphertext = data[16:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    with open(file_path[:-4], 'wb') as file:
        file.write(decrypted_text)

def encrypt_string(plaintext, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()

    print("Encrypted Message:", ciphertext)

def decrypt_string(ciphertext, password):
    salt = ciphertext[:16]
    ciphertext = ciphertext[16:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    print("Decrypted Message:", decrypted_text.decode())

def main():
    mode = int(input("Select a mode (1: Encrypt File, 2: Decrypt File, 3: Encrypt Message, 4: Decrypt Message): "))
    password = input("Enter password: ")

    if mode in [1, 2]:
        file_path = input("Enter file path: ")
        if mode == 1:
            encrypt_file(file_path, password)
        elif mode == 2:
            decrypt_file(file_path, password)
    elif mode in [3, 4]:
        message = input("Enter cleartext string: ")
        if mode == 3:
            encrypt_string(message, password)
        elif mode == 4:
            decrypt_string(message, password)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()

