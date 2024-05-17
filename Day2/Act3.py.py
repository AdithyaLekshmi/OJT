#print numbers from 1 to 10, but skip printing the number 5 using a for loop and the continue statement
for number in range(1,11):
    if(number==5):
        continue
    print(number)