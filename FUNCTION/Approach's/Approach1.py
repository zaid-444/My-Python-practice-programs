# Define a Function for Addition of Two Numbers

def addop(a,b):
    print("Inside Function Definitaion")
    c = a + b
    return c

print("From Main Program")
print("Type of Function = {}".format(type(addop)))
res = addop(10,20)
print(res)

print("-----------------------------")

c = addop(100,200)
print(c)