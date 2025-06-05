tuple1 = (1,2,3,4,5,6,7,8,9,10)
#indexing
print(tuple1[2])  # Accessing the 3rd element

# Slicing
print(tuple1[2:5:2])  # Accessing elements from index 2 to 4 (5 is not included) with a step of 2

print(type(tuple1))  # Checking the type of the variable 'a'

# Tuple is immutable, i.e., elements cannot be changed
# a[2] = 20  # This will raise a TypeError because tuples do not support item assignment
# Tuples can contain mixed data types   b = (1, 2, 3, 'Python', 'Java', 'PHP', 4.5, 5.6)

#To change a tuple, you need to convert it to a list, make changes, and then convert it back to a tuple
list1 = list(tuple1)  # Convert tuple to list
list1[3] = 20  # Change the 4th element using list indexing
list1.append(11)  # Add a new element to the list
list1[0:2] = [100, 200]  # Change the first two elements
tuple1 = tuple(list1)  # Convert the list back to a tuple
print(tuple1)  # Print the modified tuple
