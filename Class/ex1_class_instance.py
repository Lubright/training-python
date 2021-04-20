# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

class Car:
    accel = 3.0 # class variable
    mpg = 25

car1 = Car()
car2 = Car()

print("{} ; type: {}".format(car1, type(car1)))
print("{} ; type: {}".format(car2, type(car2)))
print("-" * 50 + "\n")

print("car1.accel = {}".format(car1.accel))
print("car2.accel = {}".format(car2.accel))
print("car1.mpg = {}".format(car1.mpg))
print("car2.mpg = {}".format(car2.mpg))
print("Car.accel = " + str(Car.accel))
print("-" * 50 + "\n")

print("id of car1.accel:", id(car1.accel))
print("id of Car.accel:", id(Car.accel))
print("change class variable...")
Car.accel = 5.0
print("car1.accel = {}".format(car1.accel)) # changed
print("car2.accel = {}".format(car2.accel)) # changed
print("-" * 50 + "\n")

# define instance variable
car1.accel = 10.0
print("car1.accel = {}".format(car1.accel))
print("car2.accel = {}".format(car2.accel))
print("-" * 50 + "\n")
