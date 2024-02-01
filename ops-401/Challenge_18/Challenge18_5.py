#!/usr/bin/env python3

import ssl
import paramiko
import getpass
from zipfile import ZipFile
import os

def unzip_with_password(zip_file_path, output_path, password):
    """
    Attempt to unzip a ZIP file with the given password.

    Args:
    - zip_file_path (str): Path to the password-protected ZIP file.
    - output_path (str): Path to the output directory for extracting files.
    - password (str): Password to try for unzipping.

    Returns:
    - bool: True if extraction is successful, False otherwise.
    """
    try:
        with ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(output_path, pwd=password.encode('utf-8'))
        print(f"Successfully extracted files with password: {password}")
        return True
    except FileNotFoundError:
        print(f"Error: ZIP file '{zip_file_path}' not found.")
    except zipfile.BadZipFile:
        print(f"Error: Invalid or corrupted ZIP file: {zip_file_path}")
    except zipfile.LargeZipFile as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return False

def brute_force_zip(zip_file_path, output_path, wordlist_path):
    """
    Brute force attack on a ZIP file using a wordlist.

    Args:
    - zip_file_path (str): Path to the password-protected ZIP file.
    - output_path (str): Path to the output directory for extracting files.
    - wordlist_path (str): Path to the wordlist file.

    Returns:
    - str or None: Password if found, None if not found.
    """
    with open(wordlist_path, 'r', errors='ignore') as wordlist:
        for line in wordlist:
            password = line.strip()
            if unzip_with_password(zip_file_path, output_path, password):
                return password  # Successfully extracted, return the password
    return None  # Password not found in the wordlist

def ssh_client():
    """
    Main function for handling SSH connection and ZIP file brute-force attack.
    """
    try:
        # Your existing SSH client code here...

        # Prompt the user for the path to the password-protected ZIP file
        zip_file_path = input("Enter the path to the password-protected ZIP file: ").strip()
        # Prompt the user for the output path for extracting files
        output_path = input("Enter the output path for extracting files: ").strip()
        # Prompt the user for the path to the wordlist (e.g., RockYou.txt)
        wordlist_path = input("Enter the path to the wordlist (e.g., RockYou.txt): ").strip()

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
