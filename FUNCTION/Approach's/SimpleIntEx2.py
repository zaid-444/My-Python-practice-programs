# Write a python program which will Cal simple Interest and total amount to pay by using Function's

def takeValues():
    p = float(input("Enter Principal Amount: "))
    t = int(input("Enter time: "))
    r = float(input("Enter rate: "))
    return p,t,r


def calsimpleint():
    p,t,r = takeValues()
    si = (p*r*t)/100
    tot = si+p
    return p,t,r,si,tot

def displayresult():
    p,t,r,si,tot = calsimpleint()
    print("-"*50)
    print("Amount you want  : {}".format(p))
    print("Rate of Interest : {}".format(r))
    print("Time in Year's   : {}".format(t))
    print("-"*50)
    print("Your Interest is : {}".format(si))
    print("You have to pay  : {}".format(tot))
    print("-"*50)


displayresult()