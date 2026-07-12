class Vehicles:

    def __init__(self, vehicle_type):
        print("Vehicles is a :", vehicle_type)

class Car(Vehicles):

    def __init__(self):
        Vehicles.__init__("Car")

print(issubclass(Car, Vehicles))
