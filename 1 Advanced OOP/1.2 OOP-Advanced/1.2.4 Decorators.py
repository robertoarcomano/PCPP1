"""
1. Decorators are used to:
    1.1 Perform operations before and after a call to a wrapped object
    1.2 prevent its execution
2. Use
    2.1 the validation of arguments;
    2.2 the modification of arguments;
    2.3 the modification of returned objects;
    # 2.4 the measurement of execution time;
    2.5 message logging;
    2.6 thread synchronization;
    2.7 code refactorization;
    2.8 caching.
3. Use closure the use a wrapper function inside a decorator
4. You can pass own arguments to decorator by creating a generic decorator and then creating 2 wrappers
5. You can use more than 1 decorator: they will be executed starting from the outer to the inner
6. You can use a Class decorating: use __init__ amd __call__
7. You can use a Class decorating with arguments: use __init__ amd __call__
8. You can decorate a Class
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


myfunction_new(1, 2, a=1)
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


class ClassDecorating:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("ClassDecorating.pre. args:", args, " kwargs:", kwargs)
        self.function(*args, **kwargs)
        print("ClassDecorating.post. args:", args, " kwargs:", kwargs)


@ClassDecorating
def myfunction_with_class_decorating(*args, **kwargs):
    print("myfunction_with_class_decorating. args:", args, "kwargs:", kwargs)


myfunction_with_class_decorating(1, b=2)
print()


class ClassDecoratingWithArguments:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            print("ClassDecoratingWithArguments.pre. args:", args, " kwargs:", kwargs)
            function(*args, **kwargs)
            print("ClassDecoratingWithArguments.post. args:", args, " kwargs:", kwargs)

        return wrapper


@ClassDecoratingWithArguments(3, c=2)
def myfunction_with_class_decorating_with_arguments(*args, **kwargs):
    print("myfunction_with_class_decorating_with_arguments. args:", args, "kwargs:", kwargs)


myfunction_with_class_decorating_with_arguments(1, b=2)
print()


def myfunction_decorator_of_class(class_):
    class_.__old_getattribute__ = class_.__getattribute__

    def new_getattr(self, name):
        if name == "name":
            print("name is read")
        return class_.__old_getattribute__(self, name)

    class_.__getattribute__ = new_getattr
    return class_


@myfunction_decorator_of_class
class ClassDecorator:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class_decorator = ClassDecorator("class_decorator")
class_decorator.get_name()
print()
