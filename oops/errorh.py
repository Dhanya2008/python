# a=100
# b=0
# c=a/b
# print(c)


# error handling - giving another chance to the program to run
# try block-declaring the code which may cause an error
# except block- handling the error

try:
    a=100
    b=0
    c=a/b
    print(c)
except Exception as e:
    print(e)
    print("Please provide a non zero value for b")
    

#name error
name=456
print(name)
try:
    Name=1452
    print(Name)
except NameError as e:
    print("Name error",e)
    
try:
    name=input("Enter the name ")
    print(namee)
except NameError as e:
    print(e)
    name=input("Please enter the name again ")
    print(name)
    print("Variable name is not defined")


