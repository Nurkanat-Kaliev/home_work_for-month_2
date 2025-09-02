class Car:

    def __init__(self,color,model):
        self.color = color
        self.model = model

    def driving_at(self,speed):
        print(f"{self.model} is driving at speed {speed}")
car_honda = Car("silver","honda")
print(car_honda.color)

car_bmw = Car("black","bmw")
car_bmw.driving_at(67)
car_bmw.color = "white"
print(car_bmw.color,car_bmw.model)