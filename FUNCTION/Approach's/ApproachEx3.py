# Define a Function for Addition of Two Numbers

# INPUT:   Taking from Function call
# PROCESS: Taken Place in Function Body
# OUTPUT:  Display Inside of function body

def addop(a,b):
    c = a + b
    print("Sum({},{})={}".format(a,b,c))


a = float(input("Enter Value of A: "))
b = float(input("Enter Value of B: "))

addop(a,b)