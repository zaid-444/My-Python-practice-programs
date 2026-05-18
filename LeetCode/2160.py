# 2160. Minimum Sum of Four Digit Number After Splitting Digits

def minimumSum(num):
    n = list(str(num))
    n.sort()
    n1 = int(n[0] + n[2])
    n2 = int(n[1] + n[3])
    return n1 + n2

num = int(input("Enter 4 Digit Number: "))
res = minimumSum(num)

print("-"*30)
print("Minimum Sum is =",res)
print("-"*30)