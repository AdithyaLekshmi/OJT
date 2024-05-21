# Write a Python program that renames a 
#file named ‘old_name.txt to’ ‘new_name.txt’.


import os
# Specify the old and new file names
old_name = 'old_name.txt'
new_name = 'new_name.txt'

# Check if the file with the old name exists
if os.path.exists(old_name):
    # Rename the file
    os.rename(old_name, new_name)
    print(f"File renamed from {old_name} to {new_name} successfully.")
else:
    print(f"The file {old_name} does not exist.")
