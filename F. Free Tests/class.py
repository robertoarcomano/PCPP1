class MyClass:
    def __init__(self, name):
        self.name = name

my_object = MyClass("Roberto")
print(getattr(my_object, "name"))
setattr(my_object, "name", "Roby")
print(getattr(my_object, "name"))
