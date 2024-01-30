import nltk
import time

def offensive_mode(word_list_path):
    try:
        with open(word_list_path, 'r', encoding='latin-1') as file:
            words_list = file.read().splitlines()

        for word in words_list:
            time.sleep(1)  # Add a delay of 1 second between words
            print(word)

    except FileNotFoundError:
        print(f"Error: Word list file '{word_list_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def defensive_mode(search_string, word_list_path):
    try:
        with open(word_list_path, 'r', encoding='latin-1') as file:
            words_list = file.read().splitlines()

        if search_string in words_list:
            print(f"The string '{search_string}' appears in the word list.")
        else:
            print(f"The string '{search_string}' does not appear in the word list.")

    except FileNotFoundError:
        print(f"Error: Word list file '{word_list_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    nltk.download('words')  # Download NLTK words dataset

    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")

    mode = input("Enter mode (1 or 2): ")

    try:
        if mode == "1":
            word_list_path = input("Enter word list file path: ")
            offensive_mode(word_list_path)

        elif mode == "2":
            search_string = input("Enter string to search: ")
            word_list_path = input("Enter word list file path: ")
            defensive_mode(search_string, word_list_path)

        else:
            print("Invalid mode. Please enter either '1' or '2'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
