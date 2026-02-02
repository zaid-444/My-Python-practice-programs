# Write a python program which will Cal simple Interest and total amount to pay by using Function's

def simpleint():
    p = float(input("Enter Principal Amount: "))
    t = float(input("Enter Time: "))
    r = float(input("Enter Rate of Interest: "))
    print("-"*50)
    si = (p * t * r) / 100
    totamt = p + si
    print("Simple Interest =", si)
    print("Total amount to pay =", totamt)

simpleint()