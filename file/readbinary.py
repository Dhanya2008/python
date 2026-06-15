from pickle import *
name=open("Shri.txt",'rb')

content=load(name)
print(content)
content1=load(name)
print(content1)
content2=load(name)
print(content2)