# Program for Accepting Two Numerical and Decide Biggest and Check for equality also

a = float(input("Enter First Value: "))
b = float(input("Enter Second Value: "))

if (a>b):
    print("Big({},{})={}".format(a,b,a))

if (b>a):
    print("Big({},{})={}".format(a,b,b))

if (a==b):
    print("{},{} Both are Equal".format(a,b))

print("Program Completed")

