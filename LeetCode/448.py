# 448. Find All Numbers Disappeared in an Array

def findDisappearedNumbers(nums):
    n = len(nums)
    s = set(nums)
    lst = []
    for i in range(1,n+1):
        if i not in s:
            lst.append(i)
    return lst


nums = [ int(i) for i in input("> ").split() ]
res = findDisappearedNumbers(nums)
print("~"*20)
print("Output:",res)
print("~"*20)