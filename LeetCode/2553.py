# 2553. Separate the Digits in an Array

def sepDigits(nums):
    lst = [ int(ch) for num in nums for ch in str(num) ]
    return lst

nums = [ int(n) for n in input("Enter Nums: ").split() ]
print("Old List:",nums)
print("New List:",sepDigits(nums))