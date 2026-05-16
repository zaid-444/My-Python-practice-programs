# 2427. Number of Common Factors

def commonFact(a,b):
    count = 0
    mx = max(a,b)
    for i in range(1,mx+1):
        if a%i == 0  and b%i == 0:
            count += 1
    return count

a = int(input("Enter Value of A: "))
b = int(input("Enter Value of B: "))

print("-"*50)
res = commonFact(a,b)
print("Output =",res)
print("-"*50)