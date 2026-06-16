# 2057. Smallest Index With Equal Value

def smallestEqual(nums):
    for i in range(len(nums)):
        if i%10 == nums[i]:
            return i
    return -1


nums = [ int(i) for i in input("> ").split() ]
res = smallestEqual(nums)
print("~"*20)
print("smallestEqual:",res)
print("~"*20)