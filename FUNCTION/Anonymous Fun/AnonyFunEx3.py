# Write a python program which will accept three numerical values and find max and min by using anonymous function and check for equality

maxv = lambda a,b,c: a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "All are equal"
minv = lambda a,b,c: a if a<=b and a<c else b if b<a and b<=c else c if c<=a and c<b else "All are equal"

print("-"*50)
a,b,c = int(input("Enter value of a: ")),int(input("Enter value of b: ")),int(input("Enter value of c: "))
print("-"*50)

resmax = maxv(a,b,c)
print("Big({},{},{}) = {}".format(a,b,c,resmax))
print("-"*50)

resmin = minv(a,b,c)
print("Small({},{},{}) = {}".format(a,b,c,resmin))
print("-"*50)