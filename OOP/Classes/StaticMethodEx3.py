class Student:
    def getstuddet(self):
        self.sno = int(input("Enter Student Number: "))
        self.sname = input("Enter Student Name: ")
        self.marks = float(input("Enter Student Marks: "))
    def disstud(self):pass

class Employee:
    def getempdet(self):
        self.eno = int(input("\nEnter Employee Number: "))
        self.ename = input("Enter Employee Name: ")

class Teacher:
    def getteacherdet(self):
        self.tno = int(input("\nEnter Teacher Number: "))
        self.tname = input("Enter Teacher Name: ")
        self.expr = float(input("Enter Teacher EXP: "))
        self.sub = input("Enter Teacher Subject: ")

class Xyz:
    @staticmethod
    def disobjdata(obj,x):
        print("="*50)
        print("{} Information".format(x))
        for k,v in obj.__dict__.items():
            print("\t{}--->{}".format(k,v))


s = Student()
e = Employee()
t = Teacher()

s.getstuddet()
e.getempdet()
t.getteacherdet()



# Name Less Object
Xyz().disobjdata(s,"Student")
Xyz().disobjdata(e,"Employee")
Xyz().disobjdata(t,"Teacher")