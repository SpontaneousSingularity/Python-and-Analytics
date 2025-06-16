my_list = [5,3,4,0,-7,3,-5,-8,3]

print(my_list[3])

#range where start is inclusive and end is exclusive.
print(my_list[3:6])

#negative index, which starts from end of list (-1,-2,-3 and so on).
print(my_list[3:-1])

#jump of 2 , default is 1 when not specified.
print(my_list[1:6:2])

#prints whole list
print(my_list[:])

#prints whole list with jump of 3.
print(my_list[::3])

#starts with 5 and goes till end.
print(my_list[5::])

#starts with 0 and goes till 5.
print(my_list[:5:])

#goes from index 8 towards 0
print(my_list[8::-1])

my_2dlist= [[3,5,-8,-5,3],[1,6,-3,8,-3]]