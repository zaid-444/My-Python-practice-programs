# 3423. Maximum Difference Between Adjacent Elements is a Circular Array

def maxAdjaDis(nums):
    mx = abs(nums[0] - nums[-1])
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            s = nums[i] - nums[i+1]
        else:
            s = nums[i+1] - nums[i]
        if s > mx:
            mx = s
    return mx

nums = [ int(val) for val in input("Enter Nums: ").split() ]

res = maxAdjaDis(nums)
print("~"*20)
print("Output:",res)
print("~"*20)