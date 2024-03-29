#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 11
# Author Name Christen Reinhart
# Date of Latest Revision 01/22/2024
# Sources https://chat.openai.com/share/6a733667-0937-42cb-9db7-9b1ecf1ababe 
# Purpose In Python, Create a TCP Port Range Scanner 

# import modules
import sys
from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP, send
import random

# assign IP and port range
host = 'scanme.nmap.org'
port_range = [20, 21, 22, 23, 53, 80, 443]

# function to scan ports
def scan_ports(dst_port):
    src_port = random.randint(1024, 65535)
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='S'), timeout=1, verbose=0)
    # conditions to perform task based on port
    if response is None:
        print(f"Port {dst_port} is filtered and silently dropped")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            send(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='R'), verbose=0)
            print(f"Port {dst_port} is open")
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Port {dst_port} is closed")
            
# create loop to scan ports
for port in port_range:
    scan_ports(port)
    