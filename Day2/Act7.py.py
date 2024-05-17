string =input("Type String:")
vowels='aeiouAEIOU'
count=0
for char in string:
    if char in vowels:
        count += 1
print("The number of vowels is",count)
