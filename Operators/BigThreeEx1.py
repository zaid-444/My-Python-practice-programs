# Program for accepting Three Numerical values and find Biggest among of them

a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))
c = int(input("Enter Value of c: "))

res = "All are Equal" if a==b and b==c else a if a>=b and a>=c else b if b>=a and b>=c else c

print("From ({} {} {}) biggest value is {}".format(a,b,c,res))

