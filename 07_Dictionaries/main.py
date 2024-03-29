### Dictionaries ###

# Sets work inside like a hashmap

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Name": "Joseph", "Surname": "Rodriguez Kelly", "Age": 28, 1: "Python"}

my_dict = {
    "Name": "Joseph",
    "Surname": "Rodriguez Kelly",
    "Age": 28,
    "Languages": {"Python", "Java", "C/C++", "C#"},# Set inside a dictionary
    1: 1.85
    }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Name"])

my_dict["Name"] = "Martha"
print(my_dict["Name"])
print(my_dict)

print(my_dict[1])

my_dict["Street"] = "San Martin Street"
print(my_dict)


del my_dict["Street"]
print(my_dict)

print("Surname" in my_dict)
print("Street" in my_dict)
print("Rodriguez Kelly" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("Name", 1)))
print(my_other_dict.fromkeys(("Name", 1)))

# my_new_dict = my_other_dict.fromkeys(("Name", 1, "Floor"))
my_new_dict = dict.fromkeys(("Name", 1, "Floor"))
print(my_new_dict)  # Create a new dictionary without value


my_list = ["Name", 1, "Floor", "Surname"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(("Name", 1, "Floor", "Surname"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,("Josephr", "Rodriguez kelly"))
print(my_new_dict)

# my_new_dict = dict.fromkeys(my_dict,"Josephr", "Rodriguez kelly") # Won't work

my_new_dict = dict.fromkeys(my_dict, my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ["Joseph", "Rodriguez Kelly"])  # It's the same as line 66
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Rodriguez")  # It's the same as line 66
print(my_new_dict)

print("\n This value")
print(my_new_dict.values())

print("\n This new dict")
print(list(my_new_dict))
print("\n This new list value")
print(list(my_new_dict.values()))

print("\n This new tuple")
print(tuple(my_new_dict))

print("\n This new set")
print(set(my_new_dict))

print(my_new_dict)

print("Values")
print(dict.fromkeys(list(my_new_dict.values())))
print(list(dict.fromkeys(list(my_new_dict.values()))))

print("Keys")
print(dict.fromkeys(list(my_new_dict.keys())))
print(list(dict.fromkeys(list(my_new_dict.keys()))))

print("Values + keys")
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))


