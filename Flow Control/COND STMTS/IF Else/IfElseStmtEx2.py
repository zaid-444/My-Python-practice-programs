# Program for Accepting Two Numerical value and Decide biggest and check for equality also

a = int(input("Enter First Value: "))
b = int(input("Enter Seconde Value: "))

if a>b:
    print("{} is bigger than {}".format(a,b))
else:
    if b>a:
        print("{} is bigger than {}".format(b,a))
    else:
        print("{} and {} both are Equal".format(a,b))