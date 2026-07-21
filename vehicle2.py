class vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        name = "BMW"
        model = "X5"


    def display(self):
        print("Vehicle Name:", self.name)
        print("Vehicle Model:", self.model)

Vehicle1 = vehicle("BMW", "X5")
Vehicle1.display()


