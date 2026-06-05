# 2119. A Number After a Double Reversal

def isSameAftrRev(num):
    if num == 0:
        return True
    elif int(str(num)[-1]) == 0:
        return False
    else:
        return True
    
num = int(input("Enter a Number: "))
print("~"*30)
print("Result:",isSameAftrRev(num))
print("~"*30)