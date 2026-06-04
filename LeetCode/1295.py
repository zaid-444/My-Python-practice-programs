# 1295. Find Number with Even Number of Digits


def findNumbers(nums):
    count = 0
    for num in nums:
        if len(str(num))%2 == 0:
            count += 1
    return count

nums = [ int(val) for val in input("Enter Nums: ").split() ]
res = findNumbers(nums)
print("~"*30)
print("Result:",res)
print("~"*30)