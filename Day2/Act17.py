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
