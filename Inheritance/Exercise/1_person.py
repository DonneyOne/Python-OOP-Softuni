class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)


child = Child("Andon", 13)
print(child.__dict__)
