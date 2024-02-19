import os
import platform

def search_file(file_name, directory):
    hits = 0
    files_searched = 0
    if platform.system() == 'Windows':
        directory = directory.replace("/", "\\")
    for root, _, files in os.walk(directory):
        for file in files:
            if file == file_name:
                print(f"Found: {file} at {os.path.join(root, file)}")
                hits += 1
            files_searched += 1
    print(f"Total files searched: {files_searched}")
    print(f"Total hits found: {hits}")

def main():
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    search_file(file_name, directory)

if __name__ == "__main__":
    main()
