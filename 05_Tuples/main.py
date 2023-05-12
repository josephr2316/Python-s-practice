### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

print(my_tuple)
print(my_other_tuple)

my_tuple = (28, 1.85, "Joseph", "Rodriguez Kelly", "Rodriguez Kelly")
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4])  # IndexError
# print(my_tuple[-6])  # IndexError

# duoble 2 elements, triple 3 elements, quadruple 4 elements etc...

print(my_tuple.count("Rodriguez Kelly"))
print(my_tuple.index("Joseph"))
print(my_tuple.index("Rodriguez Kelly"))
print(my_tuple)

"""
my_tuple[1] = 1.90  # Values can't be changed
"""

print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(type(my_sum_tuple))

print(my_sum_tuple[3:4])
print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Joseph Dev"
my_tuple.insert(1, "Green")
print(my_tuple)
print(tuple(my_tuple))
my_tuple = tuple(my_tuple)
print(type(my_tuple))


# del my_tuple[2]  # TypeError: 'tuple' object doesn't support item deletion immutable

del my_tuple  # Delete the tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
