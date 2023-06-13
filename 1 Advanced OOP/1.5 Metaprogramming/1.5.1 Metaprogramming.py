"""
1. A metaclass is a class whose instances are classes (like Template in C++)
2. Metaclasses are related to instantiation
3. Metaclasses use:
    3.1 logging;
    3.2 registering classes at creation time;
    3.3 interface checking;
    3.4 automatically adding new methods;
    3.5 automatically adding new variables.
4. type() function:
    <class 'int'>
    <class 'list'>
    <class '__main__.Dog'>
    <class 'type'>
5. Conclusions:
    5.1 metaclasses are used to create classes;
    5.2 classes are used to create objects;
    5.3 the type of the metaclass type is type – no, that is not a typo.
    5.4 type is a class that generates classes defined by a programmer;
    5.5 metaclasses are subclasses of the type class.
6. type( , , ) creates a new class
"""
class MyClass:
    pass


myclass = MyClass()
print("MyClass.__name__:", MyClass.__name__)
print("MyClass.__class__:", MyClass.__class__)
print("type(MyClass):", type(MyClass))
print("MyClass.__bases__:", MyClass.__bases__)
print("MyClass.__dict__:", MyClass.__dict__)
print()
print("myclass.__class__:", myclass.__class__)
print("type(myclass):", type(myclass))
print("myclass.__dict__:", myclass.__dict__)
print()
print("int.__class__:", int.__class__)
print("type(int):", type(int))
print("int.__dict__:", int.__dict__)
print()
print("str.__class__:", str.__class__)
print("type(str):", type(str))
print("str.__dict__:", str.__dict__)
print()
print("bool.__class__:", bool.__class__)
print("type(bool):", type(bool))
print("bool.__dict__:", bool.__dict__)
print()
def get_name(self):
    return self.name
myattributes = { "name": "myclass1", "get_name": get_name }
MyClass1 = type("MyClass1",(MyClass,), myattributes)
print("MyClass1.__name__:", MyClass1.__name__)
print("MyClass1.__class__:", MyClass1.__class__)
print("type(MyClass1):", type(MyClass1))
print("MyClass1.__bases__:", MyClass1.__bases__)
print("MyClass1.__dict__:", MyClass1.__dict__)
print()
myclass1 = MyClass1()
print("myclass1.name:", myclass1.name)
print("myclass1.get_name():", myclass1.get_name())
print()

class Mymeta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.name = "This is my new attribute!!"
        return obj

class MyClassFromMeta(metaclass=Mymeta):
    pass

print("MyClassFromMeta.__name__:", MyClassFromMeta.__name__)
print("MyClassFromMeta.__class__:", MyClassFromMeta.__class__)
print("type(MyClassFromMeta):", type(MyClassFromMeta))
print("MyClassFromMeta.__bases__:", MyClassFromMeta.__bases__)
print("MyClassFromMeta.__dict__:", MyClassFromMeta.__dict__)

myclassfrommeta1 = MyClassFromMeta()
print("myclassfrommeta1.name:", myclassfrommeta1.name)
