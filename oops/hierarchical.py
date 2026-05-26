#hierarchical inheritance
class Dress:
    def cotton(self):
        print("It is made of cotton")
class Shirt(Dress):
    def collar(self):
        print("It has collar")
class Pant(Dress):
    def length(self):
        print("It is full length")
s=Dress()
s.cotton()
s1=Shirt()
s1.collar()
s2=Pant()
s2.length()

