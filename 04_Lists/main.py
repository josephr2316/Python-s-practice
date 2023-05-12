### Lists ###
from typing import List

my_list = list()  # We don't have to initialize the variable
my_other_list = []

print(my_list)
print(my_other_list)

print(len(my_list))
print(len(my_other_list))

# my_list: List = [35, 24, 62, 52, 30, 30, 17] # Type a list
my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [28, 1.85, "Joseph", "Rodríguez Kelly"]
print(my_other_list)
print(type(my_other_list))

print(type(my_list))  # Array and list are one, A list is a superset of an array.

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
# print(my_other_list[4]) # Won't work IndexError
# print(my_other_list[-5) # Won't work IndexError

print(my_other_list.count("Joseph"))
print(my_list.count(30))

age, height, name, surname = my_other_list
# age, height, name = my_other_list  # won't work, the list has 4 elements not 3, unpack
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)
print(height)
print(age)
print(surname)

print(my_list + my_other_list)

print(list([1,2,3,4]))
print([1,2,3,4])
print(list[1,2,3,4]) #  This is not a list




