### Strings ###

my_string = "My String"
my_other_string = 'My other String'
print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "This is a String\nwith line break"
print(my_new_line_string)

my_tab_string = "\tThis is a String with tab"
print(my_tab_string)

my_scape_string = "\\tThis is a String \\n scape"
print(my_scape_string)

# Format

name, surname, age = "Joseph", "Kelly", 29

print("My name is Elior Arthur")
print("My name is {} {} and I turned {}".format(name, surname, age))
print("My name is %s %s and I turned %d" % (name, surname, age))

# print("My name is %s %s and I turned %d" % (name, surname, "Hello"))    # Won't work

print("My names is " + name + " " + surname + " and I turned " + str(age))  # Avoid this
print(f"My name is {name} {surname} and I turned {age}")

# Character unpacking #
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(e)
print(f)

# Division/Split
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]  # Count from 0, -1, -2, etc...
print(language_slice)

language_slice = language[1:2:4]  # The third number indicate the jumb, from one character to another
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Functions
language = "python"
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("py"))
print(language.startswith("Py"))
print("Py" == "py")
