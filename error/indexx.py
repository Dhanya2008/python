#no limit chance
from array import *
arr=array('i',[458,852,65,35,458,25,252,478])
def alpha(index,limit=0):
    try:     
        print(arr[index])
    except IndexError as ierror:
        print(ierror)  
        limit+=1
        if limit <= 2:
            alpha(int(input("Tell us index")),limit)
        else:
            return
        
alpha(int(input("Tell us the index")))      

