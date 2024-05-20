from functools import reduce
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)
number =int(input("The number is : "))
result = factorial(number)
print(f"The factorial of {number} is:", result)
