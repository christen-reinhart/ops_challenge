#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 12
# Author Name Christen Reinhart
# Date of Latest Revision 01/23/2024
# Sources 
# Purpose In Python, Generating a Range of IP Addresses from a CIDR Address in Python 

#!/usr/bin/env python3

import ipaddress
from scapy.all import ICMP, IP, sr1

# Define end host and TCP port range. Take care not to populate the host bits here.
network = "10.0.2.0/24"
ip_list = ipaddress.IPv4Network(network).hosts()
hosts_count = 0

for host in ip_list:
    print("Pinging", str(host), "- please wait...")
    response = sr1(
        IP(dst=str(host))/ICMP(),
        timeout=2,
        verbose=0
    )

    if response:
        print("Response received from", str(host))
        hosts_count += 1
    else:
        print("No response from", str(host))

print(f"\n{hosts_count} hosts responded out of {len(ip_list)}")
