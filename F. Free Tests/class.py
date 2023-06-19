import abc
from common import title


class Vehicle(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def turn(self):
        return "I should do something the turn..."


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
title("astra.turn()", astra.turn())
title("honda.turn()", honda.turn())
title("getattr(honda, \"name\"):", getattr(honda, "name"))
title("setattr(my_object, \"name\", \"Honda Shadow\")")
setattr(honda, "name", "Honda Shadow")
title("getattr(my_object, \"name\"):", getattr(honda, "name"))
print()
