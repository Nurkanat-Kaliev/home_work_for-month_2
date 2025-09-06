class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Car: {self.brand} {self.model} {self.year}")

    def age_year(self,current_year):
        print(f"Car's age {current_year-self.year}")

class ElectricCar(Car):
    def __init__(self,brand, model, year, battery_capacity):
        super().__init__(brand,model,year)
        self.battery_capacity = battery_capacity

car_1 = Car("Mercedes","Benz","2018")
car_2 = ElectricCar("Tesla",3,2022,78)

car_2.info()
car_1.info()