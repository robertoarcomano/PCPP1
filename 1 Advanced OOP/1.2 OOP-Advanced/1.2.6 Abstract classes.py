"""
1 Abstract classes are a contract between
    1.1 The class designer
    1.2 The programmer
2 You need to import abc module
"""
import abc


class MyClass(abc.ABC):
    def __init__(self, name):
        self.name = name
    @abc.abstractmethod
    def presentation(self, *args, **kwargs):
        pass
    def get_name(self):
        return self.name
class MyClass1(MyClass):
    def presentation(self, *args, **kwargs):
        self.name = args[0] + " " + self.name

myclass1 = MyClass1("myclass1")
myclass1.presentation("Hello")
print(myclass1.get_name())
