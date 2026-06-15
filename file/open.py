#create file

bio=open("./Dhanya.txt","w")
print("File is created",bio.name)
bio.write("All is Well")
bio.close