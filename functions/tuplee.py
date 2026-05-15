# name=("harry","ron","hermione","neville")
# print(name)
# print(type(name))

# #slicing
# print(name[0:3])
# print(name[ :2])
# print(name[2: ])

# #tuple method
# num=(10,12,14,16,18,20,12,12)
# numm=num.count(12)
# print(numm)
# inde=num.index(14)
# print(inde)


# #append
# college=('psg','kiot','kct','cit')
# collegee=list(college)
# collegee.append('iit')
# college=tuple(collegee)
# print(college)

# #insert
# colors=('blue','green','red','yellow')
# colorss=list(colors)
# colorss.insert(1,'grey')
# colors=tuple(colorss)
# print(colors)

#adding tuple to tuple
data=('Cat','Dog','dhanya')
data1=('aswathi',)
data+=data1
print(data)

# #loop tuple
a=('hi','hello','what')
for i in range(len(a)):
     print(a[i])
    
for i in a:
     print(a)
    
    
#adding
place=('kerala','telgana','salem')
place1=(1,2,3)
result=place+place1
print(result)

#join
place=('salem','madurai','chennai')
join=place*4
print(join)

