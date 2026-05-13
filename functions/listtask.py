n=int(input("Enter the list values"))
empty_list=[]
for i in range(n):
    livalue=input("Enter list values")
    empty_list.append(livalue)
print("List data",empty_list)
index=(int(input("Enter the index position: ")))
include=(int(input("Enter the new value: ")))
empty_list.insert(index,include)
print(empty_list)


listt=[1,2,3,4,5]
add=int(input("Enter the value to be added: "))
index=int(input("Enter the index position: "))
listt.insert(index,add)
print(listt)