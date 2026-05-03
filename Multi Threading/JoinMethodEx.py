# This Program makes us to understand how to join sub threads

import threading,time

def display(lst):
    for val in lst:
        print("{}--->{}".format(threading.current_thread().name,val))
        time.sleep(1)



print("Program Started")
print("-"*50)

t1 = threading.Thread(target=display,args=([10,20,40,50,20],))
print("Is Sub thread running =",t1.is_alive())
print("-"*50)
t1.start()
print("Is Sub thread running =",t1.is_alive())
print("Number of Thread Active: ",threading.active_count())
t1.join()
print("-"*50)

print("Number of Thread Active: ",threading.active_count())
print("Is Sub thread running =",t1.is_alive())
print("\t\tProgram Ended")