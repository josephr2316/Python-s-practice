###  Classes ###

class MyEmptyPerson:
    # def __int__(self) -> None:  # def __int__(self):  # Empty constructor
    #     pass
    pass  # It will generate an error if there's no code inside, pass avoid this.


class Person:
    def __init__(self, name, surname):
        pass


print("Hello")
print(MyEmptyPerson)
print(MyEmptyPerson())

my_person = Person("Joseph", "Rodriguez")
print(my_person.name)
