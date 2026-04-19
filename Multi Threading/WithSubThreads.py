# Program for Computing Squares and cubes of list of numbers by Multiple Sub Threads

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
print("Program Started {}".format(threading.current_thread().name))
lst = [2,3,4,5,-4,2,44,0]

# Creating First Sub Thread for Executing Squares
t1 = threading.Thread(target=squares,args=(lst,)) # t1 is Thread Object Whose name--> Thread-1

# Creating Second Sub Thread for Executing Cubes
t2 = threading.Thread(target=cubes,args=(lst,)) # t2 is Thread Object Whose name--> Thread-2

# Dispatch the sub threads to the target functions by using start() of Thread class Object
t1.start()
t2.start()
t1.join()
t2.join()

print("Program Finished {}".format(threading.current_thread().name))
et = time.time()

print("Total Time Taken =",et-bt)
