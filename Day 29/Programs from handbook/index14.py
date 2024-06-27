#program to check weather the given number is prime or not
#For loop with else condition
num=int(input("Enter a Number:"))
for i in range(2,num):
    if(num%i==0):
        print("Not a Prime Number")
        breaK
    else:
      print("Prime Number")