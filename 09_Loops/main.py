### Loops ###

# While

my_condition = 0

while my_condition < 10:  # We can use else, but it does not accept the others.
    print(my_condition)
    # my_condition += 1
    my_condition += 2
else:  # It's optional
    print("My condition is greater or equal to 10")

# if my_condition == 10:
#     print("My condition is equal to 10")
# else:
#     print("My condition is greater or equal to 10") # Else can't be alone, we cannot start with else

while my_condition < 20:
    print("My condition is greater or equal to 20")
    my_condition += 1
    if my_condition == 15:
        print("My condition is equal to 15")
        print("The execution is stopped")
        break
    print(my_condition)
print("The execution continues")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

print("\n" + "List\n")
for element in my_list:
    print(element)

my_tuple = (28, 1.85, "Joseph", "Rodriguez Kelly", "Joseph")

print("\n" + "Tuple\n")
for element in my_tuple:
    print(element)

my_set = {"Joseph", "Rodriguez Kelly", 28}

print("\n" + "Set\n")
for element in my_set:
    print(element)

my_dict = {"Joseph": "Joseph", "Surname": "Rodriguez Kelly", "Age": 28, 1:"Python"}

print("\n" + "Dictionary Keys\n")
for element in my_dict:
    print(element)
    if element == "Age":
        break
    print("It's executed")
else:
    print("The for loop for the dictionary has finished")

print("\n" + "Dictionary Keys Part II\n")
for element in my_dict:
    print(element)
    if element == "Age":
        continue  # Continue to the for, stop the execution to this point.
    """
    It's like  
     if element == "Age":
     else:
        print("It's executed")

    """
    print("It's executed")
else:
    print("The for loop for the dictionary has finished")

print("\n" + "Dictionary Values\n")
for element in my_dict.values():
    print(element)

