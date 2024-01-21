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
# Encrypt Directory Recursively
# Decrypt Directory Recursively


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
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(data)

        with open(file_path + '.enc', 'wb') as file:
            file.write(encrypted_data)
        print("File encrypted successfully.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)

        with open(file_path[:-4], 'wb') as file:
            file.write(decrypted_data)
        print("File decrypted successfully.")
    except Exception as e:
        print(f"Error decrypting file: {e}")

def encrypt_string(plaintext, key):
    try:
        cipher = Fernet(key)
        ciphertext = cipher.encrypt(plaintext.encode())
        print("Encrypted Message:", ciphertext.decode())
    except Exception as e:
        print(f"Error encrypting string: {e}")

def decrypt_string(ciphertext, key):
    try:
        cipher = Fernet(key)
        decrypted_text = cipher.decrypt(ciphertext).decode()
        print("Decrypted Message:", decrypted_text)
    except Exception as e:
        print(f"Error decrypting string: {e}")

def main():
    key = generate_or_read_key()

    mode = int(input("Select a mode (1: Encrypt File, 2: Decrypt File, 3: Encrypt Message, 4: Decrypt Message): "))

    if mode in [1, 2]:
        file_path = input("Enter file path: ")
        if mode == 1:
            encrypt_file(file_path, key)
        elif mode == 2:
            decrypt_file(file_path, key)
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
