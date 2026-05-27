# 1464. Maximum Product of Two Elements in an Array

def maxProduct(nums):
    nums.sort()
    num1 = nums[-1]-1
    num2 = nums[-2]-1
    return num1*num2

nums = [ int(n) for n in input("Enter Nums: ").split() ]
print("~"*30)
print("Output:",maxProduct(nums))
print("~"*30)