# 2180. Count Integers With Even Digit Sum

def countEven(num):
    c = 0
    for i in range(1,num+1):
        s = 0
        for n in str(i):
            s += int(n)
        if s%2 == 0:
            c += 1
    return c

num = int(input("Enter any Number: "))
res = countEven(num)
print("~"*30)
print("Output:",res)
print("~"*30)