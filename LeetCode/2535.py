# 2535. Difference Between Element Sum and Digit Sum of an Array

def diffSum(nums):
    esum = 0
    dsum = 0
    for e in nums:
        esum += e
        for d in str(e):
            dsum += int(d)
    print(esum)
    print(dsum)
    print("Difference =",esum-dsum)

print("-"*50)
print("Enter List Values Separated by Space")
nums = [ int(i) for i in input().split() ]
print("-"*50)

diffSum(nums)
print("-"*50)