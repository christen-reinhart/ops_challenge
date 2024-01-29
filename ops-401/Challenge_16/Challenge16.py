#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 16
# Author Name Christen Reinhart
# Date of Latest Revision 01/29/2024
# Sources https://chat.openai.com/share/ee10763b-db45-4241-a631-97da167ec5a9
# Sources https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
# Purpose In Python, Generating Automated Brute Force Wordlist Attack

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
    nltk.download('words')
    word_list = words.words()
    return word_list    

def check_for_word(words):
    user_answer = input("Enter a word: ")  
    if user_answer in words:
        print("The word is not in the dictionary")
    else:
        print("The word is not in the dictionary")  

if __name__ == "__main__":
    external_words = get_words()
    # print(external_words
    # print(word_list)
    check_for_word(external_words)
    

    

    



    
    