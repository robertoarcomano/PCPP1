import json


def show_types(obj):
    var = globals()[obj]
    print("type({}):".format(obj), type(var), " | {}.__class__:".format(obj), var.__class__)


class MyClass:
    '''My __init__ method'''

    def __init__(self, name):
        self.name = name
        print(global_var)

    @staticmethod
    def my_static():
        print(global_var)
        return False


global_var = "ok"
my_object = MyClass("Roberto")
my_object.my_static()
print("getattr(my_object, \"name\"):", getattr(my_object, "name"))
print("setattr(my_object, \"name\", \"Roby\")")
setattr(my_object, "name", "Roby")
print("getattr(my_object, \"name\"):", getattr(my_object, "name"))
print()

show_types("my_object")
show_types("MyClass")
show_types("__name__")
""" my variable a"""
a = 2
show_types("a")
print()

print("MyClass.__dict__:", MyClass.__dict__)
print("MyClass.__doc__:", MyClass.__doc__)
print("dir():", dir())
