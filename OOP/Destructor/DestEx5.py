# Program for Demonstrating With Destructor

import time

class Employee:
    def __init__(self,eno,name):
        print("-"*50)
        self.eno = eno
        self.name = name
        print("Employee Number =",self.eno)
        print("Employee Name   =",self.name)
        print("-"*50)
    def __del__(self):
        print("GC Calls __del__() for Removing the Memory Space of Current Object")

eo1 = Employee(444,"Diazy")
eo2 = eo1
eo3 = eo2
print(id(eo1),id(eo2),id(eo3))
print("Program Finished")
time.sleep(3)