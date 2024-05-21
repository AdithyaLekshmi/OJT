# Write a Python program that reads a file and prints its content. Handle ‘FileNotFoundError’ and ‘PermissionError’ exceptions.
# Specify the file path
file_path = 'example.txt'

try:
    # Open the file in read mode ('r' mode)
    with open(file_path, 'r') as file:
        # Read the contents of the file
        contents = file.read()
        # Print the contents of the file
        print(contents)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except PermissionError:
    print(f"Permission denied when trying to read '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
