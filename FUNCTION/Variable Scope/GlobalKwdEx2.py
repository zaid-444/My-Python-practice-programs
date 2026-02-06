# Program for Demonstrating global keyword

def modify1():
    global a, b
    a = a + 1
    b = b + 1

def modify2():
    global a, b
    a = a * 2
    b = b * 3

a, b = 10, 20
print("In main program before modify1()--> a={} b={}".format(a,b))
modify1()
print("In main program after modify1()--> a={} b={}".format(a,b))
modify2()
print("In main program after modify2()--> a={} b={}".format(a,b))