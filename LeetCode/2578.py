# 2578. Split With Minimum Sum

def splitNum(num):
    s = str(num)
    lst = [ int(i) for i in s ]
    num1 = ""
    num2 = ""
    lst.sort()
    for i in range(len(lst)):
        if i%2 == 0:
            num1 += str(lst[i])
        else:
            num2 += str(lst[i])
    return int(num1)+int(num2)


num = int(input("Enter any number: "))
print("~"*25)
print(f"Output: {splitNum(num)}")
print("~"*25)