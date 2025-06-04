list1=[10,20,30,40,50]
for i in list1:
    print(i)  # Printing each element in the list
list1[0] = 100  # Modifying the first element of the list
list1.append(60)  # Adding a new element to the end of the list
list1.remove(30)  # Removing the element with value 30 from the list
list1.insert(2, 25)  # Inserting 25 at index 2 in the list
#list1.clear()  # Clearing all elements from the list
#del list1[1]  # Deleting the element at index 1 (if it exists)
list1.pop()  # Removing the last element from the list


print(list1)  # Printing the modified list