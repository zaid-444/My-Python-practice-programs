# 169. Majority Element

def majorityElem(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i,0)+1
    mx = nums[0]
    for k in d:
        if d[k] > d[mx]:
            mx = k
    return mx

nums = [ int(i) for i in input("> ").split() ]
print("~"*20)
print(f"Output: {majorityElem(nums)}")
print("~"*20)