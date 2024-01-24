#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 12
# Author Name Christen Reinhart
# Date of Latest Revision 01/23/2024
# Sources 
# Purpose In Python, Generating a Range of IP Addresses from a CIDR Address in Python 


import sys
from scapy.all import sr1, IP, ICMP, srp, Ether
from ipaddress import ip_network

def scan_ports(ip, start_port, end_port):
    # ... (existing port scanning logic)

    def icmp_ping_sweep(network):
        try:
            network = ip_network(network, strict=False)
        except ValueError as e:
            print(f"Error: {e}")
        sys.exit(1)

    host_count = 0

    print("\nPerforming ICMP Ping Sweep...\n")

    for ip in network.hosts():
        if ip == network.network_address or ip == network.broadcast_address:
            continue

        response = sr1(IP(dst=str(ip)) / ICMP(), timeout=1, verbose=0)

        if response is None:
            print(f"Host {ip} is down or unresponsive.")
        elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
            print(f"Host {ip} is actively blocking ICMP traffic.")
        else:
            print(f"Host {ip} is responding.")
            host_count += 1

    print(f"\n{host_count} hosts are online.")

def user_menu():
    print("Network Security Tool")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        # TCP Port Range Scanner mode
        host_ip = input("Enter the target IP address: ")
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        scan_ports(host_ip, start_port, end_port)
    elif choice == "2":
        # ICMP Ping Sweep mode
        network = input("Enter the network address (e.g., 10.10.0.0/24): ")
        icmp_ping_sweep(network)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    user_menu()




