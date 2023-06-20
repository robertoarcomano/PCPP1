from common import title
import time


def add_mr(func):
    def wrapper(name):
        start = time.perf_counter()
        s = "before |"
        s += func("Mr." + name)
        time.sleep(0.1)
        stop = time.perf_counter()
        s += "| after |" + str(stop - start) + " seconds"
        return s

    return wrapper


def add_params(person_title):
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


def greeting(name):
    return "Hello " + name


@add_mr
def greeting_auto(name):
    return "Hello " + name


@add_params("Ms.")
def greeting_params_auto(name):
    return "Hello " + name


greeting_manual = add_mr(greeting)
title("greeting_manual('Roby')", greeting_manual('Roby'))
title("greeting_auto('Roby')", greeting_auto('Roby'))

greeting_params_manual = add_params("Ms.")(greeting)
title("greeting_params_manual('Roby')", greeting_params_manual('Roby'))
title("greeting_params_auto('Roby')", greeting_params_auto('Roby'))
