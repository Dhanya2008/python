class Animal:
    def white(self,fluffy):
        self.fluffy=fluffy
        print("polar bear is", fluffy)
class forest(Animal):
    def white(self,fluffy):
        self.fluffy=fluffy
        print("Panda is", fluffy)
class zoo(Animal):
    def white(self,fluffy):
        self.fluffy=fluffy
        print("Koala is", fluffy)
a=Animal()
a.white("soft")
f=forest()
f.white("soft")
z=zoo()     
z.white("soft")



class Dhanya:
    def name(self):
        print("My name is Dhanya")
class Asmitha(Dhanya):
    def name(self):
        super().name()
        print("My name is Asmitha")
class Aishu(Asmitha):
    def name(self):
        super().name()
        print("My name is Aishu")
a=Aishu()
a.name()