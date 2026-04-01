# Program for Demonstrating With Destructor

import sys
import time

class Employee:
    def __init__(self,eno,name):
        print("-"*50)
        self.eno = eno
        self.name = name
        print("Current Object ID =",id(self))
        print("Employee Number =",self.eno)
        print("Employee Name   =",self.name)
        print("-"*50)
    def __del__(self):
        print("-"*70)
        global memspace
        print("GC Calls __del__() for Removing the Memory Space of Current Object")
        print("\tCurrent Object Removed:",id(self))
        memspace = memspace-sys.getsizeof(self)
        print("\tNow Vailable Memory Space =",memspace)

eo1 = Employee(444,"Diazy")
eo2 = Employee(123,"Rossum")
eo3 = Employee(101,"Rohit")
# Calculate Memory Space
memspace = sys.getsizeof(eo1) + sys.getsizeof(eo2) + sys.getsizeof(eo3)
print("Total Memory Sapce =",memspace)
time.sleep(5)