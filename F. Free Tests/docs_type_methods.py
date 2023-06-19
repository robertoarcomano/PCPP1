def title(string):
    print("###", string, "###")


my_var = 5
my_string = "ok"


class MyClass:
    static_var = 8

    def __init__(self):
        pass


def fn(a=True):
    """fn function"""
    pass


text_number = 1
title("fn.__doc__")
print(fn.__doc__)
print()

title("help(fn)")
help(fn)
print()

title("dir()")
print(dir())

title("type(var)")
print(type(my_var))
print()

title("type(string)")
print(type(my_string))
print()

title("type(fn)")
print(type(fn))
print()

title("type(MyClass)")
print(type(MyClass))
print()

title("type(MyClass.static_var)")
print(type(MyClass.static_var))
print()

title("type(MyClass.__init__)")
print(type(MyClass.__init__))
print()
