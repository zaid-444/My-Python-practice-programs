# Program to find smallest value among three numbers

a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))
c = int(input("Enter Value of c: "))

res = a if b>=a<c else b if a>=b<c else c if a>c<=b else "All are Equal"

print("From ({},{},{}) smallest number is {}".format(a,b,c,res))