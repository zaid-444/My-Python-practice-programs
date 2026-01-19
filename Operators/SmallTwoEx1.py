# Write a python program which will accept two numeric Values and find the smallest among that and check for equality

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

res = a if a<b else b

print("Small Val({},{}) = {}".format(a,b,res))