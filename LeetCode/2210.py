# 2210. Count Hills and Valleys in an Array

def countHillValley(nums):
    lst = []
    for i in range(len(nums)):
        if len(lst) == 0 or nums[i] != lst[-1]:
            lst.append(nums[i])
    c = 0
    for i in range(1,len(lst)-1):
        if (lst[i] > lst[i+1] and lst[i] > lst[i-1]) or (lst[i] < lst[i+1] and lst[i] < lst[i-1]):
            c += 1
    return c


nums = [ int(i) for i in input("> ").split() ]
res = countHillValley(nums)
print("~"*20)
print("Output:",res)
print("~"*20)