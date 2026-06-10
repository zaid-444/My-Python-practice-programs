# 2248. Intersection of Multiple Arrays

def intersection(nums):
    lst = []
    d = {}
    for num in nums:
        num = set(num)
        for n in num:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
    ln = len(nums)
    for k in d:
        if d[k] == ln:
            lst.append(k)
    lst.sort()
    return lst


nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

res = intersection(nums)
print("~"*20)
print("Output:",res)
print("~"*20)