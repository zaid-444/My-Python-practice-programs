# Program for whether the thread is running or not

import threading,time

def display(lst):
    for val in lst:
        print("{}--->{}".format(threading.current_thread().name,val))
        time.sleep(1)



print("Program Started")
print("-"*50)

t1 = threading.Thread(target=display,args=([10,20,40,50,20],))
print("Is Sub thread running =",t1.is_alive())
t1.start()
print("-"*50)
print("Is Sub thread running =",t1.is_alive())
print(threading.active_count())

print("-"*50)

print("Is Sub thread running =",t1.is_alive())
print("\t\tProgram Ended")