# 2544. Alternating Digit Sum

def alterDigSum(n):
    n = str(n)
    s = 0
    for i in range(len(n)):
        if i%2 == 0:
            s += int(n[i])
        else:
            s -= int(n[i])
    return s


n = int(input("Enter Value of N: "))

res = alterDigSum(n)
print("~"*30)
print("Alternating Digit Sum:",res)
print("~"*30)