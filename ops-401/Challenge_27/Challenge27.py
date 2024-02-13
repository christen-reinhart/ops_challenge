#!/usr/bin/env python3

# Script name: Challenge: 401 Challenge 27
# Author Name: Christen Reinhart
# Date of Latest Revision: 02/13/2024
# Sources: https://chat.openai.com/share/9a32f1fb-287a-438d-9ff2-34b5341a2fe0 
# Purpose: In Python, Ping an IP address, scan its ports, add log and rotation

import scapy.all as scapy
import logging
from logging.handlers import RotatingFileHandler

# Configure logging with log rotation
log_file = 'port_scan.log'
max_bytes = 128 * 128  # 1 KB
backup_count = 3  # Number of backup log files to keep
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

rotating_handler = RotatingFileHandler(filename=log_file, maxBytes=max_bytes, backupCount=backup_count)
rotating_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(rotating_handler)
logger.setLevel(logging.DEBUG)

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
                    logger.info(f"Port {port} is open")
                    # Send a RST packet to gracefully close the open connection
                    rst_packet = scapy.IP(dst=host_ip) / scapy.TCP(dport=port, flags="R")
                    scapy.send(rst_packet, verbose=False)
                elif tcp_flags == 0x14:
                    logger.info(f"Port {port} is closed")
                elif tcp_flags == 0x04:
                    logger.info(f"Connection to Port {port} is reset")
                elif tcp_flags == 0x10:
                    logger.info(f"Port {port} is open, but closed after connection establishment")
                else:
                    logger.warning(f"Port {port} has an unknown response")
            else:
                logger.warning(f"Port {port} does not have a TCP layer")
        else:
            logger.warning(f"No response for Port {port}")

def network_scanner(target_ip):
    # Function to perform network scanning (ping and port scan)
    # ICMP echo request packet
    icmp_packet = scapy.IP(dst=target_ip) / scapy.ICMP()

    # Send the packet and wait for a response
    response = scapy.sr1(icmp_packet, timeout=1, verbose=False)

    if response:
        logger.info(f"Host {target_ip} is responding to ICMP echo requests.")
        # Define port range for TCP port scanning
        port_range_start = int(input("Enter the starting port of the range: "))
        port_range_end = int(input("Enter the ending port of the range: "))
        port_range = (port_range_start, port_range_end)

        # Call the port scan function
        port_scan(target_ip, port_range)
    else:
        logger.warning(f"Host {target_ip} is down or unresponsive.")

# Get user input for the target IP address
target_ip = input("Enter the target IP address: ")

# Call the network scanner function
network_scanner(target_ip)
