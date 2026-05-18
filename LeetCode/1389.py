# 1389. Create Target Array in the Given Order

def createTargetArray(nums, index):
    target = []
    for i in range(len(nums)):
        ind = index[i]
        val = nums[i]
        target.insert(ind,val)
    return target

print("-"*50)
nums = [ int(i) for i in input("Enter Nums: ").split() ]
index = [ int(i) for i in input("Enter Index: ").split() ]
print("-"*50)
res = createTargetArray(nums,index)
print("Result of Target =",res)
print("-"*50)