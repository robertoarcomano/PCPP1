from common import title
import time


def add_intro(func):
    def wrapper(name):
        start = time.perf_counter()
        s = "before |"
        s += func("Mr." + name)
        time.sleep(0.1)
        stop = time.perf_counter()
        s += "| after |" + str(stop - start) + " seconds"
        return s

    return wrapper


def add_intro_with_params(person_title):
    def external_wrapper(func):
        def internal_wrapper(name):
            start = time.perf_counter()
            s = "before |"
            s += func(person_title + name)
            time.sleep(0.1)
            stop = time.perf_counter()
            s += "| after |" + str(stop - start) + " seconds"
            return s

        return internal_wrapper

    return external_wrapper


def add_thank_you_with_params(thank_you):
    def external_wrapper(func):
        def internal_wrapper(name):
            return func(name + "! " + thank_you)

        return internal_wrapper

    return external_wrapper


def greeting(name):
    return "Hello " + name


@add_intro
def greeting_auto(name):
    return "Hello " + name


@add_intro_with_params("Ms.")
def greeting_params_auto(name):
    return "Hello " + name


@add_thank_you_with_params("Thanks")
@add_intro_with_params("Ms.")
def greeting_with_thank_you_params_auto(name):
    return "Hello " + name


class UpperCase:
    def __init__(self, function):
        self.function = function

    def __call__(self, name):
        return self.function(name.upper())


@UpperCase
def greeting_upper(name):
    return "Hello " + name


class UpperCaseWithParams:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, function):
        def wrapper(name):
            return function(name.lower() + str(self.args))

        return wrapper


@UpperCaseWithParams(False)
def greeting_upper_with_params(name):
    return "Hello " + name


def upper_the_constructor(class_):
    class_.old__init__ = class_.__init__

    def new_constructor(self, name):
        class_.old__init__(self, name.upper())

    class_.__init__ = new_constructor
    return class_


@upper_the_constructor
class MyClass:
    def __init__(self, name):
        self.name = name


greeting_manual = add_intro(greeting)
title("greeting_manual('Roby')", greeting_manual('Roby'))
title("greeting_auto('Roby')", greeting_auto('Roby'))

greeting_params_manual = add_intro_with_params("Ms.")(greeting)
title("greeting_params_manual('Roby')", greeting_params_manual('Roby'))
title("greeting_params_auto('Roby')", greeting_params_auto('Roby'))

greeting_with_thank_you_params_manual = add_thank_you_with_params("Thanks")(add_intro_with_params("Ms.")(greeting))
title("greeting_with_thank_you_params_manual('Roby')", greeting_with_thank_you_params_manual('Roby'))
title("greeting_with_thank_you_params_auto('Roby')", greeting_with_thank_you_params_auto('Roby'))

greeting_upper_manual = UpperCase(greeting)
title("greeting_upper_manual('Roby')", greeting_upper_manual('Roby'))
title("greeting_upper('Roby')", greeting_upper('Roby'))

greeting_upper_with_params_manual = UpperCaseWithParams(False)(greeting)
title("greeting_upper_with_params_manual('Roby')", greeting_upper_with_params_manual('Roby'))
title("greeting_upper_with_params('Roby')", greeting_upper_with_params('Roby'))

my_obj = MyClass("Roberto")
title("my_obj.name", my_obj.name)
