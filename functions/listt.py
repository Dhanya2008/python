#list
bio=["Dhanya",17,"f",5.0]
print("list",bio)
print(type(bio))

#Adding the list new elements
#append
bio.append("Software Developer")
print(bio)
print(len(bio))

#Adding elements using insert method
bio.insert(3,565)
print(bio)

#replace
bio[5]="Teamlead"
print(bio)

salary=[40000,60000,80000,70000]
print(max(salary))
print(min(salary))
print(sum(salary))

salary.remove(60000)
print(salary)

salary.pop()
print(salary)

salary.pop(1)
print(salary)

bio.reverse()
print(bio)

#list method
#copy
hi=[23,45,66,78,23]
copy=hi.copy()
print(copy)
#count
count=hi.count(23)
print(count)


#runtime list
li=input("Enter the list values")
list=li.split(",")
print("list values")
for i in list:
    print(i)
    
    
n=int(input("Enter the list values"))
empty_list=[]
for i in range(n):
    livalue=input("Enter list values")
    empty_list.append(livalue)
print("List data",empty_list)