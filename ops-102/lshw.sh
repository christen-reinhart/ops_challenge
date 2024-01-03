#!/bin/bash
# Script Name:                  lshw.sh
# Author:                       Christen Reinhart
# Date of latest revision:      10/31/2023
# Purpose:                      Purpose conditional array
# Execution                     lshw.sh
# Additional Sources:           X

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root (use sudo)."
    exit 1
fi

# Function to display component information
display_component_info() {
    component_name=$1
    lshw -c $component_name | grep -v "bus info" | grep -v "description" | grep -v "product" | grep -v "vendor"
    echo "--------------------------------------------------"
}

# Display computer information
echo "Computer Information:"
lshw -c system | grep -v "bus info" | grep -v "description"

# Display CPU information
echo "CPU Information:"
display_component_info processor

# Display RAM information
echo "RAM Information:"
display_component_info memory

# Display Display adapter information
echo "Display Adapter Information:"
display_component_info display

# Display Network adapter information
echo "Network Adapter Information:"
display_component_info network