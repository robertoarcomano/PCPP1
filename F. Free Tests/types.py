var = 5
string = "ok"


def fn():
    pass


class MyClass:
    static_var = 8

    def __init__(self):
        pass


print(type(var))
print(type(string))
print(type(fn))
print(type(MyClass))
print(type(MyClass.static_var))
print(type(MyClass.__init__))
