# 2652. Sum Multiples

def sumOfMul(n):
    s = 0
    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            s += i
    return s

n = int(input("Enter Value of N: "))

print("-"*50)
res = sumOfMul(n)
print("Output:",res)
print("-"*50)