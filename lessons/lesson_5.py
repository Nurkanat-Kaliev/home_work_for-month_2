# 1)декоратор @staticmethod
# Декоратор используется для того чтобы определить метод который не зависит от экземпляра класса
# (не использует селф) и не зависит от самого класса (не использует cls)
# Такой метод можно вызвать без содания экземпляра класса

# class Math:
#     def __init__(self,name):
#         self.name = name
#
#     def get_name(self):
#         print(self.name)
#
#     @staticmethod
#     def add(a,b):
#         print(a+b)
#
# obj_1 = Math("Johny")
# obj_1.get_name()
# Math.add(1,9)
#
# # 2)@classmethod Декоратор
# # декоратор classmethod используется для опр-ия метода который принимает первым аргументом
# # сам класс (не экземпляр). Этот аргумент обычно назыв-ся cls. Метод класса может изменять состояние класса,
# # но не работает с состоянием конкретного экз-пляра
# class Person:
#     # Class's attributes
#     population = 0
#     math = Math
#     def __init__(self,name):
#         # instances's attributes | class's objects
#         self.name = name
#         Person.population += 1
#
#     def get_name(self):
#         print("test")
#
#     @classmethod
#     def get_population(cls):
#         cls.math("poo")
#         return print(cls.population)
#
# obj_2 = Person("Lion")
# Person.get_population()

# def simple(func):
#     def wrapper():
#         print("Before being done")
#         func()
#         print("After being done")
#
#     return wrapper
#
# @simple
# def say_hello():
#     print("Hello world")
#
# # say_hello()
#
# # @greeting_decorator(func):
# def greeting(func):
#     def wrapper(name):
#         print(f"Hello {name}")
#         func(name)
#     return wrapper
#
# @greeting
# def greeting(name):
#     print(f"how are u {name}")
#
# greeting("Aouar")
#
#
# def repeat_dec(n):
#     def dec(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return dec
#
# @repeat_dec(5)
# def hello():
#     print("Hello")
#
# hello()


