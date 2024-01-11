import os
import platform
import subprocess
import time

def ping_host(target_ip):
    """
    Function to send a single ICMP packet to the target IP.
    """
    operating_system = platform.system().lower()

    if operating_system == "windows":
        command = ["ping", "-n", "1", target_ip]
    else:
        command = ["ping", "-c", "1", target_ip]

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError:
        return False

def write_to_log(timestamp, status, target_ip, log_file):
    """
    Function to write the event details to a log file.
    """
    with open(log_file, 'a') as file:
        log_entry = f"{timestamp} Network {'Active' if status else 'Inactive'} to {target_ip}\n"
        file.write(log_entry)

def main():
    target_ip = input("Enter the target IP address: ")
    log_file = "uptime_log.txt"

    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        status = ping_host(target_ip)

        print(f"{timestamp} Network {'Active' if status else 'Inactive'} to {target_ip}")

        write_to_log(timestamp, status, target_ip, log_file)

        time.sleep(2)

if __name__ == "__main__":
    main()  