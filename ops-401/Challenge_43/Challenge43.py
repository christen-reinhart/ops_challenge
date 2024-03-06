#!/usr/bin/python3
# Script name: Challenge: 401 Challenge 43
# Author: Christen Reinhart
# Date of Latest Revision: 03/06/2024
# Sources: https://chat.openai.com/share/39ec9a01-80f9-4837-a739-c8da1ecc7e5d
# Purpose: Python script that scans IP address and ports.

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout value for the socket
timeout = 1  # You can adjust this value as needed
sockmod.settimeout(timeout)

# Collect host IP and port number from the user
hostip = input("Enter the host IP address: ")
portno = int(input("Enter the port number: "))

def portScanner(portno):
    try:
        # Attempt to connect to the specified port
        sockmod.connect((hostip, portno))
        # If the connection is successful, the port is open
        print("Port open")
        sockmod.close()  # Close the socket after use
    except socket.error:
        # If there's an error, the port is likely closed
        print("Port closed")

portScanner(portno)
