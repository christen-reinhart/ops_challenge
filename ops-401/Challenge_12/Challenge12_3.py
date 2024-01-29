#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 12
# Author Name Christen Reinhart
# Date of Latest Revision 01/23/2024
# Sources https://chat.openai.com/share/ee10763b-db45-4241-a631-97da167ec5a9
# Purpose In Python, Generating a Range of IP Addresses from a CIDR Address in Python 3

import sys
from scapy.all import sr1, IP, ICMP, srp, Ether
from ipaddress import ip_network


def icmp_ping_sweep(network_address):
    # Get all addresses in the given network
    network = ipaddress.IPv4Network(network_address, strict=False)
    target_addresses = [str(ip) for ip in network.hosts()]

    for target_ip in target_addresses:
        # Skip network address and broadcast address
        if target_ip == network.network_address or target_ip == network.broadcast_address:
            continue

        # Craft ICMP echo request packet
        packet = IP(dst=target_ip) / ICMP()

        # Send packet and wait for response
        reply = sr1(packet, timeout=1, verbose=0)

        if reply is None:
            print(f"Host {target_ip} is down or unresponsive.")
        elif reply.haslayer(ICMP) and reply[ICMP].type == 3 and reply[ICMP].code in [1, 2, 3, 9, 10, 13]:
            print(f"Host {target_ip} is actively blocking ICMP traffic.")
        else:
            print(f"Host {target_ip} is responding.")

def main():
    print("Network Security Tool - ICMP Ping Sweep Mode")
    network_address = input("Enter network address (e.g., 10.10.0.0/24): ")

    try:
        # Validate and execute ICMP Ping Sweep
        icmp_ping_sweep(network_address)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
