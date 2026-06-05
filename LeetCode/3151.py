# 3151. Special Array I

def isArraySpecial(nums):
    for i in range(len(nums)-1):
        if nums[i]%2 == 0 and nums[i+1]%2 == 0:
            return False
        elif nums[i]%2 != 0 and nums[i+1]%2 != 0:
            return False
    return True

nums = [ int(i) for i in input("Enter Numbers: ").split() ]
print("~"*30)
print("isArraySpecial:",isArraySpecial(nums))
print("~"*30)