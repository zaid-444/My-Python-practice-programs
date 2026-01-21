# Write a python program which will display the name of the digit by accepting digit from the keyboard by adding if else statement

d = int(input("Enter a Digit: "))

if d==0:
    print("{} is Zero".format(d))
else:
    if d==1:
        print("{} is One".format(d))
    else:
        if d==2:
            print("{} is Two".format(d))
        else:
            if d==3:
                print("{} is Three".format(d))
            else:
                if d==4:
                    print("{} is Four".format(d))
                else:
                    if d==5:
                        print("{} is Five".format(d))
                    else:
                        if d==6:
                            print("{} is Six".format(d))
                        else:
                            if d==7:
                                print("{} is Seven".format(d))
                            else:
                                if d==8:
                                    print("{} is Eight".format(d))
                                else:
                                    if d==9:
                                        print("{} is Nine".format(d))
                                    else:
                                        print("{} is Number".format(d))