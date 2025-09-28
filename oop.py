# first task

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def set_age(self,age):
        self.__age = age
        if self.__age < 0:
            print("Error, u are not allowed to set age under 0")
        else:
            print(self.name,self.__age)

    def get_age(self):
        return self.__age

p = Person("Alex",34)
p.set_age(23)
print(p.get_age())
p.set_age(-5)


# second task

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("I'm an animal")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())
print(cat.name, cat.speak())

# third task

class Vehicle:

    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):

    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):

    def move(self):
        return "Bike is pedaling"

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))


# fourth task

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(circle.area())
