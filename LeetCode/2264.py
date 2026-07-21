# 2264. Largest 3-Same-Digit Number in String

def func(num):
    mx = ""
    n = len(num)
    for i in range(n-2):
        if num[i] == num[i+1] == num[i+2]:
            mx = max(mx,num[i:i+3])
    return mx


num = input("Enter any number: ")
print("~"*25)
print("Output:",func(num))
print("~"*25)