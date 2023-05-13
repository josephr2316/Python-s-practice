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


