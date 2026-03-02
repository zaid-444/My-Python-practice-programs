# Program for Demonstrating Writing the Data to the file

sno = 102
sname = "Virat"
marks = 36.20

with open("student.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written Successfully")