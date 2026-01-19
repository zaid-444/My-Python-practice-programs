# Program for finding Biggest of Two Numbers and check for equality

a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))

res = a if a>b else b if b>a else "Equal"

print("Big({},{}) = {}".format(a,b,res))