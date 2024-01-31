#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 18
# Author: Christen Reinhart
# Date of Latest Revision: 01/31/2024
# Sources: https://chat.openai.com/share/10b196e4-6aa3-4072-b3be-8d3d7cddc1a9
# Purpose: In Python, Finish developing a custom tool that performs brute force attacks.

import ssl
import nltk
import time
import zipfile
import paramiko
import getpass

def unzip_with_password(zip_file_path, output_path, password):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(output_path, pwd=password.encode('utf-8'))
        print(f"Successfully extracted files with password: {password}")
        return True
    except zipfile.BadZipFile:
        return False  # Invalid or corrupted ZIP file
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

        # Prompt the user for the path to the password-protected ZIP file
        zip_file_path = input("Enter the path to the password-protected ZIP file: ")
        # Prompt the user for the output path for extracting files
        output_path = input("Enter the output path for extracting files: ")
        # Prompt the user for the path to the wordlist (e.g., RockYou.txt)
        wordlist_path = input("Enter the path to the wordlist (e.g., RockYou.txt): ")

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
        ssh.close()

if __name__ == "__main__":
    # Removed unused variable assignment
    ssh_client()

