#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 16
# Author: Christen Reinhart
# Date of Latest Revision: 01/29/2024
# Sources:
#   - https://chat.openai.com/share/ee10763b-db45-4241-a631-97da167ec5a9
#   - https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
# Purpose: In Python, Generating Automated Brute Force Wordlist Attack

import ssl
import nltk
from nltk.corpus import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    # Download NLTK words dataset
    nltk.download('words')
    # Get the list of words from NLTK
    word_list = words.words()
    return word_list

def check_for_word(words):
    # Prompt the user to enter a word
    user_answer = input("Enter a word: ")
    # Convert both the user's input and words to lowercase for case-insensitive comparison
    user_answer_lower = user_answer.lower()
    words_lower = [word.lower() for word in words]
    
    # Check if the user's word is in the list
    if user_answer_lower in words_lower:
        print("The word is in the dictionary.")
    else:
        print("The word is not in the dictionary.")

if __name__ == "__main__":
    # Get the words from NLTK
    external_words = get_words()
    # Check if a user-entered word is in the NLTK words dataset
    check_for_word(external_words)
