# 15. 3Sum


# Brute
# TC--> O(Nx3)      SC-->(no.of triplest)
def threeSum(nums):
    n = len(nums)
    s = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] == 0:
                    l = [nums[i],nums[j],nums[k]]
                    l.sort()
                    s.add(tuple(l))
    return [ list(t) for t in s ]


# Better
def threeSum(nums):
    result = set()
    n = len(nums)
    for i in range(n):
        s = set()
        for j in range(i+1,n):
            third = -(nums[i]+nums[j])
            if third in s:
                l = [nums[i],nums[j],third]
                l.sort()
                result.add(tuple(l))
            s.add(nums[j])
    return [ list(t) for t in result ]


def threeSum(nums):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                temp = [ nums[i], nums[j], nums[k] ]
                res.append(temp)
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
    return res





nums = [-1,0,1,2,-1,-4]
print("~"*30) 
print(f"Output: {threeSum(nums)}")
print("~"*30) 