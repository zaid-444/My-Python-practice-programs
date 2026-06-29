# 283. Move Zeroes

def moveZeros(nums):
    n = len(nums)
    if n == 1:
        return
    i = 0
    while i < n:
        if nums[i] == 0:
            break
        i += 1
    if i >= n:
        return
    j = i+1
    while j < n:
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
        j += 1

nums = [0,1,3,0,3,0,4]
moveZeros(nums)
print(nums)