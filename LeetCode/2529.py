# 2529. Maximum Count of Positive Integer and Negative Integer

def maximumCount(nums):
    ng = 0
    ps = 0
    for num in nums:
        if num < 0:
            ng += 1
        elif num > 0:
            ps += 1
    return max(ng,ps)

nums = [ int(num) for num in input("Enter Numbers: ").split() ]
res = maximumCount(nums)
print("~"*20)
print("Output:",res)
print("~"*20)