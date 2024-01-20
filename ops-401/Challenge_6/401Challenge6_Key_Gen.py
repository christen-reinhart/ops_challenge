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

# generate symmetric key
from cryptography.fernet import Fernet
key = Fernet.generate_key()

# save to file secret.key
with open('secret.key', 'wb') as file:
    file.write(key)