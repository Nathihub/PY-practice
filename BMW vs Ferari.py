class BMW:

    def __init__(self, color, model):
        self.color = color
        self.model = model

class Ferari:

    def __init__(self, color, model):
        self.color = color
        self.model = model

bmw = BMW("blue", "X5")
ferari = Ferari("red", "SF90")

for car in (bmw, ferari):
    print("My color is:", car.color)
    print("My model is:", car.model)