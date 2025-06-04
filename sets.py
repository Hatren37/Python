list1 = [10, 20, 30, 'Python', 'Java', 'PHP', 40, 50]
print(list1)
print(list1[3])  # Accessing the 4th element
"""     DIFFRENCES BETWEEN LIST AND SET
    Eements can be spliced and accessed using index and for loop but set elements are only accessed using for loop
    it also allows duplicate elements
    it is mutable, i.e., elements can be changed
    it is ordered, i.e., elements are stored in the order they are added"""

set1 = {10, 20, 30, 'Python', 'Java', 'PHP', 40, 50}
print(set1)

#using a for loop to access elements (order is not guaranteed)
# Note: Sets are unordered collections of unique elements.
for item in set1:
    print(item)

#Adding elements to a set
set1.add(60)
set1.add('C++')      #Only one element can be added at a time using add()

#Using update() to add multiple elements at once
set1.update([70, 80, 90])
print(set1)

#Removing elements from a set using remove() method
set1.remove(20)
print(set1)

#Removing elements from a set using discard() method
set1.discard('Java')
print(set1) #Removing an element that does not exist using discard() does not raise an error

#Clearing a set
set1.clear()
print(set1)  # This will print an empty set



set2 = {10, 10, 10, 100, 200, 200, 10}
print(set2)
#no duplicates

#print(set2[2])
#does not allow indexing

print(type(set1))
print(type(list1))
