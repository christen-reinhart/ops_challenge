#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 12
# Author Name Christen Reinhart
# Date of Latest Revision 01/23/2024
# Sources https://chat.openai.com/share/ee10763b-db45-4241-a631-97da167ec5a9
# Purpose In Python, Generating a Range of IP Addresses from a CIDR Address in Python 

import sys
from scapy.all import *
from scapy.all import sr1, TCP, IP, ICMP, srp, Ether
from ipaddress import ip_network

def tcp_port_range_scanner(ip, port_range):
    # Perform TCP port scanning on the specified IP and port range
    for port in range(port_range[0], port_range[1] + 1):
        # Craft TCP SYN packet
        packet = IP(dst=ip) / TCP(dport=port, flags="S")

        # Send packet and wait for response
        response = sr1(packet, timeout=1, verbose=0)

        if response is not None and response.haslayer(TCP):
            if response[TCP].flags == 0x12:
                print(f"Port {port} is open on {ip}")
            else:
                print(f"Port {port} is closed on {ip}")

def main():
    print("Network Security Tool")
    print("1. TCP Port Range Scanner Mode")
    print("2. ICMP Ping Sweep Mode")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        ip = input("Enter target IP address: ")
        port_range = list(map(int, input("Enter port range (start end): ").split()))
        tcp_port_range_scanner(ip, port_range)
    elif choice == "2":
        network_address = input("Enter network address (e.g., 10.10.0.0/24): ")
        icmp_ping_sweep(network_address)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
