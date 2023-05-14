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