# Program for Demonstrating Without using Destructor

class Employee:
    def __init__(self,eno,name):
        print("-"*50)
        self.eno = eno
        self.name = name
        print("Employee Number =",self.eno)
        print("Employee Name   =",self.name)
        print("-"*50)

eo1 = Employee(444,"Diazy")
eo2 = Employee(123,"Rossum")