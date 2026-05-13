name=("harry","ron","hermione","neville")
print(name)
print(type(name))

#slicing
print(name[0:3])
print(name[ :2])
print(name[2: ])

#tuple method
num=(10,12,14,16,18,20,12,12)
numm=num.count(12)
print(numm)
inde=num.index(14)
print(inde)


#append
college=('psg','kiot','kct','cit')
collegee=list(college)
collegee.append('iit')
college=tuple(collegee)
print(college)

#insert
colors=('blue','green','red','yellow')
colorss=list(colors)
colorss.insert(1,'grey')
colors=tuple(colorss)
print(colors)