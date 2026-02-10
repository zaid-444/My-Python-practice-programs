
def addop(a,b):
    c = a + b
    return c

sumop = lambda a,b : a+b

print("-"*50)
print("Type of addop =",type(addop))
x = addop(100,200)
print("Sum =",x)
print("-"*50)
print("Type of sumop =",type(sumop))
y=sumop(50,30)
print(y)