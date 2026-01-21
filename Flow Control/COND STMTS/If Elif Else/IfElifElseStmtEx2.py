# Write a python program which will display the name of the digit by accepting digit from the keyboard by adding if elif else statement

d = int(input("Enter a Digit: "))

if d==0:
    print("{} is Zero".format(d))

elif d==1:
    print("{} is One".format(d))

elif d==2:
    print("{} is Two".format(d))

elif d==3:
    print("{} is Three".format(d))

elif d==4:
    print("{} is Four".format(d))

elif d==5:
    print("{} is Five".format(d))

elif d==6:
    print("{} is Six".format(d))

elif d==7:
    print("{} is Seven".format(d))

elif d==8:
    print("{} is Eight".format(d))

elif d==9:
    print("{} is Nine".format(d))

elif d>9:
    print("{} is +VE Number".format(d))

elif d in range(-1,-10,-1):
    print("{} is -VE Digit".format(d))

else:
    print("{} is -VE Number".format(d))