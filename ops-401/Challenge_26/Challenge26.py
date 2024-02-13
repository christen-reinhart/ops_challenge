#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 26
# Author: Christen Reinhart
# Date of Latest Revision: 02/12/2024
# Sources: import logging
# Purpose: In Python, Logging capabilities to your Python tool.
# Configure logging

import logging
import os


# Configure logging
log = logging.getLogger("my_logger")

# Configure object
logging.basicConfig(filename='bruteforce.log',level=logging.INFO, format='%(asctime)s - %(levelname)s -%(message)s')

log.info("Hello, World")
log.warning("THIS IS A WARNING!")
# Define Function
def do_something():
    log.debug("Doing something!")