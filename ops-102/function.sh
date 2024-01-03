#!/bin/bash
# Script Name:                  Basic function.sh
# Author:                       Christen Reinhart
# Date of latest revision:      10/25/2023
# Purpose:                      Purpose Demo Function
# Execution                     bash function.sh 



# Basic Function
   
print_login_history() {
    # Use the last command to fetch login history
    login_history=$(last)

    # Check if the last command succeeded
    if [ $? -eq 0 ]; then
        # Print the login history
        echo "$login_history"
        echo "This is the login history."
    else
        # Handle any errors that may occur
        echo "Error: Unable to retrieve login history."
    fi
}

# Call the function
print_login_history
