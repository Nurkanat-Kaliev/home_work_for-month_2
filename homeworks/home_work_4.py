class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print(f"Car starting")

class ElectricCar:
    def start(self):
        super().start()

class Tesla(ElectricCar,Car):
    def start(self):
        super().start()
        print("Tesla ready")

car = Tesla()
car.start()
