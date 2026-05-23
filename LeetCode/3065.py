# 3065. Minimum Operations to Exceed Threshold Value

def minOperations(nums,k):
    c = 0
    for n in nums:
        if n < k:
            c += 1
    return c

nums = [ int(val) for val in input("Enter nums: ").split() ]
k = int(input("Enter K value: "))
res = minOperations(nums,k)
print("-"*20)
print("Output:",res)
print("-"*20)
