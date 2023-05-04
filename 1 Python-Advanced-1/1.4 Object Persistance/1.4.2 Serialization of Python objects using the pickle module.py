"""
1. Object serialization/deserialization
2. Use can use 'pickle' module
3. Object that can be 'pickled':
    3.1 None, booleans;
    3.2 integers, floating-point numbers, complex numbers;
    3.3 strings, bytes, bytearrays;
    3.4 tuples, lists, sets, and dictionaries containing pickleable objects;
    3.5 objects, including objects with references to other objects (remember to avoid cycles!)
    3.6 references to functions and classes, but not their definitions.
4. Saving: pickle.dump(obj, file)
5. Loading: obj = pickle.load(file)
6. The order it very important when loading
7. You can use pickle.dumps() and pickle.loads() to convert an object to a byte array
8. PicklingError exception when trying to pickle non-pickleable objects
9. RecursionError exception when exceeding the stack size
10. AttributeError exception when you cannot import data
11. No code dumped or loaded
"""
import pickle
DATAFILE = "datafile"


def dump_and_load(obj):
    with open(DATAFILE, 'wb') as file_out:
        pickle.dump(obj, file_out)
    with open(DATAFILE, 'rb') as file_in:
        return pickle.load(file_in)


def dumps_and_loads(obj):
    with open(DATAFILE, 'wb') as file_out:
        bytes_array = pickle.dumps(obj)
        file_out.write(bytes_array)
    with open(DATAFILE, 'rb') as file_in:
        bytes_array = pickle.dumps(obj)
        bytes_array = file_in.read(len(bytes_array))
        return pickle.loads(bytes_array)


obj = [
    {
        "name": "Roberto",
        "age": 48
    },
    ["name", "age", 33]
]

ret_obj = dump_and_load(obj)
print(ret_obj == obj)

ret_obj = dumps_and_loads(obj)
print(ret_obj == obj)


class MyClass:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other_obj):
        return self.name == other_obj.name


obj = MyClass("Roberto")
ret_obj = dump_and_load(obj)
print(ret_obj == obj)
