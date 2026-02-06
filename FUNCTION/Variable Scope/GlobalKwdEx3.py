# Program for Demonstrating global keyword

def modify1():
    global a, b
    a = a + 1
    b = b + 1

def getvals():
    c = a * 2
    d = b * 3
    print("Inside of getvals()--> c={} d={}".format(c,d))

a, b = 10, 20
print("In main program before modify1()--> a={} b={}".format(a,b))
modify1()
print("In main program after modify1()--> a={} b={}".format(a,b))
getvals()
print("In main prog after getvals()--> a={} b={}".format(a,b))