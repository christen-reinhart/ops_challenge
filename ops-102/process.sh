#!/bin/bash
# Script Name:                  Basic process.sh
# Author:                       Christen Reinhart
# Date of latest revision:      10/28/2023
# Purpose:                      Purpose Demo Loop
# Execution                     bash process.sh  
# Additional Sources:           X

# Declaration of variables


while true; do
    # Step 1: Display running processes
    echo "Running Processes:"
    ps aux

    # Step 2: Ask the user for a PID
    read -p "Enter the PID of the process you want to kill (or press Ctrl + C to exit): " pid

    # Check if the user wants to exit
    if [ -z "$pid" ]; then
        echo "Exiting the script."
        break
    fi

    # Step 3: Kill the process with the specified PID
    if [ "$pid" -gt 0 ] 2>/dev/null; then
        # Check if the PID is valid
        kill -9 "$pid"
        echo "Process with PID $pid has been killed."
    else
        echo "Invalid PID. Please enter a valid PID."
    fi

    echo "------------------------------------"
done