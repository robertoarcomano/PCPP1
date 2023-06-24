import abc
from common import title


class Vehicle(abc.ABC):
    object_array = []

    def __init__(self, name):
        self.name = name
        Vehicle.add_object(name)
        self.year = 2000

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @year.deleter
    def year(self):
        self.__year = None

    @abc.abstractmethod
    def turn(self):
        return "I should do something..."

    @classmethod
    def add_object(cls, object_name):
        cls.object_array.append(object_name)

    @classmethod
    def get_object_array(cls):
        return cls.object_array

    @staticmethod
    def get_factorial(n):
        ret = 1
        for i in range(1, n + 1):
            ret *= i
        return ret


class Car(Vehicle):
    def turn(self):
        return "turn the wheels"


class Motorcycle(Vehicle):
    def turn(self):
        return "tilt the vehicle"


title("honda = Motorcycle('Honda')")
print()
title("astra = Car('Astra')")
print()
honda = Motorcycle('Honda')
astra = Car('Astra')
title("Polymorphism")
title("Car.__bases__", Car.__bases__[0].__name__)
title("astra.turn()", astra.turn())
title("honda.turn()", honda.turn())
title("getattr(honda, \"name\"):", getattr(honda, "name"))
title("setattr(my_object, \"name\", \"Honda Shadow\")")
setattr(honda, "name", "Honda Shadow")
title("getattr(my_object, \"name\"):", getattr(honda, "name"))
title("class method")
title("astra.get_object_array()", astra.get_object_array())
title("honda.get_object_array()", honda.get_object_array())

title("Dynamically typed")
print("1 + 2 =", (1 + 2))
print("'1' + '2' =", ('1' + '2'))
print()

title("Factorial")
title("astra.get_factorial(5)", astra.get_factorial(5))

astra.year = 2023
title("astra.year = 2023")
title("astra.year", astra.year)
del astra.year
title("delete astra.year")
title("astra.year", astra.year)
