#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 28
# Author: Christen Reinhart
# Date of Latest Revision: 02/14/2024
# Sources: import logging
# Purpose: In Python, Implement Logging capabilities, FileHandler and StreamHandler

import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a file handler set its level to DEBUG
file_handler = logging.FileHandler('bruteforce.log')
file_handler.setLevel(logging.DEBUG)

# Create a stream handler and set its level to INFO
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# Define formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Set the formatter for handlers
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Log some messages
logger.info("Hello, World")
logger.warning("THIS IS A WARNING!")

def do_something():
    logger.debug("Doing something!")

if __name__ == "__main__":
    do_something()
