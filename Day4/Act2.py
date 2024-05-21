#  Write a python program to Delete a file

import os

# File path to delete
file_path = 'example.txt'

# Check if file exists before trying to delete it
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print(f"{file_path} has been deleted successfully.")
else:
    print(f"{file_path} does not exist.")
