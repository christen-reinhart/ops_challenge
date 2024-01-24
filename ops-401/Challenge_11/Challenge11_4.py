#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 11
# Author Name Christen Reinhart
# Date of Latest Revision 01/22/2024
# Sources https://chat.openai.com/share/ee10763b-db45-4241-a631-97da167ec5a9 
# Purpose In Python, Create a TCP Port Range Scanner 

import sys
import random
from scapy.all import Ether, IP, sniff, ARP, sr, ICMP, TCP, send

# assign IP and port range
host = 'scanme.nmap.org'
port_range = [20, 21, 22, 23, 53, 80, 443]

# function to scan ports
def scan_ports(dst_port):
    src_port = random.randint(1024, 65535)
    response = sr(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='S'), timeout=1, verbose=0)[0]
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
