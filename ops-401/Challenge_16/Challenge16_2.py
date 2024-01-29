#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 16
# Author Name Christen Reinhart
# Date of Latest Revision 01/29/2024
# Sources https://chat.openai.com/share/ee10763b-db45-4241-a631-97da167ec5a9
# Sources https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
# Purpose In Python, Generating Automated Brute Force Wordlist Attack

import nltk
from nltk.corpus import words
import time

def offensive_mode(word_list_path):
    try:
        with open(word_list_path, 'r') as file:
            words_list = file.read().splitlines()

        for word in words_list:
            time.sleep(1)  # Add a delay of 1 second between words
            print(word)

    except FileNotFoundError:
        print(f"Error: Word list file '{word_list_path}' not found.")

def defensive_mode(search_string, word_list_path):
    try:
        with open(word_list_path, 'r') as file:
            words_list = file.read().splitlines()

        if search_string in words_list:
            print(f"The string '{search_string}' appears in the word list.")
        else:
            print(f"The string '{search_string}' does not appear in the word list.")

    except FileNotFoundError:
        print(f"Error: Word list file '{word_list_path}' not found.")

if __name__ == "__main__":
    nltk.download('words')  # Download NLTK words dataset

    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")

    mode = input("Enter mode (1 or 2): ")

    if mode == "1":
        word_list_path = input("Enter word list file path: ")
        offensive_mode(word_list_path)

    elif mode == "2":
        search_string = input("Enter string to search: ")
        word_list_path = input("Enter word list file path: ")
        defensive_mode(search_string, word_list_path)

    else:
        print("Invalid mode. Please enter either '1' or '2'.")
