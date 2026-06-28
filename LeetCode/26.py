# 26. Remove Duplicates from Sorted Array

# Brute Force
def removeDuplicates(nums):
    d = {}
    for n in nums:
        d[n] = 0
    i = 0
    for k in d:
        nums[i] = k
        i += 1
    return i

def removeDuplicates(nums):
    lst = []
    for n in nums:
        if n not in lst:
            lst.append(n)
    for i in range(len(lst)):
        nums[i] = lst[i]
    return len(lst)

# Optimal
def removeDuplicates(nums):
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    j = 1
    while j < n:
        if nums[j] != nums[i]:
            i += 1
            nums[j],nums[i] = nums[i],nums[j]
        j += 1
    return i+1

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))