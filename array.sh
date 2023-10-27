#!/bin/bash
# Script Name:                  Basic array.sh
# Author:                       Christen Reinhart
# Date of latest revision:      10/26/2023
# Purpose:                      Purpose Demo Array
# Execution                     bash array.sh or ./array.sh chmod -x array.sh

# Declaration of functions 

#   index 0     index 1     index 2     index 3     index 4

# Define directory names in an array
directories=("file.txt1" "file.txt2" "file.txt3" "file.txt4" "file.txt5")

# Loop through the array and create directories
for dir in "${directories[@]}"; do
    mkdir "$dir"
    echo "Created directory: $dir"
done










