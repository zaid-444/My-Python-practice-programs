# Program for Demonstrating Instance Method

class Student:
    def readvalues(self):
        print("Current obj addr in method =",id(self))
        self.sno = int(input("Enter Student Number: "))
        self.name = input("Enter Student Name: ")
        self.marks = float(input("Enter Student Marks: "))
    def dispvalues(self):
        print("-"*50)
        print("Student Number =",self.sno)
        print("Student Name   =",self.name)
        print("Student Marks  =",self.marks)


s1 = Student()
s2 = Student()

print("Id of s1 in main program =",id(s1))
s1.readvalues()

print("-"*50)

print("Id of s2 in main program =",id(s2))
s2.readvalues()

print("-"*50)

print("First Student Details")
s1.dispvalues()

print("-"*50)

print("Second Student Details")
s2.dispvalues()