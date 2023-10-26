#!/bin/bash
# Script Name:                  Basic array.sh
# Author:                       Christen Reinhart
# Date of latest revision:      10/26/2023
# Purpose:                      Purpose Demo Array
# Execution                     bash array.sh or ./array.sh chmod -x array.sh

# Declaration of functions 

#   index 0     index 1     index 2     index 3     index 4
snacks=("skittles" "poptarts" "snickers" "tamales" "kit kat")

# Print array elements
echo ${snacks[0]}  # This will print "skittles"
echo ${snacks[1]}  # This will print "poptarts"
echo ${snacks[2]}  # This will print "snickers"
echo ${snacks[3]}  # This will print "tamales"
echo ${snacks[4]}  # This will print "kit kat"







