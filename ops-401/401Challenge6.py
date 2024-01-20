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

# pip install
from cryptography.fernet import Fernet
# read key from file

key = ''
with open('secret.key', "rb") as file:
    key = file.read()
# read from file
data = ''
with open('secret.txt', 'rb') as file:
    data = file.read()
    
# encrypt data
from cryptography.fernet import Ferent 

f = Fernet(key)

encryptedData = f.encrypt(data)

# save encrypted data
with open('secret.txt', 'wb') as file:
    file.write(encryptedData)



