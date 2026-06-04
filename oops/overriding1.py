class Payment:
    def pay(self,amount):
        print(f"Paying,{amount}")
class creditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount} credit card") 
class Upi(Payment):
    def pay(self,amount):
        print(f"Paid {amount} UPI MODE")
Payment=[creditCard(),Upi()]

for a in Payment:
    a.pay(5000)