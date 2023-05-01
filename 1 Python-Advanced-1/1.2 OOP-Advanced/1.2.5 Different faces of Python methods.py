"""
1. Self is used to reference different class instances
2. Class methods
    2.1 @classmethod
    2.2 cls instead of self
    2.3 __init__ needs to use the class name (i.e. Myclass)
    2.4. Use of class methods as an alternative constructor
3. Static methods are utility methods
    3.1 Pure algorithms not referring neither class objects nor the class
    3.2 Stateless
"""
class Myclass:
    class_counter=0
    def __init__(self, name):
        self.name = name
        self.version = ""
        Myclass.class_counter+=1
    @classmethod
    def create_with_version(cls, name, version):
        new_obj = cls(name)
        new_obj.version = version
        return new_obj
    def get_name(self):
        return self.name
    def get_version(self):
        return self.version
    @classmethod
    def get_class_counter(cls):
        return cls.class_counter
    @staticmethod
    def is_counter_more_than_2(counter):
        return False if counter < 2 else True

myclass1 = Myclass("myclass1")
myclass2 = Myclass("myclass2")
print(myclass1.get_class_counter())
print(Myclass.get_class_counter())

myclass3 = Myclass.create_with_version("myclass3","1.01")
print(myclass1.get_version())
print(myclass3.get_version())

print(Myclass.is_counter_more_than_2(Myclass.get_class_counter()))
