#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file> <permission_mode>"
    exit 1
fi

file=$1
permission_mode=$2

# Check if the file exists
if [ ! -e "$file" ]; then
    echo "Error: File '$file' not found."
    exit 1
fi

# Check if the permission mode is valid
if [[ ! "$permission_mode" =~ ^[0-7]{1,3}$ ]]; then
    echo "Error: Invalid permission mode. Please provide a valid octal mode (e.g., 755)."
    exit 1
fi

# Change the file permissions
chmod "$permission_mode" "$file"

echo "File permissions for '$file' changed to $permission_mode."