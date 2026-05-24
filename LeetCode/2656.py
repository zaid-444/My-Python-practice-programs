# 2656. Maximum Sum With Exactly K Elements

def maximizeSum(nums,k):
    s = 0
    for i in range(k):
        mx = max(nums)
        s += mx
        nums.append(mx+1)
        nums.remove(mx)
    return s

nums = [ int(val) for val in input("Enter Nums: ").split() ]
k = int(input("Enter k value: "))
res = maximizeSum(nums,k)
print("-"*40)
print("Maximum Sum:",res)
print("-"*40)