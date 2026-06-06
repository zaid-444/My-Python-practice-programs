# 3069. Distribute Elements Into Two Arrays

def resultArray(nums):
    arr1 = [nums[0]]
    arr2 = [nums[1]]
    i = 2
    while i < len(nums):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[i])
            i += 1
        else:
            arr2.append(nums[i])
            i += 1
    return arr1 + arr2

nums = [ int(i) for i in input("Enter Nums: ").split() ]
print("~"*30)
print("Result:",resultArray(nums))
print("~"*30)