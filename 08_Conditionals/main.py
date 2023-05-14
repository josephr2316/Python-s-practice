### Conditionals ###

# my_condition: bool = True
my_condition = False

if my_condition :  # It's the same as if my_condition == True
    print("The if condition is executed")

my_condition = 5 * 2
if my_condition:
    print("The second if condition is executed")

if my_condition == 11:
    print("The third if condition is executed")

if my_condition == 10:
    print("The fourth if condition is executed")

if my_condition >= 10:
    print("The fifth if condition is executed")

if my_condition > 10:
    print("The sixth if condition is executed")

if my_condition > 11:
    print("It's greater than 11")
else:
    print("It's less than or equal to 11")

my_condition = 5 * 5
my_condition = 5 * 2
my_condition = 5 * 3
if my_condition > 11 and my_condition < 20:  # if 11 < my_condition < 20:
    print("It's greater than 11 adn less than 20")
    print("It's greater than 11 adn less than 20")
else:
    print("It's less than or equal to 11 and greater than 20")
    print("It's less than or equal to 11 and greater than 20")


print("The execution continues")