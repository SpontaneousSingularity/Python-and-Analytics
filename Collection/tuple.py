#empty tuples
my_tuple = ()
numbers = tuple()

#you can update whole tuple but not individual elements.
numbers = (2,9,6,20,30)

#finds the index of 6 in tuple.
numbers.index(6)

#finds the number of time 6 occur in tuple.
numbers.count(6)

#slivcing is possible in tuple.
numbers[2:5]

#lists inside tuple can be changed.
tuple0= (1,[2,3,4],2,3,4)
tuple0[1].append(5)