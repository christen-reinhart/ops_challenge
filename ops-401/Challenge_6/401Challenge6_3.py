#!/usr/bin/env python3

# Script name Challenge: 401 Class 6
# Author Name Christen Reinhart
# Date of Latest Revision 01/20/2024
# Sources
# Purpose In Python, Create a Script 

# Prompt the user to select a mode
# Encrypt a file
# Decrypt a file 
# Encrypt a message
# Decrypt a message

# pip install cryptography 

from cryptography.fernet import Fernet # imports cryptography
import os # imports os mudule

# Function to generate or load key
def generate_or_load_key():
    if os.path.isfile("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key

# Function to manually input key
def input_key():
    key_input = input("Enter the key or key file name: ")
    if os.path.isfile(key_input):
        with open(key_input, "rb") as key_file:
            return key_file.read()
    else:
        return key_input.encode()

# Function to encrypt file
def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File {file_path} has been encrypted.")

# Function to decrypt file
def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path.replace(".encrypted", ""), "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print("File decrypted successfully.")
