# 1281. Subtract the Product and Sum of Digits of an Integer

def subtractProductAndSum(num):
    prod = 1
    summ = 0
    for n in str(num):
        prod *= int(n)
        summ += int(n)
    return prod - summ

num = int(input("Enter any Number: "))
res = subtractProductAndSum(num)
print("~"*30)
print("Difference:",res)
print("~"*30)