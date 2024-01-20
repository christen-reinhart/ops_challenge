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

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_string(input_string, key):
    f = Fernet(key)
    encrypted = f.encrypt(input_string.encode())
    print("Encrypted String:", encrypted.decode())

def decrypt_string(encrypted_string, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_string.encode())
    print("Decrypted String:", decrypted.decode())

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
    print("Folder encrypted successfully.")

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
    print("Folder decrypted successfully.")

def main():
    if not os.path.isfile("key.key"):
        write_key()

    key = load_key()

    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Recursively Encrypt a folder and its contents")
    print("6. Recursively Decrypt a folder")

    mode = int(input("Enter mode (1-6): "))

    if mode == 1 or mode == 2:
        file_path = input("Enter the filepath to the target file: ")
        if mode == 1:
            encrypt_file(file_path, key)
            print("File encrypted successfully.")
        elif mode == 2:
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
    elif mode == 3 or mode == 4:
        input_text = input("Enter the cleartext string: ")
        if mode == 3:
            encrypt_string(input_text, key)
        elif mode == 4:
            decrypt_string(input_text, key)
    elif mode == 5:
        folder_path = input("Enter the folder path to be encrypted: ")
        encrypt_folder(folder_path, key)
    elif mode == 6:
        folder_path = input("Enter the folder path to be decrypted: ")
        decrypt_folder(folder_path, key)

if __name__ == "__main__":
    main()
