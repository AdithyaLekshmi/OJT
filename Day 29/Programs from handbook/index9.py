#whileloop with else
#program to check weather the given number is prime number or not
num=int(input("enter the number:"))
i=2;
while(i<num):
    if(num%i==0):
        print("not a prime number")
        break
    i=i+1
else:
    print("prime number")