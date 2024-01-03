#!/usr/bin/env python3

# Create a new .txt file
file_name = "example.txt"

# Open the file in write mode to create it
with open(file_name, "w") as file:
    # Append three lines to the file
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Open the file in read mode and print the first line
with open(file_name, "r") as file:
    first_line = file.readline()
    print("First Line:", first_line)

# Delete the file
import os
os.remove(file_name)

print("File deleted:", file_name)