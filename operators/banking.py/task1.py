print("HDFC BANK")
acc_no=input("Enter your account no: ")
password=input("Enter your password: ")
if acc_no=="123hdfc" and password=="5678b":
    print("Your account is verified")
    current_amt=int(input("Enter your initial amount: "))
    withdraw_amt=int(input("Enter the amt you need to withdraw: "))
    print("The amount you have withdrawn: ",withdraw_amt)
    remaining_balance=current_amt-withdraw_amt
    print("The remaining amt after withdrawal: ",remaining_balance)
    deposit_amt=int(input("Enter the amt to be deposited: "))
    print("The amount you have deposited: ",deposit_amt)
    final_balance=remaining_balance+deposit_amt
    print("The final balance in your account: ",final_balance)
else:
    print("The account is not available")
    