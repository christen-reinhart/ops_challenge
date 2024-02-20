import os
import platform
import hashlib
import time

def hash_file_md5(file_path):
    """This function returns the MD5 hash of the file passed into it"""

    # Make a hash object
    h = hashlib.md5()

    # Open file for reading in binary mode
    with open(file_path, 'rb') as file:
        # Loop till the end of the file
        chunk = 0
        while chunk != b'':
            # Read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # Return the hex representation of digest
    return h.hexdigest()

def search_directory(directory):
    if platform.system() == 'Windows':
        directory = directory.replace("/", "\\")

    # Iterate through all files and directories recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Generate MD5 hash for the file
            md5_hash = hash_file_md5(file_path)

            # Get file size
            file_size = os.path.getsize(file_path)

            # Get file modification timestamp
            mod_time = time.ctime(os.path.getmtime(file_path))

            # Print file information
            print(f"Timestamp: {mod_time}")
            print(f"File Name: {file}")
            print(f"File Size: {file_size} bytes")
            print(f"MD5 Hash: {md5_hash}")
            print(f"File Path: {file_path}")
            print()

def main():
    directory = input("Enter the directory to search in: ")

    search_directory(directory)

if __name__ == "__main__":
    main()
