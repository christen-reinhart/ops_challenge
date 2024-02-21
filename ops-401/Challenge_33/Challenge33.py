#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 33
# Author: Christen Reinhart
# Date of Latest Revision: 02/21/2024
# Sources: https://chat.openai.com/share/07036ee5-b77a-47d2-8da4-5d30a9a43901
# Purpose: In Python, generating a hash value derived from a target file, uniquely identify file using virustotal


import os

apikey = os.getenv('API_KEY') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
hash = 'D41D8CD98F00B204E9800998ECF8427E' # Set your hash here. 

# This concatenates everything into a working shell statement that gets passed into virustotal-search.py
query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

os.system(query)