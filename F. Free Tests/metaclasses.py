from common import title

Dyna = type("Dyna", (), {})
title("type(Dyna)", type(Dyna))
title("Dyna.__name__", Dyna.__name__)


def set_name(obj, name):
    obj.name = name


Dyna1 = type("Dyna1", (Dyna,), {
    "name": "Dyna1 name",
    "get_name": lambda x: x.name,
    "set_name": set_name
})
title("type(Dyna1)", type(Dyna1))
title("Dyna1.__name__", Dyna1.__name__)
title("Dyna1.get_name", Dyna1.get_name)
dyna1 = Dyna1()
title("dyna1.get_name()", dyna1.get_name())
dyna1.set_name("New Dyna1 name")
title("dyna1.get_name()", dyna1.get_name())


class MyClass:
    attr = "Attribute added via normale inheritance"
    pass


class MyClass1(MyClass):
    pass


class MyMeta(type):
    attr = "Attribute added via metaclass"


class MyClassFromMeta(metaclass=MyMeta):
    pass


my_obj = MyClass()
title("type(my_obj)", type(my_obj))
title("type(MyClass)", type(MyClass))
title("MyClass1.attr", MyClass1.attr)
title("MyClassFromMeta.attr", MyClassFromMeta.attr)
