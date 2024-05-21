def convert_to_integer(s):
    """
    Converts a string to an integer.
    Handles exceptions and prints appropriate error messages.

    Parameters:
    s (str): The string to convert.

    Returns:
    int: The converted integer if successful, None otherwise.
    """
    try:
        # Attempt to convert the string to an integer
        result = int(s)
        return result
    except ValueError:
        # Handle the case where the string cannot be converted to an integer
        print(f"Error: The provided string '{s}' is not a valid integer.")
    except TypeError:
        # Handle the case where the input is not a string
        print(f"Error: The provided input '{s}' is not a string.")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
    return None

# Example usage
input_str = "123"
result = convert_to_integer(input_str)
if result is not None:
    print(f"The converted integer is: {result}")

input_str = "abc"
result = convert_to_integer(input_str)
if result is not None:
    print(f"The converted integer is: {result}")

input_str = None
result = convert_to_integer(input_str)
if result is not None:
    print(f"The converted integer is: {result}")
