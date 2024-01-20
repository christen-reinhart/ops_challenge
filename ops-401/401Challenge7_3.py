#!/usr/bin/env python3

# Script name Challenge: 401 Class 7
# Author Name Christen Reinhart
# Date of Latest Revision 01/17/2024
# Sources
# Purpose In Python, Create a Script 

# Prompt the user to select a mode
# Encrypt a file
# Decrypt a file 
# Encrypt a message
# Decrypt a message

from cryptography.fernet import Fernet
import os

def generate_or_read_key():
    key_file_path = 'secret.key'
    if not os.path.exists(key_file_path):
        key = Fernet.generate_key()
        with open(key_file_path, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(key_file_path, 'rb') as key_file:
            key = key_file.read()
    return key

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    with open(file_path + '.enc', 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)

    with open(file_path[:-4], 'wb') as file:
        file.write(decrypted_data)

def encrypt_string(plaintext, key):
    cipher = Fernet(key)
    ciphertext = cipher.encrypt(plaintext.encode())
    print("Encrypted Message:", ciphertext)

def decrypt_string(ciphertext, key):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(ciphertext).decode()
    print("Decrypted Message:", decrypted_text)

def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def decrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

def main():
    key = generate_or_read_key()

    mode = int(input("Select a mode (1: Encrypt File, 2: Decrypt File, 3: Encrypt Message, 4: Decrypt Message, 5: Encrypt Directory, 6: Decrypt Directory): "))

    if mode in [1, 2]:
        file_path = input("Enter file or directory path: ")
        if os.path.isfile(file_path):
            if mode == 1:
                encrypt_file(file_path, key)
            elif mode == 2:
                decrypt_file(file_path, key)
        elif os.path.isdir(file_path):
            if mode == 5:
                encrypt_directory(file_path, key)
            elif mode == 6:
                decrypt_directory(file_path, key)
    elif mode in [3, 4]:
        message = input("Enter cleartext string: ")
        if mode == 3:
            encrypt_string(message, key)
        elif mode == 4:
            decrypt_string(message.encode(), key)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
