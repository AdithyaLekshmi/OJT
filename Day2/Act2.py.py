#Write a Python program to print the multiplication table of a number using a for loop.

num1=int(input("Enter the Multiplication number: "))

for i in range(1,11):
    print(i,"X","=",num1,num1*i)