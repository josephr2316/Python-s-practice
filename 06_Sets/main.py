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
# print(my_other_set)  # Won't work, we deleted the instance, NameError: name 'my_other_set' is not defined

my_set = {"Joseph", "Rodriguez Kelly", 28}  # It's created haphazardly
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"C#", "Java", "Python", "C/C++"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set))  # Don't accept repetitions
print(my_new_set.union(my_new_set).union(my_set))   # Don't accept repetitions
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "Kotlin"}))

print(my_new_set.difference(my_set))

# Check more functions for the sets







