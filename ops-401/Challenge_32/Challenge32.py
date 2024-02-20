#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 31
# Author: Christen Reinhart
# Date of Latest Revision: 02/19/2024
# Sources: import logging
# Purpose: In Python, Generates hashes of files using hashlib 

# Import libraries
import hashlib
from sys import platform
import os, time

# Declare functions

# Function takes filename and produce hash
def hash_file(filename):
    
    # Create hash object
    h =  hashlib.sha1()
    
    # Open file for reading in binary mode
    with open(filename, 'rb') as file:
        
        # Loop until end of file
        chunk = 0
        while chunk != b'':
            # read 1024 bytes at a time
            chunk = file.read(1024)
            print(chunk)
            h.update(chunk)
            
        # Return hex rep of hash
        return h.hexdigest()
    
  # substitute file name for function
message = hash_file("file.log")
print(message)
  
    
            
            
            
