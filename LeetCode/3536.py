# 3536. Maximum product of Two Digits

def maxProduct(n):
    mx = float("-inf")
    smx = float("-inf")
    while n != 0:
        d = n%10
        if d > mx:
            smx = mx
            mx = d
        elif d > smx:
            smx = d
        n = n//10
    return mx*smx


n = int(input("> "))
print("~"*20)
print(f"Output: {maxProduct(n)}")
print("~"*20)