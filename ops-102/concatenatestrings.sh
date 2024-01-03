#!/bin/bash
# Script Name:                  Basic concatenatestrings.sh
# Author:                       Christen Reinhart
# Date of latest revision:      10/26/2023
# Purpose:                      Purpose Demo concatenatestrings
# Execution                     bash concatenatestrings.sh 
# Define directory names

directories=("dir1" "dir2" "dir3" "dir4")

# Create directories
for dir in "${directories[@]}"; do
    mkdir -p "$dir"
done

# Load directory paths into an array
directory_paths=()
for dir in "${directories[@]}"; do
    directory_paths+=("$dir")
done

# Create a new .txt file in each directory using array indices
for ((i=0; i<${#directories[@]}; i++)); do
    echo "This is a text file in ${directories[$i]}" > "${directory_paths[$i]}/file$i.txt"
done

# Test & validate
for dir in "${directory_paths[@]}"; do
    echo "Contents of $dir:"
    cat "$dir/file*.txt"
done