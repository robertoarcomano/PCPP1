"""
1. Multiple inhreritance: MRO problem (conflict between left first rule and specialisation rule.
    It happens when you select a base class before a more specialised one)
2. Polymorphism:
    2.1. Inheritance (same method name in different classes in the same inheritance tree)
    2.2. Duck typing (only some of the classes can manage a specific method -> otherwise exception)
         It is more generic than simple inheritance
"""
def polymorphism():
    a = 10
    print(a.__add__(20))
    a = "Hello"
    print(a.__add__(" World!"))


polymorphism()


class Person:
    def __init__(self, name):
        self.name = name
    def title(self):
        pass
    def presentation(self):
        print(self.title() + self.name)


class Man(Person):
    def title(self):
        return "Mr."


class Woman(Person):
    def title(self):
        return "Ms."


tom = Man("Tom")
lucy = Woman("Lucy")
for person in (tom, lucy):
    person.presentation()

print(help(tom))