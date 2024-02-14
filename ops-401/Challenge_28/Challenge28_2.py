#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 26
# Author: Christen Reinhart
# Date of Latest Revision: 02/12/2024
# Sources: import logging
# Purpose: In Python, Logging capabilities to your Python tool.

import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a file handler for debug logs
debug_handler = logging.FileHandler('debug.log')
debug_handler.setLevel(logging.DEBUG)

# Create a file handler for warning logs
warning_handler = logging.FileHandler('warning.log')
warning_handler.setLevel(logging.WARNING)

# Define the formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Set the formatter for both handlers
debug_handler.setFormatter(formatter)
warning_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(debug_handler)
logger.addHandler(warning_handler)

# Log some messages
logger.debug("This is a debug message")
logger.warning("This is a warning message")

def do_something():
    logger.debug("Doing something!")

if __name__ == "__main__":
    do_something()
