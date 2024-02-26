#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 36
# Author: Christen Reinhart
# Date of Latest Revision: 02/26/2024
# Sources: https://chat.openai.com/share/4599110a-614e-44ae-89b2-ecd9d77819cf
# Purpose: In Python create a script that executes from a Linux, Prompts the user to type a URL or IP address, Prompts the user to type a port number.


import os

def banner_grabbing_nc(target, port):
    print("Banner grabbing using netcat:")
    os.system(f"nc -v {target} {port}")

def banner_grabbing_telnet(target, port):
    print("\nBanner grabbing using telnet:")
    os.system(f"echo '' | telnet {target} {port}")

def banner_grabbing_nmap(target):
    print("\nBanner grabbing using Nmap:")
    os.system(f"nmap -p- --script=banner {target}")

def main():
    target = input("Enter the target URL or IP address: ")
    port = input("Enter the target port number: ")

    banner_grabbing_nc(target, port)
    banner_grabbing_telnet(target, port)
    banner_grabbing_nmap(target)

if __name__ == "__main__":
    main()
