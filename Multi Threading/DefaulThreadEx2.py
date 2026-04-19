# Program for Demonstrating MainThread Execute all the functions One by One-->Sequential Execution

import threading

def f1():
    print("{} f1 to Multi Threading Concept".format(threading.current_thread().name))

def f2():
    print("{} f2 Good Evening".format(threading.current_thread().name))

def f3():
    print("{} f3 Function Finished".format(threading.current_thread().name))

f1()
f2()
f3()