from common import title

my_var = 5
my_string = "ok"


class Base:
    pass


class MyClass(Base):
    static_var = 8

    def __init__(self):
        pass


def fn(a=True):
    """fn function"""
    pass


my_obj = MyClass()
text_number = 1
title("fn.__doc__", fn.__doc__)

title("help(fn)")
help(fn)
print()

title("dir()", dir())

title("type(var)", type(my_var))

title("type(string)", type(my_string))

title("type(fn)", type(fn))

title("type(MyClass)", type(MyClass))

title("type(MyClass.static_var)", type(MyClass.static_var))

title("type(MyClass.__init__)", type(MyClass.__init__))

title("isinstance(my_obj, Base)", isinstance(my_obj, Base))

title("issubclass(MyClass, Base)", issubclass(MyClass, Base))

real = 10.6
title("real [float]", real)

n = int(real)
title("n = int(real)", n)

h = hex(n)
title("hex(n)", hex(n))

f = float(n)
title("float(n)", f)

o = oct(n)
title("oct(n)", o)

b = bool(n)
title("b = bool(n)", b)

s = str(b)
title("str(b)", s)

print("a = [1, 2, 3]")
print("b = [1, 2, 3]")
print()

a = [1, 2, 3]
b = [1, 2, 3]
title("a == b", a == b)
title("a is b", a is b)
