# 2733. Neither Minimum nor Maximum

def findNonMinMax(nums):
    nums.sort()
    if len(nums) > 2:
        return nums[1]
    return -1

nums = [ int(i) for i in input("Enter Nums: ").split() ]
print("~"*20)
res = findNonMinMax(nums)
print("Output:",res)
print("~"*20)