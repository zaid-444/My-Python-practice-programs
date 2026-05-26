# 27. Remove Element

def removeElement(nums,val):
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k += 1
    return k

nums = [ int(n) for n in input("Enter Nums: ").split() ]
val = int(input("Enter any number: "))
res = removeElement(nums,val)
print("Output =",res)