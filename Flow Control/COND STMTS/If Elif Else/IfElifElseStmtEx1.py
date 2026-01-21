# Program for Accepting Two Numerical value and Decide biggest and check for equality also

a = int(input("Enter First Value: "))
b = int(input("Enter Seconde Value: "))

if a>b:
    print("Big({},{})={}".format(a,b,a))
elif b>a:
    print("Big({},{})={}".format(a,b,b))
else:
    print("Both the values are Equal")

print("Program Execution Completed!!")