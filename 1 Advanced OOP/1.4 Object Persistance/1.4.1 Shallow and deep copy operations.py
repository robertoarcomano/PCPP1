"""
1. Object creation
2. Value assignment
3. Object labeling
4. id() returns the ID of an object, which is
    4.1 unique
    4.2 constant
    4.3 Used to debug
    4.4 2 variables referring to the same object have the same id
5. "==" compares the values (dict, list, tuples. For normal objects it just compares the address)
6. "is" compares the IDs
7. Shallow copy: copy of the reference
8. Deep copy: copy of the content
9. When copying an object using a copy.deepcopy(), the __init__ will not be executed
"""
import time
import copy


class MyClass:
    pass


myclass1 = MyClass()
myclass2 = myclass1
myclass3 = MyClass()
print("id(MyClass): ", id(MyClass))
print("id(myclass1): ", id(myclass1))
print("id(myclass2): ", id(myclass2))
print("id(myclass3): ", id(myclass3))
print("myclass1 == myclass2:", myclass1 == myclass2)
print("myclass1 == myclass3:", myclass1 == myclass3)
print("myclass1 is myclass2:", myclass1 is myclass2)
print("myclass1 is myclass3:", myclass1 is myclass3)

o1 = [i for i in range(1,10000000)]
o2 = [i for i in range(1,10000000)]

start = time.time()
print(o1 is o2)
stop = time.time()
print("Time to execute \"is\":", stop-start)

start = time.time()
print(o1 == o2)
stop = time.time()
print("Time to execute \"==\":", stop-start)

start = time.time()
o2 = copy.copy(o1)
stop = time.time()
print("Time to execute copy.copy():", stop-start)

start = time.time()
o2 = copy.deepcopy(o1)
stop = time.time()
print("Time to execute copy.deepcopy():", stop-start)
