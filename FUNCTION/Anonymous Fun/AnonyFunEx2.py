# Write a python program which will accept two numerical values and find the biggest among them by using anonymous function

big = lambda a,b : a if a>b else b if b > a else "Both are equal"

a,b = int(input("Enter first value: ")),int(input("Enter Seconde value: "))
res = big(a,b)
print("Big ({},{}) = {}".format(a,b,res))