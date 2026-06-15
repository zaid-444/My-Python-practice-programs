# 136. Single Number

def singleNumber(nums):
    s = set(nums)
    for n in s:
        if nums.count(n) == 1:
            return n
        
nums = [ int(i) for i in input("> ").split() ]
res = singleNumber(nums)
print("~"*30)
print("Single Number:",res)
print("~"*30)