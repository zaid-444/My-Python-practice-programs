# Program for Computing Squares and cubes of list of numbers by single default thread

from DefaulThreadEx1 import threading
import time

def squares(lst):
    for val in lst:
        print("{}-->Square({}) = {}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)

def cubes(lst):
    for val in lst:
        print("{}-->Cube({}) = {}".format(threading.current_thread().name,val,val**3))
        time.sleep(1)

bt = time.time()
print("Program Started")
lst = [2,3,4,5,-4,2,44,0]
squares(lst)
print("-"*30)
cubes(lst)
print("-"*30)
print("Program finished")
et = time.time()

print("Total Time Taken =",et-bt)