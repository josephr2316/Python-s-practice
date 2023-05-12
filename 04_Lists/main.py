### Lists ###
from typing import List

# Capital letter when you want to create a constant variable, just to identify, remember the value will change,
# cus python doesn't have constants

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

print(list([1, 2, 3, 4]))
print([1, 2, 3, 4])
print(list[1, 2, 3, 4])  # This is not a list

# print(my_list * my_other_list) # Won't work
# print(my_list - my_other_list) # Won't work

my_list = "Hello Python"
print(my_list)
print(type(my_list))

my_list = list("Hello Python")
print(my_list)
my_list = list(["Hello Python"])
print(my_list)
my_list = ["Hello Python"]
print(my_list)
print(type(my_list))

my_other_list.append("EliotDev")  # To the end, is added the new element
print(my_other_list)

my_other_list.insert(1, "Green")  # The new value is insert, but rotate the previous value
print(my_other_list)

my_other_list.remove("Green")
print(my_other_list)

my_list: List = [35, 24, 62, 52, 30, 30, 17]
my_list.remove(30)  # Only delete the first element, which found with this value
print(my_list)

print(my_list.pop())  # Delete the last element
my_pop_element = my_list.pop(2)  # The index I want to pop
print(my_pop_element)
print(my_list)

del my_list[2]  # Delete an element of the list
print(my_list)

my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

print(my_new_list.reverse())
print(my_new_list)

my_other_list.insert(1, "White")
print(my_other_list)
my_other_list[1] = "Green"
print(my_other_list)

my_new_list.reverse()
var = my_new_list[::-1]
print(my_new_list)
print(var)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])
print(my_new_list[1:3])
