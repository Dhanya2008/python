# func with default aruguments
def register(name,height,location="Salem"):
    if height<="40 ft":
        print(name,"of height",height,"has been approved in",location)
    else :
        print(name,"of height",height,"has not been approved in",location)
register("DS Tech Park","40 ft","Chennai")
register("AD Automation","50 ft")