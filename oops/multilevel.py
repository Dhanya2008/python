#multilevel inheritance
class Car:
    def wheel(self):
        print("Allow Wheels")
class Benz(Car):
    def luxury(self):
        print("It is costlier")
class BYD(Benz):
    def comfort(self):
        print("It is comfortable")
b=BYD()
b.wheel()
b.luxury()
b.comfort()