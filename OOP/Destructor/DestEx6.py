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

eo1 = Employee(101,"Naresh")
eo2 = eo1
eo3 = eo2

print("No Longer Interested to maintain to the object eo1")
time.sleep(3)
del eo1

print("No Longer Interested to maintain to the object eo2")
time.sleep(3)
del eo2

print("No Longer Interested to maintain to the object eo3")
time.sleep(3)
del eo3

print("Program Finished")