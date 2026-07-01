# 1. Two Sum

# Brute
def twoSum(nums,target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]


# Optimal
def twoSum(nums,target):
    n = len(nums)
    d = {}
    for i in range(n):
        remain = target - nums[i]
        if remain in d:
            return [d[remain],i]
        d[nums[i]] = i

nums = [ int(i) for i in input("> ").split() ]
target = int(input("> "))

print("~"*20)
print(f"Output: {twoSum(nums,target)}")
print("~"*20)