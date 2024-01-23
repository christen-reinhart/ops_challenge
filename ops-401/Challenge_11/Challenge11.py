#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 11
# Author Name Christen Reinhart
# Date of Latest Revision 01/22/2024
# Sources 
# Purpose In Python, Create a TCP Port Range Scanner  

from scapy import IP, TCP, RandShort, sr1


def scan_port(ip, port):
    src_port = RandShort()
    response = sr1(IP(dst=ip)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
    
    if response is None:
        print(f"Port {port} is filtered (silently dropped).")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            send(IP(dst=ip)/TCP(sport=src_port, dport=port, flags="AR"), verbose=0)
            print(f"Port {port} is open.")
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Port {port} is closed.")
    else:
        print(f"Port {port} could not be determined.")

def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

# Example usage:
host_ip = "127.0.0.1"
start_port = 80
end_port = 100

scan_ports(host_ip, start_port, end_port)


