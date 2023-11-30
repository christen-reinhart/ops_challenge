#!/bin/bash

options=("Option 1" "Option 2" "Option 3" "Quit")

PS3="Please enter your choice: "
select opt in "${options[@]}" do

case $opt in
  "Option 1")
    echo "You chose Option 1"
    ;;
  "Option 2")
    echo "You chose Option 2"
    ;;
  "Option 3")
    echo "You chose Option 3"
    ;;
  "Quit")
    echo "Exiting the menu"
    break
    ;;
  *)
    echo "Invalid option selected"
    ;;
esac
done