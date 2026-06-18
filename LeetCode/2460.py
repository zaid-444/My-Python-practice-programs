# 2460. Apply Operations to an Array

def applyOprs(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i]*2
            nums[i+1] = 0
    lst = []
    c = 0
    for n in nums:
        if n != 0:
            lst.append(n)
        else:
            c += 1
    lst.extend([0]*c)
    return lst

nums = [ int(i) for i in input("Enter Nums: ").split() ]
res = applyOprs(nums)
print("~"*30)
print("Output:",res)
print("~"*30)