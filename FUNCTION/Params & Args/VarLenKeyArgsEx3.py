#Program for Demonstrating the Need of Keyword Variable length Arguments

def computetotal(sno,sname,cls,**marks):
    print("="*50)
    print("Student Id    = {}".format(sno))
    print("Student Name  = {}".format(sname))
    print("Student Class = {}".format(cls))
    print("-"*50)
    if len(marks) != 0:
        print("\tSubject\t\tMarks")
        print("-"*50)
        tot = 0
        for sub,mark in marks.items():
            print("\t{}\t\t{}".format(sub,mark))
            tot += mark
        print('-'*50)
        print("Total Marks  = {}".format(tot))
    

computetotal(100,"Rohit","10th",Marathi=68,Hindi=74,English=59,Maths=65,Science=71,Social=78)
computetotal(101,"Virat","12th",Hindi=66,English=78,Chem=64,Physics=55,Maths=81)
computetotal(102,"Dhoni","B.Tech(CSE)",OS=70,DBMS=50)
computetotal(103,"Rossum","Scientist")
