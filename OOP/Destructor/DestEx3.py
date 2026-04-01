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
print("No Longer Interested to maintain to the object eo1")
eo1 = None
eo2 = Employee(102,"Ramesh")
print("No Longer Interested to maintain to the object eo2")
eo2 = None
eo3 = Employee(103,"Suresh")
time.sleep(5)