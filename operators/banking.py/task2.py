def bank():
    print("Welcome to HDFC atm")
    ac=int(input("Enter yur account number: "))
    pin=input("Enter your pin: ")
    print("Username: Dhanya shri")
    print("Account no: ",ac)
bank()
def withd(initial,withdraw):
    rem=initial-withdraw
    if initial>withdraw:
        print("The initial amount in your account: ",initial)
        print("The amount you have withdrawn: ",withdraw)
        print("The remaining amount",rem)
    else:
        print("Unable to withdraw the amount")

    def deposit(depo,rem):
        amt=input("Do you want to deposit the amount: ")
        if amt=="yes":
            if depo==0:
                print("You cannot deposit the amount")
            else:
                print("The amount to be deposited:",depo)
                print("The final amount is: ",rem+depo)
        else:
            print("The remaining amount: ",rem)
    deposit(2000,7000)
withd(10000,3000)
print("Thank you")