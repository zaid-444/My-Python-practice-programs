# 628. Maximum Product of Three Numbers

def maximumProduct(nums):
    nums.sort()
    a = nums[-1]*nums[-2]*nums[-3]
    b = (nums[0]*nums[1]) * nums[-1]
    return max(a,b)

nums = [ int(i) for i in input("> ").split() ]

print("~"*20)
print(f"Output: {maximumProduct(nums)}")
print("~"*20)