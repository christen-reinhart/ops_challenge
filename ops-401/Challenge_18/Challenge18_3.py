#!/usr/bin/env python3

import zipfile
import paramiko
import getpass
import os

def unzip_with_password(zip_file_path, output_path, password):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(output_path, pwd=password.encode('utf-8'))
        print(f"Successfully extracted files with password: {password}")
        return True
    except zipfile.BadZipFile:
        print("Error: Invalid or corrupted ZIP file.")
        return False
    except zipfile.LargeZipFile as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def brute_force_zip(zip_file_path, output_path, wordlist_path):
    with open(wordlist_path, 'r', errors='ignore') as wordlist:
        for line in wordlist:
            password = line.strip()
            if unzip_with_password(zip_file_path, output_path, password):
                return password  # Successfully extracted, return the password
    return None  # Password not found in the wordlist

def ssh_client():
    try:
        # Your existing SSH client code here...

        # Provide the specific values for testing
        zip_file_path = "test1.zip"
        output_path = "output_folder"
        wordlist_path = "rockyou.txt"

        # Validate file paths
        if not (os.path.isfile(zip_file_path) and os.path.isfile(wordlist_path)):
            print("Error: Invalid file paths.")
            return

        # Perform brute-force attack on the ZIP file
        result = brute_force_zip(zip_file_path, output_path, wordlist_path)

        if result:
            print(f"Password found: {result}")
        else:
            print("Password not found in the wordlist.")

    except paramiko.AuthenticationException as e:
        print("Authentication Failed!")
        print(e)

    # Ensure to close the SSH connection regardless of the outcome
    finally:
        # Replace 'ssh' with your actual SSH connection variable
        # ssh.close()
        pass

if __name__ == "__main__":
    # Removed unused variable assignment
    ssh_client()
