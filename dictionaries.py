#Reading contents of a dictionary, ---for loop, key
d1 = {'Python': 100, 'Java': 200, 'PHP': 100, 'MySQL': 200}
for p in d1:
    print(p, ":", d1[p])

#Updating a dictionary using the update() method
d2 = {1:222, 2:333, 3:444, 4:555}
print(d2)
d2.update({1:111, 2:101})
print(d2)

#deleting a key-value pair from a dictionary using the del keyword
del d2[4]
print(d2)
del d1['PHP']
print(d1)

#Deleting a key-value pair from a dictionary using the pop() method
d3 = {'pizza': 100, 'burger': 200, 'sandwich': 150}
d3.pop('pizza')
print(d3)