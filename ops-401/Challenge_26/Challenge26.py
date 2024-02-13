#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 26
# Author: Christen Reinhart
# Date of Latest Revision: 02/12/2024
# Sources: 
# Purpose: In Python, Logging capabilities to your Python tool.

# import libraries
import logging

# create object log
log = logging.getLogger("my_logger")

# configure logging object
logging.basicConfig(filename='bruteforce.log',level=logging.INFO, format='%(asctime)s - %(levelname)s -%(messages)s')