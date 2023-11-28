import os
import sys

#ex1
def read_and_print_files(directory_path, file_extension):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        for filename in os.listdir(directory_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(directory_path, filename)

                try:
                    with open(file_path, 'r') as file:
                        file_contents = file.read()
                        print(f"Contents of {filename}:\n{file_contents}")
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]
    read_and_print_files(directory_path, file_extension)

