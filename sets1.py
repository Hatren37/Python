set1 = {1,2,3,4,5,6,}
set2 = {4,5,6,7,8,9}
# Union of two sets
set_union = set1.union(set2)
print("Union of set1 and set2:", set_union)

# Intersection of two sets
set_intersection = set1.intersection(set2)  
print("Intersection of set1 and set2:", set_intersection)

#Symentric Difference of two sets (AnB)'
symentric_difference = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symentric_difference)

# Difference of two sets B'
set_difference = set1.difference(set2)
print("Difference of set1 and set2:", set_difference)