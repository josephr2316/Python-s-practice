# Variables

MyVariable = "My String variable"
# Lo habitual es comenzarlo en minuscula con camel case, siguiendo la subida de un camello
_if = False
print(MyVariable)

my_variable = "My String variable"
print(my_variable)

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable , my_bool_variable)
type(print(my_string_variable, my_int_to_str_variable , my_bool_variable))  # No imprime el type sin el print
print(type(print(my_string_variable, my_int_to_str_variable , my_bool_variable)))  # Type ""NoneType", es una funcion del sistema no tiene un tipo de dato
print("This is the value of:", my_bool_variable)

# Funciones del sistema
# Algunas funciones del sistema
print(len(my_int_to_str_variable))
print(len(my_string_variable))

# Variables en una sola linea,!Cuidado con abusar de esta sintaxis!
name, surname, nickname, age, = "Joseph", "Rodriguez Kelly", "Elior", 28
print("My name is:", name, surname, ". I'm :", age, "years old. My nickname is: ", nickname)

# Inputs
"""
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
"""

name = 35
age = "Joseph"

# Changed the type
print(name)
print(age)

# Force the type
address: str = "My direction"
address = 32
print(type(address))

address:  int = 32
print(type(address))

address = True
print(type(address))

address = True
address = 5
address = 1.2
print(type(address))







