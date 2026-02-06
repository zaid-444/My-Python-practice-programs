# Program for Demonstrating Keword Variable Length Arguments

def disp(**z):
    print("Number of Values {}".format(len(z)))
    print("-"*50)
    for k,v in z.items():
        print("\t{}-->{}".format(k,v))
    print("-"*50)

disp(sno=101,sname="Zaid",marks=82.22)
disp(eno=1,ename="Naresh",sal=30000,role="Clerk")
disp(tno=1000,tname="Gupta",subject="Python",exp=22,city="HYD") 