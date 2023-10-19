"""
Polymorphism. Create several classes that demonstrate the polymorphism. Add the code execution samples to see why is it useful.
Any examples are up to you.
"""


class Vehicle:
    def __init__(self, speed=0):
        self.speed = speed

    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("The car is driving at {} km/h.".format(self.speed))


class Airplane(Vehicle):
    def move(self):
        print("The airplane is flying at {} km/h.".format(self.speed))


class Boat(Vehicle):
    def move(self):
        print("The boat is sailing at {} km/h.".format(self.speed))


# List of vehicles
vehicles = [Car(100), Airplane(500), Boat(20)]

# Move all vehicles
for vehicle in vehicles:
    vehicle.move()
