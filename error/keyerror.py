#key error
try:
    bioo={"Name":"Tara","Age":20,"Degree":"BE","Gender":"Female"}
    print(bioo["Name"])
    print(bioo)
    bioo["Age"]=22
    bioo.update({"Degree":"BTech"})
    print(bioo)
    bio=bioo.copy()
    print(bio)
    bioo.update({"Place":"Salem"})
    print(bioo)
    a=bioo.get("Age")
    print(a)
except KeyError as e:
    print(e)
    print("The Key, Namee is not present in the dictionary")
    bioo.pop("Age")
    print(bioo)
    for i in bioo:
        print(bioo[i])
        
        
        
        
        
bio={"name":['Annamalai','Gowthami','Priya','Sathish'],
     "skills":['html','Django','Flask'],
     "poc":[5,4,8,9,1],
     "salary":[5.5,10.5,6.5,8.5,9.5],
     "Company":'TCS'
     }
print(bio['name'][3])
try:
    details=input("tell us what you want")
    print(bio[details])
except KeyError as kerror:
    print(kerror)
    print("column/crdential",details,"not found") 
    
    details=input("tell us what you want")
    print(bio[details])
finally:
    print("Valid data")   
    
    