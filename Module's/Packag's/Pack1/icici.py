
bname = "ICICI"
addr = "HYDERABAD"

def simpleint():
    p = float(input("Enter how much amount u want: "))
    t = int(input("Enter Time: "))
    r = float(input("Enter rate of interest: "))
    si = (p * t * r)/100
    totamt = p + si
    print("*"*50)
    print("\tResult of Simple Interest")
    print("*"*50)
    print("\tAmount =",p)
    print("\tTime   =",t)
    print("\tRate   =",r)
    print("*"*50)
    print("\tSimple Interest =",si)
    print("\tTotal =",totamt)
    print("*"*50)