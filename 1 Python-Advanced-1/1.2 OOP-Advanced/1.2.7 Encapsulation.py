"""
1. Flexible Access to Properties
2. property() and @property
3. @property creates a fake attribute (only for getting)
4. @ATTRIBUTE.setter uses "=" operator
5. @ATTRIBUTE.deleter to remove the attribute
"""
class Myclass:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @name.deleter
    def name(self):
        self.__name = None


myclass = Myclass("myclass")
print(myclass.name)
myclass.name = "myclass2"
print(myclass.name)
del myclass.name
print(myclass.name)
