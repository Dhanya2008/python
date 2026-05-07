seat=1
while seat<=15:
    amount=int(input("Enter the amount "))
    if amount>=200:
        print("Seat Booked @",seat)
        seat+=1
    else:
        print("Unable to book seat")