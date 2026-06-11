# a=100
# b=0
# c=a/b
# print(c)


# error handling - giving another chance to the program to run
# try block-declaring the code which may cause an error
# except block- handling the error

# try:
#     a=100
#     b=0
#     c=a/b
#     print(c)
# except Exception as e:
#     print(e)
#     print("Please provide a non zero value for b")
    

# #name error
# name=456
# print(name)
# try:
#     Name=1452
#     print(Name)
# except NameError as e:
#     print("Name error",e)
    
# try:
#     name=input("Enter the name ")
#     print(namee)
# except NameError as e:
#     print(e)
#     name=input("Please enter the name again ")
#     print(name)
#     print("Variable name is not defined")

#value error
# try:
#     num=int(input("Enter a number "))
#     print(num)
# except ValueError as e:
#     print(e)
#     print("Dhanya")


#type error
# try:
#     data="150"+6
#     print(data)
# except TypeError as e:
#     print(e)
#     print("kumar"+"raja")


#index error
# try:
#     li=[1,2,3,4,5]
#     print(li[10])
# except IndexError as e:
#     print(e)
#     print("Value is not available in the list")
#     print(li[3])


#key error
# try:
#     alpha={"Name":"Dhanya","Age":17}
#     print(alpha["Name1"])
# except KeyError as e:
#     print("Key  error",e)
#     print(alpha["Name"])
    

# try:
#     listt=["Apple","Banana","Mango"]
#     listt.append("Grapes")
#     listt.append("Watermelon")
#     listt.insert(2,"Orange")
#     listt.remove("Banana")
#     print(listt)
#     print(listt[8])
# except IndexError as e:
#     print(e)
#     listt.append("Pineapple")
#     print("Updated list")
#     print(listt)
#     listt.pop(1)
#     print("New list")
#     print(listt)
    
    
#index error: list,tuple,array,str
# lst=[18,"Dhanya",23,43,45]
# tup=(43,44,3,11,"Shri")
# from array import *
# arr=array('f',[1,2,3,5,4,7,6,5,53,3])
# s="Viratkohli"
# print(lst[0],tup[3],arr[2],s[4])
# try:
#     index=int(input("Enter the index position: "))
#     print(lst[index],tup[index],arr[index],s[index])
# except IndexError as ierror:
#     print(ierror)
#     print("Index within",len(s))
#     index=int(input("Enter the index position: "))
#     print(lst[index],tup[index],arr[index],s[index])
# finally:
#     print("Program executed successfully")    





