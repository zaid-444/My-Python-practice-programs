# 268. Missing Number

def missNum(nums):
    for i in range(len(nums)+1):
        if i not in nums:
            return i
        
nums = [ int(i) for i in input("Enter Nums: ").split() ]

print("~"*20)
print("Missing Number:",missNum(nums))
print("~"*20)