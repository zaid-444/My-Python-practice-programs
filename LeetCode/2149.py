# 2149. Rearrange Array Elements by Sign

# Brute
def rearrangeArray(nums):
    pos = []
    neg = []
    for num in nums:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
    for i in range(len(pos)):
        nums[i*2] = pos[i]
        nums[(i*2)+1] = neg[i]
    return nums

# Optimal
def rearrangeArray(nums):
    result = [0]*len(nums)
    i = 0
    j = 1
    for num in nums:
        if num >= 0:
            result[i] = num
            i += 2
        else:
            result[j] = num
            j += 2
    return result


nums = [3,1,-2,-5,2,-4]
print("~"*20)
print(f"Output: {rearrangeArray(nums)}")
print("~"*20)