# 1291. Sequential Digits

def sequentialDigits(low,high):
    s = '123456789'
    res= []
    n = len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            num = int(s[i:j])
            if num>= low and num<=high:
                res.append(num)
    return res

low = int(input("Low Value: "))
high = int(input("High Value: "))
print("~"*30)
print("Output:",sequentialDigits(low,high))
print("~"*30)