### Sets ###

my_set = set()
my_other_set = {}

print(my_set)
print(my_other_set)

print(type(my_set))
print(type(my_other_set))  # Initially is a dictionary

my_other_set = {"Joseph", "Rodriguez Kelly", 28}
print(type(my_other_set))

print(len(my_other_set))
print(my_other_set)
# print(my_other_set[0]) # TypeError: 'set' object is not subscriptable

my_other_set.add("Joseph Dev")
print(my_other_set)  # A set is not an ordered structure, a hash to set all the elements

my_other_set.add("Joseph Dev")  # A set does not admit repetitions
print(my_other_set)

print("Rodriguez Kelly" in my_other_set)
print("Rodriguez" in my_other_set)

'''
my_other_set.remove("Rodriguez Kelly")  # Won't work, the element to be deleted has to be in the set
print(my_other_set)
'''

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

# del # Is from the system

del my_other_set







