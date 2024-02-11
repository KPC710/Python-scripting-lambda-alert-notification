import os

def list_files(directory):
    try:
        files = os.listdir(directory)
        print("Files in directory:")
        for file in files:
            print(file)
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Get the directory path from the user
    directory_path = input("Enter the directory path: ")
    list_files(directory_path)
