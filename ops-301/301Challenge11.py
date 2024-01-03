#!/bin/bash

import psutil

def get_system_info():
    cpu_times = psutil.cpu_times()

    info = {
        "User Mode Time": cpu_times.user,
        "Kernel Mode Time": cpu_times.system,
        "Idle Time": cpu_times.idle,
        "Priority User Mode Time": cpu_times.nice,
        "I/O Wait Time": cpu_times.iowait,
        "Hardware Interrupt Time": cpu_times.irq,
        "Software Interrupt Time": cpu_times.softirq,
        "Virtualized OS Time": cpu_times.steal,
        "Virtual CPU Time": cpu_times.guest
    }

    return info

if __name__ == "__main__":
    system_info = get_system_info()

    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value} seconds")