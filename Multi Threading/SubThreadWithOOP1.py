# This Program makes us to understand how to develop thread based application by using OOP

import threading,time

class Zaid:
    def display(self,lst):
        for val in lst:
            print("{}--->{}".format(threading.current_thread().name,val))
            time.sleep(1)

print("Program Started")

t1 = threading.Thread(target=Zaid().display,args=([54,34,64,34,54,34],))
t1.start()
t1.join()

print("Program Finished")