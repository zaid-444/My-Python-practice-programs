# 2520. Count the Digits That Divide a Number

def cntDigit(num):
    c = 0
    for n in str(num):
        if num%int(n) == 0:
            c += 1
    return c

print("-"*50)

num = int(input("Enter any Number: "))
res = cntDigit(num)
print("The Count is =",res)

print("-"*50)