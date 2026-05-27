class banking:
    def initial(self,name,accno,balance):
        self.n=name
        self.a=accno
        self.b=balance
        print("Name:",self.n)
        print("Account number:",self.a)
        print("Your current balance is:",self.b)
class deposit(banking):
    def dep(self,amt):
        if amt>0:
            self.b+=amt
            print("Amount deposited:",amt)
            print("Your current balance is:",self.b)
        else:
            print("Invalid amount")
    def withdr(self,amt):
        if self.b>=amt:
            self.b-=amt
            print("Amount withdrawn:",amt)
            print("Your current balance is:",self.b)
        else:
            print("Insufficient balance")
b=deposit()
b.initial("Dhanya",12345,100000.0)
b.dep(50000.0)
b.withdr(20000.0)
        
    
            

        
        