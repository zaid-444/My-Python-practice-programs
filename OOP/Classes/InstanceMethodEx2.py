# Program for Demonstrating Instance Method

class Student:
    def readvalues(self):
        self.sno = int(input("Enter Student Number: "))
        self.name = input("Enter Student Name: ")
        self.marks = float(input("Enter Student Marks: "))
        self.dispvalues() # One Instance of Current Class Calling another Instance Of Same Class by using "self"

    def dispvalues(self):
        print("-"*50)
        print("Student Number =",self.sno)
        print("Student Name   =",self.name)
        print("Student Marks  =",self.marks)


s1 = Student()
s2 = Student()

s1.readvalues()
print("-"*50)