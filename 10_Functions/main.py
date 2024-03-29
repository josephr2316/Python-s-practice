### Functions ###

def my_function():
    print("This is a function")
    # my_function()  # Loop


my_function()
my_function()
my_function()


def sum_two_values(first_number, second_number):  # sum_two_values(first_number: int, second_number: int):
    # It won't work, if you enter string,
    # need a verification in the function
    # It's a static typing, it's not dynamic typing, weak typing.
    print(first_number + second_number)
    # print(first_number / second_number)  # Won't work with String


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)


def sum_two_values_with_return(first_number, second_number):
    my_sum = first_number + second_number
    # return first_number + second_number
    return my_sum


my_result = sum_two_values_with_return(10, 5)
print(my_result)
my_result = sum_two_values(1.4, 5.2)  # Return null
print(my_result)  # No values inside


def print_name(name, surname):
    print(f"{name} {surname}")
    print("{name} {surname}")


print_name("Joseph", "Rodriguez Kelly")
print_name(surname="Rodriguez Kelly", name="Joseph")


def print_name_with_default(name, surname, alias="Without alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Joseph", "Rodriguez Kelly")
print_name_with_default("Joseph", "Rodriguez Kelly", "Elior Arthur")


def print_texts(*texts):  # * To print several texts
    for text in texts:
        print(text)
    print(texts)


def print_upper_texts(*texts):  # * To print several texts
    print(type(texts))
    for text in texts:
        print(text.upper())


def print_text(text):  # * To print several texts
    print(text)


print_texts("Hello", "Python", "Joseph Rodriguez")  # Tuple
print_upper_texts("Hello", "Python", "Joseph Rodriguez")  # Tuple
print_texts("Hello")
print_text("Hello")
