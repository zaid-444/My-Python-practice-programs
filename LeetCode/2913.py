# 2913. Subarrays Distinct Element Sum of Squares

def sumCounts(nums):
    s = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sub = nums[i:j+1]
            unq = len(set(sub))
            s += unq**2
    return s

nums = [ int(num) for num in input("Enter Numbers: ").split() ]
res = sumCounts(nums)
print("~"*30)
print("Output:",res)
print("~"*30)