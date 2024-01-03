#!/bin/bash
# Script Name:                  Basic loop.sh
# Author:                       Christen Reinhart
# Date of latest revision:      10/27/2023
# Purpose:                      Purpose Demo Loop
# Execution                     bash loop.sh or 
# Additional Sources:           X

# Declaration of variables

var=0

# Declaration of functions

# main

while [ $var -lt 10 ]
do
    echo $var
    var=$((var + 1))  # Update the variable to increment by 1
done