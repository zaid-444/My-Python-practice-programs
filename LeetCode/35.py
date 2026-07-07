# 35. Search Insert Position

# Brute TC--> O(n) SC--> O(1)
def searchInsert(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] >= target:
            return i
    return n


def searchInsert(nums,target):
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
            low = mid+1
    return lb


nums = [1,2,3,4,6,9,11]
tar = int(input("> "))
print("~"*15)
print(f"Output: {searchInsert(nums,tar)}")
print("~"*15)

s = "zaid"