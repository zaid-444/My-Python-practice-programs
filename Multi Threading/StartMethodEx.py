# Program for Understanding How to create sub threads

import threading

def welcome(name):
    print("{}---->Hi {}, Good Morning".format(threading.current_thread().name,name))

print("Program Started: ",threading.current_thread().name)


t1 = threading.Thread(target=welcome,args=(input("Enter Your Name: "),))
t1.start()

print("Program Ended: ",threading.current_thread().name)