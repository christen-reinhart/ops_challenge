import scapy.all as scapy

def port_scan(host_ip, port_range):
    # Function to perform TCP port scanning
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

def network_scanner(target_ip):
    # Function to perform network scanning (ping and port scan)
    # ICMP echo request packet
    icmp_packet = scapy.IP(dst=target_ip) / scapy.ICMP()

    # Send the packet and wait for a response
    response = scapy.sr1(icmp_packet, timeout=1, verbose=False)

    if response:
        print(f"Host {target_ip} is responding to ICMP echo requests.")
        # Define port range for TCP port scanning
        port_range_start = int(input("Enter the starting port of the range: "))
        port_range_end = int(input("Enter the ending port of the range: "))
        port_range = (port_range_start, port_range_end)

        # Call the port scan function
        port_scan(target_ip, port_range)
    else:
        print(f"Host {target_ip} is down or unresponsive.")

# Get user input for the target IP address
target_ip = input("Enter the target IP address: ")

# Call the network scanner function
network_scanner(target_ip)
