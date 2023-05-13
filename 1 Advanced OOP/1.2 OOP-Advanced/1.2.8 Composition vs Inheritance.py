"""
1. Inheritance: attention to the class explosion problem!
2. Inheritance = is_a
3. Composition = has_a. The class is a "container" (composite) of other objects
4. Composition = more responsibility to the developer who needs to implement all methods
"""
class Myclass:
    def __init__(self, name):
        self.name = name
class Firstclass(Myclass):
    pass
class Secondclass(Myclass):
    def __init__(self, name, other_obj=None):
        super().__init__(name)
        if other_obj is not None:
            self.other_obj = other_obj


firstclass = Firstclass("firstclass")
secondclass = Secondclass("secondclass", firstclass)
print(secondclass.other_obj.name)
