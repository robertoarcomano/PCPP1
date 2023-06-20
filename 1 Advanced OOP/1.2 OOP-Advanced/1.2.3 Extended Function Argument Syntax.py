"""
1. Functions can have
    1.1 No arguments
    1.2 Only mandatory arguments
    1.3 Mandatory and optional arguments (default values are specified)
2. Functions can be called
    2.1 With positional arguments
    2.2 With keyword arguments
    2.3 With a mix, first positional then keyword one
3. Function can have a variable number of arguments using
    3.1 additional positional arguments *args (tuple)
    3.2 additional keyword arguments **kwargs (dictionary)
"""


def function(a, b, c="c", *args, z="z", **kwargs):
    print("function")
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("args: ", args)
    print("z: ", z)
    print("kwargs: ", kwargs)
    sub_function(*args, **kwargs)


def sub_function(*args, **kwargs):
    print()
    print("sub_function")
    print("args: ", args)
    print("kwargs: ", kwargs)


function(1, 2, 3, 4, z="k", name="Roberto")
