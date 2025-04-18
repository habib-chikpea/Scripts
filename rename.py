import os

# Define the directory containing the Apex class files
directory = r'D:\Authorize Net\Classes'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an Apex class or its metadata
    if filename.endswith('.cls') or filename.endswith('.cls-meta.xml'):
        # Construct the full old and new file paths
        old_path = os.path.join(directory, filename)
        new_filename = f'ANet_{filename}'
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_filename}')
