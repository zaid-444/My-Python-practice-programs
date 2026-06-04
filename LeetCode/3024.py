# 3024. Type of Triangle

def triangleType(nums):
    if nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]:
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
            return "scalene"
        else:
            return "isosceles"
    else:
        return "none"
    
nums = [ int(v) for v in input("Enter Triangle Three Sides: ").split() ]
print("~"*30)
print("Result:",triangleType(nums))
print("~"*30)