"""
1. Decorators are used to:
    1.1 Perform operations before and after a call to a wrapped object
    1.2 prevent its execution
2. Use
    2.1 the validation of arguments;
    2.2 the modification of arguments;
    2.3 the modification of returned objects;
    2.4 the measurement of execution time;
    2.5 message logging;
    2.6 thread synchronization;
    2.7 code refactorization;
    2.8 caching.
3. Use closure the use a wrapper function inside a decorator
4. You can pass own arguments to decorator by creating a generic decorator and then creating 2 wrappers
5. You can use more than 1 decorators: they will be executed starting from the outer to the inner
"""
def decorator(function):
    print("I am calling the function:", function.__name__)
    return function
@decorator
def myfunction():
    print("this is myfunction")

myfunction()
print()

def decorator_new(function):
    def wrapper(*args, **kwargs):
        print("pre", function.__name__)
        function(*args, **kwargs)
        print("post", function.__name__)
    return wrapper
@decorator_new
def myfunction_new(*args, **kwargs):
    print("myfunction_new. args:", args, "kwargs:", kwargs)

myfunction_new(1,2, a=1)
print()

def generic_decorator(*decorator_args, **decorator_kwargs):
    def external_wrapper(function):
        print("generic_decorator. args:", decorator_args, "kwargs:", decorator_kwargs)
        def internal_wrapper(*args, **kwargs):
            print("pre", function.__name__)
            function(*args, **kwargs)
            print("post", function.__name__)
        return internal_wrapper
    return external_wrapper
@generic_decorator(2, b=3)
def myfunction_with_generic_decorator(*args, **kwargs):
    print("myfunction_with_generic_decorator. args:", args, "kwargs:", kwargs)

myfunction_with_generic_decorator(1, b=2)
print()

def generic_decorator_outer(*decorator_args, **decorator_kwargs):
    def external_wrapper(function):
        def internal_wrapper(*args, **kwargs):
            print("outer.pre", function.__name__)
            function(*args, **kwargs)
            print("outer.post", function.__name__)
        return internal_wrapper
    return external_wrapper
def generic_decorator_inner(*decorator_args, **decorator_kwargs):
    def external_wrapper(function):
        def internal_wrapper(*args, **kwargs):
            print("inner.pre", function.__name__)
            function(*args, **kwargs)
            print("inner.post", function.__name__)
        return internal_wrapper
    return external_wrapper
@generic_decorator_outer(1, b=2)
@generic_decorator_inner(3, b=4)
def myfunction_with_generic_stacked_decorators(*args, **kwargs):
    print("myfunction_with_generic_decorator. args:", args, "kwargs:", kwargs)

myfunction_with_generic_stacked_decorators(5, b=6)
print()
