class Vehicles:

    def __init__(self, name, color):
        self.name = name
        self.color = color

class Car(Vehicles):

    def __init__(self, name, color):
        Vehicles.__init__(self, name, color)

    def display(self):
        print("Car Name:", self.name)
        print("Car Color:", self.color)

print(issubclass(Car, Vehicles))
Vehicle2 = Car("BMW", "Black")
Vehicle2.display()



