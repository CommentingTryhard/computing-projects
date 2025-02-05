import os

input_directory = "/home/kali/Downloads/zipbomb"

def process_files(directory):
    """Processes all files in the given directory."""
    if not os.path.exists(directory):
        print(f"Error: Directory {directory} does not exist.")
        return []
    
    flags = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                content = file.read().strip()
                # Process the content (decoding logic)
                # Example placeholder:
                if "YBN24{" in content:
                    flags.append((filename, content))
    return flags

flags_found = process_files(input_directory)
for i in flags_found:
    print(i)