import abc
from common import title


class Vehicle(abc.ABC):
    object_array = []

    def __init__(self, name):
        self.name = name
        Vehicle.add_object(name)

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
