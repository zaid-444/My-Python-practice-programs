# 2169. Count Operations to Obtain Zero 

def countOpr(num1,num2):
    opr = 0
    if num1 == 0 or num2 == 0:
        return opr
    while True:
        if num1 > num2:
            num1 = num1 - num2
            opr += 1
            if num1 == 0:
                break
        else:
            num2 = num2 - num1
            opr += 1
            if num2 == 0:
                break
    return opr

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
print("~"*20)
print("Output:",countOpr(num1,num2))
print("~"*20)