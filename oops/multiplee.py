class Travels:
    def busname(self):
        print("ABC Travels")
class Travels1:
    def bustype(self):
        print("AC Sleeper")
class main(Travels,Travels1):
    def price(self):
        print("Price is 1000")
m=main()
m.busname()
m.bustype()
m.price()
        