# write a python program which will display odd numbers separatly even number separatly by using multiple threads

import threading,time

def odd(n):
    if n <= 0:
        print(f'{n} is Invalide Input')
    else:
        for i in range(1,n+1):
            if i%2 != 0:
                print("{}---Odd no. {}".format(threading.current_thread().name,i))
                time.sleep(1)

def even(n):
    if n <= 0:
        print(f'{n} is Invalide Input')
    else:
        for i in range(1,n+1):
            if i%2 == 0:
                print("{}---Even no. {}".format(threading.current_thread().name,i))
                time.sleep(1)


t1 = threading.Thread(target=odd,args=(int(input("Enter a number to generate Odd number: ")),))

t2 = threading.Thread(target=even,args=(int(input("Enter a number to generate Even number: ")),))

t1.start()
t2.start()