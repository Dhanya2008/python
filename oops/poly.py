class cuckoo:
    def sound(self):
        print("kuku")
class crow(cuckoo):
    def sound(self):
        print("kaka")
class sparrow(cuckoo):
    def sound(self):
        print("chichi")
c=cuckoo()
c.sound()   
cr=crow()
cr.sound()
s=sparrow()
s.sound()