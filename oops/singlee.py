#single inheritance
class Car:
    def steering(self):
       print("Comfortable to ride")
class Bike(Car):
    def Gear(self):
        print("six speed gear box")
b=Bike()
b.steering()
b.Gear()
