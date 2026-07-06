# 18. 4Sum


# Brute 
# TC--> O(n⁴)  SC--> O(1) including the output): O(k)
def fourSum(nums,target):
    res = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        lst = [nums[i],nums[j],nums[k],nums[l]]
                        lst.sort()
                        res.add(tuple(lst))
    return [ list(t) for t in res ]


# Better
# TC--> O(n³)  SC--> O(n + k) including Output
def fourSum(nums,target):
    res = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            s = set()
            for k in range(j+1,n):
                fourth = target - (nums[i]+nums[j]+nums[k])
                if fourth in s:
                    lst = [nums[i],nums[j],nums[k],fourth]
                    lst.sort()
                    res.add(tuple(lst))
                s.add(nums[k])
    return [ list(t) for t in res ]



# Optimal
# TC-->  O(n³)  SC-->  O(n)
def fourSum(nums,target):
    n = len(nums)
    nums.sort()
    res = []
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    res.append([nums[i],nums[j],nums[k],nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while l > k and nums[l] == nums[l+1]:
                        l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1
    return res


nums = [1,0,-1,0,-2,2]
target = 0
print("~"*30)
print(f"Output: {fourSum(nums,target)}")
print("~"*30)