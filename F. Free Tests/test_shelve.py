from common import title
import shelve


class MyClass:
    def __init__(self, name):
        self.name = name


my_obj = MyClass("my_obj")

my_shelve = shelve.open("my_shelve.data", "n")
my_shelve['my_obj'] = my_obj
my_shelve.close()

del my_shelve
my_shelve = shelve.open("my_shelve.data", "r")
title("my_shelve['my_obj']", my_shelve['my_obj'].__dict__)
