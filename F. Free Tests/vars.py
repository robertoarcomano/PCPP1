"""
The concrete behavior will depend on the Python scope in which you’re assigning the name.
If you try to assign a value to a global name inside a function,
then you’ll be creating that name in the function’s local scope, shadowing or overriding the global name.
This means that you won’t be able to change most variables that have been defined outside the function from within the function.
g = 10
def fn():
    g += 1
"""

global_var = 1
# nonlocal
# LEGB stand for Local, Enclosing, Global, and Built-in
# __code__


def fn1():
    global_var = 2
    print(global_var)


def fn2():
    # Error
    # global_var +=1
    pass


def fn3():
    nonlocal_var = 1
    def fn31():
        print(nonlocal_var)
        # Error
        # nonlocal_var +=1


def fn4():
    nonlocal_var = 1
    def fn41():
        nonlocal nonlocal_var
        print(nonlocal_var)
        nonlocal_var +=1


print(global_var)
fn1()
fn2()
fn3()
fn4()
print(global_var)

