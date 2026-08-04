# 215. Kth Largest Element in an Array

def findKthLargest(nums,k):
    nums.sort()
    return nums[-k]