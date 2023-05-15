###  Classes ###

class MyEmptyPerson:
    # def __int__(self) -> None:  # def __int__(self):  # Empty constructor
    #     pass
    pass  # It will generate an error if there's no code inside, pass avoid this.


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # pass should  be removed, although it works with it

class NewPerson:
    def __init__(self):
        self.name = "Elior"
        self.surname = "Sberkiet"
        # pass should  be removed, although it works with it

print("Hello")
print(MyEmptyPerson)
print(MyEmptyPerson())

my_person = Person("Joseph", "Rodriguez")
print(my_person.name)
print(f"{my_person.name} {my_person.surname}")

my_new_person = NewPerson()
print(my_new_person.name)
print(f"{my_new_person.name} {my_new_person.surname}")

