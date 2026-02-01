# Define a Function for Addition of Two Numbers

# INPUT:   Taking inside of Function body
# PROCESS: Taken Place in Function Body
# OUTPUT:  Given to Function Call

def addop():
    a = int(input("Enter First Value: "))
    b = int(input("Enter Second Value: "))
    res = a + b
    return a,b,res # return stmt can return one or More Number of Values


x,y,z = addop() # Function call with Multiline Assigment
print("Sum ({},{})={}".format(x,y,z))

print("---------------OR-----------------")

res = addop()
print(res,type(res))

# Define a function for Cal area and perimeter of Square sarea = side x side speri = 4 x side