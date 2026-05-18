def pinkbus():
    print("PINK BUS welcomes you...")
    name=input("Enter your name: ")
    print("Name: ",name)
    def typee(bustype,seattype,window =500000,other =300000,firstt =1000000,economy =800000):
        if bustype=="first class":
            if seattype=="window seat":
                print("You have booked first class bus with window seat")
                print("Your total amount is: ",firstt+window)
            else:
                seattype=="other"
                print("You have booked first class bus with other seat")
                print("Your total amount is: ",firstt+other)
        elif bustype=="economy":
            if seattype=="window seat":
                print("You have booked economy with window seat")
                print("Your total amount is: ",economy+window)
            else:
                seattype=="other"
                print("You have booked economy with other seat")
                print("Your total amount is: ",economy+other)
        else:
            print("Invalid!!")
            print("Your ticket is not booked")
    typee("first class","window seat")
    typee("economy","other")
pinkbus()
            
                
                
        
