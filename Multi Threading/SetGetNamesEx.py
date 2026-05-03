# Program for How set name to the Thread and how to get the name of the thread

import threading

def welcome(name):
    print("{}---->Hi {}, Good Morning".format(threading.current_thread().name,name))

print("Program Started: ",threading.current_thread().name)

t1 = threading.Thread(target=welcome,args=("Sunny",))
t1.setName("Zaid") # setName is Deprecated
t1.start()
print("Name of Sub Thread =",t1.name) # getName Deprecated

print("Program Ended: ",threading.current_thread().name)