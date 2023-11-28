import os
import sys

def count_files_by_extension(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        if not os.listdir(directory_path):
            print(f"The directory '{directory_path}' is empty.")
            return

        extension_counts = {}

        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            try:
                if os.path.isfile(file_path):
                    _, extension = os.path.splitext(filename)
                    extension_counts[extension] = extension_counts.get(extension, 0) + 1

            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

        
        print("File counts by extension:")
        for ext, count in extension_counts.items():
            print(f"{ext}: {count} files")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    
    directory_path = sys.argv[1]

   
    count_files_by_extension(directory_path)
