# Program for Demonstrating Variable Length Arguments (OR) Parameters

def dispvals(sno,sname,*a,city="PUNE"):

    print("-"*50)
    print("SNO  :",sno)
    print("NAME :",sname)
    print("CITY :",city)
    s = 0
    for v in a:
        s += v
        print(v,end=" ")
    print()
    print("SUM  :",s)

dispvals(100,"RS",10,20,30,40,50)
dispvals(200,"MP",10,20,30,40)
dispvals(300,"CM",10,20,30)
dispvals(400,"SK",10,20)
dispvals(500,"ML",10)
dispvals(600,"TS")
dispvals(700,"LT",1.1,2.2,3.3,4.4,city="HYD")