### Arithmetic Operators ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 / 3)
print(10 % 2)
print(10 / 3)
print(10 // 3)  # Flower division to convert to an  integral
print(2 ** 3)  # Power of a number
print(2 ** 3 + 3 - 7 / 1 // 4)

print("Hello" + "Python")  # Concatenate without space
print("Hello" + "Python" + "What's up?")  # Concatenate without space
# print("Hello" + 5) # Won't work
# print("Hello " + str(5)) # Won't work
# print("Hello" - "Python") # Won't work
# print("Hello" * "Python") # Won't work
print("Hello" * 5)  # Shows hello 5 times
# print("Hello" * 2 ** 3 + 3 - 7 / 1 //4) # Won't work
# print("Hello" * (2 ** 3 + 3 - 7 / 1 //4)) # Won't work
print("Hello" * (2 ** 3))  # It works cus it's an int
# print("Hello" * 2.5) # Won't work
# print("Hello" * 2.5 * 2) # Won't work
# print("Hello" * (2.5 * 2)) # Won't work

my_int = 2.5 * 5
my_float = 2.5 * 2
# print("Hello " * int(my_float) # Won't work cus it's float

6 + 10  # Doesn't show the result without print

### Comparative Operators ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)
print(3 > 4 > 2)

print("Hello" > "Python")
print("Hello" < "Python")
print("Hello" >= "Python")
print("Hello" >= "Hello")
print("Hola" >= "Bola")  # True
print("Hola" >= "Zola")  # False
print("aaaa" >= "aaaa")  # False
print("aaaa" >= "abaa")  # False
print("AAAA" >= "aaaa")  # False
print("aaaa" >= "AAAA")  # True, alphabetical sorting by ascii
print(len("aaaa") >= len("abaa"))  # Count caracters

print("Hello" >= "Bello")  # It's gonna be true, cus compare the length
print("Hello" >= "Zello")  # It's gonna be false, cus compare alphabetical order
print("Hello" <= "Python")
print("Hello" == "Hello")
print("Hello" != "Python")

### Logical Operators ###

print(3 > 4 and "Hello" > "Python")
print(3 > 4 or "Hello" > "Python")
print(3 < 4 and "Hello" < "Python")
print(3 < 4 or "Hello" < "Python")
print(3 < 4 or "Hello" > "Python")
print(3 < 4 or "Hello" > "Python" and 4 == 4)
print(3 < 4 or ("Hello" > "Python" and 4 == 4))
# print(3 < 4 not "Hello" < "Python") # Won't work
print(not (3 > 4))

