# 2670. Find the Distinct Difference Array

def distinctDiffArr(nums):
    lst = []
    for i in range(len(nums)):
        ps = set(nums[i::-1])
        ss = set(nums[i+1:])
        lst.append(len(ps)-len(ss))
    return lst

nums = [ int(i) for i in input("Enter nums: ").split() ]

print("~"*40)
print(f"Distinct Array: {distinctDiffArr(nums)}")
print("~"*40)