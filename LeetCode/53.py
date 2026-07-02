# 53. Maximum Subarray

# Brute
def maxSubArray(nums):
    mx = float("-inf")
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i,n):
            total += nums[j]
            if total > mx:
                mx = total
    return mx


# Obtimal
def maxSubArray(nums):
    mx = float("-inf")
    total = 0
    for n in nums:
        total += n
        mx = max(total,mx)
        if total < 0:
            total = 0
    return mx
nums = [ int(i) for i in input("> ").split() ]
print("~"*20)
print(f"Output: {maxSubArray(nums)}")
print("~"*20)