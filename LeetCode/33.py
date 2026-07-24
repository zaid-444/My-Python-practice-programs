# 33. Search in Rotated Sorted Array

def search(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid-1
            else:
                low = mid+1
    return -1

nums = [4,5,6,7,0,1,2]
print("~"*25)
print(f"Output: {search(nums,0)}")
print("~"*25)