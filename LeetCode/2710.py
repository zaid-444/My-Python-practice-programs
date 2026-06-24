# 2710. Remove Trailing Zeros From a String

def reZeros(num):
    num = int(num)
    while num != 0:
        if num%10 != 0:
            break
        num = num // 10
    return str(num)

num = input("Enter any Number: ")
print("~"*30)
res = reZeros(num)
print("Result:",res)
print("~"*30)