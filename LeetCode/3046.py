# 3046. Split the Array

def isPossible(nums):
    for num in nums:
        if nums.count(num) > 2:
            return False
    return True


nums = [ int(num) for num in input("Enter nums: ").split() ]
res = isPossible(nums)
print("~"*30)
print("Output:",res)
print("~"*30)