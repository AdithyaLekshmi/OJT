
# Python program for swapping of two numbers without using temporary variable

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
print("Before swapping : ",num1," ",num2)

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("After swapping : ",num1," ",num2)