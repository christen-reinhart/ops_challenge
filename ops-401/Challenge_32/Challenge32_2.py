#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 32
# Author: Christen Reinhart
# Date of Latest Revision: 02/20/2024
# Sources: import logging
# Purpose: In Python, Generates hashes of files using hashlib

import os
import platform
import hashlib

def hash_file(filename):
    """This function returns the SHA-1 hash
    of the file passed into it"""

    # Make a hash object
    h = hashlib.sha1()

    # Open file for reading in binary mode
    with open(filename, 'rb') as file:
        # Loop till the end of the file
        chunk = 0
        while chunk != b'':
            # Read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # Return the hex representation of digest
    return h.hexdigest()

def search_file(file_name, directory):
    hits = 0
    files_searched = 0
    if platform.system() == 'Windows':
        directory = directory.replace("/", "\\")
    for root, _, files in os.walk(directory):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                print(f"Found: {file} at {file_path}")
                hash_value = hash_file(file_path)
                print(f"SHA-1 Hash: {hash_value}")
                hits += 1
            files_searched += 1
    print(f"Total files searched: {files_searched}")
    print(f"Total hits found: {hits}")

def main():
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    search_file(file_name, directory)

if __name__ == "__main__":
    main()
