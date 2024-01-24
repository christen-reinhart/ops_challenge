import ipaddress
from scapy.all import *

def icmp_ping_sweep(network_address):
    # ... (previous implementation)

def tcp_port_range_scanner(ip, port_range):
    # ... (previous implementation)

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
