class supermarket:
    def biscuit(self, brand):
        self.b=brand
        print("The biscuit is available", self.b)
class amount:
    def price(self, cost):
        self.c=cost
        print("The price of the biscuit is", self.c)
class main(supermarket, amount):
    def offer(self, discount):
        self.d=discount
        print("The discount on the biscuit is", self.d)
        print("The final price of the biscuit is", self.c-self.d)
m=main()
m.biscuit("Britannia")
m.price(50)
m.offer(10)

        