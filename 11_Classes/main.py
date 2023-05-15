###  Classes ###

class MyEmptyPerson:
    # def __int__(self) -> None:  # def __int__(self):  # Empty constructor
    #     pass
    pass  # It will generate an error if there's no code inside, pass avoid this.


class Person:
    def __init__(self, name, surname, alias="Without alias"):  # If alias doesn't have a default value, has to be sent.
        self.name = name  # Public
        self.surname = surname  # Public
        # self.__name = name  # Private
        # self.__surname = surname  # Private
        self.__surname = "Marcus"  # Private
        self.full_name = f"{name} {surname} ({alias})"
        # pass should  be removed, although it works with it

    def walk(self):
        print(f"{self.full_name} is walking")

    def get_name(self):
        return self.__surname


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
print(my_person.get_name())
print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)
my_person.walk()

my_new_person = NewPerson()
print(my_new_person.name)
print(f"{my_new_person.name} {my_new_person.surname}")

my_other_person = Person("Edward", "Rojas", "Elior Arthur")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Dominigel Rodriguez Pena (who has strength)"
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = 666
print(my_other_person.full_name)
my_other_person.walk()
