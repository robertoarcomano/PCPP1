"""
The concrete behavior will depend on the Python scope in which you’re assigning the name.
If you try to assign a value to a global name inside a function,
then you’ll be creating that name in the function’s local scope, shadowing or overriding the global name.
This means that you won’t be able to change most variables that have been defined outside the function from within the function.
g = 10
def fn():
    g += 1
"""
from common import title

global_var = 1


def fn1():
    global_var = 2
    return global_var


# nonlocal
# LEGB stand for Local, Enclosing, Global, and Built-in
# __code__


def fn2():
    try:
        global_var += 1
    except BaseException as ex:
        return ex
    pass


def fn3():
    nonlocal_var = 1

    def fn31():
        nonlocal nonlocal_var
        nonlocal_var += 1
        return nonlocal_var

    return fn31()


title("global_var", global_var)
title("fn1().global_var", fn1(), "global_var", global_var)
title("fn2()", fn2())
title("fn3().nonlocal_var", fn3())
print("Reference by string. globals()['global_var']:", globals()['global_var'])
