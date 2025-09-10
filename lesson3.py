# Магические, статичные, классовые методы в классах, множественное наследование
class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model
        self.__fined = False

    def drive_to_location(self,location):
        print(f"Car {self.model} os driving to {location} {self.__fined}")

    def _test_car(self):
        print(f"test car {self.model}")

car_honda = Car("black","Honda")
print(car_honda._Car__fined)
car_honda._test_car()
