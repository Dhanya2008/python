dhanya=open("./bio.doc",'a')
print("File created",dhanya.name)
dhanya.write("Dhanya is a good girl")
print(dhanya.writable())
print(dhanya.readable())
print(dhanya.mode)
dhanya.write("My hobby is listening to music")
print("Append successfully")
dhanya.close