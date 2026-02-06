# Program for Demonstrating global keyword

def incr():
    global a
    a = a+1

def update():
    global a
    a = a*2

a = 10
print("Val of a in Main Progrma before Incr()={}".format(a))
incr()
print("Val of a in Main Program after incr()={}".format(a))
print("-"*50)
update()
print("Val of a in Main Program after update()={}".format(a))