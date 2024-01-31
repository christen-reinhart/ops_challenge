#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 17
# Author: Christen Reinhart
# Date of Latest Revision: 01/30/2024
# Sources: https://chat.openai.com/share/10b196e4-6aa3-4072-b3be-8d3d7cddc1a9
# Purpose: In Python, Python brute force tool the capability to Dump the user credential hashes

import ssl
import nltk
import time
import paramiko # need pip install
import getpass

from nltk.corpus import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    nltk.download('words')
    word_list = words.words()
    return word_list
    
def check_for_words(words):
    user_answer = input("Enter a word: ")
    if user_answer in words:
        print("The word is in the dictionary")
    else:
        print("The word is not in the dictionary")
    
def load_external_file():
    password_list = []
    with open('rockyou.txt', 'r') as file: 
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip()
            password_list.append(line)
            print(password_list)
    
def get_host():
    host = input('Enter an SSH Client to connect to or enter for default: ') or "192.168.0.140"
    return host
    
def get_user():
    user = input("Enter a username or enter for default: ") or "christen"
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
        stdin, stoudt, stderr = ssh.exec_command("whoami")
        time.sleep(3)
        output = stdout.read()
        print("-" * 50)
        print(output)
        stdin, stdout, stderr = ssh.exec_command("is -l")
        time.sleep(3)
        output = stdout.read()
        print(output)
        stdin, stdout, stderr = ssh.exec_command("uptime")
        time.sleep(3)
        output = stdout.read()
        print(output)
        print("-" *50)
        
    except paramiko.AutnenticationException as e:
        print("Authentication Failed!")
        print(e)
        
    ssh.close()
        
if __name__ == "__main__":
    external_words = get_words()
    # print (external words)
    # print (word list)
    # check for word(external words)
    #load_external_file()
    ssh_client()