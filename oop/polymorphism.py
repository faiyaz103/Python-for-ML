class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Drive!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car=Car("Audi","V8")
boat=Boat("Yatch","Y78")
plane=Plane("Boeing","787")

for x in (car,boat,plane):
    print(x.brand)
    print(x.model)
    x.move()