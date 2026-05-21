# 2485. Finde the Pivot Integer

def pivotInt(n):
    s = 0
    res = -1
    for i in range(1,n+1):
        s += i
        if s == sum(range(i,n+1)):
            res = i
            break
    return res

n = int(input("Enter any Number: "))
print("-"*52)
print("Pivot Integer:",pivotInt(n))
print("-"*52)