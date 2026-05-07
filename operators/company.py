hire=5
while hire>0:
    skills=input("Enter you skills: ")
    projects=int(input("Enter the no of projects: "))
    if (skills=="python" or skills=="java") and (projects>5 and projects<10):
        print ("You are hired")
        hire-=1
    else:
        print("Thank You")
     
    