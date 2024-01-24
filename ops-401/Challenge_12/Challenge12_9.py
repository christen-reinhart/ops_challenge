#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 12
# Author Name Christen Reinhart
# Date of Latest Revision 01/23/2024
# Sources https://chat.openai.com/share/ee10763b-db45-4241-a631-97da167ec5a9
# Purpose In Python, Generating a Range of IP Addresses from a CIDR Address in Python 

import scapy.all as scapy

def tcp_port_range_scanner(host_ip, port_range):
    # Function to perform TCP port scanning
    # Utilize the scapy library

    for port in range(port_range[0], port_range[1] + 1):
        # Create a TCP SYN packet
        syn_packet = scapy.IP(dst=host_ip) / scapy.TCP(dport=port, flags="S")

        # Send the packet and wait for a response
        response = scapy.sr1(syn_packet, timeout=1, verbose=False)

        if response:
            # Check the TCP flags in the response
            if response.haslayer(scapy.TCP) and response.getlayer(scapy.TCP).flags == 0x12:
                print(f"Port {port} is open")
                # Send a RST packet to gracefully close the open connection
                rst_packet = scapy.IP(dst=host_ip) / scapy.TCP(dport=port, flags="R")
                scapy.send(rst_packet, verbose=False)
            elif response.haslayer(scapy.TCP) and response.getlayer(scapy.TCP).flags == 0x14:
                print(f"Port {port} is closed")
            else:
                print(f"Port {port} is filtered and silently dropped")

def icmp_ping_sweep(network_address):
    # Function to perform ICMP Ping Sweep
    # Create a list of all addresses in the given network
    addresses = [str(ip) for ip in scapy.IP(bytes(network_address, 'utf-8')).hosts()]

    # Ping all addresses on the given network except for network address and broadcast address
    online_hosts = 0

    for address in addresses:
        if address != str(scapy.IP(network_address).network_address) and address != str(scapy.IP(network_address).broadcast_address):
            # Craft ICMP echo request packet
            icmp_packet = scapy.IP(dst=address) / scapy.ICMP()

            # Send the packet and wait for a response
            response = scapy.sr1(icmp_packet, timeout=1, verbose=False)

            if response:
                # Check ICMP type and code
                if response.haslayer(scapy.ICMP) and response.getlayer(scapy.ICMP).type == 3 and response.getlayer(scapy.ICMP).code in [1, 2, 3, 9, 10, 13]:
                    print(f"Host {address} is actively blocking ICMP traffic")
                else:
                    print(f"Host {address} is responding")
                    online_hosts += 1
            else:
                print(f"Host {address} is down or unresponsive")

    print(f"Number of online hosts: {online_hosts}")

# Example usage:
# Define host IP and port range for TCP port scanning
host_ip = "192.168.1.1"
port_range = (1, 100)

# Define network address for ICMP Ping Sweep
network_address = "10.10.0.0/24"

# User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode
user_choice = input("Choose mode: 1. TCP Port Range Scanner, 2. ICMP Ping Sweep: ")

if user_choice == "1":
    tcp_port_range_scanner(host_ip, port_range)
elif user_choice == "2":
    icmp_ping_sweep(network_address)
else:
    print("Invalid choice")


