"""
1. Object creation
2. Value assignment
3. Object labeling
4. id() returns the ID of an object, which is
    4.1 unique
    4.2 constant
    4.3 Used to debug
    4.4 2 variables referring to the same object have the same id
5. "==" compares the values
6. "is" compares the IDs
"""


class Myclass:
    pass


myclass1 = Myclass()
myclass2 = myclass1
myclass3 = Myclass()
print("id(Myclass): ", id(Myclass))
print("id(myclass1): ", id(myclass1))
print("id(myclass2): ", id(myclass2))
print("myclass1 == myclass2:", myclass1 == myclass2)
print("myclass1 == myclass3:", myclass1 == myclass3)
print("myclass1 is myclass2:", myclass1 is myclass2)
print("myclass1 is myclass3:", myclass1 is myclass3)
