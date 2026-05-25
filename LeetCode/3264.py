# 3264. Final Array State After K Multiplication Operations

def getFinalState(nums,k,mul):
    for i in range(k):
        mn = min(nums)
        x = mn*mul
        nums[nums.index(mn)] = x
    return nums

nums = [ int(num) for num in input("Enter Numbers: ").split() ]
k = int(input("Enter Value of K: "))
mul = int(input("Enter Multiplie: "))
print("~"*30)
print("Before:",nums)
print("After: ",getFinalState(nums,k,mul))
print("~"*30)