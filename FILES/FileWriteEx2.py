sno = input("Enter Roll no.: ")
sname = input("Enter Name: ")
marks = float(input("Enter Marks: "))

with open("student.data","a") as fp:
    fp.write(sno+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("-"*40)
    print("Data Written Successfully")
    print("-"*40)