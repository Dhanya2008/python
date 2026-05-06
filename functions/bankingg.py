balance=[10000,1000,500,2000]
def debit(money=0,pos=0):
    if money<=balance[pos]:
        balance[pos]-=money
        print(money,"Withdraw")
        return balance[pos]
    else:print("Cannot be debited")
bank=debit(50000,0)
print(bank,"Remaining Balance")
