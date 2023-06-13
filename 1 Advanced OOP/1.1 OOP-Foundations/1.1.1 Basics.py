"""
1. self cannot be used when calling a static method or without an instance
2. getattr() and setattr() to get attribute of an Object
3. __class__ shows the type:
    "type" for static class#
    "__main__".CLASS_NAME for objects
    "str" for strings
    "method" for methods
4. Instance variables: they use self -> only related to the instance
5. __dict__ shows the contents of an object/class: key/value json "__dict__(OBJECTNAME)"
6. Class variables: defined outside any methods, "__dict__(CLASSNAME)",
   __dict__(OBJECTNAME) does not show class variables
   CLASS_NAME.CLASS_ATTR_NAME = VALUE to set the value of a class
   Do not use OBJECT_NAME.CLASS_ATTR_NAME = VALUE, it creates a new instance variable!!
7. variables without SELF are just local
8. when reading a self.VARIABLE_NAME, if it doesn't exist it will use the static variable. Then COW
"""


class MyClass:
    static_var = "static"

    def __init__(self):
        static_var = "local_var"

        print("static_var:", static_var)
        print("self.static_var:", self.static_var)
        print("MyClass.static_var:", MyClass.static_var)

        self.static_var = "dynamic1"

        print("static_var:", static_var)
        print("self.static_var:", self.static_var)
        print("MyClass.static_var:", MyClass.static_var)

        print()


i1 = MyClass()
i2 = MyClass()

print(MyClass.static_var)
