#!/bin/bash
# Script Name:                  Basic conditionalarray.sh
# Author:                       Christen Reinhart
# Date of latest revision:      10/30/2023
# Purpose:                      Purpose conditional array
# Execution                     conditionalarray.sh
# Additional Sources:           X

# Loop through the array
for item in "${items[@]}"; do
    # Check if the item exists
    if [ -e "$item" ]; then
        echo "$item already exists."
    else
        # If it doesn't exist, create it
        if [[ "$item" == *"/"* ]]; then
            mkdir -p "$item"  # Create directory
            echo "Created directory: $item"
        else
            touch "$item"  # Create file
            echo "Created file: $item"
        fi
    fi
done
