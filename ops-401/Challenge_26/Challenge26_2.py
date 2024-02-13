#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 26
# Author: Christen Reinhart
# Date of Latest Revision: 02/12/2024
# Sources: https://chat.openai.com/share/9a32f1fb-287a-438d-9ff2-34b5341a2fe0
# Purpose: In Python, Logging capabilities to your Python tool.

import logging

# Configure logging
logging.basicConfig(
    filename='my_tool.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info('Starting my_tool')
    try:
        # Your tool's main functionality here
        result = 10 / 0  # Intentionally induce a ZeroDivisionError
    except ZeroDivisionError as e:
        logging.error('Encountered a division by zero error: %s', e)
    except Exception as e:
        logging.exception('An unexpected error occurred: %s', e)
    finally:
        logging.info('Exiting my_tool')

if __name__ == "__main__":
    main()
