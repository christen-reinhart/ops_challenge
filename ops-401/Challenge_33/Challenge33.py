#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 32
# Author: Christen Reinhart
# Date of Latest Revision: 02/20/2024
# Sources: https://chat.openai.com/share/07036ee5-b77a-47d2-8da4-5d30a9a43901
# Purpose: In Python, Generates hashes of files using hashlib

# The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
# Set your environment variable first to keep it out of your script here.

import os

apikey = os.getenv('API_KEY') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
hash = 'D41D8CD98F00B204E9800998ECF8427E' # Set your hash here. 

# This concatenates everything into a working shell statement that gets passed into virustotal-search.py
query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

os.system(query)