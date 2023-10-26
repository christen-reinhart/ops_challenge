#!/bin/bash
# Script Name:                  Basic array.sh
# Author:                       Christen Reinhart
# Date of latest revision:      10/26/2023
# Purpose:                      Purpose Demo Array
# Execution                     bash array.sh or ./array.sh chmod -x array.sh

# Declaration of functions 

snacks="skittles"
#   index 0     index 1     index 2     index 3     index 4
snacks=("skittles" "poptarts" "snickers" "tamales" "kit kat") 

# Declaration of functions

echo ${snacks [0]}
echo ${snacks [1]}
