#!/bin/bash

# Ask the user for a directory path
read -p "Enter a directory path to check: " user_dir

# Check if the user-specified directory exists
if [ -d "$user_dir" ]; then
    echo "$user_dir exists."
else
    echo "$user_dir does not exist."
fi