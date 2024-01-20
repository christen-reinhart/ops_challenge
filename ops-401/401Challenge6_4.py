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

import os  # Import the os module
from cryptography.fernet import Fernet

# Generate or read the key from a file
key_file_path = 'secret.key'
if not os.path.exists(key_file_path):
    key = Fernet.generate_key()
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)
else:
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()

# Read data from file
data_file_path = 'secret.txt'
with open(data_file_path, 'rb') as file:
    data = file.read()

# Encrypt data
cipher = Fernet(key)
encrypted_data = cipher.encrypt(data)

# Save encrypted data to a different file
encrypted_file_path = 'encrypted_secret.txt'
with open(encrypted_file_path, 'wb') as file:
    file.write(encrypted_data)

