### Exception Handling ###

numberOne, numberTwo = 5, 1
# print(5 + "5")
print(numberOne + numberTwo)

numberTwo = "1"

"""
if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("It was not fulfilled")
    
if numberOne > 3:
    print(numberOne + numberTwo)
else:
    print("No se cumplio")
"""

# try except
try:
    print(numberOne + numberTwo)
    print("No error has occurred")
except:
    print("An error has occurred.")

# try except else
try:
    print(numberOne + numberTwo)
    print("No error has occurred")
except:
    print("An error has occurred.")
else:  # There is no exception, it will be executed
    print("The execution continues correctly.")

# try except else finally
try:
    print(numberOne + numberTwo)
    print("No error has occurred")
except:
    print("An error has occurred.")
else:   # Optional
    # There is no exception, it will be executed
    print("The execution continues correctly.")
finally:  # Optional
    # Runs always, It's always executed
    print("The execution continues")


# Exceptions by type
try:
    print(numberOne + numberTwo)
    print("No error has occurred")
except ValueError:
    print("A ValueError has occurred.")
except TypeError:
    print("A TypeError has occurred.")

#  Capturing the exception information

try:
    print(numberOne + numberTwo)
    print("No error has occurred")
# except TypeError as error:
except ValueError as error:
    print(error)
except Exception as error:
    print(error)