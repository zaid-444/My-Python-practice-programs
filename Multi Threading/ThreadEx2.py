# Write a thread based application which will generate 1 to n numbers where n is +VE

import threading,time

class Numbers:
    def gerater(self,n):
        if n <= 0:
            print("{}---->{} Is Invalide Input".format(threading.current_thread().name,n))
        else:
            print("---------------------------------")
            print("Numbers from 1 to {}".format(n))
            print("---------------------------------")
            for i in range(1,n+1):
                print("{}----Val = {}".format(threading.current_thread().name,i))
                time.sleep(1)
            else:
                print("---------------------------------")

t1 = threading.Thread(target=Numbers().gerater,args=(int(input("Enter how many numbers u want: ")),))
t1.start()