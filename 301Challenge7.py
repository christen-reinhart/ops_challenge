#!/usr/bin/env python3

# Import libraries
import os

# Declaration of functions

def generate_directory_info(user_path):
    """
    Generate directory information for the provided path using os.walk().

    Args:
        user_path (str): The user-provided directory path.

    Returns:
        tuple: A tuple containing information about directories and files.
    """
    directory_info = []

    for (root, dirs, files) in os.walk(user_path):
        directory_info.append({
            'Directory': root,
            'Subdirectories': dirs,
            'Files': files
        })

    return directory_info

def save_to_txt(directory_info, output_file):
    """
    Save directory information to a text file.

    Args:
        directory_info (list): List containing directory information.
        output_file (str): The name of the output text file.

    Returns:
        None
    """
    with open(output_file, 'w') as file:
        for entry in directory_info:
            file.write(f"Directory: {entry['Directory']}\n")
            file.write(f"Subdirectories: {entry['Subdirectories']}\n")
            file.write(f"Files: {entry['Files']}\n\n")

def create_test_directory(test_string):
    """
    Create a test directory and subdirectories based on user input.

    Args:
        test_string (str): The user-provided string.

    Returns:
        None
    """
    test_directory = os.path.join(os.getcwd(), test_string)
    os.makedirs(test_directory, exist_ok=True)

    for i in range(1, 4):
        subdirectory_name = f"{test_string}_{i:02d}"
        subdirectory_path = os.path.join(test_directory, subdirectory_name)
        os.makedirs(subdirectory_path)

# Main

if __name__ == "__main__":
    # Read user input for directory path
    user_path = input("Enter the directory path: ")

    # Validate the path
    if not os.path.isabs(user_path):
        print("Please enter an absolute path.")
        exit()

    # Generate directory information
    directory_info = generate_directory_info(user_path)

    # Print directory information
    for entry in directory_info:
        print(f"Directory: {entry['Directory']}")
        print(f"Subdirectories: {entry['Subdirectories']}")
        print(f"Files: {entry['Files']}\n")

    # Save directory information to a text file
    output_file = "directory_info.txt"
    save_to_txt(directory_info, output_file)
    print(f"Directory information saved to {output_file}")

    # Stretch Goal: Create a test directory and subdirectories
    test_string = input("Enter a string for the test directory: ")
    create_test_directory(test_string)
    print(f"Test directory '{test_string}' created with subdirectories.")