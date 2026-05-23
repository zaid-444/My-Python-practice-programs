# 1979. Finde Greatest Common Divisor of Array

def findGCD(nums):
    mn = min(nums)
    mx = max(nums)
    for i in range(mn,0,-1):
        if mn % i == 0 and mx % i == 0:
            return i

nums = [ int(val) for val in input("Enter nums: ").split() ]
res = findGCD(nums)
print("------------------")
print("Output:",res)
print("------------------")