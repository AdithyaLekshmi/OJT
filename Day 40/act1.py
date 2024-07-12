#Write a Python program that removes and prints every third number from a list of numbers
#  until the list is empty.

def remove_third(numbers):
    i = 2
    while i < len(numbers):
        print(numbers.pop(i))
        i += 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_third(numbers)


