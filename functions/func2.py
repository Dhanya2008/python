#without parameter
def place():
    tour=input("Whwre do you want to go?")
    if tour=="Ooty":
        print("Don't go")
    elif tour=="Yercaud":
        print("Go with friends")
    elif tour=="Coorg":
        print("Go with family")
    else:
        print("Veetla iru")
place()












#with parameter
def prompt(qual,ref):
    if qual=="ug" and ref=="hr":
        print("You are in US based team")
    elif qual=="pg" and ref=="teamlead":
        print("Yu are in Russian based team")
    else:
        print("You are hired")
prompt("ug","hr")
prompt("pg","hr")
prompt(qual="pg",ref="teamlead")
