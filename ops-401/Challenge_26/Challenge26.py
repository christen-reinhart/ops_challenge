#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 18
# Author: Christen Reinhart
# Date of Latest Revision: 01/31/2024
# Sources: https://chat.openai.com/share/10b196e4-6aa3-4072-b3be-8d3d7cddc1a9
# Purpose: In Python, Finish developing a custom tool that performs brute force attacks.

# import libraries
import logging

# create object log
log = logging.getLogger("my_logger")

# configure logging object
logging.basicConfig(filename='bruteforce.log',level=logging.INFO, format='%(asctime)s - %(levelname)s -%(messages)s')