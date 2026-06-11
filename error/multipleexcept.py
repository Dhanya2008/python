petrol=(120,150,220,450,250,650,892,45,1450,450,652,980,786)
try:
    litre=int(input("Tell us litre filled"))
    index=int(input("Select position to find Milage "))
    print("Selected distance is",petrol[index])
    print(petrol[index]/litre)
except ValueError as Verror:
    print(Verror)
    print("Data are whole Numeric value")
    litre=int(input("Tell us litre filled"))
    index=int(input("Select position to find Milage "))
    print("Selected distance is",petrol[index])
    print(petrol[index]/litre)
except IndexError as ierror:
    print(ierror)
    print("Index should within",len(petrol))
    index=int(input("Select Position inorder to find ,milage"))
    print("selected distance",petrol[index])
    print(petrol[index]/litre) 
except ZeroDivisionError as Zerror:
    print(Zerror)
    print("Litre not to be zero")
    litre=int(input("tell us litre Filled"))
    print("selected distance",petrol[index])
    print(petrol[index]/litre)
except Exception as e:
    print(e)    
