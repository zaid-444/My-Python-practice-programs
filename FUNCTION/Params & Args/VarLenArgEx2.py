# Program for Demonstrating Variable Length Arguments (OR) Parameters

def dispvals(sno,sname,*a):

    print("-"*50)
    print("SNO  :",sno)
    print("NAME :",sname)
    s = 0
    for v in a:
        s += v
        print(v,end=" ")
    print()
    print("SUM  :",s)

dispvals(100,"RS",10,20,30,40,50) # Function Call-1 with 5 Pos Args
dispvals(200,"MP",10,20,30,40) # Function Call-2 with 4 Pos Args
dispvals(300,"CM",10,20,30) # Function Call-3 with 3 Pos Args
dispvals(400,"SK",10,20) # Function Call-4 with 2 Pos Args
dispvals(500,"ML",10) # Function Call-5 with 1 Pos Args
dispvals(600,"TS") # Function Call-6 with 0 Pos Args