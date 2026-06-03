from abc import ABC
class bus(ABC):
    def volvo(self):
        print("Luxury bus")
class lorry(bus):
    def volvo(self):
        print("huge")
class car(bus):
    def volvo(self):
        print("costly")
v=bus()
v.volvo()
l=lorry()
l.volvo()  
c=car()
c.volvo()


    