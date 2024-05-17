#Create a list and access its elements
list = [1, 2, 3, 4, 5]
print("First element:", list[0])
print("Last element:", list[-1])

#Append an element to a list.

list = [1, 2, 3]
print("Old list:",list)
list.append(4)
print("Updated list:", list)

#Find the index of an element in a list

flist = ['a', 'b', 'c', 'd', 'e']
element_to_find = 'c'
index = flist.index(element_to_find)
print(f"Index of {element_to_find}:", index)

#Find the sum of elements in a list

slist = [10, 20, 30, 40, 50]
total_sum = sum(slist)
print("Sum of elements:", total_sum)

#Reverse a list
re_list = [1, 2, 3, 4, 5]
re_list.reverse()
print("Reversed list:", re_list)


#Sort a list in ascending order
slist = [5, 2, 8, 1, 3]
slist.sort()
print("Sorted list (ascending):", slist)

#Check if an element exists in a list

clist = [10, 20, 30, 40, 50]
element_to_check = 30
if element_to_check in clist:
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")