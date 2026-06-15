from pickle import *
name=open("Shri.txt",'wb')
cartoon=['Bheem','Dholu','Bholu','Indhumathi']
college={"Name":"IIT","Dept":"BTech"}
location=("Bangalore","Salem")

dump(cartoon,name)
dump(college,name)
dump(location,name)
name.close()



