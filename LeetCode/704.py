# 704. Binary Search

def search(nums,target):
    n = len(nums)
    high = n-1
    low = 0
    while high >= low:
        mid = (high+low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1

nums = [-1,0,3,5,9,12]
print("~"*25)
print(f"Output: {search(nums,-1)}")
print("~"*25)