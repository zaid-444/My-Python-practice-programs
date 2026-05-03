# Write a thread based application which will generate 1 to n numbers where n is +VE

import threading,time

class Numbers:
    def __init__(self,n):
        self.n = n
    def gerater(self):
        if self.n <= 0:
            print("{}---->{} Is Invalide Input".format(threading.current_thread().name,self.n))
        else:
            print("---------------------------------")
            print("Numbers from 1 to {}".format(self.n))
            print("---------------------------------")
            for i in range(1,self.n+1):
                time.sleep(0.5)
                print("{}----Val = {}".format(threading.current_thread().name,i))
            else:
                print("---------------------------------")



threading.Thread(target=Numbers(int(input("Enter any number: "))).gerater).start()