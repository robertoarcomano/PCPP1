from common import title
import time


def add_mr(func):
    def wrapper(name):
        start = time.perf_counter()
        s = "before\n"
        s += "   " + func("Mr." + name)
        time.sleep(0.1)
        s += "\nafter\n"
        stop = time.perf_counter()
        s += "\n"
        s += str(stop - start) + " seconds"
        return s

    return wrapper


def greeting1(name):
    return "Hello " + name


@add_mr
def greeting2(name):
    return "Hello " + name


greeting1_d = add_mr(greeting1)
title("greeting1_d('Roby')", greeting1_d('Roby'))

title("greeting2('Roby')", greeting2('Roby'))
