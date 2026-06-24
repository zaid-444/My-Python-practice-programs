# 442. Find All Duplicates in an Array

def findDuplicates(nums):
    d = {}
    for n in nums:
        d[n] = d.get(n,0)+1
    lst = []
    for k in d:
        if d[k] > 1:
            lst.append(k)
    lst.sort()
    return lst


nums = [ int(i) for i in input("Enter Nums: ").split() ]
print("~"*30)
print(f"Output: {findDuplicates(nums)}")
print("~"*30)