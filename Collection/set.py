# #empty set
# setA = set()

# setA = {1, 2, 3, 4, 5}
# setA.add(6)

# #set automatically removes duplicate values.
# setA = {1,23,45,45,23}
# print(setA) # the output will be {1, 45, 23}.

A = {1, 6, 3, 13}
B = {2, 4, 5, 6, 10, 12}

print(f"Set A UNion Set B ={A.union(B)}")

print(f"Set A INtersection Set B ={A.intersection(B)}")

print(f"Set A Difference Set B ={A.difference(B)}")

print(f"Set B Difference Set A ={B.difference(A)}")

#set is unordered collection of items, ie it does not maintain the position of items

A.add(7)
A.discard(6)
A.update([8, 9, 10])   #add multiple items to set 