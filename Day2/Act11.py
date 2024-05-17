#Create a tuple and access its elements.
my_tuple = (1, 2, 3, 4, 5)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])


#Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)


#Find the length of a tuple
ftuple = (10, 20, 30, 40, 50)
length = len(ftuple)
print("Length of the tuple:", length)


#Check if an element exists in a tuple
etuple = (10, 20, 30, 40, 50)
element_to_check = 30
if element_to_check in etuple:
    print(f"{element_to_check} exists in the tuple.")
else:
    print(f"{element_to_check} does not exist in the tuple.")


#Count the occurrences of an element in a tuple
ctuple = (1, 2, 3, 1, 2, 3, 1, 2, 3)
element_to_count = 2
count = ctuple.count(element_to_count)
print(f"Occurrences of {element_to_count}:", count)


#Iterate over a tuple and print its elements
ituple = (10, 20, 30, 40, 50)
for element in ituple:
    print(element)

#Find the index of an element in a tuple
et = ('a', 'b', 'c', 'd', 'e')
element_to_find = 'c'
index = et.index(element_to_find)
print(f"Index of {element_to_find}:", index)
