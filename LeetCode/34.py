# 34. Find First and Last Position of Element in Sorted Array


# Brute
def searchRange(nums,target):
    n = len(nums)
    first = -1
    last = -1
    for i in range(n):
        if nums[i] > target:
            break
        elif nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first,last]



# Optimal
def lowerBound(nums,target):
    n = len(nums)
    lb = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid + 1
    return lb
def upperBound(nums,target):
    n = len(nums)
    ub = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] > target:
            ub = mid
            high = mid-1
        else:
            low = mid + 1
    return ub

def searchRange(nums,target):
    lb = lowerBound(nums,target)
    if lb == len(nums) or nums[lb] != target:
        return [-1, -1]
    ub = upperBound(nums,target)
    return [lb,ub-1]

nums = [5,7,7,8,8,10]
target = int(input("Enter target: "))
print("~"*20)
print(f"Output: {searchRange(nums,target)}")
print("~"*20)