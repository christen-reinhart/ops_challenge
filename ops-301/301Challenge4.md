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

#!/bin/bash

while true; do
    clear  # Clears the screen for a cleaner menu display

    # Display the menu options
    echo "====== Menu ======"
    echo "1. Hello World"
    echo "2. Ping Self"
    echo "3. IP Info"
    echo "4. Exit"

    # Prompt the user for their choice
    read -p "Enter your choice (1-4): " choice

    case $choice in
        1)
            echo "Hello World!"
            ;;
        2)
            ping -c 4 127.0.0.1  # Ping the loopback address (localhost)
            ;;
        3)
            ifconfig  # Display network adapter information
            ;;
        4)
            echo "Exiting the menu."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    # Add a pause to display feedback before clearing the screen
    read -p "Press Enter to continue..."
done