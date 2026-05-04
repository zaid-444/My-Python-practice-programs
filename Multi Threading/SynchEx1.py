# Program for Demonstrating Dead Lock Result Occurence

import threading,time

def table(n):
    L.acquire()
    if n <= 0:
        print("{}---{} Is invalid input".format(threading.current_thread().name,n))
    else:
        print("-"*40)
        print("Mul Table for:",n)
        print("-"*40)
        for i in range(1,11):
            print("\t{}\t{} x {} = {}".format(threading.current_thread().name,n,i,n*i))
            time.sleep(0.4)
        print("-"*40)
    L.release()

L = threading.Lock()
t1 = threading.Thread(target=table,args=(2,))
t1.name = "Zaid"
t2 = threading.Thread(target=table,args=(3,))
t2.name = "Raahi"
t3 = threading.Thread(target=table,args=(5,))
t3.name = "Shivi"
t4 = threading.Thread(target=table,args=(7,))
t4.name = "Saloni"

t1.start()
t2.start()
t3.start()
t4.start()