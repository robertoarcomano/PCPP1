class Vehicle:
    def turn(self):
        print("I should do something the turn...")


class Car(Vehicle):
    def turn(self):
        print("turn the wheels")


class Motorcycle(Vehicle):
    def turn(self):
        print("tilt the vehicle")


honda = Motorcycle()
astra = Car()
astra.turn()
honda.turn()
