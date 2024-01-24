import ipaddress
from scapy.all import *

def tcp_port_range_scanner(ip, port_range):
    # ... (existing port scanning logic from yesterday)

def icmp_ping_sweep(network_address):
    try:
        network = ipaddress.IPv4Network(network_address, strict=False)
    except ValueError as e:
        print(f"Error: {e}")
        return

    host_count = 0

    print("\nPerforming ICMP Ping Sweep...\n")

    for ip in network.hosts():
        if ip == network.network_address or ip == network.broadcast_address:
            continue

        response = sr1(IP(dst=str(ip)) / ICMP(), timeout=1, verbose=0)

        if response is None:
            print(f"Host {ip} is down or unresponsive.")
        elif response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
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
        ip = input("Enter target IP address: ")
        port_range = list(map(int, input("Enter port range (start end): ").split()))
        tcp_port_range_scanner(ip, port_range)
    elif choice == "2":
        # ICMP Ping Sweep mode
        network_address = input("Enter network address (e.g., 10.10.0.0/24): ")
        icmp_ping_sweep(network_address)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    user_menu()
