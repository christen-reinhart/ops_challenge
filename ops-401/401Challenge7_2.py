#!/usr/bin/env python3

# Script name Challenge: 401 Class 7
# Author Name Christen Reinhart
# Date of Latest Revision 01/17/2024
# Sources
# Purpose In Python, Create a Script 


from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import os
import getpass
import argparse

def generate_salt(size=16):
    """Generate the salt used for key derivation."""
    return secrets.token_bytes(size)

def derive_key(salt, password):
    """Derive the key from the password using the salt."""
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())

def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    """Generate a key from a password and the salt."""
    if load_existing_salt:
        salt = load_salt()
    elif save_salt:
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    derived_key = derive_key(salt, password)
    return base64.urlsafe_b64encode(derived_key)

def load_salt():
    """Load the salt from the current directory."""
    return open("salt.salt", "rb").read()

def write_key():
    """Generate a key and save it into a file."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the key from the current directory."""
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Encryptor Script with Password and Recursive Folder Encryption/Decryption")
    parser.add_argument("path", help="File or folder path to encrypt/decrypt")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the file or folder")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the file or folder")
    parser.add_argument("-p", "--password", help="Password for encryption/decryption")

    args = parser.parse_args()

    if args.encrypt and args.decrypt:
        raise TypeError("Please specify whether you want to encrypt or decrypt.")
    
    if args.password is None:
        password = getpass.getpass("Enter the password: ")
    else:
        password = args.password

    if args.encrypt:
        key = generate_key(password, salt_size=16, save_salt=True)
    elif args.decrypt:
        key = generate_key(password, load_existing_salt=True)

    path = args.path
    if os.path.isfile(path):
        if args.encrypt:
            encrypt_file(path, key)
            print("File encrypted successfully.")
        elif args.decrypt:
            decrypt_file(path, key)
            print("File decrypted successfully.")
    elif os.path.isdir(path):
        if args.encrypt:
            encrypt_folder(path, key)
        elif args.decrypt:
            decrypt_folder(path, key)
    else:
        print("Invalid file or folder path.") 
