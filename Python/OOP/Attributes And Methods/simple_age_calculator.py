from datetime import date

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = date.today().year - birth_year
        return cls(name, age)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person.from_birth_year("Rafaelo", 1995)
person_2 = Person.from_birth_year("Ana", 2002)
person.display()
person_2.display()
