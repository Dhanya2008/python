price=float(input("Enter product price :"))
quantity=float(input("Enter the quantity :"))
total=price*quantity
tax=total*0.10
final=total+tax
print("Final Amt ",final)