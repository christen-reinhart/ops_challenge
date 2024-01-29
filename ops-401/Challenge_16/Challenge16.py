#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 16
# Author Name Christen Reinhart
# Date of Latest Revision 01/29/2024
# Sources https://chat.openai.com/share/ee10763b-db45-4241-a631-97da167ec5a9
# Sources https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
# Purpose In Python, Generating Automated Brute Force Wordlist Attack

import ssl
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    nltk.download('words')

if __name__ == "__main__":
    get_words()

    

    



    
    