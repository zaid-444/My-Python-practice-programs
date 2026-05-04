import threading,time

def reservation(nos):
    L.acquire()
    global ts
    if nos > ts:
        print("Hi {}, {} Seats are not Available--try next time".format(threading.current_thread().name,nos))
        print("-"*50)
        time.sleep(2)
    else:
        ts = ts-nos
        print("Hi {}, {} Seats are Reserved--Happy Journey".format(threading.current_thread().name,nos))
        print("Now Available Seats",format(ts))
        print("-"*50)
        time.sleep(2)
        if ts == 0:
            print("\tTrain is Full")
            print("-"*50)
    L.release()


L = threading.Lock()
ts = 10 # Total Seats

t1 = threading.Thread(target=reservation,args=(1,))
t1.name = "Naresh"

t2 = threading.Thread(target=reservation,args=(2,))
t2.name = "Zaid"

t3 = threading.Thread(target=reservation,args=(8,))
t3.name = "Rohit"

t4 = threading.Thread(target=reservation,args=(3,))
t4.name = "Virat"

t5 = threading.Thread(target=reservation,args=(4,))
t5.name = "Jyoti"

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()