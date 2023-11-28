import os
import sys

#ex2
def rename_files_with_prefix(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

        for index, filename in enumerate(files, start=1):
            try:
                new_filename = f"file{index}{os.path.splitext(filename)[1]}"
                old_file_path = os.path.join(directory_path, filename)
                new_file_path = os.path.join(directory_path, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    directory_path = sys.argv[1]

    rename_files_with_prefix(directory_path)
