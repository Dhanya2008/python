class college:
    def __init__(self,name,course):
        self.n=name
        self.c=course
    def display(self):
            print(self.n,self.c)
c=college("IIT","BE CSE")
c.display()
