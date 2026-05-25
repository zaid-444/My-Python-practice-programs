# 2089. Find Target Indices After Sorting Array

def targetIndices(nums,tar):
    nums.sort()
    lst = [ i for i in range(len(nums)) if nums[i] == tar]
    return lst

nums = [ int(num) for num in input("Enter Numbers: ").split() ]
tar = int(input("Enter Target Value: "))
res = targetIndices(nums,tar)
print("~"*30)
print("Output:",res)
print("~"*30)