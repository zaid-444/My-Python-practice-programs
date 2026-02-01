# Define a Function for Addition of Two Numbers

# INPUT:   Taking from Function call
# PROCESS: Taken in Function Body
# OUTPUT:  Given to Function call

def addop(x, y):
    z = x + y
    return z

print("--------------------------------")
a = float(input("Enter Value of A: "))
b = float(input("Enter Value of B: "))
res = addop(a,b)
print("Sum of ({}+{})={}".format(a,b,res))
print("--------------------------------")

x = float(input("Enter Value of A: "))
y = float(input("Enter Value of B: "))
z = addop(x,y)
print("Sum of ({}+{})={}".format(x,y,z))
print("--------------------------------")
