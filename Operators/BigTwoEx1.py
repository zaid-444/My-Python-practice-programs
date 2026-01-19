# Program for finding Biggest of Two Numbers

a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))

c = a if a>b else b

print("Big ({},{})={}".format(a,b,c))