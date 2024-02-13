#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 26
# Author Name: Christen Reinhart
# Date of Latest Revision: 02/12/2024
# Sources: https://chat.openai.com/share/9a32f1fb-287a-438d-9ff2-34b5341a2fe0
# Purpose: In Python, Ping an IP address, scan its ports, and log

import scapy.all as scapy
import logging

# Configure logging
logging.basicConfig(filename='port_scan.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def port_scan(host_ip, port_range):
    # Function to perform TCP port scanning
    for port in range(port_range[0], port_range[1] + 1):
        # Create a TCP SYN packet
        syn_packet = scapy.IP(dst=host_ip) / scapy.TCP(dport=port, flags="S")

        # Send the packet and wait for a response
        response = scapy.sr1(syn_packet, timeout=1, verbose=False)

        if response:
            # Check the TCP flags in the response
            if response.haslayer(scapy.TCP):
                tcp_flags = response.getlayer(scapy.TCP).flags

                if tcp_flags == 0x12:
                    logging.info(f"Port {port} is open")
                    # Send a RST packet to gracefully close the open connection
                    rst_packet = scapy.IP(dst=host_ip) / scapy.TCP(dport=port, flags="R")
                    scapy.send(rst_packet, verbose=False)
                elif tcp_flags == 0x14:
                    logging.info(f"Port {port} is closed")
                elif tcp_flags == 0x04:
                    logging.info(f"Connection to Port {port} is reset")
                elif tcp_flags == 0x10:
                    logging.info(f"Port {port} is open, but closed after connection establishment")
                else:
                    logging.warning(f"Port {port} has an unknown response")
            else:
                logging.warning(f"Port {port} does not have a TCP layer")
        else:
            logging.warning(f"No response for Port {port}")

def network_scanner(target_ip):
    # Function to perform network scanning (ping and port scan)
    # ICMP echo request packet
    icmp_packet = scapy.IP(dst=target_ip) / scapy.ICMP()

    # Send the packet and wait for a response
    response = scapy.sr1(icmp_packet, timeout=1, verbose=False)

    if response:
        logging.info(f"Host {target_ip} is responding to ICMP echo requests.")
        # Define port range for TCP port scanning
        port_range_start = int(input("Enter the starting port of the range: "))
        port_range_end = int(input("Enter the ending port of the range: "))
        port_range = (port_range_start, port_range_end)

        # Call the port scan function
        port_scan(target_ip, port_range)
    else:
        logging.warning(f"Host {target_ip} is down or unresponsive.")

# Get user input for the target IP address
target_ip = input("Enter the target IP address: ")

# Call the network scanner function
network_scanner(target_ip)
