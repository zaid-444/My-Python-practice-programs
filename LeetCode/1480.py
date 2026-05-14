# 1480. Running Sum of 1d Array

def runningSum(nums):
    res = []
    vali = 0
    vsum = 0
    for i in nums:
        vali = i
        vsum += vali
        res.append(vsum)
    return res

print("-"*50)
print("Enter List Values Separated by Space")
nums = [ int(i) for i in input().split() ]
print("-"*50)

res = runningSum(nums)
print("Old List Values =",nums)
print("After Adding =",res)
print("-"*50)